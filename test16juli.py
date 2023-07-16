import pygame

pygame.init()
sound = pygame.mixer.Sound("audio.wav")
sound.play()
try:
    while pygame.mixer.get_busy(): pass
except KeyboardInterrupt:
    print("playback stopped by user")
