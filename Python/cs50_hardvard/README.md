# Hardvard CS50


## SET 0 FUNCTIONS AND VARIABLES
- Basics
    - name = input("What's your name? ")  Inputs 
    - print(f"hello, {name}")
    - name = name.strip() removes whitespaces
    - name = name.title()  capitalizes first letter
    - x = float(input("What's x? "))  Accept fixed type
    - round(x / y, 2)
    - z = x / y Decimal
    - z = x // y Entero
    - print(f"{z:.2f}")  2 decimals
    print(f"{z:,}")  coma para cada 3 numeros
    - def hello(to="world"): print("hello,", to)  DEfault
    - n * n square

- Linux commands
    - rmdir folder
    - rm file
    - code hello.py #create
    - python hello.py  #excute
    - mv hello.py goodbye.py #cambiar nombre


## SET 1 CONDITIONALS
- Basics
    -  < , >, <=, >= , ==, !=
    -  usuario = int(input("pregunta "))
    - if , elif, else
    - and , or
    - % modulo
    - Pythonic (ternario): return True if n % 2 == 0 else False
    - match 
        -  name = input("What's your name? ")

            match name: 
                case "Harry" | "Hermione" | "Ron":
                    print("Gryffindor")
                case "Draco":
                    print("Slytherin")
                case _:
                    print("Who?")

## SET 2 EXCEPTIONS 
- Errors
    - Runtime: No le gusto al comilador
    - Syntax errors: ^^^^^
    - try and except, else  Ej:  excpet ValueError: pass , else: break (for while loop)
    - pass
    - ZeroDivisionError, OSError (can't open), NameError, ValueError, RuntimeError (unable to habdle error), FileNotFoundError, ConnectionError, 
    - raise (frozar excepcion) Ej: raise RuntimeError
    - exc :  
        - exc must be exception instance or None.
        - Ej: raise RuntimeError from exc , except ConnectionError as exc: raise RuntimeError('Failed to open database') from exc
    - finally:
        -  Siempre se ejecuta
        - executes a break, continue or return  (exeption is not riase)
    - with :
        -   objects like files to be used in a way that ensures they are always cleaned up promptly and correctly
        -  with open("myfile.txt") as 
- Problems
    - filename.split('.')[-1 ].lower() Dividir deespues del punto Ej hola.png queda ["hola", "png"], tomar el ultimo
    - mensaje.split()[0 ]  Dividir el mensaje y toar el primero
