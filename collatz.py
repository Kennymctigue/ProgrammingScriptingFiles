# kenny mctigue, 08/02/2018
# collatz conjecture task wk3
# https://study.com/academy/lesson/history-of-the-collatz-conjecture.html
# https://stackoverflow.com/questions/13366830/collatz-conjecture-sequence

n = int(input("Enter any integer number:")) #Allows the user of the program to enter the integer they choose


while n > 1: #continue loop until the input number is reduced to 1
    if (n % 2 == 0): # if the integer can be dived by two evenly
        n = n / 2 #divide the number by 2
    else:
        n = (n * 3)+1 #multiply the number by 3 and add 1
    print (n) #print the eventual value of n
    
    
   # program when run in python with a starting value of 17
PS C:\Users\Kenny\Documents\DataAnalytics\ProgrammingScripting\Exercises> python collatz.py
Enter any integer number:17
52
26.0
13.0
40.0
20.0
10.0
5.0
16.0
8.0
4.0
2.0
1.0


