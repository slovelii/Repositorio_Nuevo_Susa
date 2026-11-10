import random
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configuración de la página
st.set_page_config(
    page_title="SpeedSketch Studio - Retos de Dibujo",
    page_icon="⚡",
    layout="wide"
)

# --- ESTILOS CSS Y TIPOGRAFÍAS ARTÍSTICAS ---
st.markdown("""
    <style>
    /* Importar una tipografía moderna y geométrica para artistas */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');

    /* Aplicar tipografía a toda la app */
    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
    }

    /* Estilo general oscuro tipo estudio de diseño digital */
    .stApp {
        background-color: #0e1117;
        color: #f0f2f6;
    }

    /* Barra lateral estilizada */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }

    /* Títulos atractivos */
    h1 {
        color: #58a6ff;
        font-weight: 700;
        letter-spacing: -1px;
    }
    
    h2, h3 {
        color: #79c0ff;
    }

    /* Caja de retos personalizada */
    .challenge-box {
        background: linear-gradient(135deg, #1f6feb22 0%, #23863622 100%);
        border: 2px dashed #58a6ff;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .challenge-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #ffa657;
    }
    </style>
""", unsafe_allow_html=True)

# Lista de retos de dibujo rápido
retos_dibujo = [
    "🤖 Un robot cocinando comida tradicional en 2 minutos.",
    "🐙 Un pulpo DJ en una fiesta espacial.",
    "🏰 Un castillo flotante hecho completamente de dulces.",
    "🐱 Un gato ninja saltando entre azoteas borrosas.",
    "🍄 Un hongo gigante que sirve de faro para naves diminutas.",
    "🐉 Un dragón diminuto durmiendo plácidamente sobre una taza de té caliente.",
    "🌵 Un cactus con gafas de sol surfeando en una ola de neón.",
    "🚀 Un astronauta persiguiendo un sombrero volador en la gravedad cero."
]

# Inicializar el estado del reto actual si no existe
if 'current_challenge' not in st.session_state:
    st.session_state.current_challenge = random.choice(retos_dibujo)

# Interfaz Principal
st.title("⚡ SpeedSketch Studio")
st.markdown("### *Entrena tu agilidad mental y visual con retos de dibujo rápido.*")

# Sección del Reto Actual
st.markdown(
    f"""
    <div class="challenge-box">
        <div class="challenge-title">🎯 RETO ACTIVO:</div>
        <h2 style="color: #f0f2f6; margin-top: 5px;">{st.session_state.current_challenge}</h2>
    </div>
    """,
    unsafe_allow_html=True
)

col_btn1, col_btn2, _ = st.columns([1, 1, 2])
with col_btn1:
    if st.button("🎲 Cambiar de Reto"):
        st.session_state.current_challenge = random.choice(retos_dibujo)
        st.rerun()

st.write("") # Espaciador

# Configuración en la Barra Lateral
with st.sidebar:
    st.subheader("🎨 Controles del Estudio")

    st.markdown("---")
    st.subheader("📏 Lienzo")
    canvas_width = st.slider("Ancho del tablero", 300, 800, 600, 50)
    canvas_height = st.slider("Alto del tablero", 200, 700, 400, 50)

    st.markdown("---")
    st.subheader("🖌️ Herramientas")
    # Drawing mode selector
    drawing_mode = st.selectbox(
        "Herramienta:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    # Stroke width slider
    stroke_width = st.slider('Ancho de línea', 1, 30, 8)

    st.markdown("---")
    st.subheader("🎨 Paleta y Fondo")
    # Stroke color picker
    stroke_color = st.color_picker("Color de trazo", "#58a6ff")

    # Background color
    bg_color = st.color_picker("Color de fondo", "#0d1117")

# Contenedor central del Canvas
st.markdown("#### ✏️ Tu Espacio de Creación:")
canvas_result = st_canvas(
    fill_color="rgba(88, 166, 255, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",
)
