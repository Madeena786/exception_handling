def handle_value_error():
    try:
        number=int(input("Enter a number: "))
        print("You entered:", number)

    except ValueError:
        print("Error: Please enter numbers only.")
    finally:
        print("ValueError handling completed.\n")
def handle_zero_division():
    try:
        number1=int(input("Enter first number: "))
        number2=int(input("Enter second number: "))
        resultz=number1 / number2
        print("Division result:", result)
    except ValueError:
        print("Error: Please enter numbers only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    finally:
        print("ZeroDivisionError handling completed.\n")
def handle_index_error():
    try:
        numbers=list(map(int, input("Enter list elements separated by space: ").split()))
        index=int(input("Enter index: "))
        print("Value:", numbers[index])
    except ValueError:
        print("Error: Please enter valid numbers.")
    except IndexError:
        print("Error: Index is out of range.")
    finally:
        print("IndexError handling completed.\n")
def handle_key_error():
    try:
        student={
            "name":"Madeena",
            "age":21,
            "course":"MCA"
        }
        key=input("Enter key (name/age/course): ")
        print("Value:", student[key])
    except KeyError:
        print("Error: Key not found.")
    finally:
        print("KeyError handling completed.\n")
def handle_type_error():
    try:
        number=10
        text="Hello"
        result=number + text
        print(result)
    except TypeError:
        print("Error: Cannot add an integer and a string.")
    finally:
        print("TypeError handling completed.\n")
print("*************************************")
print("      EXCEPTION HANDLING PROGRAM")
print("*************************************")
print("\n1. VALUE ERROR")
handle_value_error()
print("2. ZERO DIVISION ERROR")
handle_zero_division()
print("3. INDEX ERROR")
handle_index_error()
print("4. KEY ERROR")
handle_key_error()
print("5. TYPE ERROR")
handle_type_error()
print("*************************************")
print("      PROGRAM EXECUTION COMPLETED")
print("*************************************")


