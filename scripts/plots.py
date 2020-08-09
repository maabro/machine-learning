# Plots
import pandas as pd # https://pandas.pydata.org/docs/
import os # https://docs.python.org/3/library/os.html
import matplotlib.pyplot as plt # https://matplotlib.org/contents.html

main_path = 'D:/curso_python/datasets'
file_name = 'customer-churn-model/Customer Churn Model.txt'
full_path = os.path.join(main_path, file_name) # carga el path completo

data = pd.read_csv(full_path)

# Scatter Plot
data.plot(kind ="scatter", x="Day Mins", y="Day Charge")
# https://datacarpentry.org/python-ecology-lesson-es/08-putting-it-all-together/index.html
plt.show() # mostrar el gráfico