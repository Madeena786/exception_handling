## **Task 18 - Practice Exception Handling**



###### **Introduction**



Exception handling is an important concept in Python programming.



Sometimes errors can occur while a program is running. These errors are called exceptions. Instead of allowing the program to stop suddenly, Python provides exception handling to handle these errors properly.



In this task, I created a Python program that demonstrates different types of exceptions using `try`, `except`, and `finally`.



###### **Objective**



The main objectives of this task are:



1. &#x20;To understand exception handling in Python.
2. &#x20;To handle runtime errors safely.
3. &#x20;To use `try` and `except` blocks.
4. &#x20;To use `finally` for code that must execute at the end.
5. &#x20;To provide meaningful error messages to users.
6. &#x20;To practice handling different types of exceptions.



###### **Technology Used**



\- Python

\- IDLE / Python Interpreter

###### 

###### **Exceptions Covered**



This project demonstrates five different exceptions:



1\. ValueError

2\. ZeroDivisionError

3\. IndexError

4\. KeyError

5\. TypeError



###### **Exception Descriptions**



**1. ValueError**



A `ValueError` occurs when a function receives a value of the correct type but an inappropriate value.



Example:



```python

number = int("abc")

In this project, it occurs when the user enters text instead of a number.



**2. ZeroDivisionError**

A ZeroDivisionError occurs when a number is divided by zero.

Example:

10 / 0





**3. IndexError**

An IndexError occurs when we try to access a list index that does not exist.

Example:

numbers = \[10, 20, 30]print(numbers\[5])





**4. KeyError**

A KeyError occurs when we try to access a dictionary key that does not exist.

Example:

student = {"name": "Madeena"}print(student\["salary"])





**5. TypeError**

A TypeError occurs when an operation is performed on incompatible data types.

Example:

number = 10text = "Hello"result = number + text





###### **Python Program**



def handle\_value\_error():

&#x20;   try:

&#x20;       number=int(input("Enter a number: "))

&#x20;       print("You entered:", number)



&#x20;   except ValueError:

&#x20;       print("Error: Please enter numbers only.")

&#x20;   finally:

&#x20;       print("ValueError handling completed.\\n")

def handle\_zero\_division():

&#x20;   try:

&#x20;       number1=int(input("Enter first number: "))

&#x20;       number2=int(input("Enter second number: "))

&#x20;       resultz=number1 / number2

&#x20;       print("Division result:", result)

&#x20;   except ValueError:

&#x20;       print("Error: Please enter numbers only.")

&#x20;   except ZeroDivisionError:

&#x20;       print("Error: Cannot divide by zero.")

&#x20;   finally:

&#x20;       print("ZeroDivisionError handling completed.\\n")

def handle\_index\_error():

&#x20;   try:

&#x20;       numbers=list(map(int, input("Enter list elements separated by space: ").split()))

&#x20;       index=int(input("Enter index: "))

&#x20;       print("Value:", numbers\[index])

&#x20;   except ValueError:

&#x20;       print("Error: Please enter valid numbers.")

&#x20;   except IndexError:

&#x20;       print("Error: Index is out of range.")

&#x20;   finally:

&#x20;       print("IndexError handling completed.\\n")

def handle\_key\_error():

&#x20;   try:

&#x20;       student={

&#x20;           "name":"Madeena",

&#x20;           "age":21,

&#x20;           "course":"MCA"

&#x20;       }

&#x20;       key=input("Enter key (name/age/course): ")

&#x20;       print("Value:", student\[key])

&#x20;   except KeyError:

&#x20;       print("Error: Key not found.")

&#x20;   finally:

&#x20;       print("KeyError handling completed.\\n")

def handle\_type\_error():

&#x20;   try:

&#x20;       number=10

&#x20;       text="Hello"

&#x20;       result=number + text

&#x20;       print(result)

&#x20;   except TypeError:

&#x20;       print("Error: Cannot add an integer and a string.")

&#x20;   finally:

&#x20;       print("TypeError handling completed.\\n")

print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")

print("      EXCEPTION HANDLING PROGRAM")

print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")

print("\\n1. VALUE ERROR")

handle\_value\_error()

print("2. ZERO DIVISION ERROR")

handle\_zero\_division()

print("3. INDEX ERROR")

handle\_index\_error()

print("4. KEY ERROR")

handle\_key\_error()

print("5. TYPE ERROR")

handle\_type\_error()

print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")

print("      PROGRAM EXECUTION COMPLETED")

print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")







###### **Sample Output**

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

&#x20;     EXCEPTION HANDLING PROGRAM

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



1\. VALUE ERROR

Enter a number: abc

Error: Please enter numbers only.

ValueError handling completed.



2\. ZERO DIVISION ERROR

###### Enter first number: 10

Enter second number: 0

Error: Cannot divide by zero.

ZeroDivisionError handling completed.



3\. INDEX ERROR

Enter list elements separated by space: 10 20 30 40

Enter index: 5

Error: Index is out of range.

IndexError handling completed.



4\. KEY ERROR

Enter key (name/age/course): salary

Error: Key not found.

KeyError handling completed.



5\. TYPE ERROR

Error: Cannot add an integer and a string.

TypeError handling completed.



\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

&#x20;     PROGRAM EXECUTION COMPLETED

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



###### **Features**

1. &#x20;Handles invalid numeric input.
2. &#x20;Handles division by zero.
3. &#x20;Handles invalid list indexes.
4. &#x20;Handles missing dictionary keys.
5. &#x20;Handles incompatible data types.
6. &#x20;Displays meaningful error messages.
7. &#x20;Uses separate functions for different exceptions.
8. &#x20;Uses finally to display completion messages.



###### **Concepts Learned**

Through this task, I learned:

1. &#x20;Exception handling
2. &#x20;try block
3. &#x20;except block
4. &#x20;finally block
5. &#x20;Multiple exception handling
6. &#x20;ValueError
7. &#x20;ZeroDivisionError
8. &#x20;IndexError
9. &#x20;KeyError
10. &#x20;TypeError
11. &#x20;Functions in Python
12. &#x20;User input handling



###### **Conclusion**

This project helped me understand how Python handles runtime errors using exception handling.

By using try, except, and finally, errors can be handled safely and users can receive meaningful error messages instead of the program stopping unexpectedly.

This task improved my understanding of practical Python programming and error handling.

