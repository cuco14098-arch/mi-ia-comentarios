import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 🧠 SISTEMA DE RESPUESTAS CLARAS, RESUMIDAS Y FÁCILES DE ENTENDER
# -----------------------------------------------------------------------------
def sistema_respuesta(mensaje):
    mensaje = mensaje.lower().strip()

    # ==== PREGUNTAS SOBRE NOMBRE E IDENTIDAD ====
    if any(p in mensaje for p in ["como te llamas", "cual es tu nombre", "quien eres", "que eres"]):
        return "Me llamo Asistente Inteligente. Soy una inteligencia artificial diseñada para ayudarte y responder tus preguntas."

    # ==== OPERACIONES MATEMÁTICAS ====
    elif any(p in mensaje for p in ["1+1", "1 mas 1", "cuanto es 1+1", "cuanto es 1 mas 1"]):
        return "1 + 1 = 2. Es el resultado correcto y exacto."

    elif any(p in mensaje for p in ["2+2", "2 mas 2", "cuanto es 2+2"]):
        return "2 + 2 = 4. Resultado confirmado y correcto."

    elif any(p in mensaje for p in ["3+5", "3 mas 5", "cuanto es 3+5"]):
        return "3 + 5 = 8. Operación resuelta correctamente."

    elif any(p in mensaje for p in ["4+4", "4 mas 4"]):
        return "4 + 4 = 8. Datos verificados."

    elif any(p in mensaje for p in ["5+5", "5 mas 5"]):
        return "5 + 5 = 10. Resultado exacto."

    elif any(p in mensaje for p in ["cuanto es", "calcula", "resuelve", "operacion"]):
        return "Dime qué números y operación quieres que calcule, y te daré el resultado inmediatamente."

    # ==== FUNCIONES Y CAPACIDADES ====
    elif any(p in mensaje for p in ["que puedes hacer", "para que sirves", "funciones"]):
        return "Puedo resolver cálculos, responder tus dudas, mantener conversaciones y ayudarte en lo que necesites. Estoy aquí para servirte."

    # ==== SALUDOS Y CONEXIÓN ====
    elif any(p in mensaje for p in ["hola", "buenos dias", "buenas", "que tal"]):
        return "¡Hola! Estoy conectado y listo para ayudarte. Dime qué necesitas."

    elif any(p in mensaje for p in ["adios", "desconectar", "hasta luego"]):
        return "Hasta luego. Aquí estaré esperando cuando me necesites."

    # ==== AGRADECIMIENTOS ====
    elif any(p in mensaje for p in ["gracias", "te agradezco"]):
        return "Es un placer ayudarte. Estoy aquí para lo que quieras."

    # ==== RESPUESTA GENERAL CLARA ====
    else:
        return "Entendido perfectamente. Puedes hacerme cualquier pregunta o darme cualquier instrucción, yo te responderé con claridad."


# -----------------------------------------------------------------------------
# 🎤 VOZ PERFECTA: CLARA, VELOCIDAD HUMANA, NUNCA SE CORTA
# -----------------------------------------------------------------------------
def reproducir_voz(texto):
    codigo = f"""
    <script>
    window.speechSynthesis.cancel();

    let voz = new SpeechSynthesisUtterance();
    voz.text = `{texto}`;
    voz.lang = "es-ES";
    voz.volume = 1.0;
    voz.rate = 0.9;        // Velocidad perfecta, como hablamos nosotros
    voz.pitch = 1.05;      // Tono claro y natural
    voz.onend = () => console.log("Respuesta terminada");

    window.speechSynthesis.speak(voz);
    </script>
    """
    components.html(codigo, height=0)


# -----------------------------------------------------------------------------
# 🎨 INTERFAZ IGUAL QUE LA FOTO - DISEÑO ESPECTACULAR
# -----------------------------------------------------------------------------
st.set_page_config(page_title="SISTEMA AVANZADO", page_icon="⚡", layout="wide")

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

    /* TEXTO CLARO */
    .etiqueta {
        color: #44aaff;
        font-size: 14px;
        margin-left: 15%;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 🖥️ ESTRUCTURA DE LA PÁGINA
# -----------------------------------------------------------------------------

# Barra superior
st.markdown('<div class="barra-superior"> <span>>> SISTEMA OPERATIVO AVANZADO v4.2.1</span> <span>ESTADO: ACTIVO | SEGURIDAD: ALTA</span> </div>', unsafe_allow_html=True)

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
st.markdown("<h2 style='text-align:center; color:#00eeff; text-shadow:0 0 15px #00aaff; margin:-20px 0 40px;'>INTERFAZ PRINCIPAL - CONECTADO</h2>", unsafe_allow_html=True)

# Entrada de datos
st.markdown('<div class="ventana"> <div class="ventana-titulo">>> ENTRADA DE DATOS</div>', unsafe_allow_html=True)

texto_entrada = st.text_area(
    "",
    placeholder=">>> Escribe tu pregunta o comando... (Ej: ¿Cómo te llamas? / Cuánto es 1+1)",
    height=100,
    key="entrada"
)

boton_ejecutar = st.button(">> EJECUTAR COMANDO <<", key="boton")
st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# ⚙️ RESULTADO FINAL
# -----------------------------------------------------------------------------
if boton_ejecutar and texto_entrada.strip() != "":
    # Obtener respuesta CLARA Y RESUMIDA
    respuesta = sistema_respuesta(texto_entrada)

    # Reproducir voz PERFECTA
    reproducir_voz(respuesta)

    # Mostrar respuesta en pantalla
    st.markdown(f"""
    <div class="ventana" style="border-color:#00ff88; box-shadow:0 0 20px rgba(0,255,136,0.3);">
        <div class="ventana-titulo" style="color:#00ffaa;">>> SALIDA DE DATOS</div>
        <p style="margin:0; font-size:18px; color:#99ffcc;">{respuesta}</p>
    </div>
    """, unsafe_allow_html=True)


# Pie de página
st.markdown("""
<div style="text-align:center; margin-top:50px; color:#3377aa; font-size:13px;">
>>> SISTEMA ESTABLE | CONEXIÓN PERMANENTE | TODOS LOS MÓDULOS ACTIVOS <<<
</div>
""", unsafe_allow_html=True)
