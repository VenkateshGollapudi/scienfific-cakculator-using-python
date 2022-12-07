print('SCIENTIFIC CALCULATOR')

print('THE FOLLOWING OPERATIONS YOU CAN PERFORM')
while True:
    print('''
    BASIC MATHS OPERATION

    1) ADDITION
    2) SUBTRACTION
    3) MULTIPY
    4) DIVIDE

    ADVANCE MATHS OPERATION
    5) MOD
    6) SQUARE ROOT 
    7) EXPONENT

    TRIGONOMETRY OPERATIONS
    8) SIN
    9) COS
    10) TANGENT

    CONVERSION OPERATIONS
    11) RADIAN TO DEGREE
    12) DEGREE TO RADIAN''')

    choice=int(input('Which operation do you want to perform: '))
    if choice==1:
        a=int(input('Enter first number:'))
        b=int(input('Enter second number: '))
        print('result:',a+b)
    if choice==2:
        a=int(input('Enter first number:'))
        b=int(input('Enter second number: '))
        print('result:',a-b)
    if choice==3:
        a=int(input('Enter first number:'))
        b=int(input('Enter second number: '))
        print('result:',a*b)
    if choice==4:
        a=int(input('Enter first number:'))
        b=int(input('Enter second number: '))
        print('result:',a/b)

    if choice==5:
        a=int(input('Enter first number:'))
        b=int(input('Enter second number: '))
        print('result:',a%b)

    if choice==6:
        import math
        a=int(input('Enter number: '))
        print('result:',math.sqrt(a))

    if choice==7:
        import math
        a=int(input('Enter number: '))
        b=int(input('Enter power/exponent: '))
        print('result:',math.pow(a,b))

    if choice==8:
        import math
        a=int(input('Enter number: '))
        print('result:',math.sin(a))

    if choice==9:
        import math
        a=int(input('Enter number: '))
        print('result:',math.cos(a))

    if choice==10:
        import math
        a=int(input('Enter number: '))
        print('result:',math.tan(a))

    if choice==11:
        import math
        a=int(input('Enter number in radian: '))
        print('result:',math.degrees(a))

    if choice==12:
        import math
        a=int(input('Enter number in degrees: '))
        print('result:',math.radians(a))
    cont=input('Do you want to perform more calculations???(Y/N): ')
    if cont=='Y' or cont=='y':
        continue
    else:
        break