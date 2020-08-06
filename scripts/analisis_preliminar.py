# Análisis preliminar
import pandas as pd # https://pandas.pydata.org/docs/
import os # https://docs.python.org/3/library/os.html

main_path = 'D:/curso_python/datasets'
file_name = 'titanic/titanic3.csv'
full_path = os.path.join(main_path, file_name) # carga el path completo

data = pd.read_csv(full_path)
data.head() # printa n columnas del principio
data.tail() # printa n columnas del final
data.shape # printa las dimensiones
data.columns.values # printa los valores de las cabeceras de la tabla

# Resumen de los estadísticos básicos de variables númericas
data.describe() # printa estadísticos básicos
# count cuenta, mean el promedio, std desviación estandar, min valor mínimo,
# max valor máximo, cuantiles
data.dtypes # devuelve los tipos de datos

# Valores que faltan
pd.isnull(data['body']) # si son nulos
pd.notnull(data['body']) # si no lo son

pd.isnull(data['body']).values.ravel().sum() # suma los valores que son nulos
# https://numpy.org/doc/stable/reference/generated/numpy.ravel.html
pd.notnull(data['body']).values.ravel().sum() # suma los valores que no son nulos

# Borrado de valores que faltan
data.dropna(axis=0, how='all') # borra una fila si todas las columnas contienen NaN
data2 = data
data2.dropna(axis=0, how='any') # borra una fila si alguna de las columnas contien NaN

# Remplazar los valores faltantes
data3 = data
data3.fillna(0) # rellena los NaN con 0

data5 = data # hacer el remplazo por columnas, añadiendo lo más indicado
data5['body'] = data5['body'].fillna(0)
data5['home.dest'] = data5['home.dest'].fillna('Desconocida')

# Estadística
data5['age'].fillna(data['age'].mean()) # rellena los NaN con el promedio de la columna.
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html
data5['age'].fillna(method='ffill') # rellena los NaN con el primer valor conocido hacia delante.
data5['age'].fillna(method='backfill') # rellena los NaN el primer valor conocido hacia atras.

# Variables dummy
# sirve para separar variables categoricas
dummy_sex = pd.get_dummies(data['sex'], prefix = 'sex') # coniverte la columna sex en dos columnas que toman valores 1 o 0 dependiendo el género.
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html

data.drop(['sex'], axis=1) # borramos la columna sex
pd.concat([data, dummy_sex], axis=1) # concatena el dataset original con las dos columnas nuevas.

def createDummies(df, var_name):
    dummy = pd.get_dummies(df[var_name], prefix = var_name)
    df = df.drop(var_name, axis = 1)
    df = pd.concat([df, dummy], axis=1)
    return df