from operation import *

a = kali(4, 6)
b = jumlah(2, a)
c = kurang(b, 4)
print('a. 2 + 4 * 6 - 4 =', c)

d = jumlah(4, 7)
e = kurang(6, 9)
f = kali(d, e)
print('b. (4 + 7) * (6 -9) =', f)

g = jumlah(10, 2)
h = jumlah(7, 5)
i = kurang(12, 34)
j = bagi(g, h)
k = bagi(j, i)
print('c. (10 + 2) / (7 + 5) / (12 - 34) =', k)
