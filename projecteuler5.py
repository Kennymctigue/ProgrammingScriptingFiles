#  Kenny McTigue, 25/02/2018
#  Project Euller 5, to find the smallest real number divisible by each number from 1-20
#  https://projecteuller.net/problem=5
#  https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution
#  https://stackoverflow.com/questions/31840761/project-euler-5-using-python?rq=1
#  http://code.jasonbhill.com/python/project-euler-problem-5/
#  https://code.mikeyaworski.com/python/project_euler/problem_5


n = 2520 # n is the number to be found starting at 2520
r = 1 # remainder of 

while r != 0: # loop that runs until the reminder from the for loop is equal to zero

  for i in range(10,20): # multiples of 2520 to be divided by each of the range 11 - 20, 1-10 already included. 

    r = n % i # n is divided by each number in the range 
    
    if r != 0: # if any of the divisions do not equal zero then break
      break

  n = n + 2520 #add the base amount to n to go back to the begining of the loop

print("The smallest real number divisible by each number from 1-20 is", n - 2520) # 


# Program as it runs in python
S C:\Users\Kenny\Documents\DataAnalytics\ProgrammingScripting\Exercises> python projecteuler5.py
The smallest real number divisible by each number from 1-20 is 232792560

