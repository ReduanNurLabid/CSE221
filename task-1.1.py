#o(n^2)
import sys

f = open("input1.txt", "r")
g = open("Output1.txt", "w")

n, target = list(map(int, f.readline().split(" ")))
items = list(map(int, f.readline().split(" ")))

for i in range(n):
    for j in range(i+1, n):
        if items[i] + items[j] == target:
            g.write(str(i + 1) + " " + str(j + 1))
            sys.exit()
g.write("IMPOSSIBLE")

f.close()
g.close()
