def calci():
    print('Welcome to CALCULATOR PRIME.')
    print('+ for addition, - for subtraction, * for multiply, / for divide, ** for power')
    oper = input('Please enter the operation you to perform: ')

    num1 = int(input('Enter your first no: '))
    num2 = int(input('Enter your second no: '))

    if oper =='+':
        print(num1 + num2)
    elif oper =='-':
        print(num1 - num2)
    elif oper =='*':
        print(num1 * num2)
    elif oper == '/':
        print(num1 / num2)
    elif oper == '**':
        print(num1 ** num2)
    else:
        print('operator not supported')
    again()

def again():
    calci_again = input('Do you want to use calulator prime again ?(Type y for yes and n for no): ').lower()

    if calci_again == 'y':
        calci()
    elif calci_again == 'n':
        print('See you later')
    else:
        again()

calci()
