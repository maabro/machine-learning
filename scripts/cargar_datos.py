import pandas as pd # https://pandas.pydata.org/docs/
import os # https://docs.python.org/3/library/os.html
import csv # https://docs.python.org/3/library/csv.html
import urllib3 # https://urllib3.readthedocs.io/en/latest/user-guide.html
import json # https://docs.python.org/3/library/json.html

main_path = 'D:/curso_python/datasets'
file_name = 'titanic/titanic3.csv'
full_path = os.path.join(main_path, file_name) # carga el path completo

# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html?highlight=read_csv#pandas.read_csv
data = pd.read_csv(full_path)
# print(data.columns.values) muestra los nombres de las columnas

# Cargar cabeceras de otro archivo
data_cols = pd.read_csv(main_path + '/customer-churn-model/Customer Churn Columns.csv') # carga el nombre de las columnas
data_col_list = data_cols['Column_Names'].tolist() # lista los elementos de una columna
data2 = pd.read_csv(main_path + '/customer-churn-model/Customer Churn Model.txt',
                    header = None, names = data_col_list) # quitas las cabeceras originales y colocas las del archivo
# print(data2.columns.values)

# Cargar datos con la función open
# https://docs.python.org/3/library/functions.html#open
data3 = open(main_path + '/customer-churn-model/Customer Churn Model.txt', 'r')
cols = data3.readline().strip().split(',')
n_cols = len(cols) # numero de columnas
counter = 0
main_dict = {}
for col in cols:
    main_dict[col] = []

for line in data3:
    values = line.strip().split(',')
    for i in range(n_cols):
        main_dict[cols[i]].append(values[i])
    counter += 1
print("El data set tiene %d filas y %d columnas"%(counter,n_cols))

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
df3 = pd.DataFrame(main_dict)
# print(df3.head())

# Leer y escribir ficheros
infile = main_path + '/customer-churn-model/Customer Churn Model.txt' # fichero de lectura
outfile = main_path + '/customer-churn-model/Tab Customer Churn Model.txt' #fichero de escritura
with open(infile, 'r') as infile1: # abrir el fichero de lectura
    with open(outfile, 'w') as outfile1: # el de escritura
        for line in infile1:
            fields = line.strip().split(',') # campos de las filas, separados por comas
            outfile1.write('\t'.join(fields)) # guarda el fichero con las tabulaciones
            outfile1.write('\n') # insertar un intro despues de cada fila
df4 = pd.read_csv(outfile, sep = '\t')

# Leer datos desde URL
medals_url = 'http://winterolympicsmedals.com/medals.csv'
medals_data = pd.read_csv(medals_url)

http = urllib3.PoolManager()
r = http.request('GET', medals_url)




print(r.status)