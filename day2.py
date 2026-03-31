# my python journey day-2
# Raj Gajare | Prime2.0
# function to calculate factorial of n
def factorial(n):
    if(n==0 or n==1):
        return 1
    else :
        return factorial(n-1)*n
    
# taking user input
num=int(input("Enter Number to calculate Its Factorial: "))
result=factorial(num)
print("The Factorial of",num,"is:",result)