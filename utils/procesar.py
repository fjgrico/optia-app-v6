import cv2
import numpy as np
import mediapipe as mp
from PIL import Image

def detectar_forma_del_rostro(image_path):
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

    image = cv2.imread(image_path)
    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if not results.multi_face_landmarks:
        return "desconocido"

    # Aquí puedes añadir tu lógica para analizar proporciones faciales
    return "ovalado"  # o cuadrado, redondo, etc.

def superponer_gafas(image_path, gafas_path):
    base_img = Image.open(image_path).convert("RGBA").resize((600, 600))
    gafas = Image.open(gafas_path).convert("RGBA").resize((300, 100))
    base_img.paste(gafas, (150, 200), gafas)
    forma = detectar_forma_del_rostro(image_path)
    return base_img, forma
