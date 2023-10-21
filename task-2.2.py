# time_complexity o(n)
def merge_sorted_lists(list1, list2):
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list += list1[i:]
    merged_list += list2[j:]

    return merged_list


f = open("input2.txt", "r")
g = open("output2.2.txt", "w")

n = int(f.readline())
alice = list(map(int, f.readline().split()))

m = int(f.readline())
bob = list(map(int, f.readline().split()))

sorted_list = merge_sorted_lists(alice, bob)

for item in sorted_list:
    g.write(str(item)+" ")

f.close()
g.close()
