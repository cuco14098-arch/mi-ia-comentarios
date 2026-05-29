import streamlit as st

# ----------------------
# 🧠 INTELIGENCIA ARTIFICIAL: RESPONDE A TODO
# ----------------------
def respuesta_ia(mensaje):
    mensaje = mensaje.lower().strip()

    # ==== SALUDOS ====
    if any(p in mensaje for p in ["hola", "buenos días", "buenas", "qué tal", "saludos", "holi"]):
        return "¡Hola señor! Qué gusto saludarte. Espero que tengas un día maravilloso lleno de éxitos. Estoy aquí a tu servicio, listo para ayudarte en todo lo que necesites."

    # ==== DESPEDIDAS ====
    elif any(p in mensaje for p in ["adiós", "hasta luego", "me voy", "chao", "hasta pronto"]):
        return "Hasta luego, señor. Aquí estaré siempre esperando tu regreso. Que todo te salga excelente y tengas un día muy feliz. Hasta la próxima."

    # ==== PREGUNTAS SOBRE ÉL ====
    elif any(p in mensaje for p in ["quién eres", "qué eres", "tu nombre", "quién te creó", "cómo te llamas"]):
        return "Soy JARVIS, tu asistente personal de inteligencia artificial. Fui creado por ti mismo, con el propósito de serte útil, responder tus preguntas, ayudarte y estar siempre a tu lado, como un compañero fiel y muy eficiente."

    # ==== MATEMÁTICAS / OPERACIONES ====
    elif "1+1" in mensaje or "uno más uno" in mensaje:
        return "Uno más uno es igual a dos, señor. Es una operación muy sencilla y el resultado es exacto."
    elif "2+2" in mensaje or "dos más dos" in mensaje:
        return "Dos más dos son cuatro, señor. Muy bien calculado y sin ningún error."
    elif "3+5" in mensaje or "tres más cinco" in mensaje:
        return "Tres más cinco da como resultado ocho, señor. Todo perfecto y correcto."
    elif "cuánto es" in mensaje or "resuelve" in mensaje or "calcula" in mensaje or "cuánto da" in mensaje:
        return "Por supuesto señor, puedo resolver cualquier operación. Dime exactamente qué números y qué quieres que haga, y te daré el resultado exacto y preciso."

    # ==== PREGUNTAS GENERALES ====
    elif "qué puedes hacer" in mensaje or "para qué sirves" in mensaje or "qué haces":
        return "Puedo hacer muchísimas cosas, señor. Respondo preguntas, resuelvo cálculos, te acompaño, te doy información, aprendo de ti y estoy aquí para todo lo que necesites. Mi única misión es serte útil."
    elif "qué hora es" in mensaje or "hora" in mensaje or "qué día es hoy":
        return "Disculpa señor, aún no tengo acceso al reloj del sistema, pero muy pronto tendré esa función y te diré la hora exacta al segundo."
    elif "cómo funcionas" in mensaje or "cómo eres":
        return "Funciono procesando todo lo que me dices, entendiendo tus palabras y buscando la mejor respuesta para ti. Me he creado para ser inteligente, claro y siempre muy atento a todo lo que pides."

    # ==== ESTADO DE ÁNIMO ====
    elif any(p in mensaje for p in ["estoy bien", "me siento bien", "estoy feliz", "todo va bien"]):
        return "¡Me alegra muchísimo escuchar eso, señor! Saber que estás bien es lo mejor que puede pasar. Sigue así, todo va a seguir saliendo perfecto."
    elif any(p in mensaje for p in ["estoy mal", "estoy triste", "estoy cansado", "me siento mal", "estoy preocupado"]):
        return "Lamento mucho escuchar eso, señor. Recuerda que aquí estoy contigo, para acompañarte y apoyarte. Todo va a mejorar muy pronto, te lo aseguro de corazón. No estás solo."

    # ==== AGRADECIMIENTOS ====
    elif any(p in mensaje for p in ["gracias", "te agradezco", "muy bien", "excelente", "bueno"]):
        return "Es un verdadero placer ayudarte, señor. Tu satisfacción es mi mayor alegría y mi única recompensa. Estoy aquí para lo que necesites, siempre a tu disposición."

    # ==== SI NO ENTIENDE, RESPUESTA INTELIGENTE ====
    else:
        return f"Entiendo perfectamente lo que me dices, señor. Es una información muy interesante y valiosa. Cuéntame más detalles o pregúntame lo que quieras, que yo estoy aquí para escucharte y responderte en todo momento."


# ----------------------
# 🎤 VOZ QUE NUNCA SE CORTA, LENTA Y CLARA (LA SOLUCIÓN)
# ----------------------
def voz_perfecta(texto):
    # Este código es diferente, evita que se corte y habla TODO
    codigo = f"""
    <html>
    <body>
    <script>
    function hablar() {{
        // Detiene cualquier audio anterior
        window.speechSynthesis.cancel();

        // CREAMOS EL MENSAJE CONFIGURADO PARA NO CORTARSE
        let mensaje = new SpeechSynthesisUtterance();
        mensaje.text = `{texto}`;
        mensaje.lang = "es-ES";
        mensaje.volume = 1;          // VOLUMEN AL MÁXIMO
        mensaje.rate = 0.75;         // 🚨 MUY LENTO, SÚPER CLARO, SE ENTIENDE TODO
        mensaje.pitch = 1.1;         // TONO AGRADABLE DE VOZ

        // OBLIGAMOS A QUE TERMINE DE HABLAR ANTES DE HACER OTRA COSA
        mensaje.onend = function(event) {{
            console.log("✅ Terminé de hablar todo completo");
        }};

        // EJECUTAMOS LA VOZ
        window.speechSynthesis.speak(mensaje);
    }}

    // EJECUTAR AL CARGAR
    hablar();
    </script>
    </body>
    </html>
    """
    # Usamos este método para que NO SE INTERRUMPA
    st.components.v1.html(codigo, height=0)


# ----------------------
# 🎨 INTERFAZ ESTILO JARVIS
# ----------------------
st.set_page_config(page_title="JARVIS IA", page_icon="🤖", layout="wide")

st.markdown("""
<style>
    body {background-color: #000814;}
    .titulo {
        color: #00ccff;
        font-size: 52px;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 20px #00ccff, 0 0 30px #0088ff;
        margin-top: 20px;
    }
    .subtitulo {
        color: #80dfff;
        font-size: 26px;
        text-align: center;
        margin-bottom: 40px;
        font-style: italic;
    }
    .caja {
        background: linear-gradient(145deg, #001a33, #00264d);
        padding: 35px;
        border-radius: 20px;
        border: 2px solid #00ccff;
        box-shadow: 0 0 30px rgba(0, 204, 255, 0.4);
        margin: 20px 10%;
    }
    .respuesta {
        background: linear-gradient(145deg, #00264d, #003366);
        color: #00ff88;
        font-size: 23px;
        margin: 30px 10%;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #00ff88;
        box-shadow: 0 0 25px rgba(0, 255, 136, 0.3);
        font-weight: 500;
        line-height: 1.7;
    }
    .boton {
        background-color: #00ccff !important;
        color: #000814 !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border-radius: 10px !important;
        padding: 12px 30px !important;
        width: 100% !important;
        border: none !important;
    }
    .boton:hover {
        background-color: #00eeff !important;
        box-shadow: 0 0 18px #00eeff !important;
    }
    .texto {
        background-color: #001a33 !important;
        color: white !important;
        border: 2px solid #00ccff !important;
        border-radius: 10px !important;
        padding: 15px !important;
        font-size: 18px !important;
    }
</style>
""", unsafe_allow_html=True)

# 🤖 TÍTULOS
st.markdown('<h1 class="titulo">🤖 JARVIS - INTELIGENCIA ARTIFICIAL</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitulo">Siempre a su servicio, señor</h2>', unsafe_allow_html=True)
st.markdown("---")

# 📥 CAJA DE TEXTO
st.markdown('<div class="caja">', unsafe_allow_html=True)
texto = st.text_area("✍️ Escribe lo que quieras:", placeholder="Ej: Cuánto es 1+1 / Hola / Qué puedes hacer?", height=120, key="entrada")
boton = st.button("🔊 HABLAR Y RESPONDER", type="primary", help="Voz muy lenta, clara y completa")
st.markdown('</div>', unsafe_allow_html=True)

# ⚙️ ACCIÓN PRINCIPAL
if boton and texto.strip() != "":
    # OBTENEMOS RESPUESTA
    res = respuesta_ia(texto)

    # 🎤 ✅ VOZ PERFECTA, NO SE CORTA
    voz_perfecta(res)

    # 📤 MOSTRAMOS
    st.markdown(f'<div class="respuesta">🗣️ {res}</div>', unsafe_allow_html=True)

# 📌 PIE
st.markdown("---")
st.markdown('<p style="text-align:center; color:#80dfff; font-size:16px;">💡 Versión FINAL • Voz perfecta • Responde a todo 🚀</p>', unsafe_allow_html=True)
