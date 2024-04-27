#https://cs50.harvard.edu/python/2022/psets/0/

# 1. Lower case mensaje
greet = input().lower()
print(greet)

# 2. add "..." in every space between words
mensaje = input()
modified_mensaje = mensaje.replace(' ', '...')
print(modified_mensaje)

# 3. Replace the face with emoji
face = input()
def convert(mensaje):
    if ":)" in mensaje:
        return mensaje.replace(":)", "🙂")
    elif ":(" in face:
        return mensaje.replace(":(", "🙁")
    else: return mensaje



print(convert(face))