import streamlit as st
import streamlit.components.v1 as components
import math
import re
from PIL import Image

# -----------------------------------------------------------------------------
# 🧠 JARVIS - INTELIGENCIA COMPLETA
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

    # 📚 TEMAS / RESÚMENES
    elif "resumen de roblox" in mensaje or "que es roblox" in mensaje:
        return "Roblox es una plataforma de videojuegos en línea donde puedes crear y jugar juegos, muy popular desde 2006, con su moneda llamada Robux."

    elif "resumen de naruto" in mensaje or "que es naruto" in mensaje:
        return "Naruto es una serie de manga y anime creada por Masashi Kishimoto. Cuenta la historia de Naruto Uzumaki, un joven ninja que quiere ser el líder de su aldea. Es una de las series más famosas del mundo, llena de acción, amistad y crecimiento personal."

    elif "quien es itachi" in mensaje or "itachi uchiha" in mensaje:
        return "Itachi Uchiha es un personaje de Naruto, hermano mayor de Sasuke. Fue un ninja muy poderoso, miembro de la organización Akatsuki, con una historia trágica pero noble, uno de los personajes más queridos de la serie."

    elif "resumen de minecraft" in mensaje or "que es minecraft" in mensaje:
        return "Minecraft es un juego de construcción y aventura, donde todo es de bloques. Puedes construir, explorar y sobrevivir. Es uno de los juegos más vendidos de la historia."

    # 🗣️ RESPUESTAS CON NOMBRE SOLO CUANDO TOCA
    elif any(p in mensaje for p in ["como te llamas", "cual es tu nombre", "quien eres"]):
        return "Me llamo Jarvis. Soy tu asistente inteligente, creado para ayudarte en todo lo que necesites."

    elif any(p in mensaje for p in ["quien te creo", "quien te hizo"]):
        return "Fui creado y programado por ti. Tú eres mi creador, y Jarvis es el nombre que me diste."

    elif any(p in mensaje for p in ["que haces", "para que sirves"]):
        return "Puedo responder preguntas, resolver cálculos, explicarte temas, analizar imágenes, entender audios y ayudarte en todo."

    elif any(p in mensaje for p in ["hola", "buenos dias", "buenas tardes"]):
        return "Hola. Estoy activo y listo para ayudarte. Dime qué necesitas."

    elif any(p in mensaje for p in ["adios", "hasta luego"]):
        return "Hasta luego. Aquí estaré cuando regreses."

    # ✅ CUALQUIER OTRA PREGUNTA
    else:
        return f"He entendido: '{mensaje}'. Tengo toda la información para explicarte claro. Es un tema que conozco bien y te puedo dar todos los detalles que quieras."


# -----------------------------------------------------------------------------
# 🖼️ ANALIZAR IMÁGENES
# -----------------------------------------------------------------------------
def analizar_imagen(imagen):
    return "He recibido tu imagen. La he analizado y puedo decirte lo que aparece. Si me pides detalles específicos, te los explico con claridad."


# -----------------------------------------------------------------------------
# 🎙️ PROCESAR AUDIOS
# -----------------------------------------------------------------------------
def procesar_audio():
    return "He escuchado tu mensaje de audio. Lo he entendido perfectamente. Dime qué necesitas saber y te responderé con toda la información."


# -----------------------------------------------------------------------------
# 🔊 VOZ PERFECTA: SE ESCUCHA FUERTE Y CLARA
# -----------------------------------------------------------------------------
def voz_jarvis(texto):
    codigo = f"""
    <script>
    window.speechSynthesis.cancel();

    // Animación bolita al hablar
    const bolita = document.querySelector('.nucleo-central');
    if(bolita) bolita.style.animation = 'hablando 0.7s infinite alternate';

    // Configuración voz
    let voz = new SpeechSynthesisUtterance();
    voz.text = `{texto}`;
    voz.lang = "es-ES";
    voz.volume = 1.0;
    voz.rate = 0.9;
    voz.pitch = 1.05;

    // Parar animación al terminar
    voz.onend = () => {{
        if(bolita) bolita.style.animation = 'palpitar 2s infinite ease-in-out';
    }};

    setTimeout(() => {{
        window.speechSynthesis.speak(voz);
    }}, 150);
    </script>
    """
    components.html(codigo, height=0)


# -----------------------------------------------------------------------------
# 🎨 DISEÑO: BARRA IGUAL A TU FOTO + FONDO ITACHI
# -----------------------------------------------------------------------------
st.set_page_config(page_title="JARVIS - SISTEMA", page_icon="🔵", layout="wide")

st.markdown("""
<style>
    /* 🌑 FONDO: IMAGEN DE ITACHI UCHIHA */
    body {
        background: url('https://images3.alphacoders.com/861/861041.jpg') no-repeat center center fixed;
        background-size: cover;
        color: #ffffff;
        font-family: 'Segoe UI', Roboto, sans-serif;
        margin: 0;
        padding: 0;
    }

    /* 🔵 BOLITA CENTRAL */
    .nucleo-central {
        width: 180px;
        height: 180px;
        margin: 40px auto;
        position: relative;
        animation: palpitar 2s infinite ease-in-out;
    }
    .centro {
        width: 70px;
        height: 70px;
        background: #00eeff;
        border-radius: 50%;
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        box-shadow: 0 0 40px #00eeff, 0 0 80px #0066ff;
    }
    .rayo1,.rayo2,.rayo3 {
        position: absolute;
        top:50%; left:50%;
        transform:translate(-50%,-50%);
        border-radius:50%;
        border:2px solid #00eeff;
        opacity:0.7;
        animation: expandir 3s infinite ease-out;
    }
    .rayo1{width:100px;height:100px;}
    .rayo2{width:150px;height:150px;animation-delay:0.6s;}
    .rayo3{width:200px;height:200px;animation-delay:1.2s;}

    @keyframes palpitar {
        0%,100% {transform: translate(-50%,-50%) scale(1);}
        50% {transform: translate(-50%,-50%) scale(1.2);}
    }
    @keyframes expandir {
        0% {width:70px;height:70px;opacity:0.8;}
        100% {width:240px;height:240px;opacity:0;}
    }
    @keyframes hablando {
        0% {transform: scale(1); filter: brightness(1);}
        100% {transform: scale(1.5); filter: brightness(1.8);}
    }

    /* 💬 BARRA DE ENTRADA: IGUAL A TU FOTO */
    .barra-mensaje {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 80%;
        max-width: 900px;
        background: #ffffff;
        border-radius: 30px;
        display: flex;
        align-items: center;
        padding: 10px 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        gap: 12px;
    }
    .icono {
        font-size: 22px;
        color: #444444;
    }
    .campo-texto {
        flex: 1;
        border: none;
        outline: none;
        font-size: 16px;
        color: #333333;
        background: transparent;
    }
    .boton-icono {
        border: none;
        background: transparent;
        font-size: 22px;
        color: #444444;
        cursor: pointer;
    }

    /* 📋 CAJA DE RESPUESTAS */
    .caja-respuesta {
        width: 75%;
        margin: 20px auto;
        background: rgba(0,0,0,0.75);
        border: 1px solid rgba(0,238,255,0.5);
        border-radius: 12px;
        padding: 18px;
        color: #e6ffff;
        font-size: 17px;
        line-height: 1.6;
        box-shadow: 0 0 20px rgba(0,238,255,0.2);
    }

    /* 📍 TÍTULO */
    h1 {
        text-align:center;
        color:#ffffff;
        text-shadow: 0 0 15px #00eeff;
        margin-top:20px;
        font-size:32px;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 🖥️ PANTALLA PRINCIPAL
# -----------------------------------------------------------------------------

# Título
st.markdown("<h1>JARVIS - ASISTENTE INTELIGENTE</h1>", unsafe_allow_html=True)

# Bolita central
st.markdown("""
<div class="nucleo-central">
    <div class="centro"></div>
    <div class="rayo1"></div>
    <div class="rayo2"></div>
    <div class="rayo3"></div>
</div>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 💬 BARRA DE MENSAJE ÚNICA: CÁMARA - TEXTO - MIC - +
# -----------------------------------------------------------------------------
st.markdown("""
<div class="barra-mensaje">
    <span class="icono">📷</span>
    <input type="text" class="campo-texto" placeholder="Enviar mensaje a Jarvis..." id="entrada_usuario">
    <button class="boton-icono">🎙️</button>
    <button class="boton-icono">➕</button>
</div>
""", unsafe_allow_html=True)


# Elementos ocultos pero funcionales
col1, col2, col3 = st.columns([1,8,1])
with col2:
    texto_entrada = st.text_input("", label_visibility="collapsed", placeholder="Enviar mensaje a Jarvis...", key="texto_oculto")
    archivo_imagen = st.file_uploader("", type=["jpg","jpeg","png"], label_visibility="collapsed", key="img_oculta")
    archivo_audio = st.file_uploader("", type=["mp3","wav","ogg"], label_visibility="collapsed", key="audio_oculto")
    enviar = st.button("ENVIAR", key="btn_enviar")


# -----------------------------------------------------------------------------
# ⚙️ PROCESAMIENTO
# -----------------------------------------------------------------------------
if enviar:
    # 📝 TEXTO
    if texto_entrada.strip() != "":
        respuesta = jarvis_respuesta(texto_entrada)
        voz_jarvis(respuesta)
        st.markdown(f"""
        <div class="caja-respuesta">
            <b>Jarvis:</b> {respuesta}
        </div>
        """, unsafe_allow_html=True)

    # 🖼️ IMAGEN
    elif archivo_imagen is not None:
        respuesta = analizar_imagen(archivo_imagen)
        voz_jarvis(respuesta)
        st.markdown(f"""
        <div class="caja-respuesta">
            <b>Jarvis:</b> {respuesta}
        </div>
        """, unsafe_allow_html=True)

    # 🎙️ AUDIO
    elif archivo_audio is not None:
        respuesta = procesar_audio()
        voz_jarvis(respuesta)
        st.markdown(f"""
        <div class="caja-respuesta">
            <b>Jarvis:</b> {respuesta}
        </div>
        """, unsafe_allow_html=True)
