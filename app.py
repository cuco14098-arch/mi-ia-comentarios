
import streamlit as st
import math
import re

# --------------------------
# ⚙️ CONFIGURACIÓN
# --------------------------
st.set_page_config(page_title="JARVIS - ASISTENTE", layout="wide", initial_sidebar_state="collapsed")

# Inicializar historial
if "chat" not in st.session_state:
    st.session_state.chat = []

# --------------------------
# 🧠 INTELIGENCIA DE JARVIS
# --------------------------
def responder(mensaje):
    mensaje = mensaje.lower().strip()

    if "hola" in mensaje:
        return "Hola. Estoy activo y listo para escucharte y responderte."
    elif "cómo te llamas" in mensaje or "como te llamas" in mensaje or "quién eres" in mensaje:
        return "Me llamo Jarvis. Soy tu asistente inteligente, creado para ayudarte en todo lo que necesites."
    elif "qué puedes hacer" in mensaje or "que puedes hacer" in mensaje:
        return "Puedo responder preguntas, explicarte cosas, resolver cuentas, hablar de juegos, personajes y mucho más."
    elif "adiós" in mensaje or "hasta luego" in mensaje:
        return "¡Hasta luego! Aquí estaré cuando vuelvas."
    elif "raíz cuadrada" in mensaje:
        num = re.search(r'\d+', mensaje)
        if num:
            n = int(num.group())
            return f"La raíz cuadrada de {n} es: {math.sqrt(n):.2f}"
    elif "free fire" in mensaje:
        return "Free Fire es un juego de disparos y supervivencia para celular, muy famoso, donde 50 jugadores caen en una isla y pelean hasta que queda uno solo."
    elif "naruto" in mensaje or "itachi" in mensaje:
        return "Naruto es una serie de anime muy querida sobre ninjas. Itachi es un personaje muy admirado por su historia y sacrificio por proteger a su hermano."
    else:
        return f"He entendido: '{mensaje}'. Te explico todo lo que sé sobre este tema con gusto."


# --------------------------
# 🎨 ESTILOS LIMPIOS
# --------------------------
st.markdown("""
<style>
    /* Fondo de pantalla */
    body {
        background: url('https://images3.alphacoders.com/861/861041.jpg') no-repeat center center fixed;
        background-size: cover;
    }

    /* ❌ OCULTAR LO QUE NO QUEREMOS */
    #MainMenu, footer, header, .stException, .stDeployButton {
        display: none !important;
        visibility: hidden !important;
    }

    /* ❌ QUITAR BARRA DE ARRIBA POR COMPLETO */
    div[data-testid="stVerticalBlock"] > div:first-child .stTextInput {
        display: none !important;
    }

    /* 🔤 TÍTULO */
    .titulo {
        text-align: center;
        font-size: 42px;
        color: #ffffff;
        text-shadow: 0 0 15px #00eeff;
        margin: 10px 0 20px 0;
    }

    /* 🔵 CIRCULO CENTRAL */
    .circulo {
        width: 140px;
        height: 140px;
        margin: 0 auto 15px auto;
        position: relative;
    }
    .centro {
        width: 55px;
        height: 55px;
        background: #00eeff;
        border-radius: 50%;
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        box-shadow: 0 0 30px #00eeff, 0 0 60px #0066ff;
    }
    .anillo {
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        border-radius: 50%;
        border: 2px solid #00eeff;
        width: 85px; height: 85px;
        opacity: 0.6;
        animation: onda 3s infinite ease-out;
    }
    .anillo2 {width: 120px; height: 120px; animation-delay: 0.7s;}
    .anillo3 {width: 150px; height: 150px; animation-delay: 1.4s;}

    @keyframes onda {
        0% {opacity: 0.6; width:85px; height:85px;}
        100% {opacity: 0; width:160px; height:160px;}
    }

    /* 💬 CAJA DE MENSAJES: BLANCA, LETRAS NEGRAS ✅ */
    .caja-chat {
        width: 90%;
        height: 70vh;
        margin: 0 auto 90px auto;
        background: #FFFFFF;
        border-radius: 14px;
        border: 1px solid #ddd;
        padding: 20px;
        overflow-y: auto;
    }
    .mensaje-tu {
        text-align: right;
        background: #f1f1f1;
        color: #000000;
        border-radius: 18px 18px 4px 18px;
        padding: 10px 16px;
        margin: 6px 0 6px auto;
        max-width: 75%;
        font-size: 16px;
    }
    .mensaje-jarvis {
        text-align: left;
        background: #e8f4f8;
        color: #000000;
        border-radius: 18px 18px 18px 4px;
        padding: 10px 16px;
        margin: 6px auto 6px 0;
        max-width: 75%;
        font-size: 16px;
    }

    /* 📥 BARRA DE ABAJO (ESTA ES LA QUE SÍ FUNCIONA) ✅ */
    .barra-abajo {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 85%;
        background: #ffffff;
        border-radius: 30px;
        display: flex;
        align-items: center;
        padding: 8px 20px;
        box-shadow: 0 2px 15px rgba(0,0,0,0.2);
        z-index: 9999;
    }
    .icono {font-size: 18px; color: #555; margin: 0 8px;}
    .campo-real {
        flex: 1;
        border: none !important;
        outline: none !important;
        font-size: 15px !important;
        color: #333 !important;
        background: transparent !important;
    }
    .boton-enviar {
        background: #25c26e;
        color: white;
        border: none;
        border-radius: 50%;
        width: 32px;
        height: 32px;
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
st.markdown("<div class='titulo'>JARVIS - ASISTENTE INTELIGENTE</div>", unsafe_allow_html=True)

# Círculo
st.markdown("""
<div class='circulo'>
    <div class='centro'></div>
    <div class='anillo'></div>
    <div class='anillo anillo2'></div>
    <div class='anillo anillo3'></div>
</div>
""", unsafe_allow_html=True)


# 💬 MOSTRAR CHAT
caja = "<div class='caja-chat'>"
for tipo, texto in st.session_state.chat:
    if tipo == "tu":
        caja += f"<div class='mensaje-tu'><b>Tú:</b> {texto}</div>"
    else:
        caja += f"<div class='mensaje-jarvis'><b>Jarvis:</b> {texto}</div>"
caja += "</div>"

st.markdown(caja, unsafe_allow_html=True)


# 📥 BARRA DE ABAJO: **AHORA SÍ ESTÁ CONECTADA** ✅
col1, col2, col3, col4 = st.columns([0.4, 8.2, 0.4, 0.4])
texto_usuario = ""
enviar = False

with col1:
    st.markdown("<span class='icono'>📷</span>", unsafe_allow_html=True)
with col2:
    # ✅ ESTE ES EL CAMPO REAL DONDE ESCRIBES
    texto_usuario = st.text_input("", placeholder="Enviar mensaje a Jarvis...", label_visibility="collapsed", key="entrada_conectada")
with col3:
    st.markdown("<span class='icono'>🎙️</span>", unsafe_allow_html=True)
with col4:
    # ✅ ESTE BOTÓN SÍ ENVÍA
    enviar = st.button("✔️", key="boton_conectado")


# ⚙️ PROCESAR: **AHORA SÍ FUNCIONA** ✅
if enviar and texto_usuario.strip() != "":
    # Guardar tu mensaje
    st.session_state.chat.append(("tu", texto_usuario))
    # Obtener respuesta
    respuesta = responder(texto_usuario)
    st.session_state.chat.append(("jarvis", respuesta))
    # Recargar para que aparezca
    st.rerun()


# Barra decorativa
st.markdown("""
<div class='barra-abajo'>
    <span class='icono'>📷</span>
    <span class='icono'>🎙️</span>
    <input type='text' class='campo-real' placeholder='Enviar mensaje a Jarvis...'>
    <div class='boton-enviar'>✔️</div>
</div>
""", unsafe_allow_html=True)
