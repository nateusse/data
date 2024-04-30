"""
# 1. Lower case mensaje
greet = input().lower()
print(greet)

# 2. add "..." in every space between words
mensaje = input()
modified_mensaje = mensaje.replace(' ', '...')
print(modified_mensaje)

# 3. Replace the face with emoji
def convert(mensaje):
        mensaje =  mensaje.replace(":)", "🙂")
        mensaje = mensaje.replace(":(", "🙁")
        return mensaje

def main():
    face = input()
    return (convert(face))

print(main())

#4. prompts the user for mass as an integer (in kilograms) 
#and then outputs the equivalent number of Joules as an integer. 
#Assume that the user will input an integer.

def einstein(mass):
    c = 300000000
    return mass * c ** 2


"""
"""
5. Complet eprogram to leave tip

dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO


def percent_to_float(p):
    # TODO


main()

"""

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    return (f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = float(d[1:])
    return d


def percent_to_float(p):
    p = float(p[:-1])
    return p / 100


print(main())

