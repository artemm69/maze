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

def settings_menu(screen):
    global current_maze_color, current_cube_color, maze_width, maze_height
    settings_active = True

    # Кнопки для выбора цветов лабиринта и кубика
    maze_color_buttons = [
        {"color": color, "rect": pygame.Rect(700, 100 + i * 60, 50, 50)}
        for i, color in enumerate(color_options)
    ]
    cube_color_buttons = [
        {"color": color, "rect": pygame.Rect(200, 100 + i * 60, 50, 50)}
        for i, color in enumerate(color_options)
    ]
    while settings_active:
        screen.fill((0, 0, 0))
        # загружаем картинку
        bg = pygame.image.load("1.jpg")
        # заполняем фон картинкой
        screen.blit(bg, (0, 0))

        # Рисуем кнопки для выбора цвета лабиринта и кубика
        for button in maze_color_buttons:
            pygame.draw.rect(screen, button["color"], button["rect"])
        for button in cube_color_buttons:
            pygame.draw.rect(screen, button["color"], button["rect"])

        # Добавляем подписи
        label1 = menu_font.render("Выбор цвета лабиринта", 1, (255,255,255))
        screen.blit(label1, (700 - label1.get_width() // 2, 50))
        label2 = menu_font.render("Выбор цвета кубика", 1, (255,255,255))
        screen.blit(label2, (200 - label2.get_width() // 2, 50))

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                settings_active = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Проверяем нажатие на кнопки цвета лабиринта и кубика
                for button in maze_color_buttons:
                    if button["rect"].collidepoint(mouse_pos):
                        current_maze_color = button["color"]
                        break

                # Проверяем нажатие на кнопки цвета лабиринта и кубика
                for button in cube_color_buttons:
                    if button["rect"].collidepoint(mouse_pos):
                        current_cube_color = button["color"]
                        break
        clock.tick(60)


