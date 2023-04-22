import random
list = [random.randint(0,10) for i in range(20)]
print(list)
def most_common_number(list):
    counts = {}
    for num in list:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return max(counts, key=lambda x: (counts[x], -x))
print(most_common_number(list))


