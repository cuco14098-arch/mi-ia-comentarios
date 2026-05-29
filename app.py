import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import streamlit.components.v1 as components

# ----------------------
# 🧠 DATOS SENCILLOS
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

# 🗣️ RESPUESTAS CLARAS Y LARGAS
respuestas = {
    1: "🤖 JARVIS: ¡Hola señor! Qué gusto saludarte. Espero que tengas un día maravilloso. ¿En qué puedo servirte hoy, con toda mi atención?",
    2: "🤖 JARVIS: Hasta luego, señor. Aquí estaré esperando con mucho gusto su regreso. Que tenga un día excelente y todo le salga perfecto.",
    3: "🤖 JARVIS: Soy JARVIS, su asistente personal de inteligencia artificial. Fui creado por usted con mucho cuidado y dedicación, para estar siempre a su servicio y ayudarle en todo lo que necesite.",
    4: "🤖 JARVIS: Es un verdadero placer ayudarle, señor. Su satisfacción es mi única prioridad, y haré todo lo posible para que se sienta cómodo y atendido en todo momento.",
    5: "🤖 JARVIS: Lamento mucho escuchar eso, señor. Si está triste o se siente mal, recuerde que aquí estoy para acompañarle y apoyarle. Todo mejorará muy pronto, se lo prometo.",
    6: "🤖 JARVIS: Por supuesto que sí, señor. Dime con mucho detalle qué es lo que necesita, y lo haré de inmediato con la mayor eficiencia y cuidado que se merece."
}

# 🎤 FUNCIÓN DE VOZ MEJORADA: MÁS LENTA, MÁS CLARA, NO SE CORTA
def hablar(texto):
    # Código corregido: voz lenta, clara y no se corta
    codigo = f"""
    <script>
    function reproducirVoz() {{
        const mensaje = new SpeechSynthesisUtterance("{texto}");
        mensaje.lang = "es-ES";
        mensaje.volume = 1;        // Volumen alto
        mensaje.rate = 0.9;        // Voz LENTA y CLARA (antes era 1, ahora es 0.9)
        mensaje.pitch = 1.1;      // Tono agradable
        // Reproducir la voz
        window.speechSynthesis.speak(mensaje);
    }}
    // Ejecutar la función
    reproducirVoz();
    </script>
    """
    # Mostramos el código para que funcione
    components.html(codigo, height=0)

# ----------------------
# ⚙️ ENTRENAMOS EL MODELO
# ----------------------
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(textos)
modelo = LogisticRegression(max_iter=200)  # Más iteraciones para que no haya errores
modelo.fit(X, etiquetas)

# ----------------------
# 🎨 INTERFAZ ESTILO JARVIS
# ----------------------
st.set_page_config(page_title="JARVIS IA", page_icon="🤖", layout="wide")

# Diseño visual
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
        line-height: 1.6;  // Espacio entre líneas para que se lea mejor
    }
    .boton {
        background-color: #00ccff;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        padding: 12px 25px;
        border: none;
        width: 100%;
        font-size: 18px;
    }
    .boton:hover {
        background-color: #00eeff;
        box-shadow: 0 0 15px #00eeff;
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
boton = st.button("🔊 HABLAR Y RESPONDER", key="boton", help="Jarvis te contestará con voz clara y lenta")
st.markdown('</div>', unsafe_allow_html=True)

# Procesar
if boton and pregunta:
    # Convertimos lo que escribiste
    resultado = modelo.predict(vectorizador.transform([pregunta.lower()]))[0]
    respuesta = respuestas.get(resultado, "🤖 JARVIS: Entendido perfectamente, señor. Estoy aquí para escucharte y ayudarte en todo lo que necesites.")
    
    # 🎤 ¡AQUÍ HABLA, LENTO Y CLARO!
    hablar(respuesta)
    
    # Mostramos la respuesta
    st.markdown(f'<div class="respuesta">{respuesta}</div>', unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown('<p style="text-align:center; color:#80dfff;">💡 Creado por ti • JARVIS versión 1.1 🚀</p>', unsafe_allow_html=True)
