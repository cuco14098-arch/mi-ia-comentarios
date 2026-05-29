import streamlit as st
import math
import re

# ⚙️ CONFIGURACIÓN
st.set_page_config(page_title="JARVIS", layout="wide", initial_sidebar_state="collapsed")

# Historial
if "chat" not in st.session_state:
    st.session_state.chat = []

# 🧠 Respuestas
def responder(mensaje):
    mensaje = mensaje.lower().strip()
    if "hola" in mensaje:
        return "Hola. Estoy activo y listo para escucharte y responderte."
    elif "cómo te llamas" in mensaje or "quién eres" in mensaje:
        return "Me llamo Jarvis. Soy tu asistente inteligente, creado para ayudarte en todo lo que necesites."
    elif "adiós" in mensaje:
        return "¡Hasta luego! Aquí estaré cuando vuelvas."
    else:
        return f"He entendido: '{mensaje}'. Te explico lo que sé."

# 🎨 ESTILOS - SOLO LO NECESARIO
st.markdown("""
<style>
    /* ❌ OCULTAR TODO LO DE ARRIBA Y COSAS DE STREAMLIT */
    #MainMenu, footer, header, .stException, .stDeployButton, div[data-testid="stVerticalBlock"] > div:first-child, .stTextInput > label {
        display: none !important;
        visibility: hidden !important;
    }

    /* 💬 CAJA DE CHAT */
    .caja {
        width: 90%;
        height: 75vh;
        margin: 0 auto 20px auto;
        background: #FFFFFF;
        border: 1px solid #ddd;
        border-radius: 12px;
        padding: 15px;
        overflow-y: auto;
    }
    .tu {
        text-align: right;
        background: #f0f0f0;
        color: #000000;
        border-radius: 16px 16px 4px 16px;
        padding: 8px 12px;
        margin: 4px 0 4px auto;
        max-width: 70%;
    }
    .jarvis {
        text-align: left;
        background: #e6f7ff;
        color: #000000;
        border-radius: 16px 16px 16px 4px;
        padding: 8px 12px;
        margin: 4px auto 4px 0;
        max-width: 70%;
    }

    /* 📥 BARRA DE ABAJO FIJA Y FUNCIONAL */
    .barra-fija {
        position: fixed;
        bottom: 15px;
        left: 5%;
        width: 90%;
        background: #ffffff;
        border-radius: 25px;
        padding: 6px 15px;
        box-shadow: 0 1px 6px #ccc;
        z-index: 999999;
    }
</style>
""", unsafe_allow_html=True)


# 🔤 TÍTULO
st.markdown("<h1 style='text-align:center; color:white; text-shadow: 0 0 8px #00eeff;'>JARVIS - ASISTENTE</h1>", unsafe_allow_html=True)


# 💬 MOSTRAR MENSAJES
caja_contenido = "<div class='caja'>"
for tipo, texto in st.session_state.chat:
    if tipo == "tu":
        caja_contenido += f"<div class='tu'><b>Tú:</b> {texto}</div>"
    else:
        caja_contenido += f"<div class='jarvis'><b>Jarvis:</b> {texto}</div>"
caja_contenido += "</div>"

st.markdown(caja_contenido, unsafe_allow_html=True)


# 📥 AQUÍ LO IMPORTANTE: BARRA Y BOTÓN QUE SÍ SE PUEDEN USAR
st.markdown("<div class='barra-fija'>", unsafe_allow_html=True)

col1, col2 = st.columns([8.5, 1.5])

with col1:
    entrada = st.text_input("", placeholder="Escribe tu mensaje aquí...", label_visibility="collapsed", key="entrada_final")

with col2:
    enviado = st.button("📩 ENVIAR", type="primary", key="boton_final")

st.markdown("</div>", unsafe_allow_html=True)


# ⚙️ ACCIÓN DE ENVIAR - 100% FUNCIONAL
if enviado and entrada.strip() != "":
    st.session_state.chat.append( ("tu", entrada) )
    respuesta = responder(entrada)
    st.session_state.chat.append( ("jarvis", respuesta) )
    st.rerun()
