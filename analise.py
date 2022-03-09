import pandas as pd
import plotly.express as px

#Passo 1: Importar a base de dados
tabela = pd.read_csv(r"C:/Users/davig/Desktop/Coisas/Programas/Python/Intensivão/Aula 2/telecom_users.csv")


#Passo 2: Visualizar a base de dados
    #Entender as informações que você tem
    #Descobrir as falhas da base de dados


#Passo 3: Tratamento de dados
    #Analisar se os dados estão no formato correto
tabela=tabela.drop("Unnamed: 0",axis=1)
tabela["TotalGasto"]= pd.to_numeric(tabela["TotalGasto"],errors ="coerce")
    #Existe alguma coluna completamente vazia?
tabela = tabela.dropna(how="all",axis=1)
    #Existe alguma informação em alguma linha vazia?
tabela = tabela.dropna(how="any",axis=0)

#Passo 4: Análise inicial / Análise Global
    #Clientes que cancelaram e que não cancelaram
print(tabela["Churn"].value_counts())
    #A % de clientes que cancelaram e que não cancelaram
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

#Passo 5: Análise detalhada(Buscar a causa/solução do problema)
    #Criar o gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela,x=coluna,color="Churn")
    #Exibir gráfico
    grafico.show()

##