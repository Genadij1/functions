import random
list = [random.randint(1, 10) for i in range(10)]
def get_unique_number(list):
    unique = []
    for i in list:
        if i not in unique:
            unique.append(i)
    return unique
print(list)
print(get_unique_number(list))
