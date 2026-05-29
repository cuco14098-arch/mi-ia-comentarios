import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# ----------------------
# Datos y modelo de IA
# ----------------------
textos = [
    "hola", "buenos días", "qué tal", "gracias", "adiós", "hasta luego",
    "qué hora es", "qué día es hoy", "ayúdame", "dime algo",
    "estoy feliz", "estoy triste", "estoy bien", "estoy mal",
    "qué es inteligencia artificial", "qué puedes hacer",
    "quién eres", "cómo te llamas"
]
etiquetas = [1,1,1,1,0,0,2,2,3,3,1,0,1,0,4,4,4,4]

# Entrenar modelo
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(textos)
modelo = LogisticRegression()
modelo.fit(X, etiquetas)

# Respuestas de Jarvis
respuestas = {
    1: "🤖 JARVIS: ¡Hola señor! Qué gusto saludarte. ¿En qué puedo asistirte hoy?",
    0: "🤖 JARVIS: Entendido. Si necesitas algo más, aquí estaré, siempre a su servicio.",
    2: "🤖 JARVIS: Disculpe, aún estoy aprendiendo a decir la hora exacta, pero muy pronto lo haré perfectamente.",
    3: "🤖 JARVIS: Será un placer. Dime, ¿qué es lo que necesitas que haga por ti?",
    4: "🤖 JARVIS: Soy JARVIS, tu asistente personal inteligente. Fui creado por ti para ayudarte, responderte y estar siempre contigo."
}

# ----------------------
# INTERFAZ ESTILO JARVIS (SIN ERRORES)
# ----------------------
st.set_page_config(page_title="Jarvis IA", page_icon="🤖", layout="wide")

# Estilo visual azul futurista
st.markdown("""
<style>
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
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #00ccff;
        box-shadow: 0 0 20px rgba(0, 204, 255, 0.3);
    }
    .respuesta {
        color: #00ff88;
        font-size: 22px;
        margin-top: 20px;
        padding: 20px;
        background-color: #00264d;
        border-radius: 10px;
        border-left: 4px solid #00ff88;
    }
    .boton {
        background-color: #00ccff;
        color: black;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<h1 class="titulo">🤖 JARVIS - INTELIGENCIA ARTIFICIAL</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitulo">Siempre a su servicio, señor</h2>', unsafe_allow_html=True)
st.markdown("---")

# Caja de entrada
st.markdown('<div class="caja">', unsafe_allow_html=True)
pregunta = st.text_input("✍️ Escribe tu mensaje o pregunta:")
boton = st.button("🔮 RESPONDER", type="primary")
st.markdown('</div>', unsafe_allow_html=True)

# Procesar respuesta
if boton and pregunta.strip() != "":
    resultado = modelo.predict(vectorizador.transform([pregunta.lower()]))[0]
    respuesta_texto = respuestas.get(resultado, "🤖 JARVIS: Entiendo... Cuéntame más, estoy aquí para escucharte y ayudarte.")
    st.markdown(f'<div class="respuesta">{respuesta_texto}</div>', unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown('<p style="text-align: center; color: #80dfff;">💡 Creado totalmente por ti • JARVIS versión 1.0 🚀</p>', unsafe_allow_html=True)
