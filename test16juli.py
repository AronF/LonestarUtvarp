import pygame

pygame.init()
sound = pygame.mixer.Sound("audio.wav")
sound.play()
try:
    while True: pass
except KeyboardInterrupt:
    print("playback stopped by user")
