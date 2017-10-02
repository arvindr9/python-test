import numpy as np

f = open('text.in')
out = open('text.out', 'w')
for line in f:
    arr = line.split(" ")
    arr = list(map(int, arr))
    arrN = np.asarray(arr)
    out.write(str(np.sum(arrN))+ "\n")





