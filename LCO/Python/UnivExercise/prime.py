print("Enter a number: ")
number = int(input())
if number > 1:
    for i in range(2,number):
        if(number%i == 0):
            print(number,"is not a prime number")
            print(i,"times",number//i,"is",number)
            break
    else:
        print(number,"is a prime number")
