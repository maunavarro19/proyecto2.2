import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import geopandas as gpd

data = pd.read_csv("BCM.csv")
gdf = gpd.read_parquet("pro212.parquet")

st.title("Proyecto 2")

munis = data["entidad"].unique().tolist()

mun = st.selectbox("Seleccione un municipio: ",
             munis)

filtro = data[data["entidad"] == mun]



gen = (filtro
       .groupby("clas_gen")["total_recaudo"]
       .sum())

total_gen = gen.sum()

gen = (gen / total_gen).round(2)

det = (filtro
       .groupby("clasificacion_ofpuj")["total_recaudo"]
       .sum())

total_det = det.sum()

det = (det / total_det).round(3)



# Pie chart Para el primer gráfico

colores_personalizados = ["#1D2783", "#3a4a52", "#b11738"]  

fig1 = px.pie(
    names=gen.index,
    values=gen.values,
    title="Distribución General de Recursos",
    color_discrete_sequence=colores_personalizados
)
st.plotly_chart(fig1)

# Para el segundo gráfico no se muestra  
fig2 = px.pie(
    names=det.index,
    values=det.values,
    title="Detalle de Recursos"
)


# tree map 

fin = (filtro
       .groupby(["clas_gen", "clasificacion_ofpuj"])["total_recaudo"]
       .sum()
       .reset_index())

colores_personalizados2 = ["#1D2783", "#3a4a52", "#b11738"]
fig = px.treemap(fin, path=[px.Constant("Total"),
                            "clas_gen",
                            "clasificacion_ofpuj"],
                            values="total_recaudo",
                            color_discrete_sequence=colores_personalizados2)

st.plotly_chart(fig)

#mapa georef

filtro2 = gdf[gdf["entidad"] == mun][["codigo_alt", "geometry"]]

fig, ax = plt.subplots(1, 1)

filtro2.plot(ax=ax)

ax.set_axis_off()

st.pyplot(fig)