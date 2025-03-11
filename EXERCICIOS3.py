'''
1.
number = int(input('Number: '))

if number <= 0:
    print('Number must be positive')
for i in range(1, number+1):
    print(i)
'''

'''
2. 
def getNumber():
    return int(input('Number: '))

def identifyNegativeNumber():
    number = getNumber()
    total = 0

    while number >= 0:
        total += number
        number = getNumber()
    else:
        print(f'Total: {total}')

identifyNegativeNumber()
'''
'''
3.
number = int(input('Number between 1 and 10: '))
k=1

for i in range(10):
    print(f'{number} times {k} is {number*k}')
    k += 1
'''

'''
4.
a = int(input('Start of interval: '))
b = int(input('End of interval: '))

for i in range(a,b+1):
    if i % 2 != 0:
        print(i)
'''

'''
5.
number = int(input('Number of fibonacci sequence terms you would like to show: '))

n, k = 0, 1

for i in range(number):
    print(n, end=" ")
    n, k = k, n + k
'''