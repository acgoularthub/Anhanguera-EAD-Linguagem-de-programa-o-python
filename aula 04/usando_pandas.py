import pandas as pd
import numpy as np

#criando um dicionário
cliente = {'Nome': ['Marcelo', 'Ana', 'Joyce', 'Gustavo', 'Miranha', 'Gwen'],
'Idade': [20, 19, 21, 15, 20, 19],
'Telefone':[8499696969, 8499111111, 8499112469, 8499241124, 8491112222, 5556969]}


print(cliente) #imprime o "array" do dicionário

print("\nE.......\n")

df = pd.DataFrame(cliente) #cria um dataframe com indice automático

print(df) #exibe o dataframe do dicionário cliente

print('\n')

print(df.Nome) #imprime apenas a coluna nome do dataframe criado

print('\n')

print(df.Idade.mean()) #imprime a média das idades

s= pd.Series(("Carla", "lis"), index=['03', '07']) #cria uma série e atribui o inice indicado pelo programador

print('\n')
print(s)