import itertools

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

##################################################################

n = str(input("Vvedi n = "))

for i in range(2,int(n)):
    A = list(itertools.permutations(list(str(i)))) ##spisok vozm perestanovok

    f = True
    for j in range(len(A[0])): ## perebiraem
        k = ''.join(A[j])
        f = f and IsPrime(int(k))
    if f:
        print("chislo " + str(i) + " overprostoe")