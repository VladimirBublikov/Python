## заполняем матрицу нулями с дополнением промежуточных индексов для линий
def fillMtrx(M):
    for i in range(len(M[0])):
        M[0][i] = "■"           ##chr(18)
        M[len(M)-1][i] = "■"    ##chr(18)
    for i in range(1, len(M) - 1):
        M[i][0] = "■"           ##chr(18)
        M[i][len(M[i])-1] = "■" ##chr(18)


## Выводим матрицу красиво для глаз
def wrtMtrx(M):
    for i in range(len(M)):
        s = ""
        for j in range(len(M[0])):
            if str(M[i][j]) == "0":
                s += " " * 3
            else:
                s += str(M[i][j]) + " " * 2
        print(s)


def fillY(M, x, d): ## заполняем по Y
    for i in range(d*2-1):
        M[1+i][x*2] = "□"

def fillX(M, x, d): ## заполняем по X
    for i in range(d*2-1):
        M[x*2][1+i] = "□"


## Рекурсия для определения делений
def kvadrat(a, b, M):
    if a != b:
        if a < b:
            fillY(M, b - a, a)
            return kvadrat(a, b - a, M) + 1
        else:
            fillX(M, a - b, b)
            return kvadrat(a - b, b, M) + 1

        ##print("{ " + str(a-b) + "; " + str(b) + " }")
    else:
        return 0


## MAIN

a = int(input("Vvedi a = "))
b = int(input("Vvedi b = "))

M = [[0] * (b * 2 + 1) for i in range(a * 2 + 1)]
fillMtrx(M)

k = kvadrat(a, b, M)

wrtMtrx(M)

print("kol-vo delenii = " + str(k))
