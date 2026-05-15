import pygame
import random
import sys
import os
# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ant Smasher")

# Images
ANT_IMG = pygame.image.load(os.path.join('Assets For Ant Smasher', 'Ant image.jpeg'))
ANT_IMG = pygame.transform.scale(ANT_IMG, (50, 50))

SPIDER_IMG = pygame.image.load(os.path.join('Assets For Ant Smasher', 'spider.jpeg'))
SPIDER_IMG = pygame.transform.scale(SPIDER_IMG, (50, 50))

# Fonts
FONT = pygame.font.SysFont("Arial", 30)

# Clock
clock = pygame.time.Clock()

# Classes
class Ant:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 50)
        self.y = 0
        self.speed = random.randint(3, 6)
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def move(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self):
        screen.blit(ANT_IMG, (self.x, self.y))


class Spider:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 50)
        self.y = 0
        self.speed = random.randint(2, 5)
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def move(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self):
        screen.blit(SPIDER_IMG, (self.x, self.y))


def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont("Arial", size)
    label = font.render(text, True, color)
    screen.blit(label, (x, y))


def main():
    ants = []
    spiders = []
    score = 0
    game_over = False

    SPAWN_ANT = pygame.USEREVENT + 1
    SPAWN_SPIDER = pygame.USEREVENT + 2
    pygame.time.set_timer(SPAWN_ANT, 1000)
    pygame.time.set_timer(SPAWN_SPIDER, 3000)

    while True:
        screen.fill((200, 255, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_over:
                continue
            if event.type == SPAWN_ANT:
                ants.append(Ant())
            if event.type == SPAWN_SPIDER:
                spiders.append(Spider())
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for ant in ants:
                    if ant.rect.collidepoint(mouse_pos):
                        ants.remove(ant)
                        score += 1
                        break
                else:
                    for spider in spiders:
                        if spider.rect.collidepoint(mouse_pos):
                            game_over = True

        if not game_over:
            for ant in ants[:]:
                ant.move()
                if ant.y > HEIGHT:
                    game_over = True
                ant.draw()

            for spider in spiders[:]:
                spider.move()
                if spider.y > HEIGHT:
                    spiders.remove(spider)
                spider.draw()

            draw_text(f"Score: {score}", 30, (0, 0, 0), 10, 10)
        else:
            draw_text("Game Over", 50, (255, 0, 0), WIDTH // 2 - 120, HEIGHT // 2 - 25)
            draw_text(f"Final Score: {score}", 40, (0, 0, 0), WIDTH // 2 - 100, HEIGHT // 2 + 30)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()