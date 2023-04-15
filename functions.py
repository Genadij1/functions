
def fibonachi(f):
    if f == 0:
        return 0
    elif f == 1:
        return 1
    else:
        return fibonachi(f-1) + fibonachi(f-2)  
f = int(input('enter '))
print(fibonachi(f))