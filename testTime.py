import timeit

lst = [0, 1, 0, 2, 0, 3, 0, 1, 2, 5, 6, 1, 4, 1]

t1 = timeit.Timer("list(filter(lambda i: i!=1, lst))", "from __main__ import lst")
t2 = timeit.Timer("filter(lambda i: i!=1, lst)", "from __main__ import lst")
t3 = timeit.Timer("while 1 in lst: lst.remove(1)", "from __main__ import lst")
t4 = timeit.Timer("[x for x in lst if x!=1]", "from __main__ import lst")

print("list -> filter -> lambda   | " + str(t1.timeit()))
print("filter -> lambda           | " + str(t2.timeit()))
print("while 1 in lst             | " + str(t3.timeit()))
print("[x for x in lst if x!=1]   | " + str(t4.timeit()))
