import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pyttsx3
import threading

# ----------------------
# Datos y modelo de IA
# ----------------------
textos = [
    "hola", "buenos días", "qué tal", "gracias", "adiós", "hasta luego",
    "qué hora es", "qué día es hoy", "ayúdame", "dime algo",
    "estoy feliz", "estoy triste", "estoy bien", "estoy mal",
    "qué es inteligencia artificial", "qué puedes hacer"
]
etiquetas = [1,1,1,1,0,0,2,2,3,3,1,0,1,0,4,4]

# Entrenar modelo
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(textos)
modelo = LogisticRegression()
modelo.fit(X, etiquetas)

# Respuestas de Jarvis
respuestas = {
    1: "¡Hola! Qué gusto saludarte. ¿En qué te puedo ayudar?",
    0: "Entiendo, si necesitas algo más aquí estoy para ti.",
    2: "La hora actual es... (próximamente te diré la hora exacta)",
    3: "Claro que sí, dime qué necesitas y lo haré por ti.",
    4: "Soy tu asistente inteligente, puedo responder preguntas, ayudarte y acompañarte en lo que quieras."
}

# ----------------------
# Función para hablar (voz)
# ----------------------
def hablar(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    engine.say(texto)
    engine.runAndWait()

# ----------------------
# INTERFAZ ESTILO JARVIS
# ----------------------
st.set_page_config(page_title="Jarvis IA", page_icon="🤖", layout="wide")

# Estilo visual
st.markdown("""
<style>
    .titulo {color: #00ccff; font-size: 48px; font-weight: bold; text-align: center;}
    .subtitulo {color: #80dfff; font-size: 24px; text-align: center; margin-bottom: 30px;}
    .caja {background-color: #001a33; padding: 20px; border-radius: 15px; border: 2px solid #00ccff;}
    .respuesta {color: #00ff88; font-size: 22px; margin-top: 20px; padding: 15px; background-color: #00264d; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<h1 class="titulo">🤖 JARVIS - INTELIGENCIA ARTIFICIAL</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitulo">Tu asistente personal inteligente</h2>', unsafe_allow_html=True)
st.markdown("---")

# Caja de entrada
st.markdown('<div class="caja">', unsafe_allow_html=True)
pregunta = st.text_input("✍️ Escribe tu pregunta o mensaje:")
boton = st.button("🔮 RESPONDER COMO JARVIS")
st.markdown('</div>', unsafe_allow_html=True)

# Procesar respuesta
if boton and pregunta:
    # Predecir tipo de pregunta
    resultado = modelo.predict(vectorizador.transform([pregunta.lower()]))[0]
    respuesta_texto = respuestas.get(resultado, "¡Interesante! Cuéntame más sobre eso.")
    
    # Mostrar respuesta
    st.markdown(f'<div class="respuesta">🗣️ JARVIS: {respuesta_texto}</div>', unsafe_allow_html=True)
    
    # Reproducir voz (en algunos navegadores funciona, en otros necesitas activar el audio)
    threading.Thread(target=hablar, args=(respuesta_texto,)).start()

# Pie de página
st.markdown("---")
st.markdown('<p style="text-align: center; color: #80dfff;">💡 Creado por ti - Como Jarvis, siempre a tu servicio 🚀</p>', unsafe_allow_html=True)
