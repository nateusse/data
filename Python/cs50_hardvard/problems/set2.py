"""
user = input("camelCase: ")
snake_case = ""
for mayuscula in user:
    if mayuscula == mayuscula.upper():
         snake_case += mayuscula.replace(mayuscula, f"_{mayuscula.lower()}")
    else: snake_case += mayuscula
print("snake_case: " + snake_case)


amount = 50
print ("Amount Due: " + str(amount))
while amount > 0 :
    user = int(input("Insert coin: "))
    if user not in [25, 10, 5]:
        print ("Amount Due: " + str(amount))
        continue
    amount -= user
    change = amount
    if amount > 0:
        print ("Amount Due: " + str(amount))
    else:
        print ("Change Owed: " + str(abs(change)))

user = input("Input: ")
res = ""
for letter in user:
    if letter.lower() not in ["a", "e", "i", "o", "u"]:
        res += letter
print ("Output: " + str(res))

"""