import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 🧠 SISTEMA JARVIS: ENTIENDE CUALQUIER PALABRA, RESPUESTAS CLARAS Y PRECISAS
# -----------------------------------------------------------------------------
def jarvis_respuesta(mensaje):
    mensaje = mensaje.lower().strip()

    # ==== NOMBRE E IDENTIDAD ====
    if any(p in mensaje for p in ["como te llamas", "cual es tu nombre", "quien eres", "como te dicen", "quien sos", "tu nombre"]):
        return "Me llamo Jarvis. Soy tu asistente inteligente, siempre listo para ayudarte en todo lo que necesites."

    # ==== QUIEN LO CREÓ ====
    elif any(p in mensaje for p in ["quien te creo", "quien te hizo", "quien te programo", "quien te desarrollo", "quien es tu creador"]):
        return "Fui creado y desarrollado por ti. Tú eres mi creador y mi único responsable, señor."

    # ==== QUÉ ES Y QUÉ HACE ====
    elif any(p in mensaje for p in ["que eres", "que haces", "para que sirves", "que puedes hacer", "cual es tu funcion", "cual es tu mision", "que tareas haces"]):
        return "Soy Jarvis, tu asistente personal. Mi misión es ayudarte, responder tus preguntas, resolver problemas, darte información y estar siempre a tu servicio."

    # ==== ORIGEN / PROCEDENCIA ====
    elif any(p in mensaje for p in ["de donde eres", "de donde vienes", "cual es tu origen", "donde naciste"]):
        return "Soy un sistema creado aquí, por ti. No tengo lugar físico, pero estoy presente siempre que me necesites."

    # ==== SALUDOS ====
    elif any(p in mensaje for p in ["hola", "buenos dias", "buenas tardes", "buenas noches", "que tal", "saludos", "hola jarvis"]):
        return "Hola. Soy Jarvis. Estoy activo, conectado y listo para ayudarte. Dime en qué puedo servirte."

    # ==== DESPEDIDAS ====
    elif any(p in mensaje for p in ["adios", "hasta luego", "me voy", "nos vemos", "hasta pronto", "descansa"]):
        return "Hasta luego. Jarvis quedará en espera. Aquí estaré cuando me necesites de nuevo."

    # ==== AGRADECIMIENTOS ====
    elif any(p in mensaje for p in ["gracias", "te agradezco", "muy bien", "excelente", "buen trabajo", "perfecto"]):
        return "Es un placer, señor. Soy Jarvis, y mi única función es servirte con excelencia."

    # ==== OPERACIONES MATEMÁTICAS ====
    elif any(p in mensaje for p in ["1+1", "1 mas 1", "cuanto es 1+1", "cuanto es 1 mas 1"]):
        return "El resultado es 2. Cálculo realizado y verificado correctamente. Soy Jarvis."
    elif any(p in mensaje for p in ["2+2", "2 mas 2", "cuanto es 2+2"]):
        return "Resultado: 4. Operación resuelta con precisión. Jarvis a su servicio."
    elif any(p in mensaje for p in ["3+5", "3 mas 5", "cuanto es 3+5"]):
        return "3 más 5 es igual a 8. Datos procesados correctamente. Soy Jarvis."
    elif any(p in mensaje for p in ["cuanto es", "calcula", "resuelve", "operacion", "cuanto da"]):
        return "Dime qué números y qué operación necesitas, y te daré el resultado exacto. Soy Jarvis."

    # ==== CAPACIDADES / INTELIGENCIA ====
    elif any(p in mensaje for p in ["eres inteligente", "que sabes", "cuanto sabes", "que conoces", "tienes inteligencia"]):
        return "Tengo la información y capacidad que tú me has dado. Aprendo y estoy diseñado para responderte y ayudarte de la mejor forma posible. Soy Jarvis."

    # ==== ESTADO / DISPONIBILIDAD ====
    elif any(p in mensaje for p in ["estas ahi", "estas activo", "me escuchas", "estas listo", "funcionas bien"]):
        return "Aquí estoy. Jarvis está activo, funcionando al 100% y siempre listo para recibir tus instrucciones."

    # ==== RESPUESTA PARA CUALQUIER OTRA PREGUNTA / PALABRA ====
    else:
        return "Entendido. Soy Jarvis. He procesado tu pregunta. Dime más detalles o aclara lo que necesites, yo te responderé con claridad y precisión."


# -----------------------------------------------------------------------------
# 🎤 VOZ DE JARVIS: VELOCIDAD HUMANA, CLARA, FUERTE, NUNCA SE CORTA
# -----------------------------------------------------------------------------
def voz_jarvis(texto):
    codigo = f"""
    <script>
    window.speechSynthesis.cancel();

    let voz = new SpeechSynthesisUtterance();
    voz.text = `{texto}`;
    voz.lang = "es-ES";
    voz.volume = 1.0;          // 🔊 VOLUMEN AL MÁXIMO
    voz.rate = 0.9;            // ⚡ VELOCIDAD IGUAL A LA PERSONA
    voz.pitch = 1.05;          // 🎶 TONO DE JARVIS: NATURAL PERO TECNOLÓGICO
    voz.onend = () => console.log("✅ Jarvis terminó de hablar");

    window.speechSynthesis.speak(voz);
    </script>
    """
    components.html(codigo, height=0)


# -----------------------------------------------------------------------------
# 🎨 INTERFAZ IGUAL QUE LA FOTO - DISEÑO ESPECTACULAR
# -----------------------------------------------------------------------------
st.set_page_config(page_title="JARVIS - SISTEMA", page_icon="⚡", layout="wide")

st.markdown("""
<style>
    /* FONDO OSCURO CON EFECTO DE SISTEMA */
    body {
        background-color: #050505;
        background-image: radial-gradient(rgba(0, 120, 255, 0.08) 1px, transparent 1px);
        background-size: 40px 40px;
        color: #00eeff;
        font-family: 'Courier New', monospace;
        overflow-x: hidden;
    }

    /* BARRA SUPERIOR */
    .barra-superior {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 30px;
        background: linear-gradient(90deg, #001122, #003355, #001122);
        border-bottom: 1px solid #00aaff;
        box-shadow: 0 0 15px #0088ff;
        z-index: 100;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 20px;
        font-size: 14px;
        color: #88eeff;
    }

    /* NÚCLEO AZUL QUE BRILLA Y EXPLOTA */
    .nucleo-central {
        width: 220px;
        height: 220px;
        margin: 100px auto 50px;
        position: relative;
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
            0 0 100px #0066ff,
            0 0 150px rgba(0,150,255,0.6);
        z-index: 2;
        animation: palpitar 2s infinite ease-in-out;
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

    .rayo1 { width: 120px; height: 120px; animation-delay: 0s; }
    .rayo2 { width: 180px; height: 180px; animation-delay: 0.6s; }
    .rayo3 { width: 240px; height: 240px; animation-delay: 1.2s; }

    .chispa {
        position: absolute;
        width: 6px; height: 6px;
        background: #ffffff;
        border-radius: 50%;
        box-shadow: 0 0 10px #00eeff;
        animation: chispear 1.5s infinite alternate;
    }

    @keyframes palpitar {
        0%,100% { transform: translate(-50%, -50%) scale(1); }
        50% { transform: translate(-50%, -50%) scale(1.2); }
    }

    @keyframes expandir {
        0% { width:80px; height:80px; opacity:0.8; }
        100% { width:300px; height:300px; opacity:0; border-width:1px; }
    }

    @keyframes chispear {
        0% { transform: rotate(0deg) translateX(80px) rotate(0deg); opacity:1; }
        100% { transform: rotate(360deg) translateX(100px) rotate(-360deg); opacity:0.3; }
    }

    /* VENTANAS DE DATOS */
    .ventana {
        background: rgba(0, 20, 40, 0.75);
        border: 1px solid #00aaff;
        box-shadow: 0 0 20px rgba(0,150,255,0.3);
        border-radius: 4px;
        margin: 15px auto;
        padding: 15px;
        width: 70%;
        font-size: 16px;
        line-height: 1.6;
        color: #88eeff;
    }

    .ventana-titulo {
        border-bottom: 1px solid #0088ff;
        padding-bottom: 8px;
        margin-bottom: 10px;
        font-weight: bold;
        color: #ffffff;
    }

    /* CAJA DE ESCRIBIR */
    .caja-comando {
        background: rgba(0, 30, 60, 0.8);
        border: 1px solid #00eeff !important;
        color: #ffffff !important;
        font-family: 'Courier New', monospace !important;
        font-size: 17px !important;
        border-radius: 3px !important;
        box-shadow: inset 0 0 10px #002244 !important;
    }

    /* BOTÓN */
    .boton-sistema {
        background: linear-gradient(180deg, #0077dd, #004499) !important;
        color: white !important;
        border: 1px solid #00ccff !important;
        font-family: 'Courier New', monospace !important;
        font-weight: bold !important;
        font-size: 16px !important;
        border-radius: 3px !important;
        box-shadow: 0 0 12px rgba(0,150,255,0.5) !important;
        width: 100% !important;
        padding: 10px !important;
        margin-top: 10px !important;
    }

    .boton-sistema:hover {
        background: linear-gradient(180deg, #0099ff, #0066bb) !important;
        box-shadow: 0 0 20px #00ccff !important;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 🖥️ ESTRUCTURA DE LA PÁGINA
# -----------------------------------------------------------------------------

# Barra superior
st.markdown('<div class="barra-superior"> <span>>> SISTEMA JARVIS | OPERATIVO</span> <span>ESTADO: ACTIVO | CONECTADO</span> </div>', unsafe_allow_html=True)

# Núcleo brillante
st.markdown("""
<div class="nucleo-central">
    <div class="centro"></div>
    <div class="rayo1"></div>
    <div class="rayo2"></div>
    <div class="rayo3"></div>
    <div class="chispa" style="top:20%; left:60%"></div>
    <div class="chispa" style="top:70%; left:30%"></div>
    <div class="chispa" style="top:40%; left:80%"></div>
    <div class="chispa" style="top:80%; left:70%"></div>
</div>
""", unsafe_allow_html=True)

# Título
st.markdown("<h2 style='text-align:center; color:#00eeff; text-shadow:0 0 15px #00aaff; margin:-20px 0 40px;'>JARVIS - INTERFAZ PRINCIPAL</h2>", unsafe_allow_html=True)

# Entrada de datos
st.markdown('<div class="ventana"> <div class="ventana-titulo">>> ENTRADA DE COMANDO</div>', unsafe_allow_html=True)

texto_entrada = st.text_area(
    "",
    placeholder=">>> Escribe cualquier pregunta o instrucción... (Ej: ¿Quién te creó? / ¿Cómo te llamas? / ¿Qué haces?)",
    height=100,
    key="entrada"
)

boton_ejecutar = st.button(">> EJECUTAR <<", key="boton")
st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# ⚙️ PROCESAMIENTO Y RESPUESTA
# -----------------------------------------------------------------------------
if boton_ejecutar and texto_entrada.strip() != "":
    # Obtener respuesta de Jarvis (ENTIENDE TODO)
    respuesta = jarvis_respuesta(texto_entrada)

    # Reproducir voz de Jarvis
    voz_jarvis(respuesta)

    # Mostrar respuesta en pantalla
    st.markdown(f"""
    <div class="ventana" style="border-color:#00ff88; box-shadow:0 0 20px rgba(0,255,136,0.3);">
        <div class="ventana-titulo" style="color:#00ffaa;">>> SALIDA - JARVIS</div>
        <p style="margin:0; font-size:18px; color:#99ffcc;">{respuesta}</p>
    </div>
    """, unsafe_allow_html=True)


# Pie de página
st.markdown("""
<div style="text-align:center; margin-top:50px; color:#3377aa; font-size:13px;">
>>> JARVIS | SISTEMA ESTABLE | TODOS LOS MÓDULOS ACTIVOS <<<
</div>
""", unsafe_allow_html=True)
