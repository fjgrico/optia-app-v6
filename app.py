import streamlit as st
from utils.procesar import superponer_gafas
from utils.recomendaciones import obtener_recomendacion_por_forma
from utils.pdf_generator import generar_pdf
import tempfile
from PIL import Image
import urllib.parse

st.set_page_config(page_title="OPTIA V6", layout="centered")
st.title("🧠 OPTIA V6 – Recomendador Visual con IA")

foto = st.file_uploader("📷 Sube tu foto (JPG o PNG)", type=["jpg", "jpeg", "png"])
modelo = st.selectbox("🕶️ Modelo de gafas", ["modelo1", "modelo2"])
estilo = st.selectbox("🎨 Estilo", ["Clásico", "Deportiva", "Aviador", "Minimalista"])
color = st.selectbox("🎨 Color de montura", ["Negro", "Azul", "Rojo", "Transparente"])
cristal = st.selectbox("🔎 Tipo de cristal", ["Transparente", "Antirreflejo", "Polarizado", "Fotocromático"])

nombre = st.text_input("📝 Tu nombre")
email = st.text_input("📧 Tu email")
rgpd = st.checkbox("✅ Acepto la política de privacidad")

if foto and nombre and email and rgpd:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_img:
        tmp_img.write(foto.read())
        tmp_path = tmp_img.name

    resultado, forma = superponer_gafas(tmp_path, f"gafas/{modelo}.png")
    st.image(resultado, caption=f"Forma de rostro detectada: {forma}", use_column_width=True)

    if forma != "desconocido":
        with st.spinner("🔎 Analizando rostro y generando recomendación..."):
            recomendacion = obtener_recomendacion_por_forma(forma)
        st.success("✅ Recomendación personalizada:")
        st.markdown(f"> {recomendacion}")

        imagen_final = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        resultado.save(imagen_final.name)
        pdf_path = generar_pdf(imagen_final.name, recomendacion, nombre=nombre)

        with open(pdf_path, "rb") as pdf_file:
            st.download_button("📄 Descargar informe PDF", data=pdf_file, file_name="informe_optia.pdf", mime="application/pdf")

        mensaje = f"OPTIA para {nombre}: Tu rostro es {forma}. Recomendación: {recomendacion}"
        mensaje_encoded = urllib.parse.quote(mensaje)
        enlace = f"https://wa.me/?text={mensaje_encoded}"
        st.markdown(f"[📲 Enviar por WhatsApp]({enlace})", unsafe_allow_html=True)
