def square(x):
    result = 0
    for i in range(0, x):
        result += x
    return result

print(square(5))

def getPerson():
    name = "John"
    age = 25
    city = "Toronto"
    return name, age, city

name, age, city = getPerson()

print(name, age, city)
