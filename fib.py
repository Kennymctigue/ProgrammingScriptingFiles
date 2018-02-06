Week 1 Exersize

# Ian McLoughlin
# A program that displays Fibonacci numbers.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 36
ans = fib(x)
print("Fibonacci number", x, "is", ans)


My name is Kenny so k=11 + Y=25 = 36
Fibonacci number 14,930,352

Week 2 Task
# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "McTigue"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

My surname is McTigue

The first letter M is number 77

The last letter e is number 101

Fibonacci number 178 is 7084593923980518516849609894969925639



The ord() command well generate a numerical value for an unicode character based on the characters position on the unicode list.
