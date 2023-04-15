
def avarege(numbers):
    return sum(numbers)/len(numbers)
numbers=[]
nums = int(input('length:'))
while len(numbers)<nums:
        numbers.append(int(input('number:')))
print(avarege(numbers)) 
  

