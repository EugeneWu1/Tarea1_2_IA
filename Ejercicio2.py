import pandas as pd

df = pd.read_csv('./Tarea1.2/clima.csv')

print(df.info())
#1.Cargue el dataset y conviértelo en un DataFrame.
#2.Calcule la temperatura promedio de cada ciudad.
#3.Determine el registro con la temperatura más alta y el más bajo en el dataset.
#4.Identifique qué ciudad tuvo la temperatura más alta y cuál la más baja en todo el dataset.
#5.Encuentre cuántos registros tienen una temperatura mayor a 30°C.
#6.Cuenta cuántos días en total hay registrados por cada ciudad.

print('------------------------------------')

#2.Calcule la temperatura promedio de cada ciudad.
#365 x 3 FECHA, CIUDAD, TEMPERATURA
temp_promedio = df.groupby('Ciudad')['Temperatura'].mean()
print(f'Temperatura promedio de cada ciudad: {temp_promedio}')
print('------------------------------------')

#3.Determine el registro con la temperatura más alta y el más bajo en el dataset.
#Este me dice la temperatura mas alta
#temp_alta= df['Temperatura'].max()

#Este solo me dice la fila donde esta la temperatura mas alta
temp_alta2= df['Temperatura'].idxmax()

print(f'Temperatura más alta: {temp_alta2}')

temp_baja = df['Temperatura'].idxmin()
print(f'Temperatura más baja: {temp_baja}')
print('------------------------------------')

#4.Identifique qué ciudad tuvo la temperatura más alta y cuál la más baja en todo el dataset.

#Primero lo agrupo ciudad y por la columna temperatura busco su temperaturas mas alta
ciudad_temp_alta = df.groupby('Ciudad')['Temperatura'].max()
#Sin el idxmax() me retornaria las ciudaddes con su temperatura mas alta
print(f'Ciudad con la temperatura más alta: {ciudad_temp_alta.idxmax()}')

ciudad_temp_baja = df.groupby('Ciudad')['Temperatura'].min()
print(f'Ciudad con la temperatura más baja: {ciudad_temp_baja.idxmin()}')
print('------------------------------------')

#5.Encuentre cuántos registros tienen una temperatura mayor a 30°C.
condicion = df['Temperatura'] > 30
registros = df[condicion].shape[0]
print(f'Registros con temperatura mayor a 30°C: {registros}')
print('------------------------------------')

#6.Cuenta cuántos días en total hay registrados por cada ciudad.

dias = df.groupby('Ciudad')['Fecha'].count()
print(f'Días registrados por ciudad: {dias}')