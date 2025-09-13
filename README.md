Proyecto 2 - Visualización de Recursos Municipales

Este proyecto es una app desarrollada en 'Python' con 'Streamlit' para visualizar y analizar la distribución de recursos por municipios en Colombia.  
La app contiene tres municipios, que son: Barranquilla, Cali y Medellin y te permite seleccionar un municipio, ver la composición de sus recursos y explorar la información de manera gráfica e interactiva.

Funcionalidades principales

- Selección de municipios: el usuario elige un municipio desde un desplegable, puedes elegir; Medellin, Barranquilla y Cali.  
- Distribución general de recursos: gráfico circular que muestra las categorías principales (clas_gen).  
- Detalle de recursos: gráfico circular con el desglose (clasificacion_ofpuj).  
- Treemap interactivo: visualización jerárquica de la composición de recursos.  
- Mapa georreferenciado: despliega el polígono del municipio seleccionado a partir de datos geoespaciales.  

Archivos del repositorio

- app.py -> Script principal de la aplicación.  
- BCM.csv -> Base de datos en formato CSV con la información de recaudo.  
- pro212.parquet -> Archivo en formato Parquet con geometrías para los mapas.  
- requirements.txt -> Dependencias necesarias para ejecutar la app.  
- README.md -> Documentación del proyecto.  

Tecnologías utilizadas

- [Streamlit](https://streamlit.io/) ->Interfaz web interactiva.
  
Instalación y ejecución
- bash
git config --global user.name "Mauricio Andres Navarro Alonso"
git config --global user.email "maunavarro019@gmail.com"

git init
git add .
git commit -m "first commit"

git branch -M main
git remote add origin https://github.com/maunavarro19/PROYECTO2APP.git
git push -u origin main

