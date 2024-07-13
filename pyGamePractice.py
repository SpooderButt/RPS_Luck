from functions import *

pygame.init()
fps = 30
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("RPS Test")
last_fps_display_time = pygame.time.get_ticks()
background_color = (200, 200, 200)
size = (600, 400)

image_list = ['images/Lucky_RPS_sprites_default.png', 'images/Lucky_RPS_sprites_ready.png',
              'images/Lucky_RPS_sprites_rock.png', 'images/Lucky_RPS_sprites_paper.png',
              'images/Lucky_RPS_sprites_scissors.png', 'images/Lucky_RPS_sprites_win.png',
              'images/Lucky_RPS_sprites_lose.png']
happy = pygame.image.load(image_list[4])
happy = pygame.transform.scale(happy, size)

position = (0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(background_color)
    screen.blit(happy, position)
    pygame.display.flip()
    clock.tick(fps)
    current_time = pygame.time.get_ticks()
    if current_time - last_fps_display_time >= 500:
        FPS_Counter()
        last_fps_display_time = current_time
