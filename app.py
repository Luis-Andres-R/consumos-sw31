import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Título de la app
st.title("Consumos SW31")

# Nombre del archivo donde se guardarán los datos
archivo_datos = "consumos.csv"

# Cargar datos existentes si el archivo ya existe
if os.path.exists(archivo_datos):
    st.session_state.datos = pd.read_csv(archivo_datos)
else:
    st.session_state.datos = pd.DataFrame(columns=["Fecha", "kWh"])

# Área de ingreso de datos
st.header("Ingresar Consumo")
fecha = st.date_input("Fecha", value=datetime.today())
kwh = st.number_input("kWh", min_value=0.0, step=0.1)

if st.button("Guardar Consumo"):
    nuevo_dato = pd.DataFrame({"Fecha": [fecha], "kWh": [kwh]})
    st.session_state.datos = pd.concat([st.session_state.datos, nuevo_dato], ignore_index=True)
    # Guardar los datos en el archivo CSV
    st.session_state.datos.to_csv(archivo_datos, index=False)
    st.success("Consumo guardado correctamente!")

# Mostrar los datos ingresados
st.header("Datos Registrados")
st.dataframe(st.session_state.datos)

# Revisión del total del consumo
if not st.session_state.datos.empty:
    st.header("Revisión de Datos")
    st.write("Valores ingresados en kWh:", st.session_state.datos["kWh"].tolist())
    total_consumo = st.session_state.datos["kWh"].sum()
    st.header("Total del Consumo")
    st.write(f"{total_consumo:.2f} kWh")
else:
    st.write("Ingresa al menos un dato para calcular el total.")