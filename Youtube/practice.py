# # num = float(input("Enter any number which you want : "))

# # if num > 0:
# #     print(f" {num} is +positive number")
# # elif num==0:
# #     print(f"{num} is neutral number ")
# # else:
# #     print(f"{num} is negative number")

# num = int (input("Enter num :"))

# if num%2 == 0:
#     print(f"{num} is Even number")
# else:
#     print(f"{num} is odd number")

import calendar as c

n1 = int (input("Enter year : "))
n2 = int (input("ENter month : "))

cal = c.month(n1,n2)

print(cal)