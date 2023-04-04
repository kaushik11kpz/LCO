# import prabhat
#
# val1 = prabhat.addme(5,6)
# print(val1)
#
# val2 = prabhat.subme(8,11)
# print(val2)


from prabhat import *

# print(addme(9,9))
# print(subme(7,9))

print("Input a number b/w 1 and 4:", )
choice = int(input())
if choice==1:
    print(addme(5,6))
elif choice==2:
    print(subme(9,10))
elif choice==3:
    print(multime(5,7))
elif choice==4:
    print(divme(9,3))
