marvel_heroes = ["Spiderman","Ironman","Hulk"]
dc_heroes = ["Batman","Flash","Aquaman"]

#Print from 1 to end
print(dc_heroes[1:])

#Delete 1 index
del dc_heroes[1]
print(dc_heroes)

#Insert flash at specific location
dc_heroes.insert(1,"Flash")
print(dc_heroes)

#Add Wonder woman to list
dc_heroes.append("Wonder Woman")
print(dc_heroes)

#Remove Flash
dc_heroes.remove("Flash")
print(dc_heroes)

#Reverse list
dc_heroes.reverse()
print(dc_heroes)

#Count something inside list
print(dc_heroes.count("Batman"))

#Challenge
#Combine dc_heroes and marvel_heroes
dc_heroes.extend(marvel_heroes)
print(dc_heroes)

