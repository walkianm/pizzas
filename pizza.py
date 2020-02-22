pizzas = [23, 43, 43, 80, 81, 83, 86, 88, 91, 100, 111, 121, 142, 161, 174, 176, 182, 192, 207, 216, 239, 243, 270, 281, 286, 295, 299, 332, 343, 347, 350, 352, 352, 371, 373, 374, 376, 387, 388, 408, 421, 428, 438, 438, 454, 481, 482, 504, 510, 517, 535, 537, 552, 559, 565, 567, 573, 576, 576, 579, 581, 584, 592, 599, 601, 622, 649, 653, 657, 663, 679, 681, 683, 687, 718, 721, 725, 727, 749, 752, 784, 784, 812, 826, 830, 893, 913, 915, 923, 932, 938, 941, 948, 983, 985, 990, 992, 992, 995, 996]
goal = 42069

reachable = [0] * (goal + 1)

def shiftAndAND(next_pizza):
    for i in range(goal - next_pizza, 0, -1):
        if reachable[i] != 0 and reachable[i + next_pizza] == 0:
            reachable[i + next_pizza] = next_pizza

    reachable[next_pizza] = next_pizza
    # print(reachable)

def findReachableCounts():
    for pizza in pizzas:
        if pizza < goal:
            shiftAndAND(pizza)

def orderPizzas():
    findReachableCounts()
    i = goal
    while reachable[i] == 0:
        i -= 1
    print("Can order up to %d pizzas." % i)
    pizzasToOrder = []
    while i != 0:
        pizzasToOrder.append(reachable[i])
        i -= reachable[i]
    pizzasToOrder.sort()
    print(pizzasToOrder)

orderPizzas()
