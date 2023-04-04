import random

heroes = ["Hulk","Spiderman","Logan"]
for h in heroes:
    print(h)

#anything which can be used by for in loop is called iterator
#Things/Methods which create iterator is known as generator
#To make integer iterator use yield instead of return

#Generator
def magic():
    for i in range(6):
        yield random.randint(0,20)

for number in magic():
    print("The value is", number)