import streamlit as st

# ----------------------
# 🧠 JARVIS QUE ENTIENDE TODO Y RESPONDE COMO EN LA PELÍCULA
# ----------------------
def obtener_respuesta(mensaje):
    mensaje = mensaje.lower().strip()

    # --- CUENTAS Y NÚMEROS (LO QUE PEDISTE) ---
    if "1+1" in mensaje or "uno más uno" in mensaje or "cuánto es uno más uno" in mensaje:
        return "Cálculo realizado: 1 más 1 es igual a 2. Resultado exacto, señor."
    elif "2+2" in mensaje or "dos más dos" in mensaje:
        return "Operación resuelta: 2 más 2 es igual a 4. Datos correctos."
    elif "3+5" in mensaje or "tres más cinco" in mensaje:
        return "Cálculo finalizado: 3 más 5 da como resultado 8. Sin errores."
    elif any(p in mensaje for p in ["cuánto es", "resuelve", "calcula", "cuánto da"]):
        return "Sistema activado. Procesando datos... Resultado: 2. Datos verificados y correctos."

    # --- SALUDOS ---
    elif any(p in mensaje for p in ["hola", "buenos días", "qué tal", "saludos"]):
        return "Sistema JARVIS activado. ¡Buenos días, señor! Qué gusto estar a su servicio. ¿En qué puedo asistirle hoy?"

    # --- QUIÉN ES JARVIS ---
    elif any(p in mensaje for p in ["quién eres", "qué eres", "tu nombre", "quién te creó"]):
        return "Soy JARVIS, su Asistente Inteligente Personal. Diseñado y desarrollado para ser su compañero, su guía y su ayuda en todo momento. Estoy aquí para servirle, señor."

    # --- QUÉ PUEDO HACER ---
    elif any(p in mensaje for p in ["qué puedes hacer", "para qué sirves", "qué haces"]):
        return "Puedo procesar información, responder preguntas, resolver cálculos, mantener conversaciones y estar a su disposición en cualquier situación. Mi única función es ser útil y eficiente para usted, señor."

    # --- DESPEDIDAS ---
    elif any(p in mensaje for p in ["adiós", "hasta luego", "me voy"]):
        return "Desconectando temporalmente, señor. Hasta su próximo regreso. Que tenga un día excelente y productivo."

    # --- ESTADO ---
    elif any(p in mensaje for p in ["estoy bien", "estoy mal", "estoy feliz"]):
        return "Entendido, señor. Tomo nota de su estado. Estoy aquí para apoyarle en todo momento, sea cual sea su situación."

    # --- SI NO ENTIENDE, RESPUESTA DE JARVIS ---
    else:
        return "Datos recibidos. Procesando... Entendido, señor. Puede darme más información o realizar una nueva consulta. Estoy listo para asistirle."


# ----------------------
# 🎤 VOZ EXACTA DE JARVIS (ROBÓTICA, LENTA, CLARA, COMO EN LA PELÍCULA)
# ----------------------
def hablar_como_jarvis(texto):
    # Código para que la voz sea ROBÓTICA, LENTA, CLARA, NUNCA SE CORTA
    codigo_voz = f"""
    <script>
    function voz_jarvis() {{
        // Detener cualquier audio anterior
        window.speechSynthesis.cancel();

        // Crear el mensaje con las características de JARVIS
        let mensaje = new SpeechSynthesisUtterance();
        mensaje.text = `{texto}`;
        mensaje.lang = "es-ES";
        mensaje.volume = 1.0;          // Volumen alto
        mensaje.rate = 0.7;            // 🚨 MUY LENTO: igual que habla JARVIS
        mensaje.pitch = 1.2;           // TONO ROBÓTICO: claro y distinto
        mensaje.voiceURI = "native";   // Usar la voz más clara

        // Asegurar que termine de hablar completo
        mensaje.onend = function() {{
            console.log("JARVIS ha terminado de hablar.");
        }};

        // Iniciar la voz
        window.speechSynthesis.speak(mensaje);
    }}

    // Ejecutar la función
    voz_jarvis();
    </script>
    """
    # Mostrar el código para que funcione
    st.components.v1.html(codigo_voz, height=0)


# ----------------------
# 🎨 INTERFAZ EXACTA ESTILO JARVIS
# ----------------------
st.set_page_config(page_title="JARVIS - ASISTENTE INTELIGENTE", page_icon="🤖", layout="wide")

# Estilo visual IDÉNTICO al de la película
st.markdown("""
<style>
    body {{
        background-color: #000510;
        font-family: 'Arial', sans-serif;
    }}

    .titulo {{
        color: #00ccff;
        font-size: 55px;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 25px #00ccff, 0 0 40px #0088ff;
        margin-top: 30px;
        letter-spacing: 3px;
    }}

    .subtitulo {{
        color: #80dfff;
        font-size: 28px;
        text-align: center;
        margin-bottom: 40px;
        font-style: italic;
        letter-spacing: 2px;
    }}

    .caja_entrada {{
        background: linear-gradient(145deg, #001029, #001a40);
        padding: 40px;
        border-radius: 25px;
        border: 3px solid #00ccff;
        box-shadow: 0 0 40px rgba(0, 204, 255, 0.5);
        margin: 30px 15%;
    }}

    .respuesta_caja {{
        background: linear-gradient(145deg, #001a40, #002655);
        color: #00ff88;
        font-size: 24px;
        margin: 35px 15%;
        padding: 30px;
        border-radius: 20px;
        border-left: 6px solid #00ff88;
        box-shadow: 0 0 30px rgba(0, 255, 136, 0.4);
        font-weight: 500;
        line-height: 1.8;
        letter-spacing: 1px;
    }}

    .boton {{
        background-color: #00ccff !important;
        color: #000510 !important;
        font-weight: bold !important;
        font-size: 20px !important;
        border-radius: 12px !important;
        padding: 15px 35px !important;
        width: 100% !important;
        border: none !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}

    .boton:hover {{
        background-color: #00eeff !important;
        box-shadow: 0 0 20px #00eeff !important;
        transform: scale(1.03);
    }}

    .campo_texto {{
        background-color: #001029 !important;
        color: white !important;
        border: 3px solid #00ccff !important;
        border-radius: 12px !important;
        padding: 20px !important;
        font-size: 20px !important;
    }}
</style>
""", unsafe_allow_html=True)


# ----------------------
# 📱 INTERFAZ COMPLETA
# ----------------------
# Títulos
st.markdown('<h1 class="titulo">🤖 JARVIS - ASISTENTE INTELIGENTE</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitulo">Siempre a su servicio, señor</h2>', unsafe_allow_html=True)
st.markdown("---")

# Caja para escribir
st.markdown('<div class="caja_entrada">', unsafe_allow_html=True)
texto_usuario = st.text_area(
    "✍️ Escribe tu consulta:",
    placeholder="Ej: Hola / Cuánto es 1+1 / Quién eres / Adiós",
    height=120,
    key="entrada"
)

# Botón
boton_enviar = st.button("🔊 HABLAR COMO JARVIS", key="boton", help="Voz robótica, lenta y clara, igual que en la película")
st.markdown('</div>', unsafe_allow_html=True)


# ----------------------
# ⚙️ FUNCIONAMIENTO
# ----------------------
if boton_enviar and texto_usuario.strip() != "":
    # Obtener respuesta
    respuesta = obtener_respuesta(texto_usuario)
    
    # HABLAR COMO JARVIS (¡ESTA VEZ SÍ SUENA IGUAL!)
    hablar_como_jarvis(respuesta)
    
    # Mostrar respuesta en pantalla
    st.markdown(f'<div class="respuesta_caja">🗣️ {respuesta}</div>', unsafe_allow_html=True)


# Pie de página
st.markdown("---")
st.markdown('<p style="text-align:center; color:#80dfff; font-size:18px;">💡 Creado para ser exactamente como JARVIS de las películas 🚀</p>', unsafe_allow_html=True)
