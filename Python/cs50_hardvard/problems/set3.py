"""


def fuel_percentage():
        try:
            fraction = input("Fractions: ")
            x, y = map(int, fraction.split('/'))
            percentage = round(x / y * 100)
            if x > y or y == 0:
                raise ValueError
            if percentage <= 1:
                return 'E'
            elif percentage >= 99:
                return 'F'
            else:
                return str(percentage) + '%'

        except (ValueError, ZeroDivisionError):
           fuel_percentage()

print(fuel_percentage())


menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def order():
    total = 0.0
    while True:
        try:
            item = input("Item: ")
            item = item.title()  #Mayusculas la rimera
            if item in menu:
                total+= menu[item]
                print(f"Total: ${total:.2f}")
        except EOFError:
            break

order()


def grocery_list():
    items = []
    while True:
        try:
            item = input()
            items.append(item.upper())
        except EOFError:
            break

    unicos = set(items)

    for i in sorted(unicos):
        count = items.count(i)
        print(f"{count} {i}")

grocery_list()

"""