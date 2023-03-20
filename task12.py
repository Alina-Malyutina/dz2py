sum = int(input('Enter the sum of numbers: '))
multi = int(input('Enter the product of numbers: '))
num1 = 0
num2 = 0
D = sum**2 - 4*multi
if D < 0:
    print ("There is no answer")
elif D == 0:
    num1 = sum / 2
    num2 = num1
    print(round(num1, 2), round(num2, 2))
elif D>0:
    num1 = (sum + D**0.5) / 2
    num2 = (sum - D**0.5) / 2
    print(round(num1, 2), round(num2, 2))
else:
    print('Something is uncorrect!')
