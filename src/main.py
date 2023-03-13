import pandas as pd
import matplotlib.pyplot as plt

# Importar dados da tabela para um dataframe
df = pd.read_excel("src/gastos-cartoes-corporativos-presidentes-2003-2022.xlsx")



# Remove rows that contain non-numeric values in the 'VALOR' column
df = df[pd.to_numeric(df["VALOR"], errors='coerce').notna()]

# Convert the 'VALOR' column to a numeric datatype
df["VALOR"] = pd.to_numeric(df["VALOR"])

# Agrupar os dados pelo ano e somar os valores
gastos_por_ano = df.groupby("ANO")["VALOR"].sum()

# Gerar gráfico de linhas dos gastos por ano
plt.plot(gastos_por_ano.index, gastos_por_ano.values)
plt.xlabel('Ano')
plt.ylabel('Valor (R$)')
plt.title('Gastos por ano')
plt.savefig("grafico_gastos_por_ano.png")


# Agrupar os dados pelo nome do fornecedor e somar os valores
gastos_por_fornecedor = df.groupby("NOME FORNECEDOR")["VALOR"].sum()

# Ordenar os gastos pelo fornecedor em ordem decrescente
gastos_por_fornecedor = gastos_por_fornecedor.sort_values(ascending=False)

# Selecionar os 10 maiores gastos
maiores_gastos = gastos_por_fornecedor.head(10)

# Gerar gráfico de barras dos 10 maiores gastos
plt.bar(maiores_gastos.index, maiores_gastos.values)
plt.xlabel('Fornecedor')
plt.ylabel('Valor (R$)')
plt.title('Maiores gastos por fornecedor')
plt.xticks(rotation=90)
plt.savefig("grafico_maiores_gastos_por_fornecedor.png")

# Agrupar os dados pelo nome do fornecedor e somar os valores
gastos_por_fornecedor = df.groupby("NOME FORNECEDOR")["VALOR"].sum()

# Ordenar os gastos pelo fornecedor em ordem decrescente
gastos_por_fornecedor = gastos_por_fornecedor.sort_values(ascending=False)

# Selecionar os 10 maiores gastos
maiores_gastos = gastos_por_fornecedor.head(10)

# Gerar gráfico de barras dos 10 maiores gastos
plt.bar(maiores_gastos.index, maiores_gastos.values)
plt.xlabel('Fornecedor')
plt.ylabel('Valor (R$)')
plt.title('Maiores gastos por fornecedor')
plt.xticks(rotation=90)
plt.savefig("grafico_maiores_gastos_por_fornecedor.png")
plt.show()

# Agrupar os dados pelo ano e selecionar o maior gasto
maior_gasto_por_ano = df.groupby("ANO")["VALOR"].max()

# Gerar gráfico de linhas dos maiores gastos por ano
plt.plot(maior_gasto_por_ano.index, maior_gasto_por_ano.values)
plt.xlabel('Ano')
plt.ylabel('Valor (R$)')
plt.title('Maiores gastos por ano')
plt.savefig("grafico_maior_gasto_por_ano.png")

#aqui é onde você pode dividir os anos por presidente 
df_lula = df[(df["ANO"] >= 2003) & (df["ANO"] <= 2011)]
gastos_por_ano_lula = df_lula.groupby("ANO")["VALOR"].sum()
plt.plot(gastos_por_ano_lula.index, gastos_por_ano_lula.values)
plt.xlabel('Ano')
plt.ylabel('Valor (R$)')
plt.title('Gastos por ano - Lula')
plt.savefig("grafico_gastos_por_ano_lula.png")
plt.show()

df_dilma = df[(df["ANO"] >= 2011) & (df["ANO"] <= 2016)]
gastos_por_ano_dilma = df_dilma.groupby("ANO")["VALOR"].sum()
plt.plot(gastos_por_ano_dilma.index, gastos_por_ano_dilma.values)
plt.xlabel('Ano')
plt.ylabel('Valor (R$)')
plt.title('Gastos por ano - Dilma')
plt.savefig("grafico_gastos_por_ano_dilma.png")
plt.show()

df_temer = df[(df["ANO"] >= 2017) & (df["ANO"] <= 2019)]
gastos_por_ano_temer = df_temer.groupby("ANO")["VALOR"].sum()
plt.plot(gastos_por_ano_temer.index, gastos_por_ano_temer.values)
plt.xlabel('Ano')
plt.ylabel('Valor (R$)')
plt.title('Gastos por ano - Temer')
plt.savefig("grafico_gastos_por_ano_temer.png")
plt.show()

df_bolsonaro = df[(df["ANO"] >= 2019) & (df["ANO"] <= 2023)]
gastos_por_ano_bolsonaro = df_bolsonaro.groupby("ANO")["VALOR"].sum()
plt.plot(gastos_por_ano_bolsonaro.index, gastos_por_ano_bolsonaro.values)
plt.xlabel('Ano')
plt.ylabel('Valor (R$)')
plt.title('Gastos por ano - Bolsonaro')
plt.savefig("grafico_gastos_por_ano_bolsonaro.png")

# comparando o gasto total de cada presidente
gastos_por_presidente = pd.DataFrame({'Lula': gastos_por_ano_lula.sum(), 
                                      'Dilma': gastos_por_ano_dilma.sum(),
                                      'Temer': gastos_por_ano_temer.sum(),
                                      'Bolsonaro': gastos_por_ano_bolsonaro.sum()},
                                     index=['Gasto Total'])

plt.bar(gastos_por_presidente.columns, gastos_por_presidente.values[0])
plt.xlabel('Presidente')
plt.ylabel('Valor (R$)')
plt.title('Gastos totais por Presidente')
plt.savefig("grafico_gastos_totais_por_presidente.png")




