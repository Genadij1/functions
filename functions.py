
import string

def count_volves(string):
    volves = 'aeiouy'
    count_volves = 0
    for letter in string:
        if letter in volves:
            count_volves += 1
    return count_volves 
def count_consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxz'
    count_consonants = 0
    for letter in string:
        if letter in consonants:
            count_consonants += 1   
    return count_consonants
string = str(input('enter text'))
print('count_volves: ',count_volves(string))
print('count_consonants: ',count_consonants(string))


