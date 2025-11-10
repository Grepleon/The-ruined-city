import random
import time
from tkinter import *
import random as r
import time as t
from tkinter import messagebox
from tkinter import ttk
import Color_Change as C_C
import math as m
import pygame
import threading
import os

# Mus_Destroyted_City - файл с музыкой для самой игры
# mus_menu - тоже музыка в меню

TIME_START = t.time()

# Инициализация pygame для музыки
pygame.mixer.init()


class MusicPlayer:
    def __init__(self):
        self.is_playing = False
        self.current_track = None
        self.player_thread = None

    def play_music_loop(self, music_file):
        """Бесконечно воспроизводит музыку, перезапуская когда она заканчивается"""
        try:
            self.is_playing = True
            self.current_track = music_file

            while self.is_playing:
                pygame.mixer.music.load(music_file)
                pygame.mixer.music.play()
                print(f"Играет музыка: {os.path.basename(music_file)}")

                # Ждем пока музыка не закончится
                while self.is_playing and pygame.mixer.music.get_busy():
                    t.sleep(0.1)

                if self.is_playing:
                    print("Музыка закончилась, перезапуск...")

        except Exception as e:
            print(f"Ошибка воспроизведения музыки: {e}")

    def start_music(self, music_file):
        """Запускает музыку в отдельном потоке"""
        self.stop_music()  # Останавливаем предыдущую музыку

        self.player_thread = threading.Thread(
            target=self.play_music_loop,
            args=(music_file,)
        )
        self.player_thread.daemon = True
        self.player_thread.start()

    def stop_music(self):
        """Останавливает воспроизведение музыки"""
        self.is_playing = False
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        print("Музыка остановлена")

def play_menu_music():
    """Запускает музыку для меню"""
    try:
        # Замените на путь к вашей музыке для меню
        menu_music = "mus_menu.mp3"  # или другой формат
        if os.path.exists(menu_music):
            music_player.start_music(menu_music)
        else:
            print(f"Файл музыки меню не найден: {menu_music}")
    except Exception as e:
        print(f"Ошибка запуска музыки меню: {e}")


def play_game_music():
    """Запускает музыку для игры"""
    try:
        # Замените на путь к вашей музыке для игры
        game_music = "Mus_Destroyted_City.mp3"  # или другой формат
        if os.path.exists(game_music):
            music_player.start_music(game_music)
        else:
            print(f"Файл музыки игры не найден: {game_music}")
    except Exception as e:
        print(f"Ошибка запуска музыки игры: {e}")



# Создаем глобальный объект для управления музыкой
music_player = MusicPlayer()

Paus = 1
B = 0

# Словарь для отслеживания состояния клавиш
keys_pressed = {
    'w': False, 'ц': False,  # Вверх
    's': False, 'ы': False,  # Вниз
    'a': False, 'ф': False,  # Влево
    'd': False, 'в': False,   # Вправо
    ' ': False, # зажечь спичку
    'e': False, # включить фонарик
    'f': False, # ускоренный режим
}

w = 1100
h = 600

root = Tk()
root.title('Разрушенный город')
canvas = Canvas(root, width=w, height=h, bg='black')
canvas.grid()
canvas.pack(anchor=CENTER, expand=1)


def on_key_press(event):
    """Обработчик нажатия клавиш"""
    key = event.char.lower()
    if key in keys_pressed:
        keys_pressed[key] = True
    elif event.keysym == 'space':
        keys_pressed[' '] = True
    elif event.keysym == 'Shift_L':
        keys_pressed['e'] = True


def on_key_release(event):
    """Обработчик отпускания клавиш"""
    key = event.char.lower()
    if key in keys_pressed:
        keys_pressed[key] = False
    elif event.keysym == 'Shift_L':
        keys_pressed['e'] = False


root.bind('<KeyPress>', on_key_press)
root.bind('<KeyRelease>', on_key_release)

Mx, My = 0, 0


def get_mouse_position(event):
    global Mx, My
    Mx, My = event.x, event.y


root.bind('<Motion>', get_mouse_position)


def Line(x, y, Go=0, Gradus=0, tags='- 0 -'):
    SinX = m.sin(Gradus * 0.0174533)
    SinY = m.cos(Gradus * 0.0174533)

    sx = SinX * Go
    sy = SinY * Go

    canvas.create_line(x, y, sx + x, sy + y, fill='black', tags=tags)


def RLineX(x, y, Go=0, Gradus=0, tags='- 0 -'):
    SinX = m.sin(Gradus * 0.0174533)
    SinY = m.cos(Gradus * 0.0174533)
    sx = SinX * Go
    sy = SinY * Go
    return sx + x


def RLineY(x, y, Go=0, Gradus=0, tags='- 0 -'):
    SinX = m.sin(Gradus * 0.0174533)
    SinY = m.cos(Gradus * 0.0174533)
    sx = SinX * Go
    sy = SinY * Go
    return sy + y


Game = 0
Levels = [0] * 14


class button:
    def __init__(self, x1, y1, x2, y2, cc, ccf, cct, textt, textf, color='black', name='Начать игру'):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        self._color = color
        self._cct = cct
        self._cc = cc
        self._ccf = ccf
        self._cct = cct

        self._textt = textt
        self._textf = textf

        self._name = name

        self._text = textt

        self._On = False

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.color = color
        self.colort = cct
        self.const_color = cc
        self.const_color_false = ccf
        self.const_color_true = cct

        self.textt = textt
        self.textf = textf

        self.name = name

        self.text = textt

        self.On = False

        self.objectr = self.CreateR()
        self.objectt = self.CreateT()

    def Restart(self):
        self.x1 = self._x1
        self.x2 = self._x2
        self.y1 = self._y1
        self.y2 = self._y2

        self.color = self._color
        self.colort = self._cct
        self.const_color = self._cc
        self.const_color_false = self._ccf
        self.const_color_true = self._cct

        self.textt = self._textt
        self.textf = self._textf

        self.name = self._name

        self.text = self._textt

        self.On = False

    def CreateR(self):
        return canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color, outline=self.const_color,
                                       tags='-')

    def CreateT(self):
        return canvas.create_text((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2, fill=self.colort, tags='-',
                                  text=self.text)

    def If_In(self, Mx, My):
        return max(self.x1, self.x2) > Mx >= min(self.x1, self.x2) and max(self.y1, self.y2) > My >= min(self.y1,
                                                                                                         self.y2)

    def Click(self, Mx, My, B):
        On = B == 1 and self.If_In(Mx, My)
        self.On = On != self.On

    def Hide(self):
        canvas.itemconfig(self.objectr, state='hidden')
        canvas.itemconfig(self.objectt, state='hidden')

    def Show(self):
        canvas.itemconfig(self.objectr, state='normal')
        canvas.itemconfig(self.objectt, state='normal')

    def itemconfig(self, i,state='normal'):
        if state == 'normal':
            self.Show()
        else:
            self.Hide()

    def Open(self, x, y):
        if not self.If_In(x, y):
            if self.On:
                self.color = self.const_color_false
                self.colort = self.const_color_true
                canvas.itemconfig(self.objectr, fill=self.const_color_false)
                canvas.itemconfig(self.objectt, fill=self.const_color_true, text=self.textf)
            else:
                self.color = self.const_color_false
                self.colort = self.const_color_true
                canvas.itemconfig(self.objectr, fill=self.const_color_false)
                canvas.itemconfig(self.objectt, fill=self.const_color_true, text=self.textt)
        else:
            if self.On:
                self.color = self.const_color_true
                self.colort = self.const_color_false
                canvas.itemconfig(self.objectr, fill=self.const_color_true)
                canvas.itemconfig(self.objectt, fill=self.const_color_false, text=self.textf)
            else:
                self.color = self.const_color_true
                self.colort = self.const_color_false
                canvas.itemconfig(self.objectr, fill=self.const_color_true)
                canvas.itemconfig(self.objectt, fill=self.const_color_false, text=self.textt)

class Enemy:
    def __init__(self, T, x, y, hp=15, t ='0'):
        self.x = x
        self.y = y
        self.T = T

        self.t = t

        self.hp = hp

        self.Hod = True

    def Move_Everywhere(self, Nx, Ny):
        global X, Y
        x = self.x
        y = self.y
        # Вычисляем разности координат с учётом заторенного мира
        dx = (Nx - x + X) % X
        dy = (Ny - y + Y) % Y

        # Выбираем направление движения (кратчайший путь)
        if dx > X / 2:
            dx = dx - X

        if dy > Y / 2:
            dy = dy - Y

        # Двигаемся в нужном направлении
        if dx > 0:
            self.x = (self.x + 1) % X
        elif dx < 0:
            self.x = (self.x - 1) % X

        if dy > 0:
            self.y = (self.y + 1) % Y
        elif dy < 0:
            self.y = (self.y - 1) % Y

    def Move_To_Player_No_Water(self, Nx, Ny):
        global X, Y, Type
        T = Type

        # Проверяем, не стоит ли ИИ уже рядом с игроком
        if abs(self.x - Nx) <= 1 and abs(self.y - Ny) <= 1:
            return

        # Получаем текущую позицию
        current_x, current_y = self.x, self.y

        # Проверяем доступные направления движения (без воды)
        possible_moves = []

        # Проверяем все 4 направления
        directions = [
            (1, 0),  # вправо
            (-1, 0),  # влево
            (0, 1),  # вниз
            (0, -1)  # вверх
        ]

        for dx, dy in directions:
            new_x = (current_x + dx) % X
            new_y = (current_y + dy) % Y

            # Проверяем, что клетка не вода
            tile_type = T[new_x * Y + new_y]
            if tile_type != "Вода":
                # Вычисляем расстояние до игрока от новой позиции
                dist_x = min(abs(new_x - Nx), X - abs(new_x - Nx))
                dist_y = min(abs(new_y - Ny), Y - abs(new_y - Ny))
                distance = dist_x + dist_y

                possible_moves.append((distance, new_x, new_y))

        # Если есть доступные ходы, выбираем тот, что приближает к игроку
        if possible_moves:
            # Сортируем по расстоянию (чем меньше расстояние, тем лучше)
            possible_moves.sort(key=lambda x: x[0])

            # Берём лучший ход (с наименьшим расстоянием)
            best_distance, best_x, best_y = possible_moves[0]

            # Если лучший ход действительно приближает к игроку, двигаемся
            current_dist_x = min(abs(current_x - Nx), X - abs(current_x - Nx))
            current_dist_y = min(abs(current_y - Ny), Y - abs(current_y - Ny))
            current_distance = current_dist_x + current_dist_y

            if best_distance < current_distance:
                self.x, self.y = best_x, best_y

    def Move_To_Player_To_Water(self, Nx, Ny):
        global X, Y, Type
        T = Type

        # Проверяем, не стоит ли ИИ уже рядом с игроком
        if abs(self.x - Nx) <= 1 and abs(self.y - Ny) <= 1:
            return

        # Получаем текущую позицию
        current_x, current_y = self.x, self.y

        # Проверяем доступные направления движения (без воды)
        possible_moves = []

        # Проверяем все 4 направления
        directions = [
            (1, 0),  # вправо
            (-1, 0),  # влево
            (0, 1),  # вниз
            (0, -1)  # вверх
        ]

        for dx, dy in directions:
            new_x = (current_x + dx) % X
            new_y = (current_y + dy) % Y

            # Проверяем, что клетка не вода
            tile_type = T[new_x * Y + new_y]
            if tile_type == "Вода":
                # Вычисляем расстояние до игрока от новой позиции
                dist_x = min(abs(new_x - Nx), X - abs(new_x - Nx))
                dist_y = min(abs(new_y - Ny), Y - abs(new_y - Ny))
                distance = dist_x + dist_y

                possible_moves.append((distance, new_x, new_y))

        # Если есть доступные ходы, выбираем тот, что приближает к игроку
        if possible_moves:
            # Сортируем по расстоянию (чем меньше расстояние, тем лучше)
            possible_moves.sort(key=lambda x: x[0])

            # Берём лучший ход (с наименьшим расстоянием)
            best_distance, best_x, best_y = possible_moves[0]

            # Если лучший ход действительно приближает к игроку, двигаемся
            current_dist_x = min(abs(current_x - Nx), X - abs(current_x - Nx))
            current_dist_y = min(abs(current_y - Ny), Y - abs(current_y - Ny))
            current_distance = current_dist_x + current_dist_y

            if best_distance < current_distance:
                self.x, self.y = best_x, best_y

    def Move_BOSS(self, Nx, Ny):
        global X, Y
        x = self.x
        y = self.y
        # Вычисляем разности координат с учётом заторенного мира
        dx = (Nx - x + X) % X
        dy = (Ny - y + Y) % Y

        # Выбираем направление движения (кратчайший путь)
        if dx > X / 2:
            dx = dx - X

        if dy > Y / 2:
            dy = dy - Y

        # Двигаемся в нужном направлении
        if (dx > 0 and self.t in ['2', '4']) or (dx > 1 and self.t in ['1', '3']):
            self.x = (self.x + 1) % X
        elif (dx < 0 and self.t in ['1', '3']) or (dx < -1 and self.t in ['2', '4']):
            self.x = (self.x - 1) % X

        if (dy > 0 and self.t in ['3', '4']) or (dy > 1 and self.t in ['1', '2']):
            self.y = (self.y + 1) % Y
        elif (dy < 0 and self.t in ['1', '2']) or (dy < -1 and self.t in ['3', '4']):
            self.y = (self.y - 1) % Y


Rectangles = canvas.create_rectangle(0, 200, w, 400, fill='#005522', outline='#00ffaa', state='hidden')


def S1():
    B1 = []
    B1.append(button(10, 10, 310, 160,
                     'green', 'black', '#006611',
                     'Начать игру', 'Покинуть игру',
                     name='Начать игру'))

    return B1


All_Objects = S1()


def S2():
    B2 = []
    for i in range(14):
        B2.append(
            button(15 + i * 77, h // 2 - 35 + m.sin(i) * 50, 85 + i * 77, h // 2 + 35 + m.sin(i) * 50,
                   '#00ffaa', '#005522', '#00ffaa',
                   f'{i + 1}й уровень', 'Покинуть игру',
                   name=f'Уровень-{i + 1}')
        )

    B2.append(button(w - 10, 10, w - 180, 90,
                     'red', 'black', 'red',
                     f'Назад', 'Покинуть игру',
                     name=f'Назад'))

    for i in B2:
        i.Hide()

    return B2


lvls = S2()

X, Y = 30, 30
wx = 20
coof = 20

def S3():
    B3 = []
    for x in range(X):
        for y in range(Y):
            B3.append(
                canvas.create_rectangle(x * wx, y * wx, x * wx + wx, y * wx + wx, fill='#003300', outline='#00ffaa',)
            )

    B3.append(
        canvas.create_rectangle(w - 110, 10 + 105, w - 10, 60 + 105, fill='#003300', outline='#00ffaa')
    )
    B3.append(
        canvas.create_text(w - 60, 35 + 105, fill='#00ffaa', text='Время:\n1/120 сек.')
    )

    B3.append(
        canvas.create_rectangle(w - 220, 10 + 105, w - 120, 60 + 105, fill='#003300', outline='#00ffaa')
    )
    B3.append(
        canvas.create_text(w - 170, 35 + 105, fill='#00ffaa', text='Спичек:\n25/25 штук')
    )

    B3.append(
        canvas.create_rectangle(w - 330, 70 - 45, w - 10, 150 - 45, fill='#330000', outline='#ffaa00')
    )
    B3.append(
        canvas.create_text(w - 170, 50, fill='#ffaa00', text='Жизней: 10/10')
    )

    for hp in range(10):
        B3.append(
            canvas.create_rectangle(w - 330 + hp * (28) + hp * 4, 130 - 45, w - 330 + hp * 28 + 30 + hp * 4, 150 - 45, fill='#330000', outline='#ffaa00')
        )

    B3.append(
        canvas.create_rectangle(w - 330, 10 + 105, w - 230, 60 + 105, fill='#003300', outline='#00ffaa')
    )
    B3.append(
        canvas.create_text(w - 280, 35 + 105, fill='#00ffaa', text='Энергия:\n250/250')
    )
    B3.append(
        button(w - 10, h - 10, w - 330, h - 60,
               'Grey', 'black', 'Grey',
               f'Меню', 'Выйти из меню',
               name=f'Меню')
    )


    for i in B3:
        canvas.itemconfig(i, state='hidden')
    B3[X * Y + 18].Hide()

    return B3

Objects = S3()

Nx, Ny = 15, 15 # Координаты игрока

Type = [] # название объектов
Temp = [] # температура объектов
def Gnrt():
    global Type, Temp, E, Ec, Nx, Ny
    Type = []
    Temp = []

    E, Ec = [], []

    XY = X * Y

    a = [r.randint(-100, 100) for x in range(XY)]

    for _ in range(12):
        i = 0
        for x in range(X):
            for y in range(Y):
                a[i] = (a[(i - 1) % XY] + a[(i - Y) % XY] + a[(i + 1) % XY] + a[(i + Y) % XY]) / 4 * 1.2
                i += 1


    i = -1
    for x in range(X):
        for y in range(Y):
            i += 1
            Temp.append(0)

            if a[i] > -200:
                Type.append('Земля')
            else:
                Type.append('Вода')

    while Type[(Nx * X) + Ny] == 'Вода':
        Nx += 1
        if Nx >= X:
            Nx = 0
            Ny += 1
        if Ny >= Y:
            Ny = 0
            Nx = 0


Gnrt()

E = []
Ec = []

hp = 10
sp = 25
Energy = 250

def IF(ex, ey, x, y):
    return\
    (ex + 1) % (X) == x and (ey + 1) % (Y) == y or \
    (ex - 1) % (X) == x and (ey + 1) % (Y) == y or \
    (ex + 1) % (X) == x and (ey - 1) % (Y) == y or \
    (ex - 1) % (X) == x and (ey - 1) % (Y) == y or \
    (ex + 0) % (X) == x and (ey - 1) % (Y) == y or \
    (ex + 0) % (X) == x and (ey + 1) % (Y) == y or \
    (ex + 1) % (X) == x and (ey - 0) % (Y) == y or \
    (ex - 1) % (X) == x and (ey + 0) % (Y) == y

Sword = canvas.create_line(0, 0, 5, 0, fill='white', state='hidden')

END = []

END.append(
    canvas.create_rectangle(w // 4, h // 4, w * 3 // 4, h * 3 // 4, fill = '#002200', outline = '#00ff00')
)
END.append(
    canvas.create_text(w // 2, h // 2, fill='#00ff00', text='Вы погибли...\nНажмите пробел чтобы выйти в меню')
)


for i in END:
    canvas.itemconfig(i, state='hidden')



Ending = 0

ATTACK = False
ATTACK_P = 0

import math

TO_ATTACK_SWORD = []


def generate_rotating_lines_simple(start_angle):
    """
    Генерирует линии атаки, начиная с смещением от направления к мыши
    """
    lines = []
    length = 30

    # Смещение в градусах (отрицательное = левее, положительное = правее)
    angle_offset = -60  # Начинаем на 60 градусов левее мышки

    # Диапазон вращения меча (в градусах)
    swing_range = 120

    for i in range(10):
        # Начинаем с смещенного угла и проходим диапазон атаки
        angle = math.radians(start_angle + angle_offset + (swing_range * i / 9))

        end_x = length * math.cos(angle)
        end_y = length * math.sin(angle)

        lines.append((0, 0, end_x, end_y))

    return lines

def get_cells_under_sword(start_x, start_y, end_x, end_y):
    """Возвращает список клеток, которых касается линия меча"""
    cells = set()

    # Преобразуем координаты канваса в координаты сетки
    start_grid_x = int(start_x // wx)
    start_grid_y = int(start_y // wx)
    end_grid_x = int(end_x // wx)
    end_grid_y = int(end_y // wx)

    # Используем алгоритм Брезенхема для нахождения всех клеток на пути линии
    dx = abs(end_grid_x - start_grid_x)
    dy = abs(end_grid_y - start_grid_y)

    x = start_grid_x
    y = start_grid_y

    x_inc = 1 if end_grid_x > start_grid_x else -1
    y_inc = 1 if end_grid_y > start_grid_y else -1

    error = dx - dy

    # Добавляем начальную клетку
    cells.add((x % X, y % Y))

    while x != end_grid_x or y != end_grid_y:
        error2 = error * 2

        if error2 > -dy:
            error -= dy
            x += x_inc

        if error2 < dx:
            error += dx
            y += y_inc

        # Добавляем текущую клетку с учетом цикличности
        cells.add((x % X, y % Y))

    # ДОБАВЬТЕ ЭТУ СТРОЧКУ:
    return cells


LIST_ATTACK = []
KILL_KNIGHT = 0
X_BOSS, Y_BOSS = 0, 0
PHASE_BOSS = 0
HP_BOSS = 0
N = 0
MOVE_WATER_LEVEL = [-8, -12, -12.5, -13]

def I(): # сама игра
    """Сама игра, здесь будут происходить основные игровые битвы и обработки...."""
    global Nx, Ny, Game, X, Y, Mx, My, B, Objects, E, Ec, TIME_START_GAME, hp, sp, Energy,\
        Ending, Sword, BB, ATTACK, ATTACK_P, LIST_ATTACK, TO_ATTACK_SWORD, N, KILL_KNIGHT,\
        HP_BOSS, X_BOSS, Y_BOSS, PHASE_BOSS
    N += 1

    BOSS_LEVEL = -6.5 # потом поставить 6.5, 7 - временно для тестов
    BOSS_LEVEL_2 = -12.5

    if TO_ATTACK_SWORD is None:
        TO_ATTACK_SWORD = set()

    if Game == -6 and (KILL_KNIGHT >= 5): # 0 - поставил временно, по хорошему ставить 10 (или 5 если 10 - слишком сложно)
        Energy += 100 # чтоб легче жилось и босс легче проходился
        hp += 1
        HP_BOSS = 1000
        PHASE_BOSS = 0
        Game = BOSS_LEVEL # потом поставить 6.5, 7 - временно для тестов
        Ec = [[1, 1], [1, 2], [2, 1], [2, 2]]

        in_water = True
        n = -1
        while in_water != False:
            in_water = False
            n = -1
            for coords in Ec:
                n += 1
                x, y = coords[0], coords[1]

                if Type[x * Y + y] == 'Вода':
                    in_water = True
            n = -1
            for coords in Ec:
                n += 1
                if in_water:
                    Ec[n][0] += 1

                    if Ec[n][0] >= X:
                        Ec[n][0] = 0
                        Ec[n][1] += 1


        E = [Enemy("Мега-Рыцарь", Ec[0][0], Ec[0][1], hp=1000, t='1'),
             Enemy("Мега-Рыцарь", Ec[1][0], Ec[1][1], hp=1000, t='2'),
             Enemy("Мега-Рыцарь", Ec[2][0], Ec[2][1], hp=1000, t='3'),
             Enemy("Мега-Рыцарь", Ec[3][0], Ec[3][1], hp=1000, t='4')
             ]
        X_BOSS, Y_BOSS = Ec[0][0], Ec[0][1]
    if Game == BOSS_LEVEL:

        # ход босса
        if N % 3 == 0:
            x = X_BOSS
            y = Y_BOSS
            # Вычисляем разности координат с учётом заторенного мира
            dx = (Nx - x + X) % X
            dy = (Ny - y + Y) % Y

            # Выбираем направление движения (кратчайший путь)
            if dx > X / 2:
                dx = dx - X

            if dy > Y / 2:
                dy = dy - Y

            # Двигаемся в нужном направлении
            if dx > 0:
                X_BOSS = (X_BOSS + 1) % X
            elif dx < 0:
                X_BOSS = (X_BOSS - 1) % X

            if dy > 0:
                Y_BOSS = (Y_BOSS + 1) % Y
            elif dy < 0:
                Y_BOSS = (Y_BOSS - 1) % Y

        if random.randint(1, 25) == 1:
            PHASE_BOSS = 0.1

    if PHASE_BOSS == 10:
        PHASE_BOSS = 0

    if PHASE_BOSS != 0:
        PHASE_BOSS += 1
        PHASE_BOSS = PHASE_BOSS // 1 # т. е. стать целым

        if e.T == 'Мега-Рыцарь':
            dx = min(abs(e.x - Nx), X - abs(e.x - Nx))
            dy = min(abs(e.y - Ny), Y - abs(e.y - Ny))
            d = (dx ** 2 + dy ** 2) ** 0.5

            if d <= 1:
                hp -= 1 # для босса нормально, тестил
        if e.T == 'Амфибия':
            dx = min(abs(e.x - Nx), X - abs(e.x - Nx))
            dy = min(abs(e.y - Ny), Y - abs(e.y - Ny))
            d = (dx ** 2 + dy ** 2) ** 0.5

            if d <= 1:
                hp -= 0.2
    else f"УБЕЙ БОССА!\n{HP_BOSS}/1000 хп")
                if T == 'Лед':
                    canvas.itemconfig(S, fill='#6060aa', outline='#eaeaea')
                            if n.T == 'Мега-Рыцарь': # босс
                                canvas.itemconfig(S, fill='#440011', outline='#ffaaaa')
                            if n.T == 'Мега-Рыцарь': # босс
                                canvas.itemconfig(S, fill='#110000', outline='#440011')# ты как бы чувствуешь из далека босса, сделано для баланса
                            if n.T == 'Амфибия':
                                canvas.itemconfig(S, fill='#000080', outline='#4169e1')
                            if n.T == 'Леденящий':
                                canvas.itemconfig(S, fill='#0080e0', outline='#4169e1')
                            if n.T == 'Гидра': # босс
                                canvas.itemconfig(S, fill='#360066', outline='#ffaaff')

                elif T == 'Лед':
                    canvas.itemconfig(S, fill='#000000', outline='#112266')
                if [x, y] in Ec: # плохиш
                    for n in E:
                        if [x, y] == [n.x, n.y]:
                            if n.T == 'Мега-Рыцарь': # босс
                                canvas.itemconfig(S, fill='#000000', outline='#000000')# ты как бы чувствуешь из далека босса, сделано для баланса
                            if n.T == 'Гидра': # босс
                                canvas.itemconfig(S, fill='#330033', outline='#360066')# ты как бы чувствуешь из далека босса, сделано для баланса

                if random.randint(1, X * Y * coos) == 1:
                    if not ([x, y] in Ec):
                        if Game in [-13]:  # Сделал, чтоб отдельно появлялся от мага, а то они вместе
                            E.append(Enemy("Призрак", x, y))
                            Ec.append([x, y])
                if random.randint(1, X * Y * coos) == 1:
                    if not ([x, y] in Ec):
                        if T in ['Вода']:
                            if Game in [-13]:  # Сделал, чтоб отдельно появлялся от мага, а то они вместе
                                E.append(Enemy("Амфибия", x, y))
                                Ec.append([x, y])
                if random.randint(1, X * Y * coos) == 1:
                    if not ([x, y] in Ec):
                        if T in ['Земля']:
                            if Game in [-13]:  # Сделал, чтоб отдельно появлялся от мага, а то они вместе
                                E.append(Enemy("Маг", x, y))
                                Ec.append([x, y])
                if random.randint(1, X * Y * coos) == 1:
                            if Game in [-9, -10, -11]: # Маг будет только на девятом уровне
                                E.append(Enemy("Маг", x, y))
                                Ec.append([x, y])
                        if T in ['Вода']:
                            if Game in [-7]:
                                E.append(Enemy("Амфибия", x, y, hp=225))
                                Ec.append([x, y])
                            if Game in [-8]:
                                E.append(Enemy("Леденящий", x, y, hp=225))
                                Ec.append([x, y])
                if random.randint(1, X * Y * 25) == 1:
                            if Game in [BOSS_LEVEL_2]:  # ключ для нанесения урона боссу (по другому нельзя)
                                E.append(Enemy('Ключ', x, y))
                                Ec.append([x, y])
                    if not ([x, y] in Ec):
                        if T in ['Земля']:
                            if Game in [BOSS_LEVEL]:  # ключ для нанесения урона боссу (по другому нельзя)
                                E.append(Enemy('Ключ', x, y))
                                Ec.append([x, y])
                if T == 'Лед':
                    hp -= 0.2
                if e.T == 'Ключ':
                    if [Nx, Ny] == [e.x, e.y]:
                        E.remove(e)
                        Ec.remove([e.x, e.y])
                        KEY_X = Nx
                        KEY_Y = Ny
                if e.T == 'Леденящий':
                    if IF(e.x, e.y, x, y):
                        Temp[i] -= 5
                    if [e.x, e.y] == [x, y]:
                        if Temp[i] >= 25:
                            if Game in [-8]:
                                KILL_KNIGHT += 1
                            E.remove(e)
                            Ec.remove([e.x, e.y])
                if e.T == 'Амфибия':
                    if Type[e.x * Y + e.y] != 'Вода':
                        if N % 2 == 0:
                            if e.Hod:
                                x2, y2 = e.x, e.y
                                e.Move_Everywhere(Nx, Ny)
                                Ec[Ec.index([x2, y2])] = [e.x, e.y]
                                e.Hod = not e.Hod
                    else:
                        if e.Hod:
                            x2, y2 = e.x, e.y
                            e.Move_Everywhere(Nx, Ny)
                            Ec[Ec.index([x2, y2])] = [e.x, e.y]
                            e.Hod = not e.Hod
                    if TO_ATTACK_SWORD is not None and (e.x, e.y) in TO_ATTACK_SWORD and ATTACK:
                        if e in E:
                            E.remove(e)
                        if [e.x, e.y] in Ec:
                            Ec.remove([e.x, e.y])
                if e.T == 'Мега-Рыцарь':
                    if IF(e.x, e.y, x, y):
                        if T == 'Вода': # Босс 'затопчивает' воду
                            Type[i] = 'Земля'
                    if e.t == '1':
                        e.x = X_BOSS
                        e.y = Y_BOSS
                    if e.t == '2':
                        e.x = X_BOSS + 1
                        e.y = Y_BOSS
                    if e.t == '3':
                        e.x = X_BOSS
                        e.y = Y_BOSS + 1
                    if e.t == '4':
                        e.x = X_BOSS + 1
                        e.y = Y_BOSS + 1
                    Ec[int(e.t) - 1][0] = e.x
                    Ec[int(e.t) - 1][1] = e.y

                if e.T == 'Гидра':
                    if IF(e.x, e.y, x, y):
                        if T == 'Земля': # Босс 'замокревает' землю
                            Type[i] = 'Вода'
                    if e.t == '1':
                        e.x = X_BOSS
                        e.y = Y_BOSS
                    if e.t == '2':
                        e.x = X_BOSS + 1
                        e.y = Y_BOSS
                    if e.t == '3':
                        e.x = X_BOSS
                        e.y = Y_BOSS + 1
                    if e.t == '4':
                        e.x = X_BOSS + 1
                        e.y = Y_BOSS + 1
                    Ec[int(e.t) - 1][0] = e.x
                    Ec[int(e.t) - 1][1] = e.y

            if Game <= -8:
                if Temp[i] < -45:
                    if T == 'Лед':
                        Temp[i] = -45

                if Temp[i] < -25:
                    if T == 'Вода':
                        Type[i] = 'Лед'

                if Temp[i] > -25:
                    if T == 'Лед':
                        Type[i] = 'Вода'
    for x in range(X):
        for y in range(Y):
            if (x == KEY_X or y == KEY_Y) and (x != KEY_X or y != KEY_Y):
                canvas.itemconfig(Objects[x * Y + y], outline='#e8aa0e')
                if [x, y] in Ec:
                    for e in E:
                        if e.T == 'Мега-Рыцарь':
                            if e.x == x and e.y == y:
                                print('Было попадание')
                                HP_BOSS -= 50 # На самом деле снесется 100 ХП

            if PHASE_BOSS != 0:
                if (
                        (x == X_BOSS or y == Y_BOSS or x == X_BOSS + 1 or y == Y_BOSS + 1)
                        and
                (x != X_BOSS or y != Y_BOSS or x != X_BOSS + 1 or y != Y_BOSS + 1)

                )\
                        :
                    canvas.itemconfig(Objects[x * Y + y], outline=Color_0_to_5[int(PHASE_BOSS) - 1])
            if PHASE_BOSS == 10:
                if (
                        (x == X_BOSS or y == Y_BOSS or x == X_BOSS + 1 or y == Y_BOSS + 1)
                        and
                (x != X_BOSS or y != Y_BOSS or x != X_BOSS + 1 or y != Y_BOSS + 1)

                )\
                        :
                    canvas.itemconfig(Objects[x * Y + y], fill="#ff3333", outline="#ff3333")

                    if Nx == x and Ny == y:
                        hp -= 3.4

            if PHASE_BOSS == -10:
                if (
                        (x == X_BOSS or y == Y_BOSS or x == X_BOSS + 1 or y == Y_BOSS + 1)
                        and
                (x != X_BOSS or y != Y_BOSS or x != X_BOSS + 1 or y != Y_BOSS + 1)

                )\
                        :
                    canvas.itemconfig(Objects[x * Y + y], fill="#c71585", outline="#c71585")

                    if Nx == x and Ny == y:
                        hp -= 3.4

