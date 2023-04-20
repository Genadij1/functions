import random
list=[random.randint(0, 20) for i in range(10)]
list2=[random.randint(0, 20) for i in range(10)]
print(list,list2)

def scalar(list,list2):
    scalar = sum([list[i]*list2[i] for i in range(len(list))])
    return(scalar)
print(scalar(list,list2))
