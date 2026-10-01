import streamlit as st
import os

# ==========================================
# 1. CONFIGURACIÓN DE PÁGINA
# ==========================================
st.set_page_config(
    page_title="Portafolio IA | Estiven Serna", 
    page_icon="🧠", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. INYECCIÓN DE CSS (DISEÑO Y ANIMACIONES)
# ==========================================
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .title-gradient {
        font-size: 2.8rem;
        font-weight: 700;
        background: -webkit-linear-gradient(45deg, #4A00E0, #8E2DE2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .app-card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        margin-bottom: 1rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    /* Modo oscuro compatible */
    @media (prefers-color-scheme: dark) {
        .app-card {
            background-color: #1e1e1e;
            border: 1px solid #333;
        }
    }

    .app-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==========================================
# 3. BARRA LATERAL (PERFIL)
# ==========================================
with st.sidebar:
    st.title("Estiven Serna")
    st.subheader("Estudiante de Diseño Interactivo | 6to Semestre")
    st.write("Apasionado por la integración de tecnologías inmersivas, inteligencia artificial y narrativas visuales.")
    st.divider()
    st.write("📍 Medellín, Colombia")
    st.write("🔗 [Mi LinkedIn](#)")
    st.write("🔗 [Mi GitHub](#)")

# ==========================================
# 4. BASE DE DATOS DE LAS 10 APLICACIONES
# ==========================================
apps_ia = [
    {
        "titulo": "Detección de Objetos",
        "tag": "Computer Vision / YOLO",
        "icono": "👁️",
        "desc": "Esta aplicación utiliza redes neuronales convolucionales para identificar y localizar múltiples objetos dentro de una imagen en tiempo real, trazando cajas delimitadoras con sus respectivas etiquetas y niveles de confianza.",
        "url": "https://yolov5cmc.streamlit.app/"
    },
    {
        "titulo": "WordCloud Studio",
        "tag": "NLP / Data Viz",
        "icono": "☁️",
        "desc": "Genera nubes de palabras dinámicas a partir de textos extensos. Esta herramienta de procesamiento de lenguaje natural resalta los términos más frecuentes, facilitando el análisis visual rápido de grandes volúmenes de datos textuales.",
        "url": "#"
    },
    {
        "titulo": "Traductor Neuronal",
        "tag": "Sequence-to-Sequence",
        "icono": "🌐",
        "desc": "Rompe las barreras del idioma con esta herramienta de traducción automática. Capaz de interpretar y convertir texto entre múltiples idiomas con alta precisión, conservando el contexto y la semántica original de las oraciones.",
        "url": "#"
    },
    {
        "titulo": "Demo TF-IDF en Español",
        "tag": "Information Retrieval",
        "icono": "📊",
        "desc": "Descubre la relevancia de las palabras en tus documentos. Esta aplicación implementa el algoritmo TF-IDF para extraer conceptos clave y analizar la importancia relativa de los términos en un corpus específico de textos en español.",
        "url": "#"
    },
    {
        "titulo": "Análisis de Sentimiento",
        "tag": "Clasificación de Texto",
        "icono": "🎭",
        "desc": "Evalúa el tono emocional detrás de las palabras. Esta herramienta clasifica textos según su polaridad (positiva, negativa o neutral), siendo ideal para analizar opiniones de usuarios o interacciones masivas en redes sociales.",
        "url": "#"
    },
    {
        "titulo": "Traductor de Imágenes",
        "tag": "OCR + Translation",
        "icono": "📸",
        "desc": "Combina tecnología OCR con modelos de traducción automática. Al subir una imagen que contenga texto en otro idioma, la aplicación extrae los caracteres procesables y los traduce instantáneamente a tu idioma de preferencia.",
        "url": "#"
    },
    {
        "titulo": "Reconocimiento Óptico (OCR)",
        "tag": "Optical Character Recognition",
        "icono": "📄",
        "desc": "Digitaliza texto impreso o escrito con facilidad. Esta herramienta extrae la información contenida en imágenes o documentos escaneados, transformándolos en texto completamente editable mediante algoritmos de visión artificial.",
        "url": "#"
    },
    {
        "titulo": "Agente de IA",
        "tag": "LLM / Conversational",
        "icono": "🤖",
        "desc": "Interactúa con un asistente virtual impulsado por modelos de lenguaje grande (LLM). Este agente está diseñado para comprender intenciones, mantener el contexto de la conversación y resolver consultas complejas de manera natural.",
        "url": "https://dataagente.streamlit.app/"
    },
    {
        "titulo": "Analizador de PDF con LLM",
        "tag": "RAG / Document AI",
        "icono": "📚",
        "desc": "Sube tus documentos PDF y chatea con ellos. Esta aplicación utiliza Generación Aumentada por Recuperación (RAG) para extraer información clave, resumir textos largos y responder preguntas precisas sobre tus propios archivos.",
        "url": "https://chatpdf-cc.streamlit.app/"
    },
    {
        "titulo": "Mi Primera App IA",
        "tag": "Prototipo Base",
        "icono": "🚀",
        "desc": "Un espacio de experimentación y prueba de conceptos básicos. Aquí se exploran integraciones iniciales de modelos de machine learning y estructuras de interfaz, sentando las bases para aplicaciones interactivas más robustas.",
        "url": "#"
    }
]

# ==========================================
# 5. CONTENIDO PRINCIPAL (PESTAÑAS)
# ==========================================
st.markdown('<p class="title-gradient">Portafolio de Proyectos</p>', unsafe_allow_html=True)
st.write("Explora mis herramientas desarrolladas con Inteligencia Artificial y mi perfil creativo.")

# Creación de pestañas (La de IA es la principal)
tab1, tab2 = st.tabs(["🧠 Aplicaciones de Inteligencia Artificial", "🎬 Extra: Enfoque Audiovisual y 3D"])

with tab1:
    st.write("### Mis Desarrollos en IA")
    st.write("A continuación, una colección de aplicaciones prácticas de Inteligencia Artificial, que abarcan desde Visión por Computadora hasta Procesamiento de Lenguaje Natural.")
    st.write("---")
    
    # Grid de 2 columnas para mostrar las 10 apps
    col1, col2 = st.columns(2)
    
    for i, app in enumerate(apps_ia):
        # Distribución equitativa: pares a la izquierda, impares a la derecha
        col = col1 if i % 2 == 0 else col2
        
        with col:
            # Uso de HTML dentro de Streamlit para crear el efecto "Tarjeta" con CSS
            st.markdown(f"""
            <div class="app-card">
                <h3 style="margin-top: 0;">{app['icono']} {app['titulo']}</h3>
                <p style="color: #888; font-size: 0.9em; font-weight: bold; margin-bottom: 10px;">🏷️ {app['tag']}</p>
                <p>{app['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Botón de enlace nativo de Streamlit justo debajo de la tarjeta HTML
            st.link_button(f"🔗 Abrir {app['titulo']}", app['url'], use_container_width=True)
            st.write("") # Espaciador


with tab2:
    st.write("### Perfil Creativo e Interactivo")
    st.write("Como estudiante de Diseño Interactivo, mi perfil también está fuertemente enfocado en la **animación y la creación audiovisual a través de estilos 3D y 2D**.")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.info("**Programas y Herramientas que domino:**")
        st.write("✔️ **3D y Animación:** Blender, Maya")
        st.write("✔️ **Composición Visual:** After Effects")
        st.write("✔️ **Desarrollo Interactivo:** Unity (C# / XR)")
        st.write("✔️ **VJing y Generativo:** TouchDesigner, Resolume")
        
    with col4:
        st.success("**Enfoque Profesional:**")
        st.write("""
        Busco crear narrativas visuales y experiencias inmersivas que conecten con los usuarios, 
        fusionando la programación, el diseño de interfaces y el arte digital para explorar nuevas 
        formas de interacción ciberfísica y virtual.
        """)
