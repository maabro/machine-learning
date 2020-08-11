# Plots
import pandas as pd # https://pandas.pydata.org/docs/
import numpy as np
import os # https://docs.python.org/3/library/os.html
import matplotlib.pyplot as plt # https://matplotlib.org/contents.html

main_path = 'D:/curso_python/datasets'
file_name = 'customer-churn-model/Customer Churn Model.txt'
full_path = os.path.join(main_path, file_name) # carga el path completo

data = pd.read_csv(full_path)

print(data.head())

# Scatter Plot
figure, axs = plt.subplots(2,2, sharey=True, sharex=True)
data.plot(kind ="scatter", x="Day Mins", y="Day Charge", ax=axs[0][0])
data.plot(kind ="scatter", x="Night Mins", y="Night Charge", ax=axs[0][1])
data.plot(kind ="scatter", x="Day Calls", y="Day Charge", ax=axs[1][0])
data.plot(kind ="scatter", x="Night Calls", y="Night Charge", ax=axs[1][1])

# https://datacarpentry.org/python-ecology-lesson-es/08-putting-it-all-together/index.html
plt.show() # mostrar el gráfico

# Histograma de frecuencias
k = int(np.ceil(1+np.log2(3333))) # https://es.wikipedia.org/wiki/Regla_de_Sturges
plt.hist(data['Day Calls'], bins = k) # https://matplotlib.org/3.3.0/api/_as_gen/matplotlib.pyplot.hist.html
plt.xlabel("Número de llamadas al día")
plt.ylabel("Frecuencia")
plt.title("Histograma del número de llamadas al día")

plt.show()

# Boxplot, diagrama de caja y bigotes
plt.boxplot(data['Day Calls']) # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.boxplot.html
plt.ylabel("Número de llamadas diarias")
plt.title("Boxplot de las llamadas diarias")

plt.show()