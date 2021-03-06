# Machine learning: Data science con Python
Apuntes básicos sobre el curso de data science con python.
## Entorno virtual con python
Comprobar las versiones instaladas de python y el instalador pip:
```
python --version
pip3 --version
```
Si hay que actualizar pip:
```
python -m pip install --upgrade pip
```
Comprobar lista de paquetes del instalador:
```
pip3 list
```
### Instalar el paquete Virtualenv
```
pip3 install virtualenv
```
Para comprobar la versión:
```
virtualenv --version
```
### Crear un entorno virtual
```
virtualenv test
```
### Iniciar el entorno virtual
```
./test/Scripts/activate
```
Para desactivarla usar:
```
deactivate
```
## Instalación de paquetes necesarios
- [pandas](https://pandas.pydata.org/docs/index.html)
```
pip3 install pandas
```
- [NumPy](https://numpy.org/)
```
pip3 install Numpy
```
- [matplotlib](https://matplotlib.org/)
```
pip3 install matplotlib
```
- [ipython](https://ipython.org/index.html)
```
pip3 install ipython
```
- [scikit-learn](https://scikit-learn.org/stable/)
```
pip3 install scikit-learn
```
- [urllib3](https://pypi.org/project/urllib3/)
```
pip3 install urllib3
```
- [xlrd](https://xlrd.readthedocs.io/en/latest/) opt. para abrir ficheros xls y xlsx
```
pip3 install xlrd
```
- [xlwt](https://xlwt.readthedocs.io/en/latest/) opt. para escribir ficheros xls y xlsx
```
pip3 install xlwt
```
## Introducción
### Proceso
1. Buscar el objetivo, lo que queremos estimar o predecir.
2. Los datos que tenemos, filtrarlos, etc.
3. Explorar datos, visualizarlos en gráficos, buscar patrones.
4. Crear los modelos de datos y evaluarlos.
5. Comprobar los resultados, en producción.
### Tipos de análisis
- **Retrospectivo:** ir hacia atrás, partir del efecto para llegar a la causa.
- **Predictivo:** ir hacia delante.
### Modelos predictivos
**Algoritmos**
Crean ecuaciones matemáticas basados en datos históricos. La elección depende de los datos.
- Algoritmos supervisados: necesarios datos históricos y parámetros que haya devuelto el modelo.
- Algoritmos no supervisados: no hay variables históricas.

**Datos históricos**
El modelo se construye sobre los datos pasados. Practica común, dividir los datos pasados en dos conjuntos:
- Entrenamiento, que actúa de dato histórico.
- Validación, que actúa de dato futuro.
Varias técnicas para dividir los datos históricos.

**Modelos**
El modelo devuelve una función matemática. Que tiene unos parámetros que deben de ser obtenidos de los datos históricos.
Tipos de ecuaciones:
- [Regresión lineal](https://es.wikipedia.org/wiki/Regresi%C3%B3n_lineal)
- [Regresión logística](https://es.wikipedia.org/wiki/Regresi%C3%B3n_log%C3%ADstica)

**Conocimiento para los modelos predictivos**
- Estadística
- Algoritmos
- Negocio

Andrew Lang dijo:
> Él usa la estadística como un borracho utiliza las farolas: para el apoyo en lugar de para la iluminación.
## Limpieza de datos
Utilizaremos el paquete pandas para la limpieza de datos. Los datos se organizan en un **dataset** (un fichero), cuando este fichero se carga dentro de un programa pasa a ser un **dataframe**.
### Valores que faltan
Los valores que faltan en un **dataset** pueden venir por dos razones:
- Extracción de los datos: cuando se extraen los datos de una BD por ejemplo, puede contener errores que generen un NaN. La solución optimizando el sistema de extracción.
- Recolección de los datos: cuando se obtienen los datos, algunos de ellos no existen.

No se pueden hacer operaciones sobre valores que falten. Hay varios métodos para solucionar el problema de los valores que faltan en el **dataset**:
- Borrar directamente los valores que faltan, solución agresiva.
- Substituir los valores faltantes:
  - Remplazar todos los NaN por el mismo valor.
  - Remplazar por columnas y añadir el valor más indicado.
  - Remplazar todos por un valor estadístico (mediana, ...)

## Manejo de datos
### Data Wrangling
Proceso de transformar y mapear los datos de un dataset.
- [Cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)