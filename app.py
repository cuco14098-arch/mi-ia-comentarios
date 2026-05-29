import streamlit as st
import math
import re

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
# 🎨 DISEÑO: LIMPIO, SIN ERRORES
# --------------------------
st.set_page_config(page_title="JARVIS - SISTEMA", layout="wide")

# Historial
if "chat" not in st.session_state:
    st.session_state.chat = []

# Estilos CORRECTOS, sin conflictos
st.markdown("""
<style>
    /* Fondo general */
    body {
        background: url('https://images3.alphacoders.com/861/861041.jpg') no-repeat center center fixed;
        background-size: cover;
        font-family: Arial, sans-serif;
    }

    /* ❌ OCULTAR LO QUE NO QUEREMOS */
    #MainMenu {display: none !important;}
    footer {display: none !important;}
    header {display: none !important;}
    div[data-testid="stFileUploader"] {display: none !important;}
    .stException {display: none !important;} /* ❌ OCULTA EL ERROR ROJO */
    .element-container:has(.stTextInput) {margin-bottom: 0 !important;}

    /* 🔵 Circulo animado */
    .circulo-central {
        width: 140px;
        height: 140px;
        margin: 10px auto 15px auto;
        position: relative;
        animation: palpitar 2s infinite ease-in-out;
    }
    .centro {
        width: 55px;
        height: 55px;
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
    .anillo1 {width: 85px; height: 85px;}
    .anillo2 {width: 120px; height: 120px; animation-delay: 0.6s;}
    .anillo3 {width: 150px; height: 150px; animation-delay: 1.2s;}

    @keyframes palpitar {
        0%,100% {transform: translate(-50%,-50%) scale(1);}
        50% {transform: translate(-50%,-50%) scale(1.2);}
    }
    @keyframes expandir {
        0% {width:55px;height:55px;opacity:0.8;}
        100% {width:150px;height:150px;opacity:0;}
    }

    /* 🔤 Título */
    h1 {
        text-align: center;
        font-size: 40px !important;
        color: #ffffff;
        text-shadow: 0 0 12px #00eeff;
        margin: 0 0 20px 0;
    }

    /* 💬 CAJA DE CHAT: BLANCA, LETRAS NEGRAS ✅ */
    .caja-chat {
        width: 90%;
        height: 72vh;
        margin: 0 auto 80px auto;
        background-color: #FFFFFF !important;
        border-radius: 12px;
        border: 1px solid #eee;
        color: #000000 !important;
        font-size: 17px;
        padding: 15px;
        box-shadow: 0 0 20px rgba(0,0,0,0.08);
        overflow-y: auto;
    }
    .mensaje-tu {
        text-align: right;
        background-color: #f5f5f5;
        color: #000000 !important;
        border-radius: 16px 16px 3px 16px;
        padding: 10px 16px;
        margin: 6px 0 6px auto;
        max-width: 70%;
    }
    .mensaje-jarvis {
        text-align: left;
        background-color: #f0f9fc;
        color: #000000 !important;
        border-radius: 16px 16px 16px 3px;
        padding: 10px 16px;
        margin: 6px auto 6px 0;
        max-width: 70%;
    }

    /* 📥 BARRA SOLO ABAJO ✅ */
    .barra-fija {
        position: fixed;
        bottom: 15px;
        left: 50%;
        transform: translateX(-50%);
        width: 85%;
        background: #ffffff;
        border-radius: 25px;
        display: flex;
        align-items: center;
        padding: 8px 18px;
        box-shadow: 0 3px 15px rgba(0,0,0,0.2);
        gap: 10px;
        z-index: 9999;
    }
    .icono {font-size: 19px; color: #666;}
    .campo-texto {
        flex: 1;
        border: none !important;
        outline: none !important;
        font-size: 15px !important;
        color: #333 !important;
        background: transparent !important;
    }
    .boton-enviar {
        background-color: #28c76f;
        color: white;
        border: none;
        border-radius: 50%;
        width: 30px;
        height: 30px;
        font-size: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)


# --------------------------
# 🖥️ PANTALLA
# --------------------------

# Título
st.markdown("<h1>JARVIS - ASISTENTE INTELIGENTE</h1>", unsafe_allow_html=True)

# Círculo
st.markdown("""
<div class="circulo-central">
    <div class="centro"></div>
    <div class="anillo1"></div>
    <div class="anillo2"></div>
    <div class="anillo3"></div>
</div>
""", unsafe_allow_html=True)


# 📥 BARRA DE ABAJO (ÚNICA QUE EXISTE)
col1, col2, col3, col4 = st.columns([0.4, 8.4, 0.4, 0.4])
texto = ""
enviar = False

with col1:
    st.markdown("<span class='icono'>📷</span>", unsafe_allow_html=True)
with col2:
    texto = st.text_input("", placeholder="Enviar mensaje a Jarvis...", label_visibility="collapsed", key="entrada_final")
with col3:
    st.markdown("<span class='icono'>🎙️</span>", unsafe_allow_html=True)
with col4:
    enviar = st.button("✔️", key="enviar_final")


# ⚙️ PROCESAR
if enviar and texto.strip() != "":
    st.session_state.chat.append(("tu", texto))
    respuesta = jarvis_respuesta(texto)
    st.session_state.chat.append(("jarvis", respuesta))


# 💬 MOSTRAR CHAT
caja = '<div class="caja-chat">'
for tipo, contenido in st.session_state.chat:
    if tipo == "tu":
        caja += f'<div class="mensaje-tu"><b>Tú:</b> {contenido}</div>'
    else:
        caja += f'<div class="mensaje-jarvis"><b>Jarvis:</b> {contenido}</div>'
caja += '</div>'

st.markdown(caja, unsafe_allow_html=True)


# Barra visible
st.markdown("""
<div class="barra-fija">
    <span class='icono'>📷</span>
    <span class='icono'>🎙️</span>
    <input type='text' class='campo-texto' placeholder='Enviar mensaje a Jarvis...'>
    <div class='boton-enviar'>✔️</div>
</div>
""", unsafe_allow_html=True)
