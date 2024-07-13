import pygame, sys

clock = pygame.time.Clock()
def FPS_Counter():
    received_fps = clock.get_fps()
    rounded_fps = round(received_fps, 2)
    print(f"FPS: {rounded_fps}")