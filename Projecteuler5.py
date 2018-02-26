#  Kenny McTigue, 25/02/2018
#  Project Euller 5, to find the smallest real number divisible by each number from 1-20
#  https://projecteuller.net/problem=5

n = 2520 # number to be found
r = 1 # remainder

while r != 0: # loop that runs until the reminder from the for loop is equal to 0

  for i in range(10,20): # multiples of 2520 to be divided by each of the range 11 - 20, 1-10 already included. 

    r = n % i
    
    if r != 0: 
      break

  n = n + 2520 

print("The smallest real number divisible by each number from 1-20 is", n - 2520)
