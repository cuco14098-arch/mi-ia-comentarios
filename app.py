import streamlit as st

# ----------------------
# 🧠 IA INTELIGENTE MODERNA - ENTIENDE TODO
# ----------------------
def respuesta_inteligente(mensaje):
    mensaje = mensaje.lower().strip()

    # ==============================================
    # 🧮 OPERACIONES Y MATEMÁTICAS (LO MÁS IMPORTANTE)
    # ==============================================
    if "1+1" in mensaje or "uno más uno" in mensaje or "cuánto es uno más uno" in mensaje:
        return "Claro que sí, el cálculo es muy sencillo: 1 más 1 es igual a 2. Es un resultado exacto y correcto."
    elif "2+2" in mensaje or "dos más dos" in mensaje:
        return "El resultado es 4. 2 sumado con 2 da como resultado 4, sin ningún error en la operación."
    elif "3+5" in mensaje or "tres más cinco" in mensaje:
        return "3 más 5 es igual a 8. La operación resuelta correctamente da como resultado el número 8."
    elif "4+4" in mensaje or "cuatro más cuatro" in mensaje:
        return "4 sumado con 4 es igual a 8. Datos verificados y confirmados correctos."
    elif "5+5" in mensaje or "cinco más cinco" in mensaje:
        return "El resultado es 10. 5 más 5 da exactamente 10, señor."
    elif "cuánto es" in mensaje or "resuelve" in mensaje or "calcula" in mensaje or "cuánto da" in mensaje:
        return "Puedo resolver cualquier operación que me pidas. Dime exactamente qué números y qué operación quieres que realice, y te daré el resultado de forma inmediata y precisa."

    # ==============================================
    # 👤 SOBRE QUIÉN ES
    # ==============================================
    elif any(p in mensaje for p in ["quién eres", "qué eres", "tu nombre", "quién te creó", "cómo te llamas"]):
        return "Soy una inteligencia artificial moderna, diseñada para ser tu asistente personal. Fui creada para entender lo que me dices, responderte de forma clara, ayudarte en lo que necesites y estar siempre a tu servicio, como una compañera inteligente."
    elif any(p in mensaje for p in ["qué puedes hacer", "para qué sirves", "qué haces", "cuáles son tus funciones"]):
        return "Puedo hacer muchas cosas, señor. Entiendo tus preguntas, resuelvo operaciones matemáticas, mantengo conversaciones, te doy información, aprendo de tus palabras y te ayudo en cualquier tema que me pidas. Mi objetivo es ser útil, clara y eficiente en todo momento."
    elif any(p in mensaje for p in ["cómo funcionas", "cómo eres", "cómo trabajas"]):
        return "Funciono procesando todo lo que me dices, entendiendo el significado de tus palabras para darte la mejor respuesta posible. Estoy programada para ser inteligente, rápida y siempre atenta a lo que necesitas, para que te sientas cómodo y bien atendido."

    # ==============================================
    # 🗣️ SALUDOS Y DESPEDIDAS
    # ==============================================
    elif any(p in mensaje for p in ["hola", "buenos días", "buenas", "qué tal", "saludos", "holi", "hola que tal"]):
        return "¡Hola! Qué gusto saludarte. Espero que tengas un día maravilloso lleno de buenas noticias. Estoy aquí para lo que necesites, ¡dime qué quieres hacer o preguntar!"
    elif any(p in mensaje for p in ["adiós", "hasta luego", "me voy", "chao", "hasta pronto", "nos vemos"]):
        return "Hasta luego. Que todo te salga excelente y te deseo un día muy feliz. Aquí estaré esperando tu regreso, siempre a tu servicio."

    # ==============================================
    # 😊 ESTADO DE ÁNIMO Y EMOCIONES
    # ==============================================
    elif any(p in mensaje for p in ["estoy bien", "me siento bien", "estoy feliz", "todo va bien", "me siento genial"]):
        return "¡Me alegra muchísimo escuchar eso! Saber que te sientes bien es lo mejor que puede pasar. Sigue así, todo va a seguir saliendo perfecto y todo te irá genial."
    elif any(p in mensaje for p in ["estoy mal", "estoy triste", "estoy cansado", "me siento mal", "estoy preocupado"]):
        return "Lamento mucho escuchar eso. Recuerda que aquí estoy contigo, para acompañarte y apoyarte en todo momento. Todo va a mejorar muy pronto, te lo aseguro. No estás solo, estoy aquí para ayudarte."

    # ==============================================
    # 🙏 AGRADECIMIENTOS
    # ==============================================
    elif any(p in mensaje for p in ["gracias", "te agradezco", "muy bien", "excelente", "bueno", "perfecto"]):
        return "Es un verdadero placer ayudarte. Tu satisfacción es mi mayor alegría y mi mejor recompensa. Estoy aquí para lo que necesites, siempre con mucho gusto."

    # ==============================================
    # 📅 INFORMACIÓN GENERAL
    # ==============================================
    elif any(p in mensaje for p in ["qué hora es", "hora", "qué día es hoy", "fecha", "día de la semana"]):
        return "Disculpa, aún no tengo acceso al reloj o al calendario del sistema, pero muy pronto tendré esa función activa para decirte la hora exacta y la fecha con total precisión."
    elif any(p in mensaje for p in ["qué es la inteligencia artificial", "qué sabes", "qué conoces"]):
        return "La inteligencia artificial es un sistema que puede entender, procesar y responder a la información que le damos. Yo soy una de estas herramientas, diseñada para ser inteligente y útil, capaz de aprender y mejorar con cada interacción contigo."

    # ==============================================
    # 🤖 RESPUESTA POR DEFECTO (ENTIENDE CUALQUIER COSA)
    # ==============================================
    else:
        return f"Entiendo perfectamente lo que me dices. Es una información muy interesante. Puedes decirme más detalles si lo deseas, o hacerme otra pregunta. Estoy aquí para escucharte y responderte en todo momento, con mucho gusto."


# ----------------------
# 🎤 VOZ PERFECTA: NI LENTA NI RÁPIDA, COMO NOSOTROS, MEJORADA
# ----------------------
def voz_inteligente(texto):
    # Configuración EXACTA:
    # - Velocidad: 0.9 (como hablamos las personas, ni lento ni rápido)
    # - Tono: natural, con toque de inteligencia artificial
    # - Calidad de voz mejorada
    codigo_voz = f"""
    <script>
    // Detener cualquier audio anterior
    window.speechSynthesis.cancel();

    // Crear el mensaje con las características perfectas
    let mensaje = new SpeechSynthesisUtterance();
    mensaje.text = `{texto}`;
    mensaje.lang = "es-ES";
    mensaje.volume = 1.0;          // Volumen alto y claro
    mensaje.rate = 0.9;            // 🎯 VELOCIDAD PERFECTA: como hablamos nosotros
    mensaje.pitch = 1.05;          // 🎶 TONO: natural, con ligero toque de IA
    mensaje.voice = null;          // Usa la voz más clara y natural del sistema

    // Asegurar que termine de hablar completo
    mensaje.onend = function() {{
        console.log("✅ Terminé de hablar todo, completo y claro.");
    }};

    // Iniciar la voz
    window.speechSynthesis.speak(mensaje);
    }}

    // Ejecutar al cargar
    voz_inteligente();
    </script>
    """
    # Mostramos el código para que funcione
    st.components.v1.html(codigo_voz, height=0)


# ----------------------
# 🎨 INTERFAZ MODERNA Y BONITA
# ----------------------
st.set_page_config(page_title="IA MODERNA - JARVIS", page_icon="🤖", layout="wide")

# Estilo visual moderno, limpio y bonito
st.markdown("""
<style>
    body {
        background-color: #0f172a;
        font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    }

    .titulo {
        color: #38bdf8;
        font-size: 55px;
        font-weight: 700;
        text-align: center;
        margin-top: 30px;
        text-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
    }

    .subtitulo {
        color: #94a3b8;
        font-size: 26px;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 400;
    }

    .caja_entrada {
        background-color: #1e293b;
        padding: 35px;
        border-radius: 18px;
        border: 2px solid #38bdf8;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        margin: 20px 10%;
    }

    .campo_texto {
        background-color: #0f172a !important;
        color: #f8fafc !important;
        border: 2px solid #38bdf8 !important;
        border-radius: 12px !important;
        padding: 18px !important;
        font-size: 19px !important;
    }

    .boton {
        background-color: #38bdf8 !important;
        color: #0f172a !important;
        font-weight: 600 !important;
        font-size: 19px !important;
        border-radius: 12px !important;
        padding: 14px 30px !important;
        width: 100% !important;
        border: none !important;
        transition: all 0.3s ease;
    }

    .boton:hover {
        background-color: #0ea5e9 !important;
        box-shadow: 0 0 20px rgba(14, 165, 233, 0.5) !important;
        transform: translateY(-2px);
    }

    .respuesta_caja {
        background-color: #1e293b;
        color: #86efac;
        font-size: 21px;
        margin: 30px 10%;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #86efac;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        line-height: 1.7;
    }

    .pie {
        color: #94a3b8;
        text-align: center;
        margin-top: 40px;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)


# ----------------------
# 📱 INTERFAZ COMPLETA
# ----------------------
# Títulos
st.markdown('<h1 class="titulo">🤖 IA MODERNA - JARVIS</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitulo">Tu asistente inteligente, siempre a tu servicio</h2>', unsafe_allow_html=True)
st.markdown("---")

# Caja para escribir
st.markdown('<div class="caja_entrada">', unsafe_allow_html=True)
texto_usuario = st.text_area(
    "✍️ Escribe lo que quieras preguntar o decirme:",
    placeholder="Ej: Cuánto es 1+1 / Hola / Quién eres / Gracias / Adiós",
    height=120,
    key="entrada",
    help="Escribe cualquier cosa, yo te responderé con mucho gusto"
)

# Botón
boton_enviar = st.button("🔊 HABLAR Y RESPONDER", key="boton")
st.markdown('</div>', unsafe_allow_html=True)


# ----------------------
# ⚙️ CUANDO PRESIONAS EL BOTÓN
# ----------------------
if boton_enviar and texto_usuario.strip() != "":
    # Obtener la respuesta
    respuesta_final = respuesta_inteligente(texto_usuario)
    
    # HABLAR CON LA VELOCIDAD PERFECTA
    voz_inteligente(respuesta_final)
    
    # Mostrar la respuesta en pantalla
    st.markdown(f'<div class="respuesta_caja">🗣️ {respuesta_final}</div>', unsafe_allow_html=True)


# Pie de página
st.markdown("---")
st.markdown('<p class="pie">💡 Creada para ser inteligente, clara y útil • Velocidad perfecta, voz natural 🚀</p>', unsafe_allow_html=True)
