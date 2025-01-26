import pygame
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
)

pygame.init()



time = 0

HEIGHT = 720
WIDTH = 1280

game_over = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blahaj Nom Noms")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (173, 216, 230)

shark_img = pygame.image.load("shark.png")
shark_width, shark_height = 160, 100
shark_img = pygame.transform.scale(shark_img, (shark_width, shark_height))
shark_x, shark_y = WIDTH // 10, HEIGHT // 2
shark_velo = 10 

fish_img = pygame.image.load("fish.png")
fish_width, fish_height = 120, 90
fish_img = pygame.transform.scale(fish_img, (fish_width, fish_height))
fish_velo = 10
fish_amt = 10
fish_list = [
    pygame.Rect(
        random.randint(WIDTH, WIDTH + 500),
        random.randint(0, HEIGHT - fish_height),
        fish_width,
        fish_height,
    )
    for i in range(fish_amt)
]

score = 0
font = pygame.font.Font(None, 40)

clock = pygame.time.Clock()

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keyP = pygame.key.get_pressed()
    if keyP[K_UP] and shark_y > 0:
        shark_y -= shark_velo
    if keyP[K_DOWN] and shark_y < HEIGHT - 100:
        shark_y += shark_velo
    
    for fish in fish_list[:]:
        fish.x -= fish_velo
        if fish.x + fish_width < 0:
            fish.x = random.randint(WIDTH, WIDTH + 500)
            fish.y = random.randint(0, HEIGHT - fish_height)

    shark_rect = pygame.Rect(shark_x, shark_y, shark_width, shark_height)
    for fish in fish_list[:]:
        if shark_rect.colliderect(fish):
            fish.x = random.randint(WIDTH, WIDTH + 500)
            fish.y = random.randint(0, HEIGHT - fish_height)
            score += random.randint(1, 25)


    screen.fill(BLUE)
    screen.blit(shark_img, (shark_x, shark_y, shark_width, shark_height))
    for fish in fish_list:
        screen.blit(fish_img, (fish.x, fish.y))

    score_display = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_display, (1100, 10))

    time += 1
    if time == 60*10:
        print("GAMEOVER")
        shark_velo = 0
        fish_velo = 0
        game_over = True
    
    if game_over:
        gameOver = font.render('GAME OVER', True, BLACK)
        screen.blit(gameOver, (WIDTH//2,HEIGHT//2))

    pygame.display.update()

pygame.QUIT