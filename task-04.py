def find_max(arr):
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[mid:])

    return max(left_max, right_max)


f = open("input4.txt", "r")
g = open("output4.txt", "w")
n = int(f.readline())
alice = list(map(int, f.readline().split()))

max_value = find_max(alice)
g.write(str(max_value))

f.close()
g.close()

# the time complexity of this code is o(logn)
