import turtle as t
def FULL_COLOR():
    sp_color = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    Full_combinations = []
    Hod = 0
    for Number1 in range(len(sp_color)):
        for Letter1 in range(len(sp_color)):
            for Number2 in range(len(sp_color)):
                for Letter2 in range(len(sp_color)):
                    for Number3 in range(len(sp_color)):
                        for Letter3 in range(len(sp_color)):
                            Full_combinations.append(
                                '#' + sp_color[Number1] + sp_color[Letter1] + sp_color[Number2] + sp_color[Letter2] +
                                sp_color[Number3] + sp_color[Letter3]
                            )
    return Full_combinations
def Teplote_colro(R=100):
    import Color_Change as c

    C = c.FULL_COLOR()

    l = len(C)

    # t.speed(0)

    # t.goto(-500,0)
    # t.goto(500,0)
    # t.goto(-500,0)
    ccc = []


    for i in range(R):
        color = C[int(i * (l / R))]
        ccc.append(color)
        # t.forward(1000 / (R))
        # t.color(color)
    return ccc

def Impossible_color():
    a = 0
    b = 0
    c = 0
    sp_color = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    Full_combinations = []

    for Number in range(len(sp_color)):
        for Letter in range(len(sp_color)):
            a = sp_color[Number] + sp_color[Letter]
            Full_combinations.append(a)


    return Full_combinations

def Co_Ch(co1,co2):
    s = Impossible_color()

    a1 = s.index(co1[0 + 1] + co1[1 + 1])
    b1 = s.index(co1[2 + 1] + co1[3 + 1])
    c1 = s.index(co1[4 + 1] + co1[5 + 1])

    a2 = s.index(co2[0 + 1] + co2[1 + 1])
    b2 = s.index(co2[2 + 1] + co2[3 + 1])
    c2 = s.index(co2[4 + 1] + co2[5 + 1])

    Ca = []
    Cb = []
    Cc = []

    if a1 < a2:
        Direction_of_color_change = 1
    else:
        Direction_of_color_change = -1

    for This_Color in range(a1,a2+Direction_of_color_change,Direction_of_color_change):

        Ma = max(a1,a2)
        ma = min(a1,a2)

        Ca.append(s[This_Color])

    if b1 < b2:
        Direction_of_color_change = 1
    else:
        Direction_of_color_change = -1

    for This_Color in range(b1, b2+Direction_of_color_change,Direction_of_color_change):

        Mb = max(b1, b2)
        mb = min(b1, b2)

        Cb.append(s[This_Color])

    if c1 < c2:
        Direction_of_color_change = 1
    else:
        Direction_of_color_change = -1

    for This_Color in range(c1, c2+Direction_of_color_change,Direction_of_color_change):

        Mc = max(c1, c2)
        mc = min(c1, c2)

        Cc.append(s[This_Color])

    return([Ca,Cb,Cc])

def Co_Th(c1,c2,Repeat=20,Step=0):
    Ms = Co_Ch(c1,c2)
    #print(Ms)
    M = []
    Mf = []

    Ma = Ms[0]
    Mb = Ms[1]
    Mc = Ms[2]

    #print('--------')

    la = len(Ma)
    lb = len(Mb)
    lc = len(Mc)

    Ml = max(la,lb,lc)
    ml = min(la,lb,lc)

    Mn = []
    Mystery_and_Absolutism = la * lb * lc
    Na = int(Mystery_and_Absolutism / la)
    Nb = int(Mystery_and_Absolutism / lb)
    Nc = int(Mystery_and_Absolutism / lc)
    Mn = []
    for Mystery_Color in range(la):
        for Mystery_Number in range(Na):
            Mn.append(Ma[Mystery_Color])
    Ma = Mn
    Mn = []
    for Mystery_Color in range(lb):
        for Mystery_Number in range(Nb):
            Mn.append(Mb[Mystery_Color])
    Mb = Mn
    Mn = []
    for Mystery_Color in range(lc):
        for Mystery_Number in range(Nc):
            Mn.append(Mc[Mystery_Color])
    Mc = Mn

    Mf = []
    for i in range(Repeat):
        Given_Value = int((len(Ma)) / (Repeat) * i)
        Mf.append(Ma[Given_Value]+Mb[Given_Value]+Mc[Given_Value])
    Mf.append(Ma[-1]+Mb[-1]+Mc[-1])
    Value = Mf[Step]


    return Value
def CH_Color_pl(COLOR):

    import wartiable as w
    import turtle as t

    C = Impossible_color()

    l = len(C)

    if 1 == 1:
        f = Impossible_color()
        CS = []

        color = COLOR

        a = color[1] + color[2]
        b = color[3] + color[4]
        c = color[5] + color[6]

        A = f.index(a)
        B = f.index(b)
        C = f.index(c)

        CS = []

        Ma = max(A, B, C)
        Mi = min(A, B, C)
        Ms = A + B + C - Ma - Mi

        Na = f[A]
        Nb = f[B]
        Nc = f[C]

        Sa = f[w.modmax(int((C + B)), 255)]
        Sb = f[w.modmax(int((A + C)), 255)]
        Sc = f[w.modmax(int((A + B)), 255)]

        Dc = f[w.modmax(int((C + B)), 255)]
        Da = f[w.modmax(int((A + C)), 255)]
        Db = f[w.modmax(int((A + B)), 255)]

        cS2 = Trio('#' + Na + Nb + Nc,
                   '#' + Da + Db + Dc,  # Какая - то сложная промежуточная формула
                   '#' + Sa + Sb + Sc,
                   Stair=100)
        cS_ = CCh_list_h('#' + Sa + Sb + Sc,
                         '#' + Db + Dc + Da,  # Какая - то сложная промежуточная формула
                         Repeat=100)
        CS_ = CCh_list_h('#' + Db + Dc + Da,
                        '#' + Na + Nb + Nc,  # Какая - то сложная промежуточная формула
                        Repeat=100)

        cS = cS2 + cS_ + CS_

        COLORIUM = []
        scMAX = [1, 1.4, 2, 1, 1.75, 1, 1.5, 2, 1]

        for i in cS:
            CS.append(i)
            COLORIUM.append(i)

    return COLORIUM

def CCh_list(c1,c2,Repeat=20):
    Ms = Co_Ch(c1,c2)
    #print(Ms)
    M = []
    Mf = []

    Ma = Ms[0]
    Mb = Ms[1]
    Mc = Ms[2]

    #print('--------')


    la = len(Ma)
    lb = len(Mb)
    lc = len(Mc)

    Ml = max(la,lb,lc)
    ml = min(la,lb,lc)

    Mn = []
    Mystery_and_Absolutism = la * lb * lc
    Na = int(Mystery_and_Absolutism / la)
    Nb = int(Mystery_and_Absolutism / lb)
    Nc = int(Mystery_and_Absolutism / lc)
    Mn = []
    for Mystery_Color in range(la):
        for Mystery_Number in range(Na):
            Mn.append(Ma[Mystery_Color])
    Ma = Mn
    Mn = []
    for Mystery_Color in range(lb):
        for Mystery_Number in range(Nb):
            Mn.append(Mb[Mystery_Color])
    Mb = Mn
    Mn = []
    for Mystery_Color in range(lc):
        for Mystery_Number in range(Nc):
            Mn.append(Mc[Mystery_Color])
    Mc = Mn

    Mf = []
    for i in range(Repeat):
        Given_Value = int((len(Ma)) / (Repeat) * i)
        Mf.append(Ma[Given_Value]+Mb[Given_Value]+Mc[Given_Value])
    Mf.append(Ma[-1]+Mb[-1]+Mc[-1])
    Step = 0
    Value = Mf[Step]

    return Mf
def CCh_list_h(c1,c2,Repeat=20):
    Ms = Co_Ch(c1,c2)
    #print(Ms)
    M = []
    Mf = []

    Ma = Ms[0]
    Mb = Ms[1]
    Mc = Ms[2]

    #print('--------')


    la = len(Ma)
    lb = len(Mb)
    lc = len(Mc)

    Ml = max(la,lb,lc)
    ml = min(la,lb,lc)

    Mn = []
    Mystery_and_Absolutism = la * lb * lc
    Na = int(Mystery_and_Absolutism / la)
    Nb = int(Mystery_and_Absolutism / lb)
    Nc = int(Mystery_and_Absolutism / lc)
    Mn = []
    for Mystery_Color in range(la):
        for Mystery_Number in range(Na):
            Mn.append(Ma[Mystery_Color])
    Ma = Mn
    Mn = []
    for Mystery_Color in range(lb):
        for Mystery_Number in range(Nb):
            Mn.append(Mb[Mystery_Color])
    Mb = Mn
    Mn = []
    for Mystery_Color in range(lc):
        for Mystery_Number in range(Nc):
            Mn.append(Mc[Mystery_Color])
    Mc = Mn

    Mf = []
    for i in range(Repeat):
        Given_Value = int((len(Ma)) / (Repeat) * i)
        Mf.append(f'#{Ma[Given_Value]+Mb[Given_Value]+Mc[Given_Value]}')
    Mf.append(f'#{Ma[-1]+Mb[-1]+Mc[-1]}')
    Step = 0
    Value = Mf[Step]

    return Mf
def Trio(c1,c2,c3,Stair=20):
    sp1 = CCh_list_h(c1, c2, Repeat=Stair)
    sp2 = CCh_list_h(c2, c3, Repeat=Stair)
    SP = sp1+sp2

    return SP



def Change_of_color():
    t.goto(-200,0)
    t.speed(0)
    Stair = 100
    #sp = Co_Th_SP('#8205f7', '#fc0303', Repeat=Stair)
    ts = Trio('#ebf705','#46f705','#ff00ff',Stair=Stair)
    t.pensize(25)

    for i in range(len(ts)):
        t.color('#'+ts[i])
        t.forward(20000/int(Stair**2))

    t.hideturtle()
    t.done()

def Color_Sequence_n(color,ColCh=9,Smooth=10,type=1,dark=0):
    f = Impossible_color()

    a = color[1] + color[2]
    b = color[3] + color[4]
    c = color[5] + color[6]

    A = f.index(a)
    B = f.index(b)
    C = f.index(c)

    Mn = A + B + C

    dark = Mn // 3

    Returne = Color_Sequence(color,ColCh=ColCh,Smooth=Smooth,type=1,dark=dark)
    return Returne

def Color_Sequence(color,ColCh=9,Smooth=10,type=1,dark=0):
    if type == 1:

        f = Impossible_color()
        CS = []
        sc = ['#ff0000', '#ff6600', '#ffff00', '#00ff00', '#00ffdd', '#0000ff', '#8800ff', '#ff00ff', '#ff0000'] # РаДуГа Хе - Хе :)
        COLORIUM = []
        scMAX = [1, 1.4, 2, 1, 1.75, 1, 1.5, 2, 1]

        for C in range(len(sc) - 1):
            sc[C] = Lite_or_Dark(sc[C], lux = dark)

        for C in range(len(sc)-1):
            cS = CCh_list_h(sc[C], sc[C + 1], Repeat=25)

            for i in cS:
                CS.append(i)
                COLORIUM.append(i)


        return COLORIUM [int ((int (ColCh * (len (COLORIUM) / Smooth))) % (len (COLORIUM)))]


def Lite_or_Dark(color,lux=10,Smooth=10,type=1):
    if type == 1:
        f = Impossible_color()
        l = len(f)

        a = color[1] + color[2]
        b = color[3] + color[4]
        c = color[5] + color[6]

        A = f.index(a)
        B = f.index(b)
        C = f.index(c)

        Na = A + lux
        Nb = B + lux
        Nc = C + lux

        if Na > l - 1:
            Na = l - 1
        if Nb > l - 1:
            Nb = l - 1
        if Nc > l - 1:
            Nc = l - 1

        if Na < 0:
            Na = 0
        if Nb < 0:
            Nb = 0
        if Nc < 0:
            Nc = 0

        Nf = '#' + f[Na] + f[Nb] + f[Nc]

        return Nf
    if type == 2:
        L = []
        for i in range(Smooth):
            luX = (i * lux) / Smooth
            luX = int(luX)
            L . append( Lite_or_Dark(color,lux=luX,Smooth=Smooth,type=1) )
        return L


def iUKHFDGKUHkhKkuuUyYIOouiUI():

    YGjygJYGL = Lite_or_Dark('#ff00ff',lux = -200, Smooth= 20,type=2)
    for i in YGjygJYGL:
        t.color(i)
        t.forward(10)
    t.done()
