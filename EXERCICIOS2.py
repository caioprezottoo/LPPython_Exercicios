'''
1.
num = int(input('Number: '))

if num % 2 == 0:
    print(f'{num} is an even number.')
else:
    print(f'{num} is an odd number.')
'''

'''
2.
num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))

if num1 > num2:
    print(f'{num1} is greater than {num2}.')
elif num1 < num2:
    print(f'{num2} is greater than {num1}.')
else:
    print(f'{num1} and {num2} are equal.')
'''

'''
3.
age = int(input('Age: '))

if age < 18:
    print('You are a minor')
elif age >= 18 and age <= 59:
    print('You are an adult')
else:
    print('You are an elder')
'''

'''
4.
examScore1 = float(input('1st Exam Score: '))
examScore2 = float(input('2nd Exam Score: '))

average = (examScore1 + examScore2) / 2


if average >= 7:
    print('Approved')
elif average >= 5 and average < 7:
    print('Retake Test')
else:
    print('Failed')
'''

'''
5.
def verifyValidTriangle(num1, num2, num3):
    if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
        return True
    else:
        return False

num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))
num3 = int(input('Number 3: '))

if verifyValidTriangle(num1, num2, num3):
    print('Valid Triangle')
else:
    print('Invalid Triangle')
'''