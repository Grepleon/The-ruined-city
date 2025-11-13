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
PHASE_BOSS_2 = 0

def I(): # сама игра
    """Сама игра, здесь будут происходить основные игровые битвы и обработки...."""
    global Nx, Ny, Game, X, Y, Mx, My, B, Objects, E, Ec, TIME_START_GAME, hp, sp, Energy,\
        Ending, Sword, BB, ATTACK, ATTACK_P, LIST_ATTACK, TO_ATTACK_SWORD, N, KILL_KNIGHT,\
        HP_BOSS, X_BOSS, Y_BOSS, PHASE_BOSS, PHASE_BOSS_2
    N += 1

    BOSS_LEVEL = -6.5 # потом поставить 6.5, 7 - временно для тестов
    BOSS_LEVEL_2 = -12.5
    BOSS_LEVEL_FINAL = -14.5 # ПОСЛЕДНИЙ УРОВЕНЬ - ЭТО БОСС!

    if TO_ATTACK_SWORD is None:
        TO_ATTACK_SWORD = set()

    if Game == -6 and (KILL_KNIGHT >= 5): # 0 - поставил временно, по хорошему ставить 10 (или 5 если 10 - слишком сложно)
        PHASE_BOSS_2 = 0
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

        return 'БОСС'

    if Game == -12 and (
            KILL_KNIGHT >= 5):  # 0 - поставил временно, по хорошему ставить 10 (или 5 если 10 - слишком сложно)
        PHASE_BOSS_2 = 0
        Energy += 100  # чтоб легче жилось и босс легче проходился
        hp += 1
        HP_BOSS = 1000
        PHASE_BOSS = 0
        Game = BOSS_LEVEL_2
        Ec = [[1, 1], [1, 2], [2, 1], [2, 2]]

        in_water = True
        n = -1
        while in_water != False:
            in_water = False
            n = -1
            for coords in Ec:
                n += 1
                x, y = coords[0], coords[1]

                if Type[x * Y + y] != 'Вода':
                    in_water = True
            n = -1
            for coords in Ec:
                n += 1
                if in_water:
                    Ec[n][0] += 1

                    if Ec[n][0] >= X:
                        Ec[n][0] = 0
                        Ec[n][1] += 1

        E = [Enemy("Гидра", Ec[0][0], Ec[0][1], hp=1000, t='1'),
             Enemy("Гидра", Ec[1][0], Ec[1][1], hp=1000, t='2'),
             Enemy("Гидра", Ec[2][0], Ec[2][1], hp=1000, t='3'),
             Enemy("Гидра", Ec[3][0], Ec[3][1], hp=1000, t='4')
             ]

        X_BOSS, Y_BOSS = Ec[0][0], Ec[0][1]

        return 'БОСС'

    if Game == -14:
        PHASE_BOSS_2 = 0
        Energy = 500 # чтоб легче жилось и босс легче проходился
        hp = 12
        HP_BOSS = 1000
        PHASE_BOSS = 0
        Game = BOSS_LEVEL_FINAL
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


        E = [Enemy("Некромант", Ec[0][0], Ec[0][1], hp=1000, t='1'),
             Enemy("Некромант", Ec[1][0], Ec[1][1], hp=1000, t='2'),
             Enemy("Некромант", Ec[2][0], Ec[2][1], hp=1000, t='3'),
             Enemy("Некромант", Ec[3][0], Ec[3][1], hp=1000, t='4')
             ]

        X_BOSS, Y_BOSS = Ec[0][0], Ec[0][1]

        return 'БОСС'

    for i in E:
        if i.T == 'Мега-Рыцарь':
            pass # для тестов, Мега-Рыцарь есть, но не отображается
    if int(hp) <= 0:

        for i in END:
            canvas.itemconfig(i, state='normal')
        canvas.itemconfig(END[1], text='Вы погибли...\nНажмите пробел чтобы выйти в главное меню')
        if keys_pressed[' ']:
            play_menu_music()
            Game = 1
            for i in lvls:
                i.Show()

                Objects[X * Y + 18].Hide()

                i.Restart()
            canvas.itemconfig(Rectangles, state='normal')
            canvas.config(bg='#001000')
            for i in Objects:
                canvas.itemconfig(i, state='hidden')
            for i in END:
                canvas.itemconfig(i, state='hidden')
            canvas.itemconfig(Sword, state='hidden')

        return 'Выход из ф-я'

    if         (t.time() - TIME_START_GAME >= 120 and Game == -1) \
            or (t.time() - TIME_START_GAME >= 150 and Game == -2) \
            or (t.time() - TIME_START_GAME >= 180 and Game == -3) \
            or (KILL_KNIGHT >= 10 and Game == -4) \
            or (KILL_KNIGHT >= 10 and Game == -5) \
            or (HP_BOSS <= 0 and Game == BOSS_LEVEL) \
            or (t.time() - TIME_START_GAME >= 140 and Game == -7) \
            or (t.time() - TIME_START_GAME >= 150 and Game == -8) \
            or (KILL_KNIGHT >= 10 and Game == -9) \
            or (t.time() - TIME_START_GAME >= 100 and Game == -10) \
            or (t.time() - TIME_START_GAME >= 180 and Game == -11) \
            or (HP_BOSS <= 0 and Game == BOSS_LEVEL_2) \
            or (t.time() - TIME_START_GAME >= 160 and Game == -13) \
            or (HP_BOSS <= 0 and Game == BOSS_LEVEL_FINAL) \
            :

        for i in END:
            canvas.itemconfig(i, state='normal')
        canvas.itemconfig(END[1], text='Вы победили!\n\nНажмите пробел чтобы выйти в главное меню')
        if keys_pressed[' ']:
            play_menu_music()
            Game = 1

            Objects[X * Y + 18].Hide()

            for i in lvls:
                i.Show()
                i.Restart()
            canvas.itemconfig(Rectangles, state='normal')
            canvas.config(bg='#001000')
            for i in Objects:
                canvas.itemconfig(i, state='hidden')
            for i in END:
                canvas.itemconfig(i, state='hidden')
            canvas.itemconfig(Sword, state='hidden')

        return 'Выход из ф-я'

    for i in [Objects[18 + X * Y]]:
        III = i
        i.Click(Mx, My, B)
        i.Open(Mx, My)

        if i.On:
            if i.name == 'Меню':
                canvas.itemconfig(END[0], state='normal')
                canvas.itemconfig(END[1], state='normal', text='Вы в меню.\nНажмите левый шифт, чтобы вернуться в игру. Нажмите пробел, чтобы выйти в главное меню')
                if keys_pressed[' ']:
                    play_menu_music()
                    Game = 1

                    Objects[X * Y + 18].Hide()

                    for i in lvls:
                        i.Show()
                        i.Restart()
                    canvas.itemconfig(Rectangles, state='normal')
                    canvas.config(bg='#001000')
                    for i in Objects:
                        canvas.itemconfig(i, state='hidden')
                    for i in END:
                        canvas.itemconfig(i, state='hidden')
                    canvas.itemconfig(Sword, state='hidden')
                    III.On = False
                if keys_pressed['e']:
                    canvas.itemconfig(END[0], state='hidden')
                    canvas.itemconfig(END[1], state='hidden',
                                      text='Вы в меню.\nНажмите левый шифт, чтобы вернуться в игру. Нажмите пробел, чтобы выйти в главное меню')
                    i.On = False
            return 'Вообще-то мы в меню'

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

    if Game == BOSS_LEVEL_2:

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
            PHASE_BOSS = -0.1

    if Game == BOSS_LEVEL_FINAL:

        # ход босса
        if random.randint(1, 25) == 1:
            PHASE_BOSS = -0.1
        if random.randint(1, 25) == 1: # босс иногда будет телепортиоваться
            PHASE_BOSS_2 = 1
        if PHASE_BOSS_2 == 10:
            PHASE_BOSS_2 = 0
            if random.randint(1, 3) == 1:
                PHASE_BOSS = -0.1
        if PHASE_BOSS_2 > 0:
            PHASE_BOSS_2 += 1
        if PHASE_BOSS_2 == 5:
            a = random.randint(0, X - 3)
            b = random.randint(0, Y - 3)
            Ec = [[a + 1, b + 1], [a + 1, b + 2], [a + 2, b + 1], [a + 2, b + 2]]
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

            for i in range(4):
                E[i].x = Ec[i][0]
                E[i].y = Ec[i][1]

            X_BOSS = Ec[0][0]
            Y_BOSS = Ec[0][1]



    if PHASE_BOSS == 10:
        PHASE_BOSS = 0

    if PHASE_BOSS == -10:
        PHASE_BOSS = 0

    if PHASE_BOSS > 0:
        PHASE_BOSS += 1
        PHASE_BOSS = PHASE_BOSS // 1 # т. е. стать целым

    if PHASE_BOSS < 0:
        PHASE_BOSS -= 1
        PHASE_BOSS = int(PHASE_BOSS)# т. е. стать целым

    for e in E:
        e.Hod = True
        if e.T == 'Призрак':
            dx = min(abs(e.x - Nx), X - abs(e.x - Nx))
            dy = min(abs(e.y - Ny), Y - abs(e.y - Ny))
            d = (dx ** 2 + dy ** 2) ** 0.5

            if d <= 2:
                hp -= 0.5

        if e.T == 'Рыцарь':
            dx = min(abs(e.x - Nx), X - abs(e.x - Nx))
            dy = min(abs(e.y - Ny), Y - abs(e.y - Ny))
            d = (dx ** 2 + dy ** 2) ** 0.5

            if d <= 1:
                hp -= 0.2  # не смотря всего на 0.2 сносит он много

        if e.T == 'Мега-Рыцарь':
            dx = min(abs(e.x - Nx), X - abs(e.x - Nx))
            dy = min(abs(e.y - Ny), Y - abs(e.y - Ny))
            d = (dx ** 2 + dy ** 2) ** 0.5

            if d <= 1:
                hp -= 1 # для босса нормально, тестил

        if e.T == 'Некромант':
            if TO_ATTACK_SWORD is not None and (e.x, e.y) in TO_ATTACK_SWORD and ATTACK:
                HP_BOSS -= 5
                if random.randint(1, 3) == 1:
                    PHASE_BOSS_2 = 1

        if e.T == 'Амфибия':
            dx = min(abs(e.x - Nx), X - abs(e.x - Nx))
            dy = min(abs(e.y - Ny), Y - abs(e.y - Ny))
            d = (dx ** 2 + dy ** 2) ** 0.5

            if d <= 1:
                hp -= 0.2

        if e.T == 'Маг':
            if e.t == '0':
                if random.randint(1, 10) == 1:
                    e.t = 1
            else:
                if e.t < 10:
                    e.t += 1
                else:
                    e.t = '0'

        if e.T == 'Гидра':
            dx = min(abs(e.x - Nx), X - abs(e.x - Nx))
            dy = min(abs(e.y - Ny), Y - abs(e.y - Ny))
            d = (dx ** 2 + dy ** 2) ** 0.5

            if d <= 1:
                hp -= 1

    # Движение игрока с учетом всех нажатых клавиш
    if not ATTACK:
        if keys_pressed['w'] or keys_pressed['ц']:  # Вверх
            if (not ((Type[(Nx * X + Ny - 1) % (X * Y)]) == 'Вода') and Game not in [-8]) or (Game in MOVE_WATER_LEVEL and (N % 2 == 0 or not ((Type[(Nx * X + Ny - 1) % (X * Y)]) == 'Вода'))):
                Ny -= 1
        if keys_pressed['s'] or keys_pressed['ы']:  # Вниз
            if (not ((Type[(Nx * X + Ny + 1) % (X * Y)]) == 'Вода') and Game not in [-8]) or (Game in MOVE_WATER_LEVEL and (N % 2 == 0 or not ((Type[(Nx * X + Ny + 1) % (X * Y)]) == 'Вода'))):
                Ny += 1
        if keys_pressed['d'] or keys_pressed['в']:  # Вправо
            if (not ((Type[(Nx * X + Ny + X) % (X * Y)]) == 'Вода') and Game not in [-8]) or (Game in MOVE_WATER_LEVEL and (N % 2 == 0 or not ((Type[(Nx * X + Ny + X) % (X * Y)]) == 'Вода'))):
                Nx += 1
        if keys_pressed['a'] or keys_pressed['ф']:  # Влево
            if (not ((Type[(Nx * X + Ny - X) % (X * Y)]) == 'Вода') and Game not in [-8]) or (Game in MOVE_WATER_LEVEL and (N % 2 == 0 or not ((Type[(Nx * X + Ny - X) % (X * Y)]) == 'Вода'))):
                Nx -= 1

    if ATTACK_P == 9:
        ATTACK = False
        ATTACK_P = 0
        LIST_ATTACK = []
        TO_ATTACK_SWORD = []

        # Убираем подсветку
        for i, obj in enumerate(Objects[:X * Y]):
            canvas.itemconfig(obj, width=1)
            if Type[i] == 'Земля':
                canvas.itemconfig(obj, outline='#00ffaa')
            elif Type[i] == 'Вода':
                canvas.itemconfig(obj, outline='#00aaff')
            elif Type[i] == 'Снег':
                canvas.itemconfig(obj, outline='#eaeaea')

        canvas.itemconfig(Sword, state='hidden')

    if ATTACK:
        ATTACK_P += 1

        # Центр игрока
        center_x = Nx * wx + wx / 2
        center_y = Ny * wx + wx / 2

        # Получаем координаты для текущего кадра атаки
        if ATTACK_P < len(LIST_ATTACK):
            line_data = LIST_ATTACK[ATTACK_P]

            # Координаты начала и конца меча
            start_x = center_x
            start_y = center_y
            end_x = center_x + line_data[2]
            end_y = center_y + line_data[3]

            # Применяем координаты к мечу
            canvas.coords(Sword, start_x, start_y, end_x, end_y)

            # Определяем клетки, которых касается меч
            TO_ATTACK_SWORD = get_cells_under_sword(start_x, start_y, end_x, end_y)
    if not ATTACK:
        if B == 1:
            # Центр игрока
            center_x = Nx * wx + wx / 2
            center_y = Ny * wx + wx / 2

            # Вектор от игрока к курсору
            dx = Mx - center_x
            dy = My - center_y

            # Вычисляем угол в градусах
            angle = math.degrees(math.atan2(dy, dx))

            ATTACK = True
            ATTACK_P = 0
            LIST_ATTACK = generate_rotating_lines_simple(angle)

            # Показываем меч и устанавливаем начальную позицию
            canvas.itemconfig(Sword, state='normal')
            if LIST_ATTACK:
                line_data = LIST_ATTACK[0]
                canvas.coords(Sword,
                              center_x, center_y,
                              center_x + line_data[2],
                              center_y + line_data[3])

    canvas.itemconfig(Objects[X * Y + 1], text=f'Время:\n{int(t.time() - TIME_START_GAME)}/{120 if Game == -1 else
    150 if Game == -2 else 140 if Game in [-7] else 150 if Game in [-8] else 100 if Game in [-10] else 160 if Game in [-13] else 180} сек.'
    if Game not in [-4, -5, -6, BOSS_LEVEL, -9, BOSS_LEVEL_2, -12, BOSS_LEVEL_FINAL] else f'Убито {"рыцарей" if
    not Game in [-5, -9, -12] else "морозов" if not Game in [-9, -12] else "магов" if not Game in [-12] else "амфибий"}:\n{KILL_KNIGHT}/{10 if not Game in [-6, -12]
    else 5}' if Game not in [BOSS_LEVEL, BOSS_LEVEL_2, BOSS_LEVEL_FINAL]
    else f"УБЕЙ БОССА!\n{HP_BOSS}/1000 хп")

    Nx, Ny = Nx % X, Ny % Y
    D = 3
    if Game != -2:
        D = 4
    if True: # False поставил временно и для тестов потом после тестов поставить True
        if Game == BOSS_LEVEL:
            if N % 30 < 10:
                if N % 10 > 5:
                    D = N % 5
                elif N % 5 != 0:
                    D = -N % 5
                elif N % 10 != 5:
                    D = 4
                else:
                    D = 1

    if Energy != 0:
        if keys_pressed['e']:
            Energy -= 1
            D += 3

    # 6 + i

    sp_index = X * Y + 6 + -3  # начальный индекс полосок HP
    canvas.itemconfig(Objects[sp_index], text=f'Спичек:\n{int(sp)}/25 штук')

    hp_index = X * Y + 6 + -1  # начальный индекс полосок HP
    canvas.itemconfig(Objects[hp_index], fill='#ffaa00', text=f'Жизней {int(hp)}/10')

    for i in range(10):
        hp_index = X * Y + 6 + i  # начальный индекс полосок HP
        canvas.itemconfig(Objects[hp_index], fill='#ffaa00' if int(i + 1) <= int(hp) else '#330000')

    canvas.itemconfig(Objects[X * Y + 6 + 11], text=f'Энергия:\n{int(Energy)}/250')

    i = -1
    for x in range(X): # цикл обработки визуализации
        for y in range(Y):
            i += 1
            S = Objects[i]
            T = Type[i]

            if x * wx + wx > Mx >= x * wx and y * wx + wx > My >= y * wx:
                canvas.itemconfig(S, width=2)
            else:
                canvas.itemconfig(S, width=1)

            dx = min(abs(x - Nx), X - abs(x - Nx))
            dy = min(abs(y - Ny), Y - abs(y - Ny))
            d = (dx ** 2 + dy ** 2) ** 0.5

            a = 0 # для тестов. Если не используется ставить a=0

            if d <= D + a: # 7.0
                if T == 'Земля':
                    canvas.itemconfig(S, fill='#003300', outline='#00ffaa')
                if T == 'Вода':
                    canvas.itemconfig(S, fill='#001144', outline='#00aaff')
                if T == 'Снег':
                    canvas.itemconfig(S, fill='#707070', outline='#eaeaea')
                if T == 'Лед':
                    canvas.itemconfig(S, fill='#6060aa', outline='#eaeaea')
                if [x, y] in Ec: # плохиш
                    for n in E:
                        if [x, y] == [n.x, n.y]:
                            if n.T == 'Холод':
                                canvas.itemconfig(S, fill='#113355', outline='#00aaff')
                            if n.T == 'Призрак':
                                canvas.itemconfig(S, fill='#309030', outline='#c0e0c0')
                            if n.T == 'Рыцарь':
                                canvas.itemconfig(S, fill='#110000', outline='#00aaff')
                            if n.T == 'Мега-Рыцарь': # босс
                                canvas.itemconfig(S, fill='#440011', outline='#ffaaaa')
                            if n.T == 'Ключ':
                                canvas.itemconfig(S, fill='#69421d', outline='yellow')
                            if n.T == 'Амфибия':
                                canvas.itemconfig(S, fill='#000080', outline='#4169e1')
                            if n.T == 'Леденящий':
                                canvas.itemconfig(S, fill='#0080e0', outline='#4169e1')
                            if n.T == 'Маг':
                                canvas.itemconfig(S, fill='#420062', outline='#c53dff')
                            if n.T == 'Гидра':  # босс
                                canvas.itemconfig(S, fill='#360066', outline='#ffaaff')
                            if n.T == 'Некромант': # босс
                                canvas.itemconfig(S, fill='#110000', outline='#c53dff')

                if Nx == x and Ny == y: # игрок
                    canvas.itemconfig(S, fill='#335500', outline='#00ffaa')
            elif d <= D + 5 + a:
                if T == 'Вода':
                    canvas.itemconfig(S, fill='#000000', outline='#001133')
                elif T == 'Снег':
                    canvas.itemconfig(S, fill='#000000', outline='#222222')
                elif T == 'Лед':
                    canvas.itemconfig(S, fill='#000000', outline='#112266')
                else:
                    canvas.itemconfig(S, fill='#000000', outline='#003300')

                if [x, y] in Ec: # плохиш
                    for n in E:
                        if [x, y] == [n.x, n.y]:
                            if n.T == 'Призрак': # ты как бы чувствуешь из далека призрака, сделано для баланса
                                canvas.itemconfig(S, fill='#001100', outline='#309030')
                            if n.T == 'Мега-Рыцарь':  # босс
                                canvas.itemconfig(S, fill='#110000',
                                                  outline='#440011')  # ты как бы чувствуешь из далека босса, сделано для баланса
                            if n.T == 'Гидра': # босс
                                canvas.itemconfig(S, fill='#330033', outline='#360066')# ты как бы чувствуешь из далека босса, сделано для баланса

            else:
                canvas.itemconfig(S, fill='#000000', outline='#000000')
    i = -1
    SP = 0

    KEY_X = -1
    KEY_Y = -1

    if sp != 0:
        if keys_pressed[' ']:
            SP = 1
            sp -= 1

    for x in range(X): # цикл обработки визуализации
        for y in range(Y):
            i += 1
            S = Objects[i]
            T = Type[i]

            dx = min(abs(x - Nx), X - abs(x - Nx))
            dy = min(abs(y - Ny), Y - abs(y - Ny))
            d = (dx ** 2 + dy ** 2) ** 0.5

            if d <= 5:
                if SP:
                    Temp[i] += 75
                    if d <= D:
                        canvas.itemconfig(S, fill='#220000', outline='#ff0000')
                    else:
                        canvas.itemconfig(S, outline='#ff0000')

            coos = 25

            if Game in [-10]:
                coos = 35
            if Game in [-13]:
                coos = 35

            if d > D:  # 'плохиши' появляются только в темноте, чтоб игрок их не видел
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
                    if not ([x, y] in Ec):
                        if T in ['Земля']:
                            if Game in [-10, -13]:  # Сделал, чтоб отдельно появлялся от мага, а то они вместе
                                E.append(Enemy("Рыцарь", x, y))
                                Ec.append([x, y])
                if random.randint(1, X * Y * coos) == 1:
                    if not ([x, y] in Ec):
                        if T in ['Земля']:
                            if Game in [-1, -3, -5, -8, -13]:  # Холод будет только на первом уровне
                                E.append(Enemy("Холод", x, y))
                                Ec.append([x, y])
                            if Game in [-4, -5, -6]:  # Рыцарь будет только на четвертом уровне
                                E.append(Enemy("Рыцарь", x, y))
                                Ec.append([x, y])
                            if Game in [-9, -10, -11]: # Маг будет только на девятом уровне
                                E.append(Enemy("Маг", x, y))
                                Ec.append([x, y])
                        if T in ['Вода']:
                            if Game in [-7, -10, -12]:
                                E.append(Enemy("Амфибия", x, y, hp=225))
                                Ec.append([x, y])
                            if Game in [-8, -13]:
                                E.append(Enemy("Леденящий", x, y, hp=225))
                                Ec.append([x, y])
                            if Game in [BOSS_LEVEL_2]:  # ключ для нанесения урона боссу (по другому нельзя)
                                E.append(Enemy('Ключ', x, y))
                                Ec.append([x, y])
                        if Game in [-2, -3, -6, -11]:
                            E.append(Enemy("Призрак", x, y, hp=225))
                            Ec.append([x, y])
                if random.randint(1, X * Y * coos) == 1:
                    if not ([x, y] in Ec):
                        if T in ['Земля']:
                            if Game in [BOSS_LEVEL]:  # ключ для нанесения урона боссу (по другому нельзя)
                                E.append(Enemy('Ключ', x, y))
                                Ec.append([x, y])

            if [Nx, Ny] == [x, y]:
                if T == 'Снег':
                    hp -= 0.2
                if T == 'Лед':
                    hp -= 0.2

            if Temp[i] > 0:
                Temp[i] -= 1

            for e in E:
                if e.T == 'Ключ':
                    if [Nx, Ny] == [e.x, e.y]:
                        E.remove(e)
                        Ec.remove([e.x, e.y])
                        KEY_X = Nx
                        KEY_Y = Ny


                if e.T == 'Холод':
                    if IF(e.x, e.y, x, y):
                        Temp[i] -= 5
                    if [e.x, e.y] == [x, y]:
                        if Temp[i] >= 25:
                            if Game in [-5]:
                                KILL_KNIGHT += 1
                            E.remove(e)
                            Ec.remove([e.x, e.y])

                if e.T == 'Леденящий':
                    if IF(e.x, e.y, x, y):
                        Temp[i] -= 5
                    if [e.x, e.y] == [x, y]:
                        if Temp[i] >= 25:
                            if Game in [-8]:
                                KILL_KNIGHT += 1
                            E.remove(e)
                            Ec.remove([e.x, e.y])

                # В функции I(), в части обработки атаки рыцаря:

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
                        if Game in [-12]:
                            KILL_KNIGHT += 1
                        if e in E:
                            E.remove(e)
                        if [e.x, e.y] in Ec:
                            Ec.remove([e.x, e.y])

                if e.T == 'Рыцарь':
                    if N % 2 == 0:
                        if e.Hod:
                            x2, y2 = e.x, e.y
                            e.Move_To_Player_No_Water(Nx, Ny)
                            Ec[Ec.index([x2, y2])] = [e.x, e.y]
                            e.Hod = not e.Hod

                    # Добавьте проверку на None:
                    if TO_ATTACK_SWORD is not None and (e.x, e.y) in TO_ATTACK_SWORD and ATTACK:
                        if Game in [-4, -6]:
                            KILL_KNIGHT += 1
                        if e in E:
                            E.remove(e)
                        if [e.x, e.y] in Ec:
                            Ec.remove([e.x, e.y])

                if e.T == 'Маг':
                    if N % 2 == 0:
                        if e.Hod:
                            x2, y2 = e.x, e.y
                            e.Move_To_Player_No_Water(Nx, Ny)
                            Ec[Ec.index([x2, y2])] = [e.x, e.y]
                            e.Hod = not e.Hod

                    # Добавьте проверку на None:
                    if TO_ATTACK_SWORD is not None and (e.x, e.y) in TO_ATTACK_SWORD and ATTACK:
                        if Game in [-9]:
                            KILL_KNIGHT += 1
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


                if e.T == 'Призрак':
                    if e.Hod:
                        x2, y2 = e.x, e.y
                        e.Move_Everywhere(Nx, Ny)
                        Ec[Ec.index([x2, y2])] = [e.x, e.y]
                        e.Hod = not e.Hod

                    dx = min(abs(e.x - Nx), X - abs(e.x - Nx))
                    dy = min(abs(e.y - Ny), Y - abs(e.y - Ny))
                    d = (dx ** 2 + dy ** 2) ** 0.5

                    if d <= D:
                        e.hp -= 0.1

                if e.hp <= 0:
                    if e.T == 'Рыцарь' and Game in [-4, -6]:
                        KILL_KNIGHT += 1
                    E.remove(e)
                    Ec.remove([e.x, e.y])



            if Temp[i] < -45:
                if T == 'Снег':
                    Temp[i] = -45

            if Temp[i] < -25:
                if T == 'Земля':
                    Type[i] = 'Снег'

            if Temp[i] > -25:
                if T == 'Снег':
                    Type[i] = 'Земля'

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

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    ex = x + dx
                    ey = y + dy

                    ei = (ex) % X * Y + (ey) % Y

                    if Temp[ei] > Temp[i]:
                        Temp[i] += 1
                        Temp[ei] -= 1

                    if Temp[ei] < Temp[i]:
                        Temp[i] -= 1
                        Temp[ei] += 1

    Attack = []

    for e in E:
        if e.T == 'Маг':
            if e.t != '0':
                Attack.append((e.x, e.y, e.t))


    for x in range(X):
        for y in range(Y):
            for a in Attack:
                dx = min(abs(a[0] - x), X - abs(a[0] - x))
                dy = min(abs(a[1] - y), Y - abs(a[1] - y))
                d = (dx ** 2 + dy ** 2) ** 0.5
                dx2 = min(abs(Nx - x), X - abs(Nx - x))
                dy2 = min(abs(Ny - y), Y - abs(Ny - y))
                d2 = (dx2 ** 2 + dy2 ** 2) ** 0.5
                if d < a[2] / 2:
                    if d2 <= D + 5 :
                        canvas.itemconfig(Objects[x * Y + y], outline=Color_0_to_10_Magic[a[2]])
                    if a[2] == 10:
                        if d2 <= D + 5:
                            canvas.itemconfig(Objects[x * Y + y], fill='#c71585', outline='#c71585')
                        if (x, y) == (Nx, Ny):
                            hp -= 1
            if (x == KEY_X or y == KEY_Y) and (x != KEY_X or y != KEY_Y):
                canvas.itemconfig(Objects[x * Y + y], outline='#e8aa0e')
                if [x, y] in Ec:
                    for e in E:
                        if e.T == 'Мега-Рыцарь':
                            if e.x == x and e.y == y:
                                print('Было попадание')
                                HP_BOSS -= 50  # На самом деле снесется 100 ХП
                        if e.T == 'Гидра':
                            if e.x == x and e.y == y:
                                print('Было попадание')
                                HP_BOSS -= 50 # На самом деле снесется 100 ХП

            if PHASE_BOSS > 0:
                if (
                        (x == X_BOSS or y == Y_BOSS or x == X_BOSS + 1 or y == Y_BOSS + 1)
                        and
                (x != X_BOSS or y != Y_BOSS or x != X_BOSS + 1 or y != Y_BOSS + 1)

                )\
                        :
                    canvas.itemconfig(Objects[x * Y + y], outline=Color_0_to_5[int(PHASE_BOSS) - 1])
            if 6 > PHASE_BOSS_2 > 0:
                if (
                        (x == X_BOSS and y == Y_BOSS) or (x == X_BOSS + 1 and y == Y_BOSS + 1) or
                        (x == X_BOSS + 1 and y == Y_BOSS) or (x == X_BOSS and y == Y_BOSS + 1)
                )\
                        :
                    canvas.itemconfig(Objects[x * Y + y], outline=Color_0_to_10_Tp[-int(PHASE_BOSS_2)])
            if PHASE_BOSS_2 > 5:
                if (
                        (x == X_BOSS and y == Y_BOSS) or (x == X_BOSS + 1 and y == Y_BOSS + 1) or
                        (x == X_BOSS + 1 and y == Y_BOSS) or (x == X_BOSS and y == Y_BOSS + 1)
                )\
                        :
                    canvas.itemconfig(Objects[x * Y + y], outline=Color_0_to_10_Tp[int(PHASE_BOSS_2) - 1 - 4])
            if PHASE_BOSS_2 == 10:
                if (
                        (x == X_BOSS and y == Y_BOSS) or (x == X_BOSS + 1 and y == Y_BOSS + 1) or
                        (x == X_BOSS + 1 and y == Y_BOSS) or (x == X_BOSS and y == Y_BOSS + 1)
                )\
                        :
                    canvas.itemconfig(Objects[x * Y + y], outline=Color_0_to_10_Tp[-1], fill=Color_0_to_10_Tp[-1])
            if PHASE_BOSS < 0:
                if (
                        (x == X_BOSS or y == Y_BOSS or x == X_BOSS + 1 or y == Y_BOSS + 1)
                        and
                (x != X_BOSS or y != Y_BOSS or x != X_BOSS + 1 or y != Y_BOSS + 1)

                )\
                        :
                    canvas.itemconfig(Objects[x * Y + y], outline=Color_0_to_10_Magic[abs(int(PHASE_BOSS)) - 1])
            if PHASE_BOSS == 10:
                if (
                        (x == X_BOSS or y == Y_BOSS or x == X_BOSS + 1 or y == Y_BOSS + 1)
                        and
                        (x != X_BOSS or y != Y_BOSS or x != X_BOSS + 1 or y != Y_BOSS + 1)

                ) \
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


    BB = 0

Color_0_to_5 = C_C.CCh_list_h('#000000', '#c20000', Repeat=10)
Color_0_to_10_Magic = C_C.CCh_list_h('#000000', '#a800db', Repeat=10)
Color_0_to_10_Tp = C_C.CCh_list_h('#000000', '#c154c1', Repeat=6)

def G():
    global All_Objects, Mx, My, B, Game, lvls, Objects, TIME_START_GAME, hp, Energy, sp, Nx, Ny, BB, KILL_KNIGHT

    HIDE = False

    for i in lvls:
        i.Click(Mx, My, B)
        i.Open(Mx, My)

        if i.On:
            if 'Уровень' in i.name:
                Game = -int(i.name.split('-')[1])
                HIDE = True
                # Запускаем музыку игры при выборе уровня
                play_game_music()
            if 'Назад' in i.name:
                Game = 0
                HIDE = True
                # Возвращаем музыку меню при возврате
                play_menu_music()

    for i in lvls:
        if HIDE:
            i.Hide()
            i.Restart()

    if Game == 0:
        canvas.itemconfig(Rectangles, state='hidden')
        canvas.config(bg='#000000')
        for i in All_Objects:
            if HIDE:
                i.Restart()
                i.Show()
    else:
        TIME_START_GAME = t.time()
        Nx = 15
        Ny = 15
        Gnrt()
        if Game < 0: # 1й уровень - борьба только с морозом; 2й уровень - борьба с призраками
            Objects[X * Y + 18].Show()
            canvas.itemconfig(Rectangles, state='hidden')
            canvas.config(bg='#000000')
            hp = 10
            Energy = 250
            sp = 25
            KILL_KNIGHT = 0

            for i in Objects:
                if HIDE:
                    canvas.itemconfig(i, state='normal')

    BB = 0

Speed = 100

def A():
    global Game, Speed, keys_pressed

    if keys_pressed['f']:
        Speed = 50
    else:
        Speed = 100

    if Game < 0:
        I()
    if Game == 0:
        M()
    if Game == 1:
        G()

    canvas.after(Speed, A)


def M():
    global All_Objects, Mx, My, B, Game, lvls

    HIDE = False

    for i in All_Objects:
        i.Click(Mx, My, B)
        i.Open(Mx, My)

        if i.On:
            if i.name == 'Начать игру':
                Game = 1
                HIDE = True
                # Запускаем музыку при переходе в меню уровней
                play_menu_music()

    if Game == 1:
        canvas.config(bg='#001000')
        canvas.itemconfig(Rectangles, state='normal')
        for i in All_Objects:
            if HIDE:
                i.Hide()
                i.Restart()
        for i in lvls:
            if HIDE:
                i.Show()
                i.Restart()


# Запускаем начальную музыку при старте программы
def on_program_start():
    """Запускается при старте программы"""
    # Можно добавить начальную музыку здесь
    print("Программа запущена")


# Обработчик закрытия окна
def on_closing():
    """Останавливает музыку при закрытии программы"""
    music_player.stop_music()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)

A()

B = 0
BB = 0


def mouse_press(event):
    global B, BB
    B = 1  # Мышь зажата
    BB = 1


def mouse_release(event):
    global B
    B = 0  # Мышь отпущена


root.bind('<ButtonPress-1>', mouse_press)  # Левая кнопка мыши
root.bind('<ButtonRelease-1>', mouse_release)  # Отпускание левой кнопки

root.mainloop()


# Запускаем программу
on_program_start()

TIME_END = t.time()
try:
    with open('StatisRG.txt', 'r') as f:
        line = f.readline().strip()
        if line:
            file_value = float(line)  # используем float вместо int
        else:
            file_value = 0.0
except (FileNotFoundError, ValueError):
    file_value = 0.0

with open('StatisRG.txt', 'w') as f:
    f.write(str(file_value + TIME_END - TIME_START))