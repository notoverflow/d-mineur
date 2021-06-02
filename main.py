from random import *
from time import *
from tkinter import *
from functools import partial


def Int_jeu(n, m, difficulte):
    nbrminne = 0
    T = []
    for i in range(n):
        temp = []
        for j in range(m):
            if random() < difficulte:
                temp.append(2)
                nbrminne += 1
            else:
                temp.append(0)

        T.append(temp)

    return T, nbrminne


def mines_autour(T):
    # création de la liste de mêdme taille que T
    M = []

    ligne = len(T)
    colone = len(T[0])
    for i in range(ligne):
        temp = []

        for j in range(colone):
            temp.append(0)
        M.append(temp)

    # pour les coins
    M[0][0] = int((T[0][1] + T[1][1] + T[1][0]) / 2)
    M[0][colone - 1] = int((T[0][colone - 2] + T[1][colone - 2] + T[1][colone - 1]) / 2)
    M[ligne - 1][0] = int((T[ligne - 2][0] + T[ligne - 2][1] + T[ligne - 1][1]) / 2)
    M[ligne - 1][colone - 1] = int((T[ligne - 1][colone - 2] + T[ligne - 2][colone - 2] + T[ligne - 2][colone - 1]) / 2)
    # colone
    for col in range(1, colone - 1):
        M[0][col] = int((T[0][col - 1] + T[1][col - 1] + T[1][col] + T[1][col + 1] + T[0][col + 1]) / 2)
        M[ligne - 1][col] = int((T[ligne - 1][col - 1] + T[ligne - 2][col - 1] + T[ligne - 2][col] + T[ligne - 2][
            col + 1] + T[ligne - 1][col + 1]) / 2)
    # lignes
    for lin in range(1, ligne - 1):
        M[lin][0] = int((T[lin + 1][0] + T[lin + 1][1] + T[lin][1] + T[lin - 1][1] + T[lin - 1][0]) / 2)
        M[lin][colone - 1] = int((T[lin + 1][colone - 1] + T[lin + 1][colone - 2] + T[lin][colone - 2] + T[lin - 1][
            colone - 2] + T[lin - 1][colone - 1]) / 2)

    # mileuuuuuu
    for c in range(1, colone - 1):
        for l in range(1, ligne - 1):
            M[l][c] = int((T[l - 1][c - 1] + T[l - 1][c] + T[l - 1][c + 1] + T[l + 1][c - 1] + T[l + 1][c] + T[l + 1][
                c + 1] + T[l][c - 1] + T[l][c + 1]) / 2)

    return M

def afficher(mat):
    print(" ")
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], "", end='')
        print(" ")
    print(" ")


def poser_drapeau(T, i, j):
    if T[i][j] == 2:
        T[i][j] = 4
    elif T[i][j] == 0:
        T[i][j] = 3


def lever_drapeau(T, i, j):
    if T[i][j] == 4:
        T[i][j] = 2
    elif T[i][j] == 3:
        T[i][j] = 0


def creuser(T, M, i, j, N, a):
    if i >= len(T) or j >= len(T[0]) or i < 0 or j < 0:
        return 0, N
    if T[i][j] == 4 or T[i][j] == 3:
        return 1, N
    if T[i][j] == 1:
        return 2, N
    if T[i][j] == 0:
        return recu_creuser(T, M, i, j, N, a)
    if T[i][j] == 2:
        return 4, N


# 0 la case n'existe pas
# 1 il y a un drapeau
# 2 la case est dejà creuser
# 3 True
# 4 False

def recu_creuser(T, M, i, j, N, a):
    global canvas
    if i >= len(T) or j >= len(T[0]) or i < 0 or j < 0:
        return 0, N
    elif T[i][j] == 4 or T[i][j] == 3:
        return 1, N
    elif T[i][j] == 1:
        return 2, N
    else:
        T[i][j] = 1
        if M[i][j] == 0:
            a.itemconfig(L[i][j], text="", fill='#000000')
        else:
            a.itemconfig(L[i][j], text=M[i][j], fill='#000000')
        N += 1
        if M[i][j] == 0:
            t, N = recu_creuser(T, M, i - 1, j - 1, N, a)
            t, N = recu_creuser(T, M, i - 1, j, N, a)
            t, N = recu_creuser(T, M, i - 1, j + 1, N, a)
            t, N = recu_creuser(T, M, i, j + 1, N, a)
            t, N = recu_creuser(T, M, i + 1, j + 1, N, a)
            t, N = recu_creuser(T, M, i + 1, j, N, a)
            t, N = recu_creuser(T, M, i + 1, j - 1, N, a)
            t, N = recu_creuser(T, M, i, j - 1, N, a)
    print(N)
    return 3, N


''''''''''''''''''''''''
'''gestion graphique '''
''''''''''''''''''''''''


def souris(a, L, event):
    global MC
    global N
    xb = str(event.x)
    yb = str(event.y)
    j = int(xb) // cell_size
    i = int(yb) // cell_size
    # if MC:
    #
    #     if T[i][j] == 3 or T[i][j] == 4:
    #         print("on fait rien car drapeau")
    #     elif T[i][j] == 2:
    #
    #         print(" ppp")
    #     else:
    #         creuser(T, M, i, j, N)
    #         print("heheheh")
    # else:
    #     a.itemconfig(L[i][j], text='d')
    #
    #     print("Case ", i, ",", j, "Appuyé en mode drapeau")
    # a.pack()
    if MC:

        if T[i][j] == 3 or T[i][j] == 4:
            print("on fait rien car drapeau")
        elif T[i][j] == 2:

            label_title = Label(windows, text="PERDU!", font=(100))
            canvas.destroy()
            label_title.pack()

            print(" ppp")
        else:
            if T[i][j] == 1:
                print("dejà creusé")
            else:
                p, N = creuser(T, M, i, j, N, a)
                print("heheheh")
    else:
        if T[i][j] == 3 or T[i][j] == 4:
            lever_drapeau(T, i, j)
            a.itemconfig(L[i][j], text='?')
        elif T[i][j] == 0 or T[i][j] == 2:

            poser_drapeau(T, i, j)
            a.itemconfig(L[i][j], text='d')

    a.pack()
    if N == n * m - nbrminnes:
        label_title = Label(windows, text="GAGNE!", font=(100), fg='blue')
        canvas.destroy()
        label_title.pack()


def changer_mode(B):
    global MC
    if MC:
        B.configure(text="mode drapeau")
        MC = False
    else:
        B.configure(text="mode creuser")
        MC = True


def decompose(t):
    h = int(t) // 3600
    m = (int(t) % 3600) // 60
    s = int(t) % 60
    return h, m, s


def tick():
    global time1
    time2 = time()
    h, m, s = decompose(time2 - time1)
    D = str(h) + ":" + str(m) + ":" + str(s)
    clock.config(text=D)
    clock.after(200, tick)


''''''''''''''''''''''''
'''programme principal'''
''''''''''''''''''''''''

N = 0
n = input("combien de ligne : ")
m = input("combien de colone : ")

try:
    val = int(n)

except ValueError:
    print("les valeur sont pas corect ")
    sys.exit()

try:
    val = int(m)

except ValueError:
    print("les valeur sont pas corect ")
    sys.exit()
n = int(n)
m = int(m)

if n <= 1 or m <= 1:
    print("les valeur sont pas corect ")
    sys.exit()

complex = float(input("pourcentage de complexité : "))
T, nbrminnes = Int_jeu(n, m, complex)

M = mines_autour(T)

afficher(T)
afficher(M)

cell_size = 40
np = n * cell_size
mp = m * cell_size
MC = True

windows = Tk()
canvas = Canvas(windows, width=mp, height=np, background='#AFDAF7')
windows.title("El demineur de Notoverflow")

windows.minsize(np, mp)

y = 0
for i in range(n):
    canvas.create_line(0, y, mp, y)
    y += cell_size
x = 0
for i in range(m):
    canvas.create_line(x, 0, x, np)
    x += cell_size
L = []
for i in range(n):
    L.append([])
    for j in range(m):
        txt = canvas.create_text(j * cell_size + (cell_size // 2), i * cell_size + (cell_size // 2),
                                 text="?", font="Arial 12 italic", fill="blue")
        L[i].append(txt)

canvas.focus_set()
canvas.bind("<Button-1>", partial(souris, canvas, L))
canvas.pack()

B = Button(windows, text='mode creuser')
B.configure(command=partial(changer_mode, B))
B.pack(side=LEFT, padx=5, pady=5)

Button(windows, text='Quitter', command=windows.destroy).pack(side=RIGHT, padx=5, pady=5)

time1 = time()
clock = Label(windows, font=('times', 20, 'bold'), bg='#2C3E50')
clock.pack(side=LEFT, padx=20, pady=5)

tick()
windows.mainloop()
#
# while N<(n*m-nbrminnes):
#
#     afficher(T)
#     afficher(M)
#     faire=input("que voulez vouis faire : (d poser un drapeau, dl lever un drapeau, c creuser  ) : ")
#     i=int(input("ligne ? "))
#     j=int(input("cologne  ?"))
#
#     if faire=="d":
#         poser_drapeau(T,i,j)
#     elif faire=="dl":
#         lever_drapeau(T,i,j)
#     elif faire=="c":
#
#         if creuser(T,M,i,j,N) ==2:
#             print("vous avez toucher une minnes perdu ")
#             sys.exit()
#             break
#         else: creuser(T,M,i,j,N)
#
#     afficher(T)
