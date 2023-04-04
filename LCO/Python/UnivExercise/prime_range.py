#Print all the prime number between a range
print("What is lower range: ")
lower_range=int(input())
print("What is upper range: ")
upper_range=int(input())

for number in range(lower_range,upper_range):
    for i in range(2,number):
        if(number%i==0):
            break
    else:
         print(number)
