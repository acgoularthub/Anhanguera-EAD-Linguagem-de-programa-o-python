import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

#Gerando numeros
x = np.random.randn(200)
y = np.random.randn(200)

#definindo dataframe
df = pd.DataFrame({'x' : x , 'y' : y })

#criando tabela de distribuição
sns.displot(df['x'])
plt.show()

#criando grafico de barras 
sns.barplot(df.x, df.y)
plt.show()

#cria um "grafico" plotando a relação de x com y
sns.scatterplot(df.x, df.y, hue = df.x)
plt.show()
