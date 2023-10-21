# time_complexity 0(nlogn)
def merge(left, right):
    merged_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    merged_list += left[i:]
    merged_list += right[j:]

    return merged_list


def mergesort(arr):
    if len(arr) < 2:
        return arr
    mid = int(len(arr) / 2)
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


f = open("input2.txt", "r")
g = open("output2.01.txt", "w")

n = int(f.readline())
alice = list(map(int, f.readline().split()))

m = int(f.readline())
bob = list(map(int, f.readline().split()))
lis = alice + bob

sorted_list = mergesort(lis)

for item in sorted_list:
    g.write(str(item) + " ")

f.close()
g.close()
