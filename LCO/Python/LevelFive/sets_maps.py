#SET
#superheroes = {1,2,3,4,6.7,"Prabhat"}

superheroes = {1,2,3,4,5}
print(superheroes)

def getSquares(num):
    return num*num

result = map(getSquares,superheroes)
actual_result = set(result)
print(actual_result)