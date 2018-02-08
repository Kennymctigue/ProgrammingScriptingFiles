# kenny mctigue 08/02/2018
# collatz conjecture task wk3

n = int(input("Enter any integer number:"))


while n > 1:
    if (n % 2 == 0):
        n = n / 2
    else:
        n = (n * 3)+1
    print (n)

