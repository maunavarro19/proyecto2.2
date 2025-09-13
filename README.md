Proyecto 2 - Visualización de Recursos Municipales

Este proyecto es una app desarrollada en 'Python' con 'Streamlit' para visualizar y analizar la distribución de recursos por municipios en Colombia.  
La app contiene tres municipios, que son: Barranquilla, Cali y Medellin y te permite seleccionar un municipio, ver la composición de sus recursos y explorar la información de manera gráfica e interactiva.

Elección de municipios

- Se depuraron tres municipios: Medellin, Cali y Barranquilla
- La aplicación carga el listado de municipios desde el archivo `BCM.csv`.  
- El usuario puede elegir un municipio específico mediante un menú desplegable.  
- Una vez seleccionado, los gráficos y mapas se actualizan automáticamente para reflejar la información de ese municipio.

Variables y transformaciones

Los datos provienen de los archivos `BCM.csv` y `pro212.parquet`:

Variables principales:

  - `entidad`: nombre del municipio.  
  - `clas_gen`: clasificación general de los recursos.  
  - `clasificacion_ofpuj`: clasificación detallada.  
  - `total_recaudo`: monto total recaudado.  

Transformaciones aplicadas:

  - Cálculo de participaciones porcentuales (`total_recaudo` relativo al total del municipio).  
  - Agrupaciones por categorías generales y detalladas.  
  - Generación de gráficos circulares (pie charts) y un treemap jerárquico para visualizar proporciones.  
  - Integración con `GeoPandas` para representar la geometría del municipio en un mapa.  


Limitaciones de los datos

- Los resultados dependen de la calidad y cobertura de los archivos `BCM.csv` y `pro212.parquet`.  
- Los valores de recaudo pueden estar sujetos a errores de registro o diferencias en la metodología de recolección.  
- La resolución espacial de los datos geográficos puede limitar el nivel de detalle en los mapas.  
- La aplicación está pensada como herramienta exploratoria; no sustituye análisis estadísticos más profundos.

URL de la app: https://proyecto212.streamlit.app/



