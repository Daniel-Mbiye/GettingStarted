pizzas = {
    "cheese": 9,
    "pepperoni": 10,
    "vegetables": 11,
    "buffalo chicken": 12
}

for pie in pizzas:
    print(pie)

for pie, price in pizzas.items():
    print(price)

for pie, price in pizzas.items():
    print("A whole {} pizza costs ${}".format(pie, price))

print(" ")

for pie, price in pizzas.items():
    print("A whole " + pie + " pizza costs $" + str(price))

    