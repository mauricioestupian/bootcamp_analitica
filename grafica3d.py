#Ejemplo de estudiantes con asistencia a clases y calificaciones
import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#Data con varias columnas 
df=pd.DataFrame({
    'Estudiante': ['Ana', 'Luis', 'Carlos', 'Marta', 'sofia', 'Jorge', 'Lucia', 'Diego'],
    'Edad': [20, 22, 21, 23, 20, 22, 21, 23],
    'Horas_Estudio': [5, 6, 4, 7, 5,  6, 7, 8],
    'Asistencia_Clases': [10, 15,11, 12, 14, 13, 12, 11],
    'Calificacion_Final': [88, 76, 82, 91, 70, 74, 85, 68],
    'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Valencia', 'Barcelona', 'Madrid', 'Valencia', 'Barcelona']
})

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Datos para los ejes
x = df['Horas_Estudio']
y = df['Asistencia_Clases']
z = df['Calificacion_Final']
# Crear la gráfica de dispersión 3D
ax.scatter(x, y, z, marker='o') 

# Etiquetas de los ejes
ax.set_xlabel('Horas de Estudio')
ax.set_ylabel('Asistencia a Clases')
ax.set_zlabel('Calificación Final')
ax.set_title('Relación entre Horas de Estudio, Asistencia y Calificación Final')
# Mostrar la gráfica
plt.show()
