n = str(input("input 4x znachnoe n = "))

A=list(n)

f=False or (A.count(A[0])>1) or (A.count(A[1])>1) or (A.count(A[2])>1) or (A.count(A[3])>1)

print("Vse ego cifri razlichni = " + str(not f))

