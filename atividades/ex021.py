import pygame   
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\davic\Downloads\What You Won t Do for Love (Instrumental).wav")
pygame.mixer.music.play()

# Evita que o programa feche antes da música tocar
while pygame.mixer.music.get_busy():
    continue