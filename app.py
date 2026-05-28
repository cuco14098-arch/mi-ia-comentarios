import streamlit as st
import joblib

# Cargar modelo
modelo = joblib.load("modelo_ia.pkl")
vec = joblib.load("vectorizador_ia.pkl")

st.set_page_config(page_title="Mi IA", page_icon="🧠")
st.title("🧠 INTELIGENCIA ARTIFICIAL - CREADA POR TI ✨")
st.subheader("¿Es un comentario POSITIVO o NEGATIVO?")
st.markdown("---")

texto = st.text_area("✍️ Escribe aquí lo que quieras analizar:")

if st.button("🔮 ANALIZAR"):
    if not texto.strip():
        st.warning("⚠️ Escribe algo primero...")
    else:
        res = modelo.predict(vec.transform([texto]))[0]
        if res == 1:
            st.success("✅ COMENTARIO POSITIVO 😊")
            st.balloons()
        else:
            st.error("❌ COMENTARIO NEGATIVO 😠")

st.markdown("---")
st.info("💡 Es tuya → la vendes, regalas o usas 🚀")
