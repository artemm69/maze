# импортируем библиотеку pygame
import pygame
# импортируем библиотеку random
import random
# импортируем библиотеку time
import time

pygame.init()
clock = pygame.time.Clock()

# Оранжевый цвет по умолчанию для лабиринта
current_maze_color = (255, 165, 0)
# Фиолетовый цвет по умолчанию для кубика
current_cube_color = (128, 0, 128)

# Цвета на выбор
color_options = [
    (255, 0, 0),
    # Красный
    (0, 255, 0),
    # Зелёный
    (0, 0, 255),
    # Синий
    (255, 255, 0),
    # Жёлтый
    (255, 165, 0),
    # Оранжевый
    (128, 0, 128)
    # Фиолетовый
]
maze_width = 930  # Ширина лабиринта
maze_height = 800  # Высота лабиринта
# Определение шрифтов
font1 = pygame.font.SysFont("comicsansms", 49, True)
font2 = pygame.font.SysFont("comicsansms", 150, True)
font3 = pygame.font.SysFont("comicsansms", 28, True)
menu_font = pygame.font.SysFont("comicsansms", 36, True)
