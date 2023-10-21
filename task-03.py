def merge(a, b):
    merged_list = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged_list.append(a[i])
            i += 1
        else:
            merged_list.append(b[j])
            j += 1

    merged_list += a[i:]
    merged_list += b[j:]

    return merged_list


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)


f = open("input3.txt", "r")
g = open("output3.txt", "w")

n = int(f.readline())
arr = list(map(int, f.readline().split(" ")))
result = mergeSort(arr)

for i in result:
    g.write(str(i)+" ")

f.close()
g.close()
