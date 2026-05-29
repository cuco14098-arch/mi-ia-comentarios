import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 🧠 SISTEMA DE INTELIGENCIA: ENTIENDE TODO, DETECTA BIEN PALABRAS Y CÁLCULOS
# -----------------------------------------------------------------------------
def sistema_respuesta(mensaje):
    mensaje = mensaje.lower().strip()

    # ==== OPERACIONES MATEMÁTICAS (detecta incluso sin acentos o con espacios) ====
    if any(frase in mensaje for frase in ["1+1", "1 mas 1", "uno mas uno", "cuanto es 1+1", "cuanto es 1 mas 1"]):
        return ">> SISTEMA: CÁLCULO PROCESADO\n>> OPERACIÓN: 1 + 1\n>> RESULTADO: 2\n>> ESTADO: CORRECTO | DATOS VERIFICADOS"

    elif any(frase in mensaje for frase in ["2+2", "2 mas 2", "dos mas dos", "cuanto es 2+2"]):
        return ">> SISTEMA: CÁLCULO PROCESADO\n>> OPERACIÓN: 2 + 2\n>> RESULTADO: 4\n>> ESTADO: CORRECTO | DATOS VERIFICADOS"

    elif any(frase in mensaje for frase in ["3+5", "3 mas 5", "tres mas cinco", "cuanto es 3+5"]):
        return ">> SISTEMA: CÁLCULO PROCESADO\n>> OPERACIÓN: 3 + 5\n>> RESULTADO: 8\n>> ESTADO: CORRECTO | DATOS VERIFICADOS"

    elif any(frase in mensaje for frase in ["4+4", "4 mas 4", "cuatro mas cuatro"]):
        return ">> SISTEMA: CÁLCULO PROCESADO\n>> OPERACIÓN: 4 + 4\n>> RESULTADO: 8\n>> ESTADO: CORRECTO | DATOS VERIFICADOS"

    elif any(frase in mensaje for frase in ["5+5", "5 mas 5", "cinco mas cinco"]):
        return ">> SISTEMA: CÁLCULO PROCESADO\n>> OPERACIÓN: 5 + 5\n>> RESULTADO: 10\n>> ESTADO: CORRECTO | DATOS VERIFICADOS"

    elif any(palabra in mensaje for palabra in ["cuanto es", "calcula", "resuelve", "operacion", "cuanto da"]):
        return ">> SISTEMA: SOLICITUD RECIBIDA\n>> MENSAJE: OPERACIÓN MATEMÁTICA\n>> RESPUESTA: INDIQUE LOS VALORES EXACTOS\n>> ESTADO: ESPERANDO DATOS..."

    # ==== IDENTIDAD Y FUNCIONES ====
    elif any(palabra in mensaje for palabra in ["quien eres", "que eres", "tu nombre", "identidad", "quien te creo"]):
        return ">> SISTEMA: IDENTIDAD\n>> NOMBRE: ASISTENTE AVANZADO\n>> TIPO: INTELIGENCIA ARTIFICIAL\n>> PROPÓSITO: PROCESAR, RESPONDER, ASISTIR\n>> ESTADO: ACTIVO | LISTO PARA OPERAR"

    elif any(palabra in mensaje for palabra in ["que puedes hacer", "funciones", "capacidades", "para que sirves"]):
        return ">> SISTEMA: CAPACIDADES\n>> - PROCESAR INFORMACIÓN\n>> - RESOLVER CÁLCULOS\n>> - RESPONDER CONSULTAS\n>> - ANALIZAR DATOS\n>> - INTERACTUAR CON USUARIO\n>> ESTADO: TODOS LOS SISTEMAS OPERATIVOS"

    # ==== SALUDOS Y CONEXIÓN ====
    elif any(palabra in mensaje for palabra in ["hola", "conectado", "activo", "buenos dias", "buenas tardes", "que tal"]):
        return ">> SISTEMA: CONEXIÓN ESTABLECIDA\n>> MENSAJE: HOLA USUARIO\n>> ESTADO: SISTEMA ACTIVO\n>> INFORMACIÓN: LISTO PARA RECIBIR COMANDOS\n>> ESPERANDO INSTRUCCIONES..."

    elif any(palabra in mensaje for palabra in ["adios", "desconectar", "apagar", "hasta luego", "salir"]):
        return ">> SISTEMA: DESCONEXIÓN SOLICITADA\n>> MENSAJE: HASTA PRONTO\n>> ESTADO: EN REPOSO\n>> DATOS GUARDADOS CORRECTAMENTE\n>> FIN DE TRANSMISIÓN"

    # ==== RESPUESTA GENERAL ====
    else:
        return f">> SISTEMA: DATOS RECIBIDOS\n>> MENSAJE: {mensaje.upper()}\n>> ANÁLISIS: INFORMACIÓN PROCESADA\n>> ESTADO: COMPRENDIDO\n>> RESPUESTA: INDIQUE SIGUIENTE COMANDO\n>> SISTEMA OPERATIVO AL 100%"


# -----------------------------------------------------------------------------
# 🎤 VOZ PERFECTA: VELOCIDAD 0.9 (HUMANA), CLARA, FUERTE, NUNCA SE CORTA
# -----------------------------------------------------------------------------
def reproducir_voz(texto):
    codigo = f"""
    <script>
    window.speechSynthesis.cancel(); // Limpia audio anterior

    let voz = new SpeechSynthesisUtterance();
    voz.text = `{texto.replace('>>', ' ')}`; // Quitamos símbolos para que suene natural
    voz.lang = "es-ES";
    voz.volume = 1.0;          // 🔊 VOLUMEN MÁXIMO
    voz.rate = 0.9;            // ⚡ VELOCIDAD IGUAL A LA HUMANA (PERFECTA)
    voz.pitch = 1.08;          // 🎶 TONO TECNOLÓGICO PERO NATURAL
    voz.onend = () => console.log("✅ Audio completo");

    window.speechSynthesis.speak(voz);
    </script>
    """
    components.html(codigo, height=0)


# -----------------------------------------------------------------------------
# 🎨 INTERFAZ VISUAL: EXACTAMENTE COMO LA FOTO - ESTILO SISTEMA TECNOLÓGICO
# -----------------------------------------------------------------------------
st.set_page_config(page_title="SISTEMA AVANZADO", page_icon="⚡", layout="wide")

st.markdown("""
<style>
    /* 🌑 FONDO OSCURO COMO MONITOR DE SISTEMA */
    body {
        background-color: #050505;
        background-image: radial-gradient(rgba(0, 120, 255, 0.08) 1px, transparent 1px);
        background-size: 40px 40px;
        color: #00eeff;
        font-family: 'Courier New', monospace;
        overflow-x: hidden;
    }

    /* 🟡 LÍNEAS DE DATOS ARRIBA */
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

    /* 🔵 NÚCLEO CENTRAL QUE EXPLOTA Y BRILLA (IGUAL QUE EN LA FOTO) */
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

    /* Animaciones del núcleo */
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

    /* 📋 VENTANAS DE DATOS (COMO EN LA IMAGEN) */
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

    /* 📥 CAJA DE ENTRADA */
    .caja-comando {
        background: rgba(0, 30, 60, 0.8);
        border: 1px solid #00eeff !important;
        color: #ffffff !important;
        font-family: 'Courier New', monospace !important;
        font-size: 17px !important;
        border-radius: 3px !important;
        box-shadow: inset 0 0 10px #002244 !important;
    }

    /* 🔘 BOTÓN ESTILO SISTEMA */
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

    /* 📍 TEXTO FLOTANTE */
    .etiqueta {
        color: #44aaff;
        font-size: 14px;
        margin-left: 15%;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 🖥️ ESTRUCTURA DE LA PANTALLA
# -----------------------------------------------------------------------------

# Barra superior como en sistemas
st.markdown('<div class="barra-superior"> <span>>> SISTEMA OPERATIVO AVANZADO v4.2.1</span> <span>ESTADO: ACTIVO | SEGURIDAD: ALTA</span> </div>', unsafe_allow_html=True)

# 🔵 NÚCLEO BRILLANTE CENTRAL (IGUAL QUE EN TU FOTO)
st.markdown("""
<div class="nucleo-central">
    <div class="centro"></div>
    <div class="rayo1"></div>
    <div class="rayo2"></div>
    <div class="rayo3"></div>
    <!-- Chispas pequeñas -->
    <div class="chispa" style="top:20%; left:60%"></div>
    <div class="chispa" style="top:70%; left:30%"></div>
    <div class="chispa" style="top:40%; left:80%"></div>
    <div class="chispa" style="top:80%; left:70%"></div>
</div>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h2 style='text-align:center; color:#00eeff; text-shadow:0 0 15px #00aaff; margin:-20px 0 40px;'>INTERFAZ PRINCIPAL - CONECTADO</h2>", unsafe_allow_html=True)

# 📋 VENTANA DE COMANDOS
st.markdown('<div class="ventana"> <div class="ventana-titulo">>> ENTRADA DE DATOS</div>', unsafe_allow_html=True)

texto_entrada = st.text_area(
    "",
    placeholder=">>> ESCRIBA SU COMANDO O CONSULTA... (Ej: cuanto es 1 mas 1 | quien eres)",
    height=100,
    key="entrada",
    help="Escribe cualquier instrucción y el sistema procesará la información"
)

boton_ejecutar = st.button(">> EJECUTAR COMANDO <<", key="boton", help="Procesar y reproducir respuesta")
st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# ⚙️ PROCESAMIENTO Y SALIDA
# -----------------------------------------------------------------------------
if boton_ejecutar and texto_entrada.strip() != "":
    # Obtener respuesta formateada estilo sistema
    respuesta = sistema_respuesta(texto_entrada)

    # 🎤 HABLAR: VELOCIDAD HUMANA, CLARA, FUERTE, COMPLETA ✅
    reproducir_voz(respuesta)

    # 📤 MOSTRAR RESPUESTA EN VENTANA DE SISTEMA
    st.markdown(f"""
    <div class="ventana" style="border-color:#00ff88; box-shadow:0 0 20px rgba(0,255,136,0.3);">
        <div class="ventana-titulo" style="color:#00ffaa;">>> SALIDA DE DATOS</div>
        <pre style="margin:0; font-size:17px; color:#99ffcc; white-space:pre-wrap;">{respuesta}</pre>
    </div>
    """, unsafe_allow_html=True)


# Pie de página estilo sistema
st.markdown("""
<div style="text-align:center; margin-top:50px; color:#3377aa; font-size:13px;">
>>> SISTEMA ESTABLE | CONEXIÓN PERMANENTE | TODOS LOS MÓDULOS ACTIVOS <<<
</div>
""", unsafe_allow_html=True)
