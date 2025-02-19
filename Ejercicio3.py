import pandas as pd

df = pd.read_csv('./Tarea1.2/calificaciones.csv')

print(df.info())

#print(df)

#1.Cargue el dataset y muestre las primeras filas.
#2.Calcule el promedio de calificaciones por materia.
#3.Identifique el estudiante con el promedio más alto.
#4.Agrupa las calificaciones por estudiante y calcule el promedio de cada uno.
#5.Identifique cuántos estudiantes tienen un promedio superior a 85.
#6.Encuentre la materia con la mayor cantidad de calificaciones registradas.
#7.Muestre los 5 estudiantes con el promedio más bajo.

#Estudiante Materia Calificacion
#2.Calcule el promedio de calificaciones por materia.
print('-------------------------------------')
promedio_calificaciones = df.groupby('Materia')['Calificación'].mean().round(2)
print(f'Promedio por clases: \n {promedio_calificaciones}')
print('-------------------------------------')

#3.Identifique el estudiante con el promedio más alto.
estudiante_promAlto = df.groupby('Estudiante')['Calificación'].mean().idxmax()
print(f'Estudiante con promedio mas alto: {estudiante_promAlto}')
print('-------------------------------------')

#4.Agrupa las calificaciones por estudiante y calcule el promedio de cada uno.
calificaciones_Estudiantes = df.groupby('Estudiante')['Calificación'].mean().round(2)
print('Calificaciones', calificaciones_Estudiantes)
print('-------------------------------------')

#5.Identifique cuántos estudiantes tienen un promedio superior a 85.
condicion = calificaciones_Estudiantes > 85
promedioAlto = calificaciones_Estudiantes[condicion]
cantidadEstudiantes = promedioAlto.count()
print(f'Cantidad de estudiantes con promedio mayor a 85: {cantidadEstudiantes}')
print('-------------------------------------')

#6.Encuentre la materia con la mayor cantidad de calificaciones registradas.
materiaCalificacion = df.groupby('Materia')['Calificación'].count().idxmax()
print(f'Materia con mas calificaciones registradas: {materiaCalificacion}')
print('-------------------------------------')

#7.Muestre los 5 estudiantes con el promedio más bajo.
promedioBajo = calificaciones_Estudiantes.sort_values().head(5)
print(f'Estudiantes con el promedio mas bajo: {promedioBajo}')