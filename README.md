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