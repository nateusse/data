"""

# 1 .Deep thought

"""
#In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
"""
def deep():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    answer = answer.strip()
    if answer == '42' or answer.lower() == 'forty-two' or answer.lower() == 'forty two':
        print('Yes')
    else:
        print('No')

deep()

# Home federal saving bank
def bank(mensaje):
    first_word = mensaje.split()[0].lower()
    if first_word ==  "hello" or first_word =="hello,"  :return "$0"
    elif first_word[0] == "h" :return "$20"
    else: return "$100"


usuario = input("Greeting: ")
print(bank(usuario))



# File extensions
def get_media_type():
    filename = input("Enter the name of a file: ")
    extension = filename.strip().split('.')[-1].lower() #divid con punto
    if extension == 'png':
        return 'image/png'
    elif extension == 'jpg' or extension == 'jpeg':
        return 'image/jpeg'
    elif extension == 'gif':
        return 'image/gif'
    elif extension == 'pdf':
        return 'application/pdf'
    elif extension == 'txt':
        return 'text/plain'
    elif extension == 'zip':
        return 'application/zip'
    else:
        return 'application/octet-stream'

print(get_media_type())

# Math interpreter
user = input("Expression: ").split()
x, symbol, y = user
x = float(x)
y = float(y)
if symbol == "+" :
   print ( x + y)
elif symbol == "/" :
   print ( x / y)
elif symbol == "-" :
   print ( x - y)
elif symbol == "*" :
   print ( x * y)



# Meal time
def main():
    time = input("Wht time is it?: ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = map(int, time.split(':'))  # Split the time into hours and minutes
    return hours + minutes / 60.0  # Convert to hours as a float

if __name__ == "__main__":
    main()

    """