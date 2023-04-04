print("Enter a number: ")
number=int(input())
factorial=1
if(number<0):
    print("Negatives don't have factorials")
elif(number==0):
    print("The factorial is",1)
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print("The result is",factorial)

