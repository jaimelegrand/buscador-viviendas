
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Buscador de Viviendas", layout="centered")

# Título
st.title("🔍 Buscador de Datos por CHIP, Cédula o Nombre")

# Instrucciones
st.markdown("Carga un archivo Excel con los datos de viviendas y busca por **CHIP**, **cédula** o **nombre del beneficiario** para ver toda la información asociada.")

# Cargar archivo Excel
uploaded_file = st.file_uploader("📁 Sube tu archivo Excel", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df.columns = df.columns.str.strip()  # Eliminar espacios en los nombres de columna

    st.success("✅ Archivo cargado correctamente.")

    # Mostrar opciones de búsqueda
    criterio = st.selectbox("🔎 Buscar por:", ["CHIP", "CC", "NOMBRE"])
    valor = st.text_input(f"Ingrese el {criterio} exacto:")

    if valor:
        resultado = df[df[criterio].astype(str).str.upper() == valor.upper()]
        if not resultado.empty:
            st.success(f"🔎 {len(resultado)} resultado(s) encontrado(s):")
            st.dataframe(resultado, use_container_width=True)
        else:
            st.warning("⚠️ No se encontraron coincidencias con ese valor.")
else:
    st.info("📌 Esperando que cargues un archivo Excel...")
