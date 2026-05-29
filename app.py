import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import streamlit.components.v1 as components

# ----------------------
# 🧠 DATOS SENCILLOS Y FUNCIONALES
# ----------------------
textos = [
    "hola", "buenos días", "qué tal",
    "adiós", "hasta luego",
    "quién eres", "qué eres",
    "gracias", "muchas gracias",
    "estoy bien", "estoy mal",
    "ayúdame", "dime algo"
]

etiquetas = [1,1,1, 2,2, 3,3, 4,4, 5,5, 6,6]

# 🗣️ RESPUESTAS CLARAS
respuestas = {
    1: "🤖 JARVIS: ¡Hola señor! Qué gusto saludarte. ¿En qué puedo ayudarle?",
    2: "🤖 JARVIS: Hasta luego, señor. Aquí estaré esperando su regreso.",
    3: "🤖 JARVIS: Soy JARVIS, su asistente inteligente, creado por usted para servirle.",
    4: "🤖 JARVIS: Es un placer ayudarle, señor. Su satisfacción es lo más importante.",
    5: "🤖 JARVIS: Espero que se sienta mejor pronto, señor. Estoy aquí para apoyarle.",
    6: "🤖 JARVIS: Claro que sí, señor. Dime qué necesita y lo haré de inmediato."
}

# 🎤 FUNCIÓN DE VOZ (SIN ERRORES)
def hablar(texto):
    js = f"""
    <script>
    function voz() {{
        let msg = new SpeechSynthesisUtterance(`{texto}`);
        msg.lang = "es-ES";
        msg.volume = 1;
        msg.rate = 1;
        window.speechSynthesis.speak(msg);
    }}
    voz();
    </script>
    """
    components.html(js, height=0)

# ----------------------
# ⚙️ ENTRENAMOS EL MODELO CORRECTAMENTE
# ----------------------
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(textos)
modelo = LogisticRegression(max_iter=1000)
modelo.fit(X, etiquetas)

# ----------------------
# 🎨 INTERFAZ ESTILO JARVIS
# ----------------------
st.set_page_config(page_title="JARVIS IA", page_icon="🤖", layout="wide")

# Estilo visual
st.markdown("""
<style>
    body {background-color: #000814;}
    .titulo {
        color: #00ccff;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 15px #00ccff;
    }
    .subtitulo {
        color: #80dfff;
        font-size: 24px;
        text-align: center;
        margin-bottom: 30px;
    }
    .caja {
        background-color: #001a33;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #00ccff;
        box-shadow: 0 0 20px rgba(0,204,255,0.3);
        margin: 20px;
    }
    .respuesta {
        color: #00ff88;
        font-size: 22px;
        padding: 20px;
        background-color: #00264d;
        border-radius: 10px;
        border-left: 4px solid #00ff88;
        margin-top: 20px;
    }
    .boton {
        background-color: #00ccff;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<h1 class="titulo">🤖 JARVIS - INTELIGENCIA ARTIFICIAL</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitulo">Siempre a su servicio, señor</h2>', unsafe_allow_html=True)
st.markdown("---")

# Caja de texto
st.markdown('<div class="caja">', unsafe_allow_html=True)
pregunta = st.text_input("✍️ Escribe tu mensaje:", placeholder="Ej: Hola, ¿quién eres?")
boton = st.button("🔊 HABLAR Y RESPONDER", key="boton")
st.markdown('</div>', unsafe_allow_html=True)

# Procesar
if boton and pregunta:
    # Convertimos lo que escribiste
    resultado = modelo.predict(vectorizador.transform([pregunta.lower()]))[0]
    respuesta = respuestas.get(resultado, "🤖 JARVIS: Entendido, señor. ¿Puede decirme algo más?")
    
    # Hacemos que hable
    hablar(respuesta)
    
    # Mostramos la respuesta
    st.markdown(f'<div class="respuesta">{respuesta}</div>', unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown('<p style="text-align:center; color:#80dfff;">💡 Creado por ti • JARVIS versión 1.0 🚀</p>', unsafe_allow_html=True)
