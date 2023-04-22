n = int(input('enter num: '))
def delitel(n):
    for i in range(1,int(n/2)+1):
        if n%i == 0:
         yield i
print(list(delitel(n)))

