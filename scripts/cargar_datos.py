# Carga de los datos
import pandas as pd # https://pandas.pydata.org/docs/
import os # https://docs.python.org/3/library/os.html
import csv # https://docs.python.org/3/library/csv.html
import urllib3 # https://urllib3.readthedocs.io/en/latest/user-guide.html

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
counter = 0
main_dict = {}
for col in cols:
    main_dict[col] = []

for line in data3:
    values = line.strip().split(',')
    for i in range(len(cols)):
        main_dict[cols[i]].append(values[i]) # cada valor a su respectiva columna
    counter += 1
print("El data set tiene %d filas"%(counter))

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
df3 = pd.DataFrame(main_dict) # convertimos el diccionario en un dataframe
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

# https://stackoverflow.com/questions/50187537/how-to-print-a-csv-content-from-remote-url-using-python-3-x
http = urllib3.PoolManager()
r = http.request('GET', medals_url)
data_map = "".join(map(chr, r.data)) # map convierte a char cada elemento del array
data_split = data_map.split('\n') # intro
# for row in data_split:
    # print(row.split(','))

str_data = r.data.decode('utf-8') # el string binario lo decodificamos a utf
lines = str_data.split('\n') # sacamos las filas
col_names = lines[0].split(',')
n_cols = len(col_names) # guardamos la cabecera, la primera linea
cnt = 0
main_dict = {} # crear el diccionario
for col in lines[0].split(','):
    main_dict[col] = []
for line in lines:
    if(counter > 0): # salta la cabecera que esta en n_cols
        values = line.strip().split(',') # separamos por comas
        for i in range(n_cols):
            main_dict[col_names[i]].append(values[i])
    cnt += 1

medals_df = pd.DataFrame(main_dict)
medals_df.to_csv(main_path + '/athletes/downloaded_medals.csv')
medals_df.to_excel(main_path + '/athletes/downloaded_medals.xls')
medals_df.to_json(main_path + '/athletes/downloaded_medals.json')

# Abrir ficheros XLS y XLSX
file_name1 = 'titanic/titanic3.xls' # o titanic3.xlsx
titanic2 = pd.read_excel(main_path + '/' + file_name1, "titanic3") # el segundo argumento es la hoja del excel
# convierte en distintos formatos
titanic2.to_csv(main_path + '/titanic/titanic_custom.csv')
titanic2.to_excel(main_path + '/titanic/titanic_custom.xls')
titanic2.to_json(main_path + '/titanic/titanic_custom.json')