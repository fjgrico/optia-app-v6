def obtener_recomendacion_por_forma(forma):
    recomendaciones = {
        "ovalado": "Tu rostro ovalado combina bien con casi cualquier montura. Te recomendamos estilo aviador o rectangular.",
        "cuadrado": "Para suavizar las líneas de tu rostro cuadrado, prueba gafas redondeadas o tipo cat-eye.",
        "redondo": "Las monturas angulares y cuadradas contrastan bien con rostros redondos.",
        "corazon": "Te favorecerán gafas que equilibren tu frente más ancha, como las aviador o sin montura.",
        "desconocido": "No pudimos detectar claramente la forma de tu rostro. Prueba con otra imagen frontal."
    }
    return recomendaciones.get(forma.lower(), "No tenemos recomendación para esta forma aún.")
