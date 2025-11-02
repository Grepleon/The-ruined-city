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
                elif T == 'Лед':
                    canvas.itemconfig(S, fill='#000000', outline='#112266')
                if [x, y] in Ec: # плохиш
                    for n in E:
                        if [x, y] == [n.x, n.y]:
                            if n.T == 'Мега-Рыцарь': # босс
                                canvas.itemconfig(S, fill='#000000', outline='#000000')# ты как бы чувствуешь из далека босса, сделано для баланса
                        if T in ['Вода']:
                            if Game in [-7]:
                                E.append(Enemy("Амфибия", x, y, hp=225))
                                Ec.append([x, y])
                            if Game in [-8]:
                                E.append(Enemy("Леденящий", x, y, hp=225))
                                Ec.append([x, y])
                if random.randint(1, X * Y * 25) == 1:
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
