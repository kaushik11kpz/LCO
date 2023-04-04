import random


# print(random.choice(range(100)))
# print(random.choice([1,4,7,45,67,23]))
# print(random.choice("PrabhatChand"))

#EVEN
# print(random.randrange(0,100,2))

#ODD
# print(random.randrange(1,100,2))

#Random between 0 and 1
# print(random.random())

# TO CONTROL RANDOMNESS'
# random.seed(20)
# print(random.random())

list_numbers = [20,45,78,34,67,56]
random.shuffle(list_numbers)
print(list_numbers)
