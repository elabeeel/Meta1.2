import pandas as pd

df = pd.read_csv('titanic.csv')

#dimensiones del DataFrame
print(f'Dimensiones del DataFrame: {df.shape}')

#número de datos y los nombres de las columnas
print(f'Número de datos en el DataFrame: {df.size}')
print(f'Nombres de las columnas: {", ".join(df.columns)}')

#10 primeras filas
print('Primeras 10 filas:')
print(df.head(10))

#10 últimas filas
print('Últimas 10 filas:')
print(df.tail(10))

#calc el porcentaje de personas que sobrevivieron y murieron
sobrevivieron = df['Survived'].sum()
murieron = df['Survived'].count() - sobrevivieron
total_personas = df['Survived'].count()

porcentaje_sobrevivieron = (sobrevivieron / total_personas) * 100
porcentaje_murieron = (murieron / total_personas) * 100

print(f'Porcentaje de personas que sobrevivieron: {porcentaje_sobrevivieron:.2f}%')
print(f'Porcentaje de personas que murieron: {porcentaje_murieron:.2f}%')

#calculamos el porcentaje de personas que sobrevivieron en cada clase
porcentaje_sobrevivieron_clase = df.groupby('Pclass')['Survived'].mean() * 100

print('Porcentaje de personas que sobrevivieron en cada clase:')
print(porcentaje_sobrevivieron_clase)