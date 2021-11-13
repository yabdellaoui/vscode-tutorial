import random

# 1- Generate value from 0 to 1 (0 and 1 are not present)
value = random.random()
print(value)

# 2- Generate an integer value from 1, to 10
value2 = random.randint(1, 10)
print(value2)

# 3- Choise radom from the given list:
my_list = ["Hi", "Hello", "Hey", "Hola", "Salut"]
value3 = random.choice(my_list)
print(value3 + " Yacine !")

# 4- Generate k random from the given list. Python3
# colors = ["Red", "Black", "Yellow", "Green"]
# value4 = random.choices(colors, k=20)
# print(value4)

# 5- take some elem randomly from the given list
my_list = list(range(1,53))
value5 = random.sample(my_list, k=5)
print(value5)


