import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
screen = pygame.display.set_mode([400, 400])
pygame.display.set_caption("Smiley Face")

# Цвета
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


# Рисуем смайлик
def drawsmiley():
    # Очищаем экран
    screen.fill(BLACK)

    # Рисуем круг лица
    pygame.draw.circle(screen, YELLOW, (200, 200), 100)

    # Глаза
    pygame.draw.circle(screen, BLACK, (150, 170), 10)
    pygame.draw.circle(screen, BLACK, (250, 170), 10)

    # Рот
    pygame.draw.arc(screen, BLACK, (150, 150, 100, 100), 0.5, 2.64, 2)


# Главный цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Рисуем смайлик
    drawsmiley()

    # Обновляем экран
    pygame.display.update()