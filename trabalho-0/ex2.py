from random import random

#a)
print()
print('--------a--------')

number =  int(random() * 10)
print(number)
print('guess a number from 0 to 10')
while True:
    guess = int(input())
    if guess > number:
        print('The number is smaller')
    elif guess < number:
        print('The number is bigger')
    else:
        break
        
for i in range(10):
    if i%2 == 1:
        continue
    print(i)
    
#b)
print()
print('--------b--------')

def foo(p1):
    print(p1)
    return 42

print(foo('argument'))


#c)
print()
print('--------c--------')

if __name__ == '__main__':
    print('run')
else:
    print('Imported')

