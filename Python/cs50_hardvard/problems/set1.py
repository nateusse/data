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


"""
# File extensions


# Math interpreter

# Meal time