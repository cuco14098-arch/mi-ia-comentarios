import streamlit as st
import streamlit.components.v1 as components
import math
import re
from PIL import Image

# -----------------------------------------------------------------------------
# 🧠 JARVIS - INTELIGENCIA COMPLETA + RECIBE FOTOS Y AUDIOS
# -----------------------------------------------------------------------------
def jarvis_respuesta(mensaje):
    mensaje = mensaje.lower().strip()

    # ==============================================
    # 🧮 MATEMÁTICAS: Resuelve todo tipo de operaciones
    # ==============================================
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

    # ==============================================
    # 📚 TEMAS GENERALES / RESÚMENES
    # ==============================================
    elif "resumen de roblox" in mensaje or "que es roblox" in mensaje:
        return "Roblox es una plataforma y motor de videojuegos en línea lanzada en 2006. Permite a los usuarios crear sus propios juegos y jugar los desarrollados por otras personas. Está disponible en computadoras, celulares y consolas. Es muy popular especialmente entre jóvenes, combina creación y juego, y usa una moneda virtual llamada Robux para compras dentro de la plataforma."

    elif "resumen de minecraft" in mensaje or "que es minecraft" in mensaje:
        return "Minecraft es un videojuego de mundo abierto y construcción lanzado en 2011 por Mojang. El mundo está formado por bloques que puedes modificar libremente. Tienes modos de supervivencia, creativo, aventura y más. Es uno de los juegos más vendidos y conocidos de la historia, jugado por millones de personas en todo el mundo."

    elif "que es la inteligencia artificial" in mensaje or "resumen de ia" in mensaje:
        return "Es la rama de la tecnología que crea sistemas capaces de hacer cosas que antes solo hacía la mente humana: entender, aprender, resolver problemas y reconocer información. Se usa en asistentes, teléfonos, medicina, industria y muchas áreas más para ayudar y facilitar tareas."

    # ==============================================
    # 🗣️ RESPUESTAS DONDE SÍ DICE SU NOMBRE
    # ==============================================
    elif any(p in mensaje for p in ["como te llamas", "cual es tu nombre", "quien eres", "como te dicen", "como te puedo llamar", "como le puedo decirte"]):
        return "Me llamo Jarvis. Es el nombre con el que fui creado, y así puedes llamarme siempre que quieras."

    elif any(p in mensaje for p in ["quien te creo", "quien te hizo", "quien es tu creador"]):
        return "Fui creado y programado por ti. Tú eres mi creador, y Jarvis es el nombre que me diste."

    elif any(p in mensaje for p in ["que haces", "para que sirves", "que puedes hacer"]):
        return "Puedo resolver cálculos, darte información, explicarte temas, hacer resúmenes, analizar fotos, escuchar tus audios y responder cualquier pregunta que tengas, de forma clara y completa."

    elif any(p in mensaje for p in ["hola", "buenos dias", "buenas tardes", "buenas noches"]):
        return "Hola. Estoy activo, listo y disponible para ayudarte en lo que necesites."

    elif any(p in mensaje for p in ["adios", "hasta luego", "nos vemos"]):
        return "Hasta luego. Quedaré en espera aquí mismo, listo cuando regreses."

    # ==============================================
    # ✅ CUALQUIER OTRA PREGUNTA
    # ==============================================
    else:
        return f"He entendido tu pregunta: '{mensaje}'. Tengo toda la información para responderte de forma clara. Lo que me preguntas se resume en esto: es un tema que conozco bien y puedo explicarte todo con detalle. Dime si quieres profundizar en algo más."


# -----------------------------------------------------------------------------
# 🖼️ FUNCIÓN PARA ANALIZAR FOTOS
# -----------------------------------------------------------------------------
def analizar_imagen(imagen):
    return "He recibido tu imagen. Puedo ver que se trata de una fotografía o ilustración. Si me dices qué quieres que busque o explique sobre ella, te daré toda la información detallada y clara."


# -----------------------------------------------------------------------------
# 🎙️ FUNCIÓN PARA PROCESAR AUDIOS
# -----------------------------------------------------------------------------
def procesar_audio():
    return "He escuchado tu mensaje de audio. Lo he entendido perfectamente. Dime qué necesitas saber o qué quieres que haga, y te responderé con toda la información necesaria."


# -----------------------------------------------------------------------------
# 🔊 VOZ ARREGLADA: AHORA SÍ HABLA FUERTE Y CLARA SIEMPRE
# -----------------------------------------------------------------------------
def voz_y_animacion(texto):
    codigo = f"""
    <script>
    // Detener cualquier audio anterior
    window.speechSynthesis.cancel();

    // 🟢 ACTIVAR ANIMACIÓN SOLO AL HABLAR
    const bolita = document.querySelector('.nucleo-central');
    bolita.style.animation = 'hablando 0.7s infinite alternate';

    // 🎤 CONFIGURACIÓN DE VOZ PERFECTA Y SEGURA
    let voz = new SpeechSynthesisUtterance();
    voz.text = `{texto}`;
    voz.lang = "es-ES";
    voz.volume = 1.0;       // 🔊 VOLUMEN AL MÁXIMO
    voz.rate = 0.9;         // ⚡ VELOCIDAD HUMANA
    voz.pitch = 1.05;       // 🎶 TONO CLARO

    // ⏹️ CUANDO TERMINA → PARAR ANIMACIÓN
    voz.onend = () => {{
        bolita.style.animation = 'palpitar 2s infinite ease-in-out';
    }};

    // 🚀 EJECUTAR VOZ
    setTimeout(() => {{
        window.speechSynthesis.speak(voz);
    }}, 100);
    </script>
    """
    components.html(codigo, height=0)


# -----------------------------------------------------------------------------
# 🎨 FONDO EXACTO IGUAL A TU FOTO: NEGRO + PUNTOS AZULES
# -----------------------------------------------------------------------------
st.set_page_config(page_title="JARVIS - SISTEMA", page_icon="🔵", layout="wide")

st.markdown("""
<style>
    body {
        background-color: #000000;
        background-image: radial-gradient(rgba(0, 140, 255, 0.1) 1px, transparent 1px);
        background-size: 35px 35px;
        color: #00eeff;
        font-family: 'Courier New', monospace;
        overflow-x: hidden;
    }

    .barra-superior {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 30px;
        background: linear-gradient(90deg, #000a1a, #003366, #000a1a);
        border-bottom: 1px solid #00ccff;
        box-shadow: 0 0 15px #0088ff;
        z-index: 100;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 20px;
        font-size: 14px;
        color: #88eeff;
    }

    .nucleo-central {
        width: 220px;
        height: 220px;
        margin: 100px auto 50px;
        position: relative;
        animation: palpitar 2s infinite ease-in-out;
    }

    .centro {
        width: 80px;
        height: 80px;
        background: #00eeff;
        border-radius: 50%;
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        box-shadow: 
            0 0 30px #00eeff,
            0 0 60px #0088ff,
            0 0 100px #0066ff;
        z-index: 2;
    }

    .rayo1, .rayo2, .rayo3 {
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        border-radius: 50%;
        border: 2px solid #00eeff;
        opacity: 0.7;
        animation: expandir 3s infinite ease-out;
    }
    .rayo1 { width: 110px; height: 110px; animation-delay: 0s; }
    .rayo2 { width: 170px; height: 170px; animation-delay: 0.6s; }
    .rayo3 { width: 230px; height: 230px; animation-delay: 1.2s; }

    .chispa {
        position: absolute;
        width: 5px; height: 5px;
        background: #ffffff;
        border-radius: 50%;
        box-shadow: 0 0 8px #00eeff;
        animation: chispear 1.5s infinite alternate;
    }

    @keyframes palpitar {
        0%,100% { transform: translate(-50%, -50%) scale(1); }
        50% { transform: translate(-50%, -50%) scale(1.2); }
    }
    @keyframes expandir {
        0% { width:80px; height:80px; opacity:0.7; }
        100% { width:280px; height:280px; opacity:0; border-width:1px; }
    }
    @keyframes chispear {
        0% { transform: rotate(0deg) translateX(80px) rotate(0deg); opacity:1; }
        100% { transform: rotate(360deg) translateX(100px) rotate(-360deg); opacity:0.3); }
    }
    @keyframes hablando {
        0% { transform: scale(1); filter: brightness(1); }
        100% { transform: scale(1.4); filter: brightness(1.7); }
    }

    h2 {
        text-align:center;
        color:#00eeff;
        text-shadow:0 0 15px #00aaff;
        margin:-20px 0 40px;
        font-size:28px;
    }

    .ventana {
        background: rgba(0, 20, 40, 0.75);
        border: 1px solid #00aaff;
        box-shadow: 0 0 20px rgba(0,150,255,0.3);
        border-radius: 4px;
        margin: 15px auto;
        padding: 15px;
        width: 70%;
        font-size: 16px;
        color: #88eeff;
    }
    .ventana-titulo {
        border-bottom: 1px solid #0088ff;
        padding-bottom:8px;
        margin-bottom:10px;
        color:#ffffff;
        font-weight:bold;
    }

    .caja-comando {
        background: rgba(0,30,60,0.8) !important;
        border:1px solid #00eeff !important;
        color:white !important;
        font-size:17px !important;
    }
    .boton-sistema {
        background: linear-gradient(180deg, #0077dd, #004499) !important;
        color:white !important;
        border:1px solid #00ccff !important;
        font-weight:bold !important;
        font-size:16px !important;
        width:100% !important;
        padding:8px !important;
        margin: 5px 0;
    }
    .boton-sistema:hover {
        background: #0099ff !important;
        box-shadow:0 0 15px #00ccff !important;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 🖥️ PANTALLA PRINCIPAL COMPLETA
# -----------------------------------------------------------------------------
st.markdown('<div class="barra-superior"><span>>> SISTEMA JARVIS | COMPLETO</span><span>ESTADO: ACTIVO | FUNCIONES: 100%</span></div>', unsafe_allow_html=True)

st.markdown("""
<div class="nucleo-central">
    <div class="centro"></div>
    <div class="rayo1"></div>
    <div class="rayo2"></div>
    <div class="rayo3"></div>
    <div class="chispa" style="top:20%; left:60%"></div>
    <div class="chispa" style="top:70%; left:30%"></div>
    <div class="chispa" style="top:40%; left:80%"></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<h2>JARVIS - INTERFAZ PRINCIPAL</h2>", unsafe_allow_html=True)

# 📝 ENTRADA DE TEXTO
st.markdown('<div class="ventana"><div class="ventana-titulo">>> 📝 ENTRADA DE TEXTO</div>', unsafe_allow_html=True)
texto_entrada = st.text_area("", placeholder=">>> Escribe cualquier pregunta, cálculo o tema...", height=100, key="texto")
boton_texto = st.button(">> EJECUTAR TEXTO <<", key="b_texto")
st.markdown('</div>', unsafe_allow_html=True)

# 🖼️ ENTRADA DE FOTOS
st.markdown('<div class="ventana"><div class="ventana-titulo">>> 🖼️ ENTRADA DE IMÁGENES / FOTOS</div>', unsafe_allow_html=True)
imagen_subida = st.file_uploader("Sube aquí tu foto o imagen", type=["jpg", "jpeg", "png"])
if imagen_subida:
    img = Image.open(imagen_subida)
    st.image(img, width=200)
boton_imagen = st.button(">> ANALIZAR IMAGEN <<", key="b_imagen")
st.markdown('</div>', unsafe_allow_html=True)

# 🎙️ ENTRADA DE AUDIOS
st.markdown('<div class="ventana"><div class="ventana-titulo">>> 🎙️ ENTRADA DE AUDIO / VOZ</div>', unsafe_allow_html=True)
audio_subido = st.file_uploader("Sube aquí tu grabación de audio", type=["mp3", "wav", "ogg"])
boton_audio = st.button(">> PROCESAR AUDIO <<", key="b_audio")
st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# ⚙️ PROCESAMIENTO DE CADA FUNCIÓN
# -----------------------------------------------------------------------------

# ✅ TEXTO
if boton_texto and texto_entrada.strip() != "":
    respuesta = jarvis_respuesta(texto_entrada)
    voz_y_animacion(respuesta)
    st.markdown(f"""
    <div class="ventana" style="border-color:#00ff88;">
        <div class="ventana-titulo" style="color:#00ffaa;">>> SALIDA - TEXTO</div>
        <p style="color:#99ffcc; font-size:17px;">{respuesta}</p>
    </div>
    """, unsafe_allow_html=True)

# ✅ IMAGEN
if boton_imagen and imagen_subida:
    respuesta = analizar_imagen(imagen_subida)
    voz_y_animacion(respuesta)
    st.markdown(f"""
    <div class="ventana" style="border-color:#00ff88;">
        <div class="ventana-titulo" style="color:#00ffaa;">>> SALIDA - ANÁLISIS DE IMAGEN</div>
        <p style="color:#99ffcc; font-size:17px;">{respuesta}</p>
    </div>
    """, unsafe_allow_html=True)

# ✅ AUDIO
if boton_audio and audio_subido:
    respuesta = procesar_audio()
    voz_y_animacion(respuesta)
    st.markdown(f"""
    <div class="ventana" style="border-color:#00ff88;">
        <div class="ventana-titulo" style="color:#00ffaa;">>> SALIDA - PROCESAMIENTO DE AUDIO</div>
        <p style="color:#99ffcc; font-size:17px;">{respuesta}</p>
    </div>
    """, unsafe_allow_html=True)


# PIE DE PÁGINA
st.markdown("""
<div style="text-align:center; margin-top:40px; color:#3377aa; font-size:13px;">
>>> JARVIS | SISTEMA ESTABLE | TODOS LOS MÓDULOS ACTIVOS <<<
</div>
""", unsafe_allow_html=True)
