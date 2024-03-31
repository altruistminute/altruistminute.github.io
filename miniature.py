from PIL import Image, ImageDraw, ImageFont
import os
from random import randint

# Définir les paramètres de la miniature
width, height = 1280, 720
background_color = (0, 0, 0)  # Fond noir
text_color = (0, 255, 0)  # Texte vert
font_size = 60
font_path = "fonts/Hack-Regular.ttf"
title_text = "Découvrez\nMistral_AI"

# Créer une nouvelle image avec le fond noir
image = Image.new("RGB", (width, height), background_color)

# Ajouter le titre à l'image
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font_path, font_size)
lines = title_text.split("\n")
for i, line in enumerate(lines):
    words = line.split()
    y = (height * 0.4) + (i * font_size * 1.2)
    for j, word in enumerate(words):
        word_color = (randint(0, 255), randint(0, 255), randint(0, 255))
        word_width, word_height = draw.textsize(word, font)
        word_x = (width - sum(draw.textsize(w, font)[0] for w in words)) / 2 + sum(draw.textsize(words[k], font)[0] for k in range(j))
        draw.text((word_x, y), word, font=font, fill=word_color)

# Enregistrer la miniature
output_path = "miniature.jpg"
image.save(output_path, "JPEG", quality=90)
print(f"Miniature enregistrée à l'emplacement : {output_path}")
