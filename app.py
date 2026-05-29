
import streamlit as st
import math
import re

# ⚙️ CONFIGURACIÓN
st.set_page_config(page_title="JARVIS - ASISTENTE", layout="wide", initial_sidebar_state="collapsed")

# Historial de mensajes
if "chat" not in st.session_state:
    st.session_state.chat = []

# 🧠 RESPUESTAS DE JARVIS
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


# 🎨 ESTILOS - SOLO OCULTAMOS LO DE STREAMLIT, NO TOCAMOS NUESTRAS BARRAS
st.markdown("""
<style>
    /* Fondo de pantalla */
    body {
        background: url('https://images3.alphacoders.com/861/861041.jpg') no-repeat center center fixed;
        background-size: cover;
        font-family: Arial, sans-serif;
    }

    /* ❌ OCULTAR SOLO EL MENÚ, PIE DE PÁGINA Y ERRORES */
    #MainMenu, footer, header, .stException, .stDeployButton {
        display: none !important;
        visibility: hidden !important;
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

    /* 💬 CAJA DE CHAT (BLANCA, LETRAS NEGRAS) */
    .caja-chat {
        width: 90%;
        height: 65vh;
        margin: 20px auto;
        background: #FFFFFF !important;
        border-radius: 14px;
        border: 1px solid #ddd;
        padding: 20px;
        overflow-y: auto;
        color: #000000 !important;
    }
    .mensaje-tu {
        text-align: right;
        background: #f1f1f1;
        color: #000000 !important;
        border-radius: 18px 18px 4px 18px;
        padding: 10px 16px;
        margin: 6px 0 6px auto;
        max-width: 75%;
    }
    .mensaje-jarvis {
        text-align: left;
        background: #e8f4f8;
        color: #000000 !important;
        border-radius: 18px 18px 18px 4px;
        padding: 10px 16px;
        margin: 6px auto 6px 0;
        max-width: 75%;
    }

    /* 🟢 ESTILO DE LA BARRA QUE SÍ SE QUEDA (LA DE ARRIBA) */
    .barra-arriba {
        width: 90%;
        margin: 0 auto;
        display: flex;
        gap: 10px;
        align-items: center;
        background: white;
        padding: 8px 15px;
        border-radius: 25px;
        box-shadow: 0 1px 4px #ccc;
    }
</style>
""", unsafe_allow_html=True)


# --------------------------
# PANTALLA PRINCIPAL
# --------------------------

# Título
st.markdown("<div class='titulo'>JARVIS - ASISTENTE INTELIGENTE</div>", unsafe_allow_html=True)

# Círculo animado
st.markdown("""
<div class='circulo'>
    <div class='centro'></div>
    <div class='anillo'></div>
    <div class='anillo anillo2'></div>
    <div class='anillo anillo3'></div>
</div>
""", unsafe_allow_html=True)


# 🟢 >>>> AQUÍ ESTÁ LA BARRA DE ARRIBA, LA ÚNICA QUE EXISTE Y SE QUEDA <<<<
st.markdown("<div class='barra-arriba'>", unsafe_allow_html=True)
col1, col2 = st.columns([9, 1])

with col1:
    # AQUÍ ESCRIBES, ESTÁ VISIBLE Y FUNCIONA
    texto = st.text_input("", placeholder="Escribe tu mensaje aquí...", label_visibility="collapsed", key="barra_unica_definitiva")

with col2:
    # AQUÍ ESTÁ EL BOTÓN, SE PUEDE PULSAR
    enviar = st.button("✔️", key="boton_unico_definitivo")

st.markdown("</div>", unsafe_allow_html=True)


# ⚙️ FUNCIÓN DE ENVIAR
if enviar and texto.strip() != "":
    st.session_state.chat.append(("tu", texto))
    respuesta = responder(texto)
    st.session_state.chat.append(("jarvis", respuesta))
    st.rerun()


# 💬 CAJA DE CHAT
caja = "<div class='caja-chat'>"
for tipo, texto_mensaje in st.session_state.chat:
    if tipo == "tu":
        caja += f"<div class='mensaje-tu'><b>Tú:</b> {texto_mensaje}</div>"
    else:
        caja += f"<div class='mensaje-jarvis'><b>Jarvis:</b> {texto_mensaje}</div>"
caja += "</div>"

st.markdown(caja, unsafe_allow_html=True)


# ❌ >>>> AQUÍ NO HAY NADA, NO ESCRIBÍ NINGUNA BARRA DE ABAJO, POR ESO NO APARECE <<<<
