import pandas as pd
import numpy as np

cliente = {'Nome': ['Marcelo', 'Ana', 'Joyce', 'Gustavo', 'Miranha', 'Gwen'],
'Idade': [20, 19, 21, 15, 20, 19],
'Telefone':[8499696969, 8499111111, 8499112469, 8499241124, 8491112222, 5556969]}

print(cliente)

print("\nE.......\n")

df = pd.DataFrame(cliente)

print(df)

print('\n')

print(df.Nome) #imprime apenas a coluna nome

print('\n')

print(df.Idade.mean()) #imprime a média das idades