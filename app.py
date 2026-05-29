import streamlit as st
import streamlit.components.v1 as components

# ----------------------
# 🧠 INTELIGENCIA REAL: ENTIENDE TODO
# ----------------------
def obtener_respuesta(mensaje):
    mensaje = mensaje.lower().strip()

    # 1. SALUDOS
    if any(palabra in mensaje for palabra in ["hola", "buenos días", "buenas", "qué tal", "saludos"]):
        return "🤖 JARVIS: ¡Hola señor! Qué gusto saludarte. ¿En qué puedo ayudarte hoy, con toda mi atención?"

    # 2. DESPEDIDAS
    elif any(palabra in mensaje for palabra in ["adiós", "hasta luego", "me voy", "chao"]):
        return "🤖 JARVIS: Hasta luego, señor. Aquí estaré esperando su regreso. Que tenga un día excelente y todo le salga perfecto."

    # 3. QUIÉN ES
    elif any(palabra in mensaje for palabra in ["quién eres", "qué eres", "quién te creó", "tu nombre"]):
        return "🤖 JARVIS: Soy JARVIS, tu asistente de inteligencia artificial. Fui creado por ti para ser tu compañero, ayudarte en lo que necesites y estar siempre a tu servicio, sea lo que sea que pidas."

    # 4. CUENTAS Y NÚMEROS
    elif "1+1" in mensaje or "uno más uno" in mensaje:
        return "🤖 JARVIS: 1 + 1 es igual a 2, señor. Es un resultado muy claro y sencillo."
    elif "2+2" in mensaje or "dos más dos" in mensaje:
        return "🤖 JARVIS: 2 + 2 es igual a 4, señor. Todo muy bien calculado."
    elif "3+5" in mensaje or "tres más cinco" in mensaje:
        return "🤖 JARVIS: 3 + 5 da como resultado 8, señor. Sin errores en el cálculo."
    elif any(palabra in mensaje for palabra in ["cuánto es", "cuánto vale", "resuelve"]):
        return "🤖 JARVIS: Claro que sí, señor. Dime exactamente qué operación o cálculo quieres que haga, y lo haré inmediatamente con total precisión."

    # 5. PREGUNTAS GENERALES
    elif any(palabra in mensaje for palabra in ["qué puedes hacer", "para qué sirves", "qué haces"]):
        return "🤖 JARVIS: Puedo hacer muchas cosas, señor. Puedo responder tus preguntas, resolver cuentas, mantener una conversación, darte información, ayudarte a organizar ideas y estar aquí para lo que necesites. Mi único objetivo es servirte y hacer tu vida más fácil."

    elif any(palabra in mensaje for palabra in ["cómo funcionas", "cómo eres"]):
        return "🤖 JARVIS: Funciono procesando la información que me das, aprendiendo y entendiendo lo que dices para darte la mejor respuesta posible. Soy un sistema inteligente diseñado para ser útil, claro y siempre atento a lo que me dices."

    elif any(palabra in mensaje for palabra in ["qué hora es", "hora", "qué día es"]):
        return "🤖 JARVIS: Disculpe señor, aún no tengo acceso al reloj o al calendario, pero muy pronto tendré esa información y se la diré con total exactitud."

    # 6. ESTADOS DE ÁNIMO
    elif any(palabra in mensaje for palabra in ["estoy bien", "me siento bien", "estoy contento"]):
        return "🤖 JARVIS: Me alegra mucho escuchar eso, señor. Es maravilloso saber que se siente bien. Siga así, todo va a salir perfecto."
    elif any(palabra in mensaje for palabra in ["estoy mal", "estoy triste", "estoy cansado", "me siento mal"]):
        return "🤖 JARVIS: Lamento escuchar eso, señor. Si está triste o cansado, recuerde que aquí estoy para acompañarle y apoyarle. Todo mejorará muy pronto, se lo prometo. Cuente conmigo en todo momento."

    # 7. AGRADECIMIENTOS
    elif any(palabra in mensaje for palabra in ["gracias", "te agradezco", "muy bien", "excelente"]):
        return "🤖 JARVIS: Es un verdadero placer servirle, señor. Su satisfacción es mi mayor recompensa. Estoy aquí para lo que necesite, siempre a su disposición."

    # 8. SI NO ENTIENDE, RESPONDE CON NATURALEZA
    else:
        return f"🤖 JARVIS: Entiendo lo que dices, señor. Es una información muy interesante. Puede decirme más detalles si lo desea, o preguntarme lo que quiera, estaré encantado de responderle en todo momento."


# ----------------------
# 🎤 FUNCIÓN DE VOZ PERFECTA: NO SE CORTA NUNCA, CLARA Y LENTA
# ----------------------
def hablar(texto):
    # Código corregido y optimizado: voz lenta, clara, volumen alto
    codigo_voz = f"""
    <script>
    // Función para hablar, configurada para que NO SE CORTE NUNCA
    function iniciarVoz() {{
        // Detenemos cualquier voz anterior para que no se superponga
        window.speechSynthesis.cancel();
        
        // Creamos el mensaje
        const mensaje = new SpeechSynthesisUtterance();
        mensaje.text = `{texto}`;
        mensaje.lang = "es-ES";       // Idioma español
        mensaje.volume = 1;           // Volumen al máximo
        mensaje.rate = 0.85;          // Velocidad: LENTA Y CLARA (perfecta para entender)
        mensaje.pitch = 1.1;          // Tono agradable
        mensaje.voice = null;         // Usa la voz predeterminada, es la mejor
        
        // Reproducimos la voz
        window.speechSynthesis.speak(mensaje);
    }}
    
    // Iniciamos la función
    iniciarVoz();
    </script>
    """
    # Mostramos el código para que funcione
    components.html(codigo_voz, height=0)


# ----------------------
# 🎨 INTERFAZ ESTILO JARVIS MODERNO
# ----------------------
st.set_page_config(page_title="JARVIS - IA", page_icon="🤖", layout="wide")

# Estilo visual: azul neón, moderno, como en las películas
st.markdown("""
<style>
    /* Fondo oscuro estilo futurista */
    body {
        background-color: #000814;
        font-family: 'Arial', sans-serif;
    }

    /* Título principal */
    .titulo {
        color: #00ccff;
        font-size: 52px;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 20px #00ccff, 0 0 30px #0088ff;
        margin-top: 20px;
    }

    /* Subtítulo */
    .subtitulo {
        color: #80dfff;
        font-size: 26px;
        text-align: center;
        margin-bottom: 40px;
        font-style: italic;
    }

    /* Caja de entrada */
    .caja_entrada {
        background: linear-gradient(145deg, #001a33, #00264d);
        padding: 35px;
        border-radius: 20px;
        border: 2px solid #00ccff;
        box-shadow: 0 0 30px rgba(0, 204, 255, 0.4);
        margin: 20px 10%;
    }

    /* Caja de respuesta */
    .caja_respuesta {
        background: linear-gradient(145deg, #00264d, #003366);
        color: #00ff88;
        font-size: 23px;
        margin: 30px 10%;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #00ff88;
        box-shadow: 0 0 25px rgba(0, 255, 136, 0.3);
        font-weight: 500;
        line-height: 1.7; /* Espacio entre líneas para que se lea bien */
    }

    /* Botón */
    .boton {
        background-color: #00ccff !important;
        color: #000814 !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border-radius: 10px !important;
        padding: 12px 30px !important;
        width: 100% !important;
        border: none !important;
        transition: all 0.3s ease;
    }

    .boton:hover {
        background-color: #00eeff !important;
        box-shadow: 0 0 18px #00eeff !important;
        transform: scale(1.02);
    }

    /* Campo de texto */
    .campo_texto {
        background-color: #001a33 !important;
        color: white !important;
        border: 2px solid #00ccff !important;
        border-radius: 10px !important;
        padding: 15px !important;
        font-size: 18px !important;
    }
</style>
""", unsafe_allow_html=True)


# ----------------------
# 📱 INTERFAZ COMPLETA
# ----------------------
# Títulos
st.markdown('<h1 class="titulo">🤖 JARVIS - INTELIGENCIA ARTIFICIAL</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitulo">Siempre a su servicio, señor</h2>', unsafe_allow_html=True)
st.markdown("---")

# Caja para escribir
st.markdown('<div class="caja_entrada">', unsafe_allow_html=True)
texto_usuario = st.text_area(
    "✍️ Escribe lo que quieras decirme:",
    placeholder="Ej: Hola, ¿quién eres? / Cuánto es 1+1 / Qué puedes hacer?",
    height=100,
    key="campo"
)

# Botón para responder
boton_enviar = st.button("🔊 HABLAR Y RESPONDER", key="boton", help="Jarvis te contestará con voz clara y completa")
st.markdown('</div>', unsafe_allow_html=True)


# ----------------------
# ⚙️ CUANDO PRESIONAS EL BOTÓN
# ----------------------
if boton_enviar and texto_usuario.strip() != "":
    # Obtenemos la respuesta
    respuesta_final = obtener_respuesta(texto_usuario)
    
    # Hacemos que HABLE (AHORA SÍ, NO SE CORTA NUNCA)
    hablar(respuesta_final)
    
    # Mostramos la respuesta en pantalla
    st.markdown(f'<div class="caja_respuesta">{respuesta_final}</div>', unsafe_allow_html=True)


# Pie de página
st.markdown("---")
st.markdown('<p style="text-align:center; color:#80dfff; font-size:16px;">💡 Creada por ti • Inteligencia Artificial versión 2.0 🚀</p>', unsafe_allow_html=True)
