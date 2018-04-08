# Programming Scripting Files

Repository for all exercise files related to Programming and Scripting Module of Data Analytics H.Dip

## Notes on each of the exercises

### Exercises 1 and 2 (Combined) - Fibonacci
This exercise is located in the fib.py file in the ProgrammingScriptingFiles repository
#### Summary of the exercises
This task was first to write a program in Python that would deliver the nth fibonacci number. 

According to [Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number), "In mathematics, the Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence, and characterized by the fact that every number after the first two is the sum of the two preceding ones"

The first exercise was to define a function that would deliver the nth fibonacci and to test it by asigning numeric values to the first and last letters of the programmer's name. A=1, B=2 etc. This programmer's name is Kenny so the numbers were 11 and 25 making 36.

The second exercise was to add another layer to the program by establishing the Unicode decimal number values to the first and last letters of the programmers surname.  This was done by using the ord() method function. The ord() method returns an integer representing Unicode code point for the given Unicode character. [Unicode is a computing industry standard for the consistent encoding, representation, and handling of text expressed in most of the world's writing systems](https://en.wikipedia.org/wiki/Unicode). A table showing the different number values for each latin letter type can be seen [here](https://unicodelookup.com/)


### Exercise 3 - Collatz Conjecture
This exercise is located in the collatz.py file in the ProgrammingScriptingFiles repository

This exercise was to write a program that would demonstrate the collatz conjecture. The Collatz conjecture is a mathematical sequence that always arrives at 1.  It is run as follows:  Take any positive integer,n.  Two rules are then to be followed.  If the number is evenly divisible by 2, then divide by two, otherwise multiply by 3 and add 1.  Keep repeating whichever of these actions is appropriate to your answer and one will eventually arrive at 1.  Some history of the Collatz conjecture is [here](https://study.com/academy/lesson/history-of-the-collatz-conjecture.html)

To write the program I used a "while" loop stating for the loop to continue until input number was reduced to 1 and included the two rules as stated above within the loop.  I also included an input option for the user of the program to enter the integer of their choice.  [Stackoverflow](https://stackoverflow.com/questions/13366830/collatz-conjecture-sequence) was a useful reference in writing this program

### Exercise 4 - Project Euler Problem Number 5
This exercise is located in the file projecteuler5.py in the ProgrammingScriptingFiles repository

Project Euler is a set of over 600 problems named after [Leonard Euler](https://en.wikipedia.org/wiki/Leonhard_Euler).  They are designed to test the ability of programmers and encourage logical and creative thought in programming.  From the Project Euler website ["Project Euler exists to encourage, challenge, and develop the skills and enjoyment of anyone with an interest in the fascinating world of mathematics."](https://projecteuler.net/)

For this task we were to attempt to solve problem [number 5](https://projecteuller.net/problem=5) using a "for" loop. For this exercise I consulted a number of online resources which I have listed in the file along with drawing from the lectures and the python tutorial.  After numerous failures I eventually got a solution, based on parts from these resources that worked but took a long time to run.  I took this framework as my base and made small changes piecemeal until I had something that ran faster. This was the most challenging of all the exercises we were tasked with.

### Exercise 5 - Openfile - Iris
This exercise is located in the file openfile.py in the ProgrammingScriptingFiles repository

The task in this exercise was to display the first four columns of the [Iris Data set](https://en.wikipedia.org/wiki/Iris_flower_data_set) in presentable format.

For this task I again used a combination of the lectures,the python tutorial and [stackoverflow](https://stackoverflow.com/questions/8234445/python-format-output-string-right-alignment). The Iris data set was downloaded and stored on the local drive. Before I opened it with the program I manually set to print the four headings as I couldn't figure a way to include them as part of the program and still get the alignment correct.  Then I opened the data file in the program using "with" and "open" and commanded to print the first four columns aligned to the right to line up with the manually entered headings.  Using line split I could identify the columns I required.  I couldn't align them as per the lectures so I researched ways and came up the solution as per the program.

### Exercise 6 - Factorial
This exercise is located in the file factorial.py in the ProgrammingScriptingFiles repository

The [Factorial](https://en.wikipedia.org/wiki/Factorial) of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5! = 5*4*3*2*1 = 120

This task was to write a program in python that would calculate the factorial of any given non-negative integer.  After a few failed attempts at writing a program that started at one and looped towards the number to find the factorial of, I changed and came from the angle of starting with the number and looping back to 1 as the answer increased to deliver the factorial at the end.  Again parts from the lectures, the python tutorial and [stackoverflow](https://stackoverflow.com/questions/5136447/function-for-factorial-in-python) were combined to find a solution.

## Note on the above exercises
Apart from the technical learning involved in the above exercises, what I have learned in completing this summary is the importance of documenting resources and thought processes as you write programs.  There are many references that I have not included as I failed to note them as I wrote the programs.  Likewise, there are many reasonings and logical thought processes that ought to be included as to say "it made sense to me at the time" is not sufficient, especially in the context of working on a team project. Lesson learned.


