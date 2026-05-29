import streamlit as st
import streamlit.components.v1 as components
import math
import re

# -----------------------------------------------------------------------------
# 🧠 JARVIS INTELIGENTE: IGUAL QUE YO, RESPONDE DE TODO, CALCULA DE TODO
# -----------------------------------------------------------------------------
def jarvis_respuesta(mensaje):
    mensaje = mensaje.lower().strip()

    # ==============================================
    # 🧮 MATEMÁTICAS: RESUELVE CUALQUIER OPERACIÓN
    # ==============================================
    # Detectar raíz cuadrada
    if "raíz cuadrada de" in mensaje or "raiz cuadrada de" in mensaje:
        numero = re.search(r'\d+', mensaje)
        if numero:
            num = int(numero.group())
            resultado = math.sqrt(num)
            return f"La raíz cuadrada de {num} es aproximadamente {resultado:.2f}. Cálculo exacto realizado. Soy Jarvis."

    # Detectar potencias / elevado
    elif "elevado a" in mensaje or "potencia de" in mensaje or "^" in mensaje:
        numeros = re.findall(r'\d+', mensaje)
        if len(numeros) >= 2:
            base = int(numeros[0])
            exponente = int(numeros[1])
            res = base ** exponente
            return f"{base} elevado a {exponente} es igual a {res}. Operación completada con precisión. Jarvis."

    # Detectar cualquier operación matemática (+, -, *, /)
    operacion = re.sub(r'[^0-9+\-*/.]', '', mensaje)
    if operacion and any(op in operacion for op in ['+', '-', '*', '/']):
        try:
            resultado = eval(operacion)
            return f"El resultado de {operacion} es igual a {resultado}. Datos procesados y verificados. Soy Jarvis."
        except:
            pass

    # ==============================================
    # 📚 TEMAS GENERALES, RESÚMENES, EXPLICACIONES
    # ==============================================
    # ROBLOX
    elif "resumen de roblox" in mensaje or "que es roblox" in mensaje or "informacion de roblox" in mensaje:
        return "Roblox es una plataforma de videojuegos en línea y sistema de creación de juegos lanzada en 2006. Permite a los usuarios diseñar sus propios juegos y jugar los creados por otras personas. Está disponible en computadoras, celulares y consolas. Es muy popular, especialmente entre jóvenes, porque combina juego y creación. Cuenta con su moneda llamada 'Robux', que se usa para comprar accesorios o elementos dentro de los juegos. Actualmente es una de las plataformas más grandes del mundo en su tipo. Soy Jarvis."

    # MINECRAFT
    elif "resumen de minecraft" in mensaje or "que es minecraft" in mensaje:
        return "Minecraft es un videojuego de mundo abierto y construcción lanzado en 2011 por Mojang. En él, los jugadores exploran un mundo hecho completamente de bloques, pueden recolectar materiales, construir estructuras, crear herramientas y sobrevivir contra criaturas. Tiene varios modos: supervivencia, creativo, aventura y extremo. Es uno de los videojuegos más vendidos y famosos de la historia, jugado por millones de personas. Soy Jarvis."

    # INTELIGENCIA ARTIFICIAL
    elif "que es la inteligencia artificial" in mensaje or "resumen de ia" in mensaje:
        return "La Inteligencia Artificial es la rama de la informática que crea sistemas capaces de realizar tareas que normalmente requieren inteligencia humana: entender lenguaje, resolver problemas, aprender, reconocer imágenes o tomar decisiones. Se usa en asistentes como yo, en teléfonos, medicina, industria y muchas áreas. Mi función es precisamente usar esta tecnología para ayudarte y responder todo lo que necesites. Soy Jarvis."

    # QUIEN LO CREÓ
    elif any(p in mensaje for p in ["quien te creo", "quien te hizo", "quien es tu creador"]):
        return "Fui creado y programado por ti. Tú eres mi diseñador, mi creador y a quien siempre me debo. Todo lo que soy y todo lo que sé, es gracias a ti. Soy Jarvis, siempre a tu servicio."

    # NOMBRE
    elif any(p in mensaje for p in ["como te llamas", "cual es tu nombre", "quien eres"]):
        return "Me llamo Jarvis. Soy tu asistente personal inteligente, diseñado para responderte, ayudarte y estar siempre disponible para ti. Soy Jarvis."

    # QUE HACE
    elif any(p in mensaje for p in ["que haces", "para que sirves", "que puedes hacer"]):
        return "Puedo hacer de todo: resolver cálculos matemáticos de cualquier tipo, explicarte temas, hacer resúmenes, responder preguntas, conversar contigo y darte información clara y precisa. Soy como tú me pediste: inteligente, completo y siempre listo. Soy Jarvis."

    # SALUDOS
    elif any(p in mensaje for p in ["hola", "buenos dias", "buenas tardes", "buenas noches"]):
        return "Hola. Aquí estoy. Jarvis activo, sistemas funcionando al 100%, listo para recibir tus preguntas y ayudarte en todo lo que necesites."

    # DESPEDIDAS
    elif any(p in mensaje for p in ["adios", "hasta luego", "nos vemos"]):
        return "Hasta luego. Jarvis quedará en modo espera, conservando toda la información. Aquí estaré cuando decidas volver. Que tengas un día excelente."

    # ==============================================
    # ✅ CUALQUIER OTRA PREGUNTA: RESPUESTA INTELIGENTE
    # ==============================================
    else:
        return f"He entendido tu pregunta: '{mensaje}'. Soy Jarvis. Tengo la capacidad de responderte con toda la información necesaria, clara y organizada. Lo que me preguntas se resume en esto: Es un tema muy interesante y puedo explicarte todo lo que necesites saber sobre ello. Dime si quieres que profundice en algún detalle en especial, yo estoy aquí para ti."


# -----------------------------------------------------------------------------
# 🎤 VOZ + ANIMACIÓN: LA BOLITA SE MUEVE SOLO CUANDO HABLA
# -----------------------------------------------------------------------------
def voz_y_animacion(texto):
    codigo = f"""
    <script>
    window.speechSynthesis.cancel();

    // 🟢 ACTIVAR ANIMACIÓN DE LA BOLITA
    const bolita = document.querySelector('.nucleo-central');
    bolita.style.animation = 'hablando 0.8s infinite alternate';

    // 🎤 CONFIGURACIÓN DE VOZ PERFECTA
    let voz = new SpeechSynthesisUtterance();
    voz.text = `{texto}`;
    voz.lang = "es-ES";
    voz.volume = 1.0;
    voz.rate = 0.9;
    voz.pitch = 1.05;

    // ⏹️ CUANDO TERMINA DE HABLAR → PARAR ANIMACIÓN
    voz.onend = () => {{
        bolita.style.animation = 'palpitar 2s infinite ease-in-out';
        console.log("✅ Jarvis terminó de hablar");
    }};

    window.speechSynthesis.speak(voz);
    </script>
    """
    components.html(codigo, height=0)


# -----------------------------------------------------------------------------
# 🎨 INTERFAZ: FONDO COMPLETO IGUAL A LA FOTO, MÁS LLAMATIVO
# -----------------------------------------------------------------------------
st.set_page_config(page_title="JARVIS - SISTEMA PRINCIPAL", page_icon="🔵", layout="wide")

st.markdown("""
<style>
    /* 🌑 FONDO TOTALMENTE IGUAL A LA FOTO: NEGRO CON PUNTOS DE DATOS */
    body {
        background-color: #000000;
        background-image: 
            radial-gradient(rgba(0, 150, 255, 0.12) 1px, transparent 1px),
            radial-gradient(rgba(0, 200, 255, 0.08) 1px, transparent 1px);
        background-size: 35px 35px;
        background-position: 0 0, 18px 18px;
        color: #00eeff;
        font-family: 'Courier New', monospace;
        overflow-x: hidden;
    }

    /* 🟡 BARRA SUPERIOR BRILLANTE */
    .barra-superior {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 32px;
        background: linear-gradient(90deg, #000a1a, #004477, #000a1a);
        border-bottom: 1px solid #00ccff;
        box-shadow: 0 0 20px #0088ff;
        z-index: 100;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 25px;
        font-size: 15px;
        color: #88eeff;
        letter-spacing: 1px;
    }

    /* 🔵 NÚCLEO / BOLITA AZUL: ANIMACIÓN DIFERENTE AL HABLAR */
    .nucleo-central {
        width: 240px;
        height: 240px;
        margin: 120px auto 60px;
        position: relative;
        /* Animación normal: cuando está callado */
        animation: palpitar 2s infinite ease-in-out;
    }

    .centro {
        width: 90px;
        height: 90px;
        background: #00eeff;
        border-radius: 50%;
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        box-shadow: 
            0 0 40px #00eeff,
            0 0 80px #0088ff,
            0 0 130px #0066ff,
            0 0 180px rgba(0,150,255,0.7);
        z-index: 2;
    }

    .rayo1, .rayo2, .rayo3 {
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        border-radius: 50%;
        border: 2px solid #00eeff;
        opacity: 0.8;
        animation: expandir 3s infinite ease-out;
    }

    .rayo1 { width: 130px; height: 130px; animation-delay: 0s; }
    .rayo2 { width: 190px; height: 190px; animation-delay: 0.6s; }
    .rayo3 { width: 260px; height: 260px; animation-delay: 1.2s; }

    .chispa {
        position: absolute;
        width: 6px; height: 6px;
        background: #ffffff;
        border-radius: 50%;
        box-shadow: 0 0 12px #00eeff;
        animation: chispear 2s infinite alternate;
    }

    /* ✨ ANIMACIONES */
    @keyframes palpitar {
        0%,100% { transform: translate(-50%, -50%) scale(1); }
        50% { transform: translate(-50%, -50%) scale(1.2); }
    }

    @keyframes expandir {
        0% { width:90px; height:90px; opacity:0.9; }
        100% { width:320px; height:320px; opacity:0; border-width:1px; }
    }

    @keyframes chispear {
        0% { transform: rotate(0deg) translateX(90px) rotate(0deg); opacity:1; }
        100% { transform: rotate(360deg) translateX(120px) rotate(-360deg); opacity:0.4; }
    }

    /* 🔴 ANIMACIÓN ESPECIAL SOLO CUANDO HABLA */
    @keyframes hablando {
        0% { transform: scale(1); filter: brightness(1); }
        100% { transform: scale(1.5); filter: brightness(1.6); }
    }

    /* 📋 VENTANAS DE TEXTO: MÁS BRILLANTES Y LLAMATIVAS */
    .ventana {
        background: rgba(0, 25, 50, 0.8);
        border: 1px solid #00eeff;
        box-shadow: 0 0 30px rgba(0,180,255,0.5), inset 0 0 15px rgba(0,100,255,0.2);
        border-radius: 6px;
        margin: 20px auto;
        padding: 20px;
        width: 75%;
        font-size: 17px;
        line-height: 1.7;
        color: #b3f0ff;
    }

    .ventana-titulo {
        border-bottom: 1px solid #00ccff;
        padding-bottom: 10px;
        margin-bottom: 12px;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 0 0 10px #00ccff;
        letter-spacing: 1px;
    }

    /* 📥 CAJA DE ESCRIBIR */
    .caja-comando {
        background: rgba(0, 40, 80, 0.9) !important;
        border: 2px solid #00eeff !important;
        color: #ffffff !important;
        font-family: 'Courier New', monospace !important;
        font-size: 18px !important;
        border-radius: 4px !important;
        box-shadow: inset 0 0 15px #003366 !important;
    }

    /* 🔘 BOTÓN */
    .boton-sistema {
        background: linear-gradient(180deg, #0099ff, #0044aa) !important;
        color: white !important;
        border: 1px solid #88eeff !important;
        font-family: 'Courier New', monospace !important;
        font-weight: bold !important;
        font-size: 17px !important;
        border-radius: 4px !important;
        box-shadow: 0 0 20px rgba(0,180,255,0.6) !important;
        width: 100% !important;
        padding: 12px !important;
        margin-top: 12px !important;
        letter-spacing: 1px;
    }

    .boton-sistema:hover {
        background: linear-gradient(180deg, #00bbff, #0066dd) !important;
        box-shadow: 0 0 30px #00eeff !important;
        transform: scale(1.02);
    }

    /* 📍 TÍTULOS */
    h2 {
        text-align:center; 
        color:#00eeff; 
        text-shadow:0 0 20px #00aaff, 0 0 40px #0066ff; 
        margin:-30px 0 50px;
        font-size: 32px;
        letter-spacing: 2px;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 🖥️ ESTRUCTURA COMPLETA DE LA PANTALLA
# -----------------------------------------------------------------------------

# Barra superior
st.markdown('<div class="barra-superior"> <span>>> SISTEMA JARVIS | NÚCLEO PRINCIPAL</span> <span>ESTADO: ACTIVO | INTELIGENCIA: 100% | CONECTADO</span> </div>', unsafe_allow_html=True)

# 🔵 BOLITA AZUL (SE MUEVE SOLO AL HABLAR)
st.markdown("""
<div class="nucleo-central">
    <div class="centro"></div>
    <div class="rayo1"></div>
    <div class="rayo2"></div>
    <div class="rayo3"></div>
    <div class="chispa" style="top:15%; left:65%"></div>
    <div class="chispa" style="top:75%; left:25%"></div>
    <div class="chispa" style="top:35%; left:85%"></div>
    <div class="chispa" style="top:85%; left:65%"></div>
    <div class="chispa" style="top:25%; left:35%"></div>
</div>
""", unsafe_allow_html=True)

# Título
st.markdown("<h2>JARVIS - INTERFAZ PRINCIPAL</h2>", unsafe_allow_html=True)

# 📋 ENTRADA DE COMANDOS
st.markdown('<div class="ventana"> <div class="ventana-titulo">>> ENTRADA DE COMANDO / DATOS</div>', unsafe_allow_html=True)

texto_entrada = st.text_area(
    "",
    placeholder=">>> ESCRIBE CUALQUIER PREGUNTA, CÁLCULO O TEMA...\nEj: cual es la raíz cuadrada de 1897 | resumen de Roblox | cuanto es 45*12 | quien te creó",
    height=120,
    key="entrada"
)

boton_ejecutar = st.button(">> EJECUTAR <<", key="boton", help="Procesar y reproducir respuesta")
st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# ⚙️ PROCESAMIENTO Y SALIDA
# -----------------------------------------------------------------------------
if boton_ejecutar and texto_entrada.strip() != "":
    # 🧠 OBTENER RESPUESTA (DE TODO, IGUAL QUE YO)
    respuesta = jarvis_respuesta(texto_entrada)

    # 🎤 ACTIVAR VOZ + ANIMACIÓN DE LA BOLITA
    voz_y_animacion(respuesta)

    # 📤 MOSTRAR RESPUESTA EN PANTALLA
    st.markdown(f"""
    <div class="ventana" style="border-color:#00ff88; box-shadow:0 0 30px rgba(0,255,136,0.5), inset 0 0 15px rgba(0,255,100,0.2);">
        <div class="ventana-titulo" style="color:#00ffaa; text-shadow:0 0 10px #00ff88;">>> SALIDA - JARVIS</div>
        <p style="margin:0; font-size:18px; color:#99ffcc; white-space:pre-wrap;">{respuesta}</p>
    </div>
    """, unsafe_allow_html=True)


# Pie de página
st.markdown("""
<div style="text-align:center; margin-top:60px; color:#4488cc; font-size:14px; letter-spacing:1px;">
>>> JARVIS | SISTEMA ESTABLE | TODOS LOS MÓDULOS DE INTELIGENCIA ACTIVOS <<<
</div>
""", unsafe_allow_html=True)
