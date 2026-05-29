import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Datos para entrenar la IA
textos = [
    "muy bueno", "excelente", "me encanta", "genial", "buen servicio", "increíble",
    "malo", "pésimo", "terrible", "no me gustó", "horrible", "muy mal"
]
etiquetas = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]

# Creamos y entrenamos el modelo DIRECTAMENTE aquí
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(textos)
modelo = LogisticRegression()
modelo.fit(X, etiquetas)

# Interfaz de la aplicación
st.set_page_config(page_title="Mi IA", page_icon="🧠")
st.title("🧠 INTELIGENCIA ARTIFICIAL - CREADA POR TI ✨")
st.subheader("¿Es un comentario POSITIVO o NEGATIVO?")
st.markdown("---")

texto_usuario = st.text_area("✍️ Escribe aquí lo que quieras analizar:")

if st.button("🔮 ANALIZAR"):
    if not texto_usuario.strip():
        st.warning("⚠️ Escribe algo primero...")
    else:
        resultado = modelo.predict(vectorizador.transform([texto_usuario]))[0]
        if resultado == 1:
            st.success("✅ COMENTARIO POSITIVO 😊")
            st.balloons()
        else:
            st.error("❌ COMENTARIO NEGATIVO 😠")

st.markdown("---")
st.info("💡 Es tuya → la vendes, regalas o usas 🚀")
