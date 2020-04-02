import numpy as np
import math as mt

## ============ FOR =============
y = 5
t = -7.4
n = 9
print("=" * 5 + "FOR" + "=" * 5)
for j in np.arange(0.5, 8.4, 0.3):
    w = 0.6 * j + pow(mt.e, t * j) * pow((4 * y) / n, 2)
    s = (mt.sqrt(w - 0.1 * t)) / (2 + n * n)

    print("w = " + str(round(w, 2)) + ";  s = " + str(round(s, 5)))

## ============ WHILE =============
j = 0
print("=" * 4 + "WHILE" + "=" * 4)
while j < 2:
    w = 0.6 * j + pow(mt.e, t * j) * pow((4 * y) / n, 2)
    s = (mt.sqrt(w - 0.1 * t)) / (2 + n * n)
    j += 0.1

    print("w = " + str(round(w, 2)) + ";  s = " + str(round(s, 5)))

## ========= FOR & WHILE ==========

print("=" * 2 + "FOR & WHILE" + "=" * 2)
for y in np.arange(0.1, 3, 0.5):
    j = 0.1
    while j < 0.4:
        w = 0.6 * j + pow(mt.e, t * j) * pow((4 * y) / n, 2)
        s = (mt.sqrt(w - 0.1 * t)) / (2 + n * n)
        j += 0.1

        print("w = " + str(round(w, 2)) + ";  s = " + str(round(s, 5)))