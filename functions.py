n = input('Enter name: ')
a = int(input('Enter age: '))
n1 = input('Enter name: ')
a1 = int(input('Enter age: '))
n2 = input('Enter name: ')
a2 = int(input('Enter age: '))
list = [(n,a),(n1,a1),(n2,a2)]
def sort_age(list):
    list.sort(key=lambda x: x[1])
    return(list)
print(sort_age(list))


 
