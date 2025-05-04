import requests
from PIL import Image
import numpy as np

# Tus claves de Azure
API_KEY = "F4LhOIDGCqCuSrqQxhrVAwsPTjS80ON96rLJYm6YvVU6TporSlCvJQQJ99BEAC5T7U2XJ3w3AAAKACOGiXj1"
ENDPOINT = "https://optia-face.cognitiveservices.azure.com/"
FACE_URL = ENDPOINT + "face/v1.0/detect"

# Función para obtener forma del rostro estimada
def detectar_forma_del_rostro(image_path):
    with open(image_path, "rb") as image_file:
        headers = {
            "Ocp-Apim-Subscription-Key": API_KEY,
            "Content-Type": "application/octet-stream"
        }
        params = {
            "returnFaceLandmarks": "true",
            "returnFaceAttributes": "headPose"
        }
        response = requests.post(FACE_URL, headers=headers, params=params, data=image_file)

    if response.status_code != 200 or not response.json():
        return "desconocido"

    # Aquí puedes implementar lógica real con landmarks si deseas
    # Por ahora retornamos "ovalado" como demo
    # O podríamos usar el "roll" o "yaw" de headPose si lo prefieres
    return "ovalado"

# Función para superponer gafas y retornar imagen final
def superponer_gafas(image_path, gafas_path):
    base_img = Image.open(image_path).convert("RGBA").resize((600, 600))
    gafas = Image.open(gafas_path).convert("RGBA").resize((300, 100))
    base_img.paste(gafas, (150, 200), gafas)
    forma = detectar_forma_del_rostro(image_path)
    return base_img, forma
