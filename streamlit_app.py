import streamlit as st

# Título principal de la aplicación
st.title("Introducción a la Supercomputación (HPC)")

# Sección 1: ¿Qué es la Supercomputación?
st.header("¿Qué es la Supercomputación?")
st.write("""
La **supercomputación** se refiere al uso de supercomputadoras, que son sistemas extremadamente potentes, capaces de realizar cálculos a velocidades inmensamente superiores a las computadoras convencionales. 
Esto permite resolver problemas complejos en diversas áreas, como:
- Simulaciones científicas
- Modelado climático
- Genómica
- Predicción del tiempo y más.
""")

# Sección 2: Recursos para HPC
st.header("Recursos para HPC")
st.subheader("1. Procesadores de Alto Rendimiento (CPU/GPU)")
st.write("""
La clave de la supercomputación está en los procesadores optimizados para realizar tareas masivas en paralelo:
- **CPU (Unidades de Procesamiento Central)**: Procesan las tareas generales.
- **GPU (Unidades de Procesamiento Gráfico)**: Son capaces de manejar grandes volúmenes de operaciones paralelas, ideales para simulaciones y procesamiento de datos masivo.
""")

st.subheader("2. Sistemas de Archivos Paralelos")
st.write("""
El almacenamiento y acceso a datos es fundamental. Los **sistemas de archivos paralelos**, como **Lustre** o **GPFS**, permiten que múltiples nodos de una supercomputadora accedan a archivos simultáneamente, mejorando la eficiencia del procesamiento.
""")

st.subheader("3. Redes de Baja Latencia")
st.write("""
La velocidad de las redes que interconectan los nodos de una supercomputadora es crucial. Las redes de baja latencia, como **InfiniBand**, permiten una comunicación más rápida entre los diferentes componentes, minimizando los tiempos de espera y optimizando el rendimiento general.
""")

# Sección 3: Comandos para Administración de Servidores
st.header("Comandos para Administración de Servidores")
st.write("""
Para administrar los sistemas HPC, los siguientes comandos de Linux son útiles:
""")

st.code("""
# Monitorea procesos activos
top            

# Monitorea procesos de forma interactiva con más opciones
htop           

# Muestra el uso de disco de forma humanamente legible
df -h          

# Muestra el estado de la memoria
free -h        

# Verifica el uso de la red
ifconfig       
""")

# Sección 4: Distribuciones Linux para HPC
st.header("Distribuciones Linux Comunes para HPC")
st.write("""
En entornos HPC, se prefieren ciertas distribuciones Linux que son robustas, estables y optimizadas para tareas intensivas. Algunas de las más comunes incluyen:
""")

st.subheader("1. CentOS")
st.write("""
CentOS es popular en clusters HPC debido a su estabilidad y compatibilidad con software especializado de supercomputación. Es una opción gratuita derivada de Red Hat Enterprise Linux (RHEL).
""")

st.subheader("2. Ubuntu Server")
st.write("""
Ubuntu Server es otra opción muy usada por su facilidad de uso y la gran comunidad que lo respalda. También ofrece compatibilidad con muchos paquetes de software científicos y de simulación.
""")

st.subheader("3. SUSE Linux Enterprise Server (SLES)")
st.write("""
SLES es una distribución empresarial utilizada en varios supercomputadores del mundo. Es conocida por su rendimiento y soporte especializado para HPC, especialmente en ambientes empresariales.
""")

# Sección 5: ¿Es posible utilizar una HPC en Windows?
st.header("¿Es posible utilizar una HPC en Windows?")
st.write("""
Aunque la mayoría de los entornos HPC están optimizados para sistemas basados en Linux, es posible utilizar HPC en **Windows** a través de herramientas específicas como:
- **Windows Subsystem for Linux (WSL)**: Permite ejecutar un entorno Linux dentro de Windows, facilitando el acceso a herramientas comunes en HPC.
- **Microsoft HPC Pack**: Un conjunto de herramientas para implementar y gestionar clusters de alto rendimiento en sistemas Windows.
- **Azure para HPC**: Microsoft ofrece soluciones de HPC en la nube a través de su plataforma Azure, que es compatible tanto con Windows como con Linux.

Sin embargo, la comunidad científica y empresarial que utiliza supercomputación sigue prefiriendo distribuciones Linux debido a su flexibilidad, rendimiento y compatibilidad con las bibliotecas y frameworks HPC.
""")
