# Kenny McTigue, 21/03/2018 
# Exersise 6, factorial function
# Definition of Factorial:  is the product of all positive integers less than or equal to the number being calulated the factorial of.
# https://stackoverflow.com/questions/5136447/function-for-factorial-in-python

n = int(input("Enter the number to which you require the factorial of: "))

def factorial(n): # n being the number to find the factorial of
    num = 1  # this will be the answer at the end of all calculations
    while n >= 1: 
        num = num * n # this starts with num equal to 1 and increases as it is multiplied by n in each cycle of the loop until n is equal to 1 and num is the factorial
        n = n - 1 #to reduce n by 1 to continue the loop until n = 1
    return num


print (factorial(n))

Program as it run in python tested with the integers 5, 7 and 10

PS C:\Users\Kenny\Documents\DataAnalytics\ProgrammingScripting\Exercises> python factorial.py
Enter the number to which you require the factorial of: 5
120
PS C:\Users\Kenny\Documents\DataAnalytics\ProgrammingScripting\Exercises> python factorial.py
Enter the number to which you require the factorial of: 7
5040
PS C:\Users\Kenny\Documents\DataAnalytics\ProgrammingScripting\Exercises> python factorial.py
Enter the number to which you require the factorial of: 10
3628800
