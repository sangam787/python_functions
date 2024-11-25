
"Note: For each theory Question, give at least one example." 
"Que1. What is the difference between a function and a method in Python?" 
"""
Answer-1
Functions:-

1-Function is block of code that is also called by its name. (independent)
2-The function can have different parameters or may not have any at all. 
If any data (parameters) are passed, they are passed explicitly.
3-It may or may not return any data.
4-Function does not deal with Class and its instance concept.
for example
"""
# def Subtract (a, b):
# 	return (a-b)

# print( Subtract(10, 12) ) # prints -2

# print( Subtract(15, 6) ) # prints 9

"""
Python Method

Method is called by its name, but it is associated to an object (dependent).
A method definition always includes 'self' as its first parameter.
A method is implicitly passed to the object on which it is invoked.
It may or may not return any data.
A method can operate on the data (instance variables) that is contained by the corresponding class
"""
# Python 3 User-Defined Method
# class ABC :
# 	def method_abc (self):
# 		print("I am in method_abc of ABC class. ")

# class_ref = ABC() # object of ABC class
# class_ref.method_abc()



"Que2. Explain the concept of function arguments and parameters in Python." 

"Answer-2"
"Parameters are the variables listed inside the parentheses in the function definition."
"for example"
# Here a,b are the parameters
# def sum(a,b):
#   print(a+b)
  
# sum(1,2)

"Arguments are the values passed to the function when it is called."
"for example"
# def sum(a,b):
#   print(a+b)
  
# # Here the values 1,2 are arguments
# sum(1,2)


"Que-3. What are the different ways to define and call a function in Python?" 
"""
Python def keyword is used to define a function, 
it is placed before a function name that is provided by the user to create 
a user-defined function. In Python, a function is a logical unit of code 
containing a sequence of statements indented under a name given using 
the “def” keyword. In Python def keyword is the most used keyword.
       def funtion_name(parameters):
            statement
            return expression 

for example
"""
# A simple Python function
# def fun():
#     print("Welcome to 'PW Skills'")
"""
Calling a Function in Python
After creating a function in Python we can call it 
by using the name of the functions Python followed by 
parenthesis containing parameters of that particular function. 
Below is the example for calling def function Python.
for example
"""
# A simple Python function
# def fun():
#     print("Welcome to 'PW Skills'")
# fun()





"""
Que-4. What is the purpose of the 'return' statement in a Python function?

Return Statement in Python Function
The function return statement is used to exit from a function and go back to 
the function caller and return the specified value or data item to the caller.
The return statement can consist of a variable, an expression, or a constant which 
is returned at the end of the function execution. If none of the above is present 
with the return statement a None object is returned.
for example
# """
# def addnum(*a):
#     """This function returns the sum
#     value of the entered number"""
#     return sum(a)
# print(addnum(1,2,3,4,5))


"Que-5. What are iterators in Python and how do they differ from iterables?"
"""
'Iterable' is an object, that one can iterate over. It generates an Iterator when passed to iter() method. 
An 'iterator' is an object, which is used to iterate over an iterable object using the __next__() method. 
Iterators have the __next__() method, which returns the next item of the object.

'Every iterator is also an iterable, but not every iterable is an iterator in Python.'
For example, a list is iterable but a list is not an iterator. 
An iterator can be created from an iterable by using the function iter().  
for examples:-
"""
# strA = "sangam"
# print(next(strA))  # it will give an error that 'str' obj is not an iterator
# strA = "sangam"
# itr = iter(strA)   # if we use iter()method 
# print(itr)         # now object become iterator if iterable.
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))


"""
Que-6. Explain the concept of generators in Python and how they are defined."
A Generator in Python is a function that returns an iterator using the Yield keyword.

A generator function in Python is defined like a normal function, but whenever it needs 
to generate a value, it does so with the yield keyword rather than return. If the body 
of a def contains yield, the function automatically becomes a Python generator function. 

we define a generators by using two keywords 'def' and 'yield'
for example
"""
# def simpleGeneratorFun():
#     yield "PW"
#     yield "Skills"
#     yield "course"

# for x in simpleGeneratorFun():
#     print(x)



"""
Que-7. What are the advantages of using generators over regular functions? 

Generators differ from standard functions in that they allow us to iterate 
through a sequence of values over time, instead of computing and returning a single result.


Standard Functions: Compute a value and return it once. They use the return statement.
"""
# def standard_function():
#     return [1, 2, 3]
# print(standard_function())
"""
Generators: Use the yield statement to return values one at a time, allowing iteration 
over a sequence of values without storing the entire sequence in memory.
"""
# def generator_function():
#     yield 1
#     yield 2
#     yield 3
# for x in generator_function():
#     print(x)


"""
Que-8. What is a lambda function in Python and when is it typically used? 

Python Lambda Functions are anonymous functions means that the function is without a name. 
As we already know the def keyword is used to define a normal function in Python. Similarly, 
the lambda keyword is used to define an anonymous function in Python.

Lambda funtion typically used for performing short operations/data manipulations or 
reduce the readability of code. 
for example
"""
# x = "sangam"
# upper = lambda a:a.upper()
# print(upper(x))


"""
Que-9. Explain the purpose and usage of the 'map() function in Python.

The map() function is used to apply a given function to every item of an iterable, 
such as a list or tuple, and returns a map object (which is an iterator).
"""
# s = ['1', '2', '3', '4']
# res = map(int, s)
# print(list(res))

"""
Que-10. What is the difference between `map()`, `reduce()`, and `filter() functions in Python? 

'map()'
The map() function is used to apply a given function to every item of an iterable, 
such as a list or tuple, and returns a map object (which is an iterator).
"""
# s = ['1', '2', '3', '4']
# res = map(int, s)
# print(list(res))


"""
'filter()'
The filter() method filters the given sequence with the help of a 
function that tests each element in the sequence to be true or not.

Python filter() Syntax
filter(function, sequence)
function: function that tests if each element of a sequence is true or not.
sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.
for example
"""
# def fun(variables):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if variables in letters:
#         return True
#     else:
#         return False

# sequence = ['e', 'g', 'h', 'o', 'p', 'r', 'w', 'a']
# filtrd = filter(fun,sequence)
# print('THE FILTERED LETTERS ARE:')
# for s in filtrd:
#     print(s)

"""
'reduce()'
The reduce(fun,seq) function is used to apply a particular function passed in its 
argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.
for example
"""
# python code to demonstrate working of reduce()

# # importing functools for reduce()
# import functools

# # initializing list
# lis = [1, 3, 5, 6, 2]

# # using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a, b: a+b, lis))

# # using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))


"""
11. Using pen & Paper write the internal mechanism for sum operation using 
reduce function on this given list: [47,11,42,13]; 
(Attach paper image for this answer) in doc or colab notebook.

# python code to demonstrate working of reduce()

"""
# # importing functools for reduce()
# import functools

# # initializing list
# lis = [47,11,42,13]

# # using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a, b: a+b, lis))




"Practical Questions:" 
"Que-1. Write a Python function that takes a list of numbers as input and returns the sum of all even numbers in the list." 
# def listA(*args):
#     x= []
#     for x in args:
#         if x %2 == 0:
#          x += 1
#                 return [x] 

# print(listA(1,2,3,4,5,6))




"Que-2. Create a Python function that accepts a string and returns the reverse of that string." 

# def func(x): 
#   return x[::-1]

# mytxt = func(input())

# print(mytxt)


"Que-3. Implement a Python function that takes a list of integers and returns a new list containing the squares of each number." 

# Answer-3

# def printValues():
#     # Create an empty list 'l'
#     l = list()
    
#     # Iterate through numbers from 1 to 20 (inclusive)
#     for i in range(1, 21):
#         # Calculate the square of 'i' and append it to the list 'l'
#         l.append(i**2)
    
#     # Print the list containing squares of numbers from 1 to 20
#     print(l)

# # Call the 'printValues' function to generate and print the list of squares
# printValues() 


"Que4. Write a Python function that checks if a given number is prime or not from 1 to 200." 

# Answer-4

#function to check if a given number is prime
# def isPrime(n):
#   #since 0 and 1 is not prime return false.
#     if(n==1 or n==0):  return False
  
#   #Run a loop from 2 to n-1
#     for i in range(2,n):
#     #if the number is divisible by i, then n is not a prime number.
#         if(n%i==0):
#             return False
  
#   #otherwise, n is prime number.
#     return True

# N = 200
# #check for every number from 1 to N
# for i in range(1,N+1):
#   #check if current number is prime
#     if(isPrime(i)):
#         print(i,end=" ")     

          

"Que-5. Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of terms." 
#defining function to return list of fibonacci elements
# def fibonacci(n):
    
#     l = [0,1] 
#     for i in range(2,n):
#         l.append(l[-1]+l[-2])
#     return l

# #Main function
# if __name__ == "__main__":
#    #defining the total number of elements
#     n = 10
    
#     #calling of function
#     fibo = fibonacci(n)
    
#     #displaying the function  
#     print("Fibonacci Series: ",*fibo)



"Que-6. Write a generator function in Python that yields the powers of 2 up to a given exponent." 
# def power_generator(base, exponent):
#     result = 1
#     for i in range(exponent + 1):
#         yield result
#         result *= base

# # Accept input from the user
# base = int(input("Input the base number: "))
# exponent = int(input("Input the exponent: "))

# # Create the generator object
# power_gen = power_generator(base, exponent)

# # Generate and print the powers
# print(f"Powers of {base} up to exponent {exponent}:")
# for power in power_gen:
#     print(power)




"Que-7. Implement a generator function that reads a file line by line and yields each line as a string." 
# Open the file in read mode
# with open('filename.txt', 'r') as file:
#     # Read each line in the file
#     for line in file:
#         # Print each line
#         print(line.strip())


"Que-8. Use a lambda function in Python to sort a list of tuples based on the second element of each tuple." 

# Create a list of tuples named 'subject_marks', each tuple containing a subject and its corresponding marks
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Display the original list of tuples to the console
# print("Original list of tuples:")
# print(subject_marks)

"Sort the 'subject_marks' list of tuples based on the second element of each tuple (the marks)"
"using a lambda function as the sorting key to extract the second element"
# subject_marks.sort(key=lambda x: x[1])

# Display the sorted list of tuples to the console
# print("\nSorting the List of Tuples:")
# print(subject_marks) 




"Que-9. Write a Python program that uses map() to convert a list of temperatures from Celsius to Fahrenheit." 



"Que-10. Create a Python program that uses filter() to remove all the vowels from a given string." 
# def fun(string):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if string in letters:
#         return True
#     else:
#         return False

# strA = "PW Skills"
# filtrd = filter(fun,strA)
# print('removed vowels are:')
# for s in filtrd:
#     print(s)
    
  

"""
11) Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this: 
Order Number    Book Title and Author                 Price per Item             Quantity 
34587           Learning Python, Mark Lutz                40.95                     4
98762           Programming Python, Mark Lutz             56.80                     5
77226           Head First Python, Paul Barry             32.95                     3
88112           Einführung in Python3, Bernd Klein        24.99                     3                    
            
Write a Python program, which returns a list with 2-tuples. Each tuple consists of the order number and the 
product of the price per item and the quantity. The product should be increased by 10,- € if the value of 
the order is smaller than 100,00 €. Write a Python program using lambda and map.
                                   
"""                                      
