numPizzas = 100
minSlices = 1
maxSlices = 1000

import random

def generatePizzas():
    pizzas = []
    for i in range(0, numPizzas):
        pizzas.append(random.randint(minSlices, maxSlices))
    pizzas.sort()
    print(pizzas)

generatePizzas()
