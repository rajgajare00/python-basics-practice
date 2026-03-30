# my python journey day-1
# Raj Gajare | Prime2.0

# simple Calculator function using match case statement
def calculator(num1, num2, operator):
    match operator:
        case '+':
            return num1+num2
        case '-':
            return num1-num2
        case '*':
            return num1* num2
        case '/':
            return num1/num2
        case _:
            return "Invalid Operator"
        
# taking user input
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
operator=input("Enter Operator (+, -, *, /):")

# calling calculator function and printing result
result=calculator(num1, num2, operator)
print("The result of",num1,operator,num2," is:",result)