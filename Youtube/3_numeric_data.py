#============ working with numeric(numbers) data ========================
#(int \ float)

a = 10
b = 2.3
c = 'Aditya'
d = [2,3,404,5]
print(type(a))
print(type(b))
print(type(c))
print(type(d))

x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

# ===================================================================================
# ================== arithematic operatoers =====================
# add a+b
# sub a-b
# mul a*b 
# div a/b 
# floor div a//b (complete number[remove after decimal point numbers])
# exponent a**b (squre/cube)
# modulus a%b (return remandor) 3%2 = 1


print(1%2) #odd
print(2%2) #even
print(3%2) 
print(4%2)
print(5%2) #odd
print(6%2)
print('---------------------------')
#---------------------------------------------------------------------
print(2 * 3 + 4)
print(2 * (3 + 4))
print('---------------------------')
#=====================================================================
# increment operator
num = 2
num = num + 1
print(num)

num += 30
print(num)

num *= 2
print(num)

num /= 2
print(num)

print('---------------------------')
#------------------------------------------------------------------
print(abs(-30)) # it converts -ve value into +ve absulute value
print('---------------------------')

print(round(3.75)) # prints nearest integer value
print(round(3.43))
print('---------------------------')

#===============================================================================
# =================== comparison operators ====================
# equal            2 == 2
# not equal        3 != 2
# Greater than     3 >  2
# less than        3 <  2
# Greater or equal 3 >= 2
# Less or equal    3 <= 2

print(2==3)
print(2!=3) #True
print(3>=3)
print(3>3) #False

#==================================================================
#======================= Type casting ========================
n1 = '100'  #string
n2 = '200'
n1 = int(n1)
n2 = int(n2)
print(n1 + n2)
# OR
print(int(n1) + int (n2)) # int() converts string\any into integer
#=======================================================================
#===============only way to display random values================

import random as r

a = r.randrange(10,500)
print(a)