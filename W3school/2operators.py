# ================== arithematic operatoers =====================
# add a+b
# sub a-b
# mul a*b 
# div a/b 
# floor div a//b (complete number[remove after decimal point numbers])
# exponent a**b (squre/cube)
# modulus a%b (return remandor) 3%2 = 1
# even or odd
print(1%2) #odd
print(2%2) #even
print(3%2) 
print(4%2)
print(5%2) #odd
print(6%2)
print('---------------------------')

# ================== Assignent operatoers =====================
a = 10
a += 10
a -= 10
a *= 10
a /= 10
a //= 2
a **= 5
a %= 10
print(a)
print('---------------------------')

#======================= Comparison Operators ====================
x = 1
y = 2

print(x == y)
print(x != y)
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)
print('---------------------------')

print(0 < x < y < 3) #True
print('---------------------------')
#======================== Logical operators ========================
#                          (AND , OR , NOT)

x = 5
y = 10 

print (x < 6 and y > 9) #both true
print('---------------------------')

print (x < 4 or y > 9) #one true
print('------------------------')
print (not(x < 6 and y > 9)) # reverse the result
print('------------------------')
#========================== Identity operators ========================
#                          (is , is not)

x = 2
y = 3

print (x is y)
print('------------------------')
print(x is not 3)
print('------------------------')
print(y is 3)
print('------------------------')
print ( y is not 3)
print('------------------------')

# imp =====eg.=======

x = [1,2,3] # same values but not same memory location (variable)
y = [1,2,3]

print(x == y) # true
print(x is y) # false
print('------------------------')

#============================ Membership Operator =================
# use to check the sequence\sub part is present in an object or not

a = [1,2,4,3]
y = 'aditya'

print( 1 in a) #T
print('------------------------')
print('adi' in y) #T
print('------------------------')
print ('  Adi ' not in y) #t
print('------------------------')

# =========================== bitwise operator ======================
#                             & , ^ , |