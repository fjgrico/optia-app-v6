from deepface import DeepFace
from PIL import Image
import numpy as np

def detectar_forma_del_rostro(image_path):
    try:
        analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=True)
        # Simulamos detección con tipo facial basado en emoción dominante (para demo)
        emotion = analysis[0]['dominant_emotion'].lower()
        if emotion in ["happy", "surprise"]:
            return "ovalado"
        elif emotion in ["angry", "fear"]:
            return "cuadrado"
        elif emotion in ["sad"]:
            return "redondo"
        else:
            return "corazon"
    except Exception as e:
        return "desconocido"

def superponer_gafas(image_path, gafas_path):
    base_img = Image.open(image_path).convert("RGBA").resize((600, 600))
    gafas = Image.open(gafas_path).convert("RGBA").resize((300, 100))
    base_img.paste(gafas, (150, 200), gafas)
    forma = detectar_forma_del_rostro(image_path)
    return base_img, forma
