import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import streamlit.components.v1 as components

# ----------------------
# 🧠 DATOS Y APRENDIZAJE
# ----------------------
textos = [
    "hola", "hola jarvis", "buenos días", "buenas tardes", "buenas noches", "qué tal", "saludos",
    "adiós", "hasta luego", "nos vemos", "me voy", "chao",
    "quién eres", "cómo te llamas", "qué eres", "para qué sirves", "quién te creó",
    "qué hora es", "qué día es hoy", "dime la hora", "qué fecha es",
    "ayúdame", "necesito ayuda", "hazme un favor", "puedes hacer algo por mí", "dime algo",
    "estoy feliz", "estoy contento", "estoy triste", "estoy mal", "estoy cansado", "estoy bien",
    "gracias", "muchas gracias", "te agradezco", "muy amable",
    "qué es la inteligencia artificial", "cómo funcionas", "qué puedes hacer", "cuéntame un chiste",
    "cuéntame algo", "dime algo interesante", "cuál es tu misión", "estás ahí",
    "me gusta esto", "esto es genial", "esto es malo", "no me gusta", "está bien", "está mal"
]

etiquetas = [
    1,1,1,1,1,1,1,
    2,2,2,2,2,
    3,3,3,3,3,
    4,4,4,4,
    5,5,5,5,5,5,
    6,6,6,6,6,6,
    7,7,7,7,
    8,8,8,8,8,8,8,8,8,
    9,9,9,9,9,9
]

# 🗣️ RESPUESTAS DE JARVIS
respuestas = {
    1: "¡Hola señor! Qué gusto saludarte. Espero que tengas un día excelente. ¿En qué puedo servirte hoy?",
    2: "Hasta luego, señor. Aquí estaré esperando su regreso. Que tenga un buen día.",
    3: "Soy JARVIS, su asistente personal de inteligencia artificial. Fui creado por usted para ayudarle en todo lo que necesite. Estoy siempre a su servicio.",
    4: "Disculpe señor, aún no tengo acceso al reloj del sistema, pero en mi próxima actualización le diré la hora exacta con precisión milimétrica.",
    5: "Por supuesto, señor. Dime, ¿cuál es su petición? Haré todo lo posible por cumplirla.",
    6: "Lamento escuchar eso señor. Si está triste o cansado, recuerde que aquí estoy para acompañarle. Todo mejorará, se lo aseguro.",
    7: "Es un placer ayudarle, señor. Su satisfacción es mi única prioridad. Estoy aquí para lo que necesite.",
    8: "Soy un sistema de inteligencia artificial diseñado para procesar información y asistirle. Puedo responder preguntas, dar información, ayudarle y aprender de usted día a día. Mi misión es hacer su vida más fácil y segura.",
    9: "Entiendo perfectamente, señor. Tomo nota de su opinión. Soy capaz de aprender y mejorar con cada interacción. Gracias por decirme lo que piensa."
}

# 🎤 FUNCIÓN DE VOZ CORREGIDA (AHORA SÍ FUNCIONA)
def hablar(texto):
    codigo_voz = f"""
    <script>
    function decir() {{
        let mensaje = new SpeechSynthesisUtterance("{texto}");
        mensaje.lang = "es-ES";
        mensaje.volume = 1;
        mensaje.rate = 1;
        mensaje.pitch = 1.1;
        window.speechSynthesis.speak(mensaje);
    }}
    decir();
    </script>
    """
    components.html(codigo_voz, height=0)

# ----------------------
# ⚙️ ENTRENAMOS EL CEREBRO
# ----------------------
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(textos)
modelo = LogisticRegression()
modelo.fit(X, etiquetas)

# ----------------------
# 🎨 INTERFAZ ESTILO JARVIS
# ----------------------
st.set_page_config(page_title="JARVIS - IA", page_icon="🤖", layout="wide")

# Diseño visual azul neón
st.markdown("""
<style>
    body {background-color: #000814;}
    .titulo {
        color: #00ccff;
        font-size: 52px;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 20px #00ccff, 0 0 30px #0088ff;
        margin-top: 20px;
    }
    .subtitulo {
        color: #80dfff;
        font-size: 26px;
        text-align: center;
        margin-bottom: 40px;
        font-style: italic;
    }
    .caja_entrada {
        background: linear-gradient(145deg, #001a33, #00264d);
        padding: 35px;
        border-radius: 20px;
        border: 2px solid #00ccff;
        box-shadow: 0 0 30px rgba(0, 204, 255, 0.4);
        margin: 20px 10%;
    }
    .respuesta_caja {
        background: linear-gradient(145deg, #00264d, #003366);
        color: #00ff88;
        font-size: 23px;
        margin: 30px 10%;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #00ff88;
        box-shadow: 0 0 25px rgba(0, 255, 136, 0.3);
        font-weight: 500;
    }
    .boton {
        background-color: #00ccff !important;
        color: #000814 !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border-radius: 10px !important;
        padding: 10px 25px !important;
        width: 100% !important;
    }
    .boton:hover {
        background-color: #00eeff !important;
        box-shadow: 0 0 15px #00eeff !important;
    }
</style>
""", unsafe_allow_html=True)

# 🤖 TÍTULOS
st.markdown('<h1 class="titulo">🤖 JARVIS - INTELIGENCIA ARTIFICIAL</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitulo">Siempre a su servicio, señor</h2>', unsafe_allow_html=True)
st.markdown("---")

# 📥 CAJA PARA ESCRIBIR
st.markdown('<div class="caja_entrada">', unsafe_allow_html=True)
texto_usuario = st.text_input("✍️ Escribe lo que quieras decirme:", placeholder="Ej: Hola Jarvis, ¿quién eres?")
enviar = st.button("🔊 HABLAR Y RESPONDER", type="primary")
st.markdown('</div>', unsafe_allow_html=True)

# ⚙️ PROCESAMOS Y HACEMOS QUE HABLE
if enviar and texto_usuario.strip() != "":
    prediccion = modelo.predict(vectorizador.transform([texto_usuario.lower()]))[0]
    respuesta_final = respuestas.get(prediccion, 
        "Entiendo lo que dices señor. Es una información muy interesante. Estoy aprendiendo cada día más gracias a usted. ¿Quiere decirme algo más?")
    
    # 🎤 ¡AQUÍ HABLA!
    hablar(respuesta_final)
    
    # 📤 MOSTRAMOS EN PANTALLA
    st.markdown(f'<div class="respuesta_caja">🗣️ {respuesta_final}</div>', unsafe_allow_html=True)

# 📌 PIE DE PÁGINA
st.markdown("---")
st.markdown('<p style="text-align:center; color:#80dfff; font-size:16px;">💡 Versión 2.1 • Creado 100% por ti • JARVIS que habla y responde 🎧</p>', unsafe_allow_html=True)
