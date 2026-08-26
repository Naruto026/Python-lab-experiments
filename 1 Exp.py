### 1 Exp  Develop a python program to read 2 numbers from the key board and perform the basic arithmetic 
       ### operations based on the choice. (1-Add, 2-Subtract, 3-Multiply, 4-Divide).##
def inputs():
    print("Enter two numbers:")
    num1 = int(input("Enter number 1:"))
    num2 = int(input("Enter number 2:"))
    print("Enter Number for Operation:")
    print("1 for Addtion")
    print("2 for Subtract")
    print("3 for Multiply")
    print("4 for Divide")
    oper=input("Enter operation:")
    return num1, num2, oper
num1, num2, oper = inputs()

def calculations(num1, num2, oper):

    match oper:
        case '1':
            print("Addition of two numbers is:", num1 + num2)
        case '2':
            print("Subtraction of two numbers is:", num1 - num2)
        case '3':
            print("Multiplication of two numbers is:", num1 * num2)
        case '4':
             if num2 == 0:
                print("Error: Division by zero is not allowed.") 
             else:
                 print("Division of two numbers is:", num1 / num2)
        case _:
            print("Invalid operation. Please try again.")
        # for wrong input
calculations(num1,num2,oper)


