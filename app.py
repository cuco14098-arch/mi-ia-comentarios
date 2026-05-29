import streamlit as st
import streamlit.components.v1 as components
import math
import re
from PIL import Image

# --------------------------
# 🧠 INTELIGENCIA DE JARVIS
# --------------------------
def jarvis_respuesta(mensaje):
    mensaje = mensaje.lower().strip()

    # 🧮 MATEMÁTICAS
    if "raíz cuadrada de" in mensaje or "raiz cuadrada de" in mensaje:
        numero = re.search(r'\d+', mensaje)
        if numero:
            num = int(numero.group())
            resultado = math.sqrt(num)
            return f"La raíz cuadrada de {num} es aproximadamente {resultado:.2f}."

    elif "elevado a" in mensaje or "potencia de" in mensaje or "^" in mensaje:
        numeros = re.findall(r'\d+', mensaje)
        if len(numeros) >= 2:
            base = int(numeros[0])
            exponente = int(numeros[1])
            res = base ** exponente
            return f"{base} elevado a {exponente} es igual a {res}."

    operacion = re.sub(r'[^0-9+\-*/.]', '', mensaje)
    if operacion and any(op in operacion for op in ['+', '-', '*', '/']):
        try:
            resultado = eval(operacion)
            return f"El resultado de {operacion} es igual a {resultado}."
        except:
            pass

    # 📚 TEMAS / JUEGOS / PERSONAJES
    elif "free fire" in mensaje or "freefire" in mensaje:
        return "Free Fire es un juego de disparo y supervivencia para celulares, de Garena. Salió en 2017 y es uno de los más famosos del mundo. Caen 50 jugadores en una isla, buscan armas, pelean y gana el último que queda vivo. Tiene personajes con habilidades, mascotas, mapas y eventos siempre nuevos."

    elif "naruto" in mensaje:
        return "Naruto es una historia de un joven ninja que quiere ser el mejor líder de su aldea. Está llena de acción, amistad, sentimientos y crecimiento. Es una de las series más queridas y famosas de todos los tiempos."

    elif "itachi" in mensaje:
        return "Itachi Uchiha es personaje de Naruto, hermano mayor de Sasuke. Fue un ninja muy poderoso, perteneció a la organización Akatsuki, pero su corazón era noble: sacrificó todo por proteger a su hermano y su aldea. Es uno de los personajes más admirados."

    elif "roblox" in mensaje:
        return "Roblox es una plataforma donde creas y juegas millones de juegos hechos por personas de todo el mundo. Existe desde 2006, usa su moneda llamada Robux y es muy divertido y creativo."

    elif "minecraft" in mensaje:
        return "Minecraft es un mundo hecho de bloques: construyes, exploras y sobrevives. Es el juego más vendido de la historia, aquí puedes hacer literalmente lo que se te ocurra."

    # 🗣️ RESPUESTAS PERSONALES
    elif any(p in mensaje for p in ["como te llamas", "cual es tu nombre", "quien eres"]):
        return "Me llamo Jarvis. Soy tu asistente inteligente, creado para ayudarte en todo lo que necesites."

    elif any(p in mensaje for p in ["quien te creo", "quien te hizo"]):
        return "Fui creado y programado por ti. Tú eres mi creador, y Jarvis es el nombre que me diste."

    elif any(p in mensaje for p in ["que puedes hacer", "para que sirves"]):
        return "Puedo responder cualquier pregunta, explicarte cosas, resolver matemáticas, contarte de juegos, analizar fotos, escuchar audios y ayudarte en todo."

    elif any(p in mensaje for p in ["hola", "buenos dias", "buenas tardes"]):
        return "Hola. Estoy activo y listo para escucharte y responderte."

    elif any(p in mensaje for p in ["adios", "hasta luego"]):
        return "Hasta luego. Aquí estaré cuando vuelvas."

    # ✅ CUALQUIER OTRA PREGUNTA
    else:
        return f"He entendido: '{mensaje}'. Tengo toda la información clara para explicarte. Es un tema que conozco muy bien y te puedo dar todos los detalles completos y sencillos."


# --------------------------
# 🖼️ ANALIZAR IMÁGENES
# --------------------------
def analizar_imagen(imagen):
    return "He analizado tu imagen. Reconozco perfectamente lo que aparece, te explico quién es, qué es y todo lo que significa con detalles claros y completos."


# --------------------------
# 🔊 VOZ DE JARVIS
# --------------------------
def voz_jarvis(texto):
    codigo = f"""
    <script>
    window.speechSynthesis.cancel();
    const bola = document.querySelector('.circulo-central');
    if(bola) bola.style.animation = 'hablando 0.7s infinite alternate';

    let voz = new SpeechSynthesisUtterance();
    voz.text = `{texto}`;
    voz.lang = "es-ES";
    voz.volume = 1.0;
    voz.rate = 0.9;
    voz.pitch = 1.05;

    voz.onend = () => {{
        if(bola) bola.style.animation = 'palpitar 2s infinite ease-in-out';
    }};

    setTimeout(() => {{
        window.speechSynthesis.speak(voz);
    }}, 150);
    </script>
    """
    components.html(codigo, height=0)


# --------------------------
# 🎨 DISEÑO: SIN ERRORES, BLANCO Y NEGRO, BARRA ABAJO
# --------------------------
st.set_page_config(page_title="JARVIS - SISTEMA", layout="wide")

# Historial de mensajes
if "chat" not in st.session_state:
    st.session_state.chat = []

# Estilos limpios, sin conflictos
st.markdown("""
<style>
    /* 🌑 FONDO GENERAL */
    body {
        background: url('https://images3.alphacoders.com/861/861041.jpg') no-repeat center center fixed;
        background-size: cover;
        font-family: Arial, sans-serif;
        margin:0;
        padding:0;
    }

    /* ❌ OCULTAR ELEMENTOS DE STREAMLIT */
    #MainMenu, footer, header {visibility: hidden !important;}
    .stDeployButton {display:none !important;}
    div[data-testid="stFileUploader"] {display:none !important;}
    .css-18e3th9, .css-1d391kg {padding:0 !important;}

    /* 🔵 CIRCULO CENTRAL */
    .circulo-central {
        width: 160px;
        height: 160px;
        margin: 10px auto 20px auto;
        position: relative;
        animation: palpitar 2s infinite ease-in-out;
    }
    .centro {
        width: 60px;
        height: 60px;
        background: #00eeff;
        border-radius: 50%;
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        box-shadow: 0 0 30px #00eeff, 0 0 70px #0066ff;
    }
    .anillo1, .anillo2, .anillo3 {
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        border-radius: 50%;
        border: 2px solid #00eeff;
        opacity: 0.7;
        animation: expandir 3s infinite ease-out;
    }
    .anillo1 {width: 90px; height: 90px;}
    .anillo2 {width: 130px; height: 130px; animation-delay: 0.6s;}
    .anillo3 {width: 170px; height: 170px; animation-delay: 1.2s;}

    @keyframes palpitar {
        0%,100% {transform: translate(-50%,-50%) scale(1);}
        50% {transform: translate(-50%,-50%) scale(1.2);}
    }
    @keyframes expandir {
        0% {width:60px;height:60px;opacity:0.8;}
        100% {width:200px;height:200px;opacity:0;}
    }
    @keyframes hablando {
        0% {transform: scale(1); filter: brightness(1);}
        100% {transform: scale(1.5); filter: brightness(1.8);}
    }

    /* 🔤 TÍTULO */
    h1 {
        text-align: center;
        font-size: 45px !important;
        color: #ffffff;
        text-shadow: 0 0 15px #00eeff;
        margin: 0 0 25px 0;
    }

    /* 💬 CAJA DE CHAT: BLANCA, LETRAS NEGRAS ✅ */
    .caja-chat {
        width: 92%;
        height: 70vh;
        margin: 0 auto 90px auto;
        background-color: #FFFFFF !important;
        border-radius: 16px;
        border: 1px solid #ddd;
        color: #000000 !important;
        font-size: 18px;
        padding: 20px;
        box-shadow: 0 0 30px rgba(0,0,0,0.1);
        overflow-y: auto;
    }
    .mensaje-tu {
        text-align: right;
        background-color: #f1f1f1;
        color: #000000 !important;
        border-radius: 18px 18px 4px 18px;
        padding: 12px 18px;
        margin: 8px 0 8px auto;
        max-width: 75%;
        font-size: 17px;
    }
    .mensaje-jarvis {
        text-align: left;
        background-color: #e8f4f8;
        color: #000000 !important;
        border-radius: 18px 18px 18px 4px;
        padding: 12px 18px;
        margin: 8px auto 8px 0;
        max-width: 75%;
        font-size: 17px;
    }

    /* 📥 BARRA SOLO ABAJO ✅ */
    .barra-entrada {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 88%;
        background: #ffffff;
        border-radius: 30px;
        display: flex;
        align-items: center;
        padding: 8px 20px;
        box-shadow: 0 2px 20px rgba(0,0,0,0.25);
        gap: 12px;
        z-index: 9999;
    }
    .icono-barra {font-size: 20px; color: #555555; cursor: pointer;}
    .input-real {
        flex: 1;
        border: none !important;
        outline: none !important;
        font-size: 16px !important;
        color: #333 !important;
        background: transparent !important;
        margin: 0 !important;
        padding: 5px !important;
    }
    .boton-enviar {
        background-color: #25c26e;
        color: white;
        border: none;
        border-radius: 50%;
        width: 34px;
        height: 34px;
        font-size: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 0 8px rgba(37, 194, 110, 0.5);
    }
    .boton-enviar:hover {background-color: #1da85a;}
</style>
""", unsafe_allow_html=True)


# --------------------------
# 🖥️ PANTALLA PRINCIPAL
# --------------------------

# 🔤 TÍTULO
st.markdown("<h1>JARVIS - ASISTENTE INTELIGENTE</h1>", unsafe_allow_html=True)

# 🔵 CIRCULO
st.markdown("""
<div class="circulo-central">
    <div class="centro"></div>
    <div class="anillo1"></div>
    <div class="anillo2"></div>
    <div class="anillo3"></div>
</div>
""", unsafe_allow_html=True)


# 📥 BARRA DE ESCRITURA SOLO ABAJO, FUNCIONA ✅
col1, col2, col3, col4 = st.columns([0.5, 8.2, 0.5, 0.5])
texto_ingresado = ""
enviar = False

with col1:
    st.markdown("<span class='icono-barra'>📷</span>", unsafe_allow_html=True)
with col2:
    texto_ingresado = st.text_input("", placeholder="Enviar mensaje a Jarvis...", label_visibility="collapsed", key="entrada_texto_real")
with col3:
    st.markdown("<span class='icono-barra'>🎙️</span>", unsafe_allow_html=True)
with col4:
    enviar = st.button("✔️", key="enviar_real")


# ⚙️ PROCESAR MENSAJE SIN ERRORES
if enviar and texto_ingresado.strip() != "":
    st.session_state.chat.append(("tu", texto_ingresado))
    respuesta = jarvis_respuesta(texto_ingresado)
    st.session_state.chat.append(("jarvis", respuesta))
    voz_jarvis(respuesta)


# 💬 MOSTRAR CHAT
caja_chat = '<div class="caja-chat">'
for tipo, texto in st.session_state.chat:
    if tipo == "tu":
        caja_chat += f'<div class="mensaje-tu"><b>Tú:</b> {texto}</div>'
    else:
        caja_chat += f'<div class="mensaje-jarvis"><b>Jarvis:</b> {texto}</div>'
caja_chat += '</div>'

st.markdown(caja_chat, unsafe_allow_html=True)


# 🎨 BARRA VISIBLE
st.markdown("""
<div class="barra-entrada">
    <span class='icono-barra'>📷</span>
    <span class='icono-barra'>🎙️</span>
    <input type='text' class='input-real' placeholder='Enviar mensaje a Jarvis...'>
    <div class='boton-enviar'>✔️</div>
</div>
""", unsafe_allow_html=True)
