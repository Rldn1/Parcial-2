"""
Manual de instalación de Plotly en Python

Plotly es una biblioteca de Python que permite crear gráficos interactivos y visualizaciones avanzadas.

1. Requisitos previos
Antes de instalar Plotly, asegúrate de tener:
- Python 3.7 o superior instalado.
- El gestor de paquetes pip actualizado.
Verifica las versiones con los siguientes comandos:
python --version
pip --version
Para actualizar pip:
python -m pip install --upgrade pip

2. Instalación básica
Para instalar Plotly, ejecuta el siguiente comando en la terminal o consola:
pip install plotly
Esto descargará e instalará la versión más reciente junto con sus dependencias.

3. Verificar instalación
Abre Python y ejecuta:
import plotly
print(plotly.__version__)
Si no se muestra ningún error, la instalación fue correcta.

4. Ejemplo de prueba
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="Ejemplo de gráfico con Plotly")
fig.show()
Si el gráfico se muestra correctamente, Plotly está funcionando.

5. Recursos adicionales
Documentación oficial de Plotly: https://plotly.com/python/getting-started/ 
"""