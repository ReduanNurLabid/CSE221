def target_sum(arr, t):
    seen = {}
    for i in range(len(arr)):
        num = arr[i]
        complement = t - num
        if num in seen:
            return seen[num]+1, i+1
        else:
            seen[complement] = i
    return -1


f = open("input1.txt", "r")
g = open("output1.2.txt", "w")

n, target = list(map(int, f.readline().split(" ")))
items = list(map(int, f.readline().split(" ")))

index = target_sum(items, target)
if index == -1:
    g.write("IMPOSSIBLE")
else:
    g.write(str(index[0]) + " " + str(index[1]))
f.close()
g.close()
