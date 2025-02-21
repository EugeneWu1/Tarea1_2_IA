import pandas as pd
df = pd.read_csv('./Tarea1.2/ventas.csv')

#1.Cargue los datos en un DataFrame.
#2.Calcule la cantidad total de productos vendidos por categoría.
#3.Determine cuál es el producto con el mayor total de ventas.
#4.Encuentre el precio promedio de los productos vendidos.

print(df.info())
print('------------------------------------')

#Me muestra el contenido completo del csv
#print(df)

#2.Calcule la cantidad total de productos vendidos por categoría.
total = df.groupby('Producto')['Cantidad'].sum()
print(total)
print('------------------------------------')

#3.Determine cuál es el producto con el mayor total de ventas.
#mayor =total.idxmax()

mayor = total.idxmax()
print(f'Producto con el mayor total de ventas: {mayor}')
print('------------------------------------')

#4.Encuentre el precio promedio de los productos vendidos.
mediana = df.groupby('Producto')['Precio_Unitario'].mean()
print(f'Media de los productos vendidos: {mediana}')

