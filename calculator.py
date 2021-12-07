def take_int_input(msg):
    a=input(msg)
    while type(a) != int :
        try :
            a = int(a)
            return a
        except : 
            a = input("Please give a valid input :")

Num1 = take_int_input("Please enter a number :")

Num2 = take_int_input("Please enter another number :")

print("The availabe actions are : +, -, *, / ")
Action = input("Please choose an action :")

if Action=='+' :
    R = Num1 + Num2
    print(f"The summition of the numbers is : {R}")
elif Action =='-' :
    R = Num1 - Num2
    print(f"The subtraction of the numbers is : {R}")
elif Action =='*' :
    R = Num1 * Num2
    print(f"The multiplication of the numbers is : {R}")
elif Action =='/' :
    R = Num1 / Num2 
    print(f"The quotient of the numbers is : {R}")
else :
    print("Please insert a valid action!")

input("Please press enter to exit.")