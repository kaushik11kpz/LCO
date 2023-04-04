marvel_heroes = {
    "Spiderman":90,
    "Ironman":95,
    "Captain America":100
}
dc_heroes = {
    "Batman":90,
    "Superman":80,
    "Flash":70
}
# print(len(dc_heroes))
# print(dc_heroes.clear())
# print(dc_heroes)

dc_heroes.update(marvel_heroes)
# print(dc_heroes)

#Convert a tuple to dictionary with keys and no values
myTags = ("Name", "Last_Name", "Age", "Phone_Number")
myOne = dict.fromkeys(myTags)
print((myOne))
print("My dictionary is : %s" %str(myOne))

# print(3*1**3)
# numbers = "123456"
# for n in numbers :
#     print(n)
#
# name = "Learn Code Online"
# for n in name.split():
#     print(n,end=',')


s = '{0} to {1}.in'
s.format('Welcome','LearnCodeOnline')

name="LearnCodeOnline"
print(name[:9])
print(~10)

value = 'learn-code-online'
print(value.split('-'))

print(3*7/3)