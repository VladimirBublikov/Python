import random

n = int(input("vvedin n = "))

A=[]
for i in range(n):
    A.append(int(random.random()*100))

print(A)
print("Max chislo: " + str(max(A)))

