# def addMe(num1, num2):
#     total=num1+num2
#     return total
# print(addMe(3,5))

# def sum_multiple_number(*num):
#     total=0
#     for var in num:
#         total=total+var
#     return  total
#
# print(sum_multiple_number(3,6,8,6,5,9))

#Challenge

# def challenge(num1,num2):
#     product_cost=100
#     final_cost=product_cost-(num1+num2);
#     return final_cost
#
# print(challenge(45,10))

def challenge_Big(*num):
   if len(num)<=2:
       product_cost=100
       for var in num:
           product_cost=product_cost-var
       print("Total cost is:", product_cost)
   else:
       print("The number of argument is greater than 2!!!")
   return

challenge_Big(8,9,9)