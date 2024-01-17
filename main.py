
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


def draw_button(screen, text, x, y, width, height, color):
    """ Рисует кнопку и текст на ней """

    pygame.draw.rect(screen, color, [x, y, width, height])
    text_surf = menu_font.render(text, True, (255, 255, 255))
    screen.blit(text_surf, [x + (width - text_surf.get_width()) // 2,
                            y + (height - text_surf.get_height()) // 2])

def is_button_pressed(x, y, width, height, mouse_pos):
    """ Проверяет, нажата ли кнопка """

    return x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height

# Функция для отображения главного меню
# оно появляется при запуске
def main_menu(screen):
    menu = True

    while menu:
        screen.fill((0, 0, 0))
        sizex, sizey = screen.get_size()
        bg = pygame.image.load("1.jpg")

        screen.blit(bg, (0, 0))

        button_width, button_height = 300, 70
        button_spacing = 20

        start_button_y = sizey // 2 - (2 * (button_height + button_spacing))
        size_button_y = start_button_y + button_height + button_spacing

        settings_button_y = size_button_y + button_height + button_spacing
        quit_button_y = settings_button_y + button_height + button_spacing

        button_x = sizex // 2 - button_width // 2

        # рисуем кнопку (Начать игру)
        draw_button(screen, "Начать игру", button_x, start_button_y, button_width, button_height,
                    (100, 200, 100))
        # рисуем кнопку (Выбрать размер)
        draw_button(screen, "Выбрать размер", button_x, size_button_y, button_width, button_height,
                    (100, 200, 100))
        # рисуем кнопку (Настройки)
        draw_button(screen, "Настройки", button_x, settings_button_y, button_width, button_height,
                    (100, 100, 200))
        # рисуем кнопку (Выход)
        draw_button(screen, "Выход", button_x, quit_button_y, button_width, button_height,
                    (200, 100, 100))

        pygame.display.update()
        for event in pygame.event.get():
            # прописываем условие выхода
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if is_button_pressed(button_x, start_button_y, button_width, button_height, mouse_pos):
                    return "start"

                elif is_button_pressed(button_x, size_button_y, button_width, button_height, mouse_pos):
                    return "size"

                elif is_button_pressed(button_x, settings_button_y, button_width, button_height, mouse_pos):
                    result = settings_menu(screen)
                    if result == "back":
                        continue

                elif is_button_pressed(button_x, quit_button_y, button_width, button_height, mouse_pos):
                    return "quit"
# изменение разиеров лабиринта
def choose_maze_size():
    print("Введите новую ширину лабиринта:")
    new_screen_sizex = int(input())

    # проверяем корректность разиера
    while new_screen_sizex < 300:
        print("Ширина должна быть не менее 300 пикселей. Попробуйте еще раз:")
        new_screen_sizex = int(input())

    # задается высота
    print("Введите новую высоту лабиринта:")
    new_screen_sizey = int(input())

    # проверяем корректность разиера
    while new_screen_sizey < 300:
        print("Высота должна быть не менее 300 пикселей. Попробуйте еще раз:")
        new_screen_sizey = int(input())

    return new_screen_sizex, new_screen_sizey


def get_time(hours, minutes, seconds):

    if len(str(hours)) > 1:
        a = str(hours)

    else:
        a = "0" + str(hours)


    if len(str(minutes)) > 1:
        b = str(minutes)

    else:
        b = "0" + str(minutes)


    if len(str(seconds)) > 1:
        c = str(seconds)

    else:
        c = "0" + str(seconds)


    return a + ":" + b + ":" + c

def draw_time(start_time, pause_time):
    hours, minutes, seconds = 0, 0, 0
    current_time = time.time() - pause_time - start_time
    if current_time > 3600:
        while True:
            if current_time - 3600 > 0:
                hours += 1
                current_time -= 3600
            else:
                while True:
                    if current_time - 60 > 0:
                        minutes += 1
                        current_time -= 60
                    else:
                        seconds += int(current_time)
                        break
                break

    else:
        while True:
            if current_time - 60 > 0:
                minutes += 1
                current_time -= 60
            else:
                seconds += int(current_time)
                break
    return [font1.render(get_time(hours, minutes, seconds), True, (0, 0, 0), (255, 255, 255)),
            get_time(hours, minutes, seconds)]

class cell:
    def __init__(self, up, down, left, right):
        self.visited = False
        self.walls = [up, down, left, right]

#генерируем лабиринт
class labyrinth:
    def __init__(self, id, sizex, sizey):
        self.id = id
        self.walls = []
        self.maze_walls = []
        self.cells = []

        # Вычисляем количество клеток по горизонтали и вертикали
        num_cells_x = sizex // 33
        num_cells_y = sizey // 33

        # задаем x и у
        x = 0
        t = 0

        for f in range(num_cells_y):
            for s in range(num_cells_x):
                if not (f in (0, 1, 2) and s > num_cells_x):
                    self.cells.append(cell((x + 8, t, 28, 8), (x + 8, t + 33, 28, 8), (x, t + 8, 8, 28),
                                           (x + 33, t + 8, 8, 28)))
                x += 33
            x = 0
            t += 33

        # заполняем списки
        for v in self.cells[0].walls:
            self.maze_walls.append(v)
            self.walls.append(v)
        self.cells[0].visited = True

        while len(self.walls) > 0:
            wall = random.choice(self.walls)
            divided_cells = []

            for u in self.cells:
                if wall in u.walls:
                    divided_cells.append(u)

            if len(divided_cells) > 1 and (not ((divided_cells[0].visited and divided_cells[1].visited) or
                                                ((not divided_cells[0].visited)
                                                 and (not divided_cells[1].visited)))):
                for k in divided_cells:
                    k.walls.remove(wall)

                    if k.visited == False:
                        k.visited = True

                    for q in k.walls:
                        if not q in self.walls:
                            self.walls.append(q)

                        if not q in self.maze_walls:
                            self.maze_walls.append(q)

                    if wall in self.maze_walls:
                        self.maze_walls.remove(wall)

            self.walls.remove(wall)

        for j in range(0, 720, 33):
            for i in range(0, 951, 33):
                self.maze_walls.append((i, j, 8, 8))

    def remove_walls(self, percent):
        num_walls = int(len(self.walls) * percent / 100)
        random.shuffle(self.walls)
        self.walls = self.walls[:num_walls]
    def draw(self, goal):
        screen.fill((0, 0, 0))
        for k in self.maze_walls:
            pygame.draw.rect(screen, current_maze_color, pygame.Rect(k[0], k[1], k[2], k[3]))
        pygame.draw.rect(screen, (0, 255, 0), goal)


