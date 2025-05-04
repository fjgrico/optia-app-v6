from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image

def generar_pdf(image_path, texto, nombre="Cliente"):
    pdf_file = image_path.replace(".png", ".pdf")
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, f"Informe OPTIA para {nombre}")
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 80, texto)
    c.drawImage(image_path, 100, height - 400, width=200, preserveAspectRatio=True)
    c.save()
    return pdf_file
