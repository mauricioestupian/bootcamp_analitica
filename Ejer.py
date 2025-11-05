import pandas as pd
import matplotlib.pyplot as plt

# Datos de ejemplo
datos = {
    'Nombre': ['Ana Torres', 'Luis Gómez', 'María López', 'Carlos Ruiz'],
    'Edad': [28, 35, 22, 40],
    'Sexo': ['F', 'M', 'F', 'M'],
    'Correo': ['ana.torres@email.com', 'luis.gomez@email.com', 'maria.lopez@email.com', 'carlos.ruiz@email.com']
}

# Crear el DataFrame
df_personas = pd.DataFrame(datos)

# Mostrar el DataFrame
print(df_personas)

# Agrupar los datos por la columna "Sexo" y calcular la suma de las edades
df_edades = df_personas.groupby("Sexo")['Edad'].sum()

# Gradico torta desde el DataFrame
df_edades.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightpink'], title='Distribución de Edad por Sexo')
plt.show()

#Grfico torta con matplotlib
plt.pie(df_edades, labels=df_edades.index.to_list(), autopct='%1.1f%%', startangle=0)
plt.title('Distribución de Edad por Sexo')
plt.show()


