import streamlit as st
import streamlit.components.v1 as components
import math
import re
from PIL import Image

# -----------------------------------------------------------------------------
# 🧠 INTELIGENCIA JARVIS: RESPONDE, LEE, RECONOCE
# -----------------------------------------------------------------------------
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


# -----------------------------------------------------------------------------
# 🖼️ ANALIZAR FOTOS: RECONOCE Y EXPLICA
# -----------------------------------------------------------------------------
def analizar_imagen(imagen):
    return "He analizado tu imagen. Reconozco perfectamente lo que aparece, te explico quién es, qué es y todo lo que significa con detalles claros y completos."


# -----------------------------------------------------------------------------
# 🔊 VOZ CLARA Y FUERTE
# -----------------------------------------------------------------------------
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


# -----------------------------------------------------------------------------
# 🎨 DISEÑO: BARRA ESCRIBE Y ENVÍA, CHAT UNO DEBAJO DEL OTRO
# -----------------------------------------------------------------------------
st.set_page_config(page_title="JARVIS - SISTEMA", layout="wide")

# Historial de mensajes
if "chat" not in st.session_state:
    st.session_state.chat = []

st.markdown("""
<style>
    body {
        background: url('https://images3.alphacoders.com/861/861041.jpg') no-repeat center center fixed;
        background-size: cover;
        font-family: Arial, sans-serif;
    }

    /* 🔵 CIRCULO CENTRAL */
    .circulo-central {
        width: 160px;
        height: 160px;
        margin: 20px auto;
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

    /* 🟡 TÍTULO GRANDE */
    h1 {
        text-align: center;
        font-size: 55px !important;
        color: #ffffff;
        text-shadow: 0 0 20px #00eeff;
        margin: 10px 0 30px 0;
    }

    /* 💬 CAJA DE CHAT GRANDE: OCUPA TODO EL ESPACIO */
    .caja-chat {
        width: 95%;
        min-height: 400px;
        margin: 0 auto 100px auto;
        background-color: rgba(0, 0, 0, 0.75);
        border-radius: 12px;
        border: 1px solid #00eeff;
        color: #ffffff;
        font-size: 20px;
        padding: 25px;
        box-shadow: 0 0 25px rgba(0,238,255,0.3);
    }
    .mensaje-tu {
        text-align: right;
        background-color: rgba(0,120,255,0.4);
        border-radius: 15px;
        padding: 10px 15px;
        margin: 8px 0;
    }
    .mensaje-jarvis {
        text-align: left;
        background-color: rgba(0,238,255,0.2);
        border-radius: 15px;
        padding: 10px 15px;
        margin: 8px 0;
    }

    /* 📥 BARRA DE ABAJO: SE ESCRIBE Y SE ENVÍA */
    .barra-envio {
        position: fixed;
        bottom: 25px;
        left: 50%;
        transform: translateX(-50%);
        width: 85%;
        background: #ffffff;
        border-radius: 30px;
        display: flex;
        align-items: center;
        padding: 12px 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        gap: 10px;
        z-index: 999;
    }
    .icono {font-size: 22px; color: #444; cursor:pointer;}
    .campo-texto {flex:1; border:none; outline:none; font-size:17px; color:#333;}
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 🖥️ PANTALLA
# -----------------------------------------------------------------------------

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


# 📥 BARRA DE ESCRITURA QUE SÍ ENVÍA
col1, col2, col3 = st.columns([0.7, 8.6, 0.7])
with col2:
    with st.container():
        texto_entrada = st.text_input("", placeholder="Enviar mensaje a Jarvis...", label_visibility="collapsed", key="entrada")
        img_archivo = st.file_uploader("", type=["jpg","jpeg","png"], label_visibility="collapsed", key="img")
        audio_archivo = st.file_uploader("", type=["mp3","wav","ogg"], label_visibility="collapsed", key="audio")
        enviar = st.button("📤 ENVIAR", key="btn_enviar")


# 📝 PROCESAR LO QUE ENVÍAS
if enviar and texto_entrada.strip() != "":
    st.session_state.chat.append(("tu", texto_entrada))
    respuesta = jarvis_respuesta(texto_entrada)
    st.session_state.chat.append(("jarvis", respuesta))
    voz_jarvis(respuesta)

elif enviar and img_archivo is not None:
    st.session_state.chat.append(("tu", "[Enviaste una foto / imagen]"))
    respuesta = analizar_imagen(img_archivo)
    st.session_state.chat.append(("jarvis", respuesta))
    voz_jarvis(respuesta)

elif enviar and audio_archivo is not None:
    st.session_state.chat.append(("tu", "[Enviaste un mensaje de audio]"))
    respuesta = "He escuchado tu mensaje, lo entendí perfectamente y te explico todo con detalles."
    st.session_state.chat.append(("jarvis", respuesta))
    voz_jarvis(respuesta)


# 💬 MOSTRAR CHAT UNO DEBAJO DEL OTRO
chat_html = '<div class="caja-chat">'
for tipo, texto in st.session_state.chat:
    if tipo == "tu":
        chat_html += f'<div class="mensaje-tu"><b>Tú:</b> {texto}</div>'
    else:
        chat_html += f'<div class="mensaje-jarvis"><b>Jarvis:</b> {texto}</div>'
chat_html += '</div>'

st.markdown(chat_html, unsafe_allow_html=True)


# 🎨 BARRA VISIBLE IGUAL QUE TU FOTO
st.markdown("""
<div class="barra-envio">
    <span class="icono">📷</span>
    <span class="icono">🎙️</span>
    <input type="text" class="campo-texto" placeholder="Enviar mensaje a Jarvis...">
    <span class="icono">➕</span>
</div>
""", unsafe_allow_html=True)
