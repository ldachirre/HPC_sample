import streamlit as st

# Título de la aplicación
st.title("Introducción a HPC")

# Secciones de la página
st.header("¿Qué es la Supercomputación?")
st.write("La supercomputación es el uso de supercomputadoras para realizar cálculos masivos y complejos en menor tiempo que una computadora estándar...")

st.header("Recursos para HPC")
st.write("- Procesadores de alto rendimiento (CPU/GPU)")
st.write("- Sistemas de archivos paralelos")
st.write("- Redes de baja latencia")

st.header("Comandos para Administración de Servidores")
st.code("""
# Ejemplo de algunos comandos básicos
top            # Monitorea procesos activos
htop           # Monitorea de forma interactiva
df -h          # Muestra uso de disco
""")

st.header("Distribuciones Linux para HPC")
st.write("Las distros más comunes son:")
st.write("- CentOS")
st.write("- Ubuntu Server")
st.write("- SUSE Linux Enterprise Server (SLES)")
