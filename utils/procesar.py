# Generar nuevo archivo utils/procesar.py con superposición de gafas usando landmarks faciales (ojos)
from pathlib import Path

procesar_avanzado_code = '''\
import requests
from PIL import Image
import numpy as np
import math

# Claves de Azure Face API
API_KEY = "F4LhOIDGCqCuSrqQxhrVAwsPTjS80ON96rLJYm6YvVU6TporSlCvJQQJ99BEAC5T7U2XJ3w3AAAKACOGiXj1"
ENDPOINT = "https://optia-face.cognitiveservices.azure.com/"
FACE_URL = ENDPOINT + "face/v1.0/detect"

def detectar_landmarks(image_path):
    with open(image_path, "rb") as image_data:
        headers = {
            "Ocp-Apim-Subscription-Key": API_KEY,
            "Content-Type": "application/octet-stream"
        }
        params = {
            "returnFaceLandmarks": "true",
            "returnFaceAttributes": "headPose"
        }
        response = requests.post(FACE_URL, headers=headers, params=params, data=image_data)
    if response.status_code != 200 or not response.json():
        return None
    return response.json()[0]["faceLandmarks"]

def calcular_angulo(p1, p2):
    dx, dy = p2[0]-p1[0], p2[1]-p1[1]
    return math.degrees(math.atan2(dy, dx))

def superponer_gafas(image_path, gafas_path):
    landmarks = detectar_landmarks(image_path)
    if not landmarks:
        return Image.open(image_path), "desconocido"

    eye_left = landmarks["pupilLeft"]
    eye_right = landmarks["pupilRight"]
    centro_ojos = (
        (eye_left["x"] + eye_right["x"]) / 2,
        (eye_left["y"] + eye_right["y"]) / 2
    )
    distancia_ojos = math.dist((eye_left["x"], eye_left["y"]), (eye_right["x"], eye_right["y"]))
    angulo = calcular_angulo((eye_left["x"], eye_left["y"]), (eye_right["x"], eye_right["y"]))

    # Abrir imágenes
    fondo = Image.open(image_path).convert("RGBA")
    gafas = Image.open(gafas_path).convert("RGBA")

    # Redimensionar gafas proporcionalmente a la distancia entre ojos
    escala = distancia_ojos / gafas.width * 2.0
    nuevo_tamano = (int(gafas.width * escala), int(gafas.height * escala))
    gafas_escaladas = gafas.resize(nuevo_tamano)

    # Rotar gafas
    gafas_rotadas = gafas_escaladas.rotate(-angulo, expand=True)

    # Calcular posición para pegar gafas centradas
    x = int(centro_ojos[0] - gafas_rotadas.width / 2)
    y = int(centro_ojos[1] - gafas_rotadas.height / 2)

    # Pegar gafas sobre fondo
    fondo.paste(gafas_rotadas, (x, y), gafas_rotadas)

    return fondo, "detectada"

'''

# Guardar el archivo
procesar_path = Path("/mnt/data/optia_app_v6/utils/procesar.py")
procesar_path.write_text(procesar_avanzado_code)

procesar_path.name
