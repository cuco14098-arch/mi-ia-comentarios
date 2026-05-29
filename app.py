import streamlit as st
import math
import re

# --------------------------
# CONFIGURACIÓN BÁSICA
# --------------------------
st.set_page_config(page_title="JARVIS - ASISTENTE", layout="wide", initial_sidebar_state="collapsed")

# Guardar mensajes
if "chat" not in st.session_state:
    st.session_state.chat = []

# --------------------------
# RESPUESTAS DE JARVIS
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
# ESTILOS - SOLO LO QUE HACE FALTA
# --------------------------
st.markdown("""
<style>
    /* Fondo de pantalla */
    body {
        background: url('https://images3.alphacoders.com/861/861041.jpg') no-repeat center center fixed;
        background-size: cover;
        font-family: Arial, sans-serif;
    }

    /* OCULTAR COSAS QUE NO QUEREMOS */
    #MainMenu, footer, header, .stException, .stDeployButton {
        display: none !important;
        visibility: hidden !important;
    }

    /* TÍTULO */
    .titulo {
        text-align: center;
        font-size: 42px;
        color: #ffffff;
        text-shadow: 0 0 15px #00eeff;
        margin: 10px 0 20px 0;
    }

    /* CAJA DE CHAT (BLANCA, LETRAS NEGRAS) */
    .caja-chat {
        width: 90%;
        height: 65vh;
        margin: 0 auto 20px auto;
        background: #FFFFFF;
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

    /* BARRA DE ESCRITURA DE ABAJO */
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
    .campo {
        flex: 1;
        border: none;
        outline: none;
        font-size: 16px;
        color: #333;
        background: transparent;
        padding: 5px;
    }
    .boton {
        background: #25c26e;
        color: white;
        border: none;
        border-radius: 50%;
        width: 35px;
        height: 35px;
        font-size: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        margin-left: 10px;
    }
</style>
""", unsafe_allow_html=True)


# --------------------------
# PANTALLA PRINCIPAL
# --------------------------

# Título
st.markdown("<div class='titulo'>JARVIS - ASISTENTE INTELIGENTE</div>", unsafe_allow_html=True)

# Círculo pequeño
st.markdown("""
<div style="text-align:center; margin-bottom:15px;">
    <div style="width:55px; height:55px; background:#00eeff; border-radius:50%; display:inline-block; box-shadow:0 0 20px #00eeff;"></div>
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


# 📥 BARRA DE ESCRITURA (DONDE PUEDES ESCRIBIR Y MANDAR)
col1, col2 = st.columns([8.5, 1.5])

with col1:
    # AQUÍ ESCRIBES
    texto = st.text_input("", placeholder="Escribe tu mensaje aquí...", label_visibility="collapsed", key="entrada_mensaje")

with col2:
    # AQUÍ MANDAS (SE PUEDE PICAR SIN PROBLEMAS)
    enviar = st.button("✔️", key="boton_enviar")


# ⚙️ CUANDO DAS CLIC, SE MANDA EL MENSAJE
if enviar and texto.strip() != "":
    st.session_state.chat.append(("tu", texto))
    respuesta = responder(texto)
    st.session_state.chat.append(("jarvis", respuesta))
    st.rerun()


# Barra visible
st.markdown("""
<div class='barra-abajo'>
    <input type='text' class='campo' placeholder="Escribe tu mensaje aquí...">
    <div class='boton'>✔️</div>
</div>
""", unsafe_allow_html=True)
