#=======================================================================
## Program 1
## Write a Python program to print "Hello Python"
# print('Hello world !')
# print('----------------------------------')

#=======================================================================
## Program 2
## Write a Python program to do arithmetical operations addition and division
# a = int(input('Enter first number:'))  # use float for better
# b = int(input('Enter second Number:'))

# add = a  + b
# print(f" {a} + {b} = {add}")

# div = a/b 
# print(f'{a}/{b} = {div}')
#-------------------Best code---------------------------------
# #OR# div with error handeling
# a = float(input("Enter first Number : "))
# b = float(input("Enter second Number: "))

# if b == 0:
#     print("Divisible by Zero is not valid")
# else:
#     print(f"{a}/{b} = {a/b}")

#=======================================================================
# # Program 3
# # Write a Python program to find the area of a triangle
# # area = 0.5 *base*height

# #Input the base and height from the user
# base = float(input("Enter the length of the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))

# # Calculate the area of the triangle
# area = 0.5 * base * height
# # Display the result
# print(f"The area of the triangle is: {area}")

#=======================================================================
# Program 4
# Write a Python program to swap two variables.
## my logic
# a = 5
# b = 10

# a = a^b # 5^10
# b = b^a # 10 ^ 5^10  (here replace, a = a^b)
# a = a^b # 5 ^ 10^5 (here confusion)
# print(a)
# print(b)
# #------------------------or-----------------------------------
# # Input two variables
# a = input("Enter the value of the first variable (a): ")
# b = input("Enter the value of the second variable (b): ")
# # Display the original values
# print(f"Original values: a = {a}, b = {b}")
# # Swap the values using a temporary variable
# temp = a
# a = b
# b = temp
# # Display the swapped values
# print(f"Swapped values: a = {a}, b = {b}")

# #=======================================================================
# # Program 5
# # Write a Python program to generate a random number.
# import random as a
# print(f"random number : {a.randint(1,100)}")

# #=======================================================================
# # Program 6
# # Write a Python program to convert kilometers to miles.
# km = float(input("Enter kilometers: "))
# conversion = 0.621371

# miles = km*conversion
# print(f"{km} kilometers is equal to {miles} miles")

#=======================================================================
# # Program 7
# # Write a Python program to convert Celsius to Fahrenheit

# celsius = float(input("Enter a tempeture in celsius : "))
# Fahrenheit = (f'{(celsius* 9/5) + 32 }')

# print(f'{celsius} degree celsius = {Fahrenheit} degree Fahrenheit')

#=======================================================================
# # Program 8
# # Write a Python program to display calendar.
# import calendar as c
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))

# cal = c.month(year, month)
# print(cal)
#=======================================================================

# Program 9
# Write a Python program to solve quadratic equation.
import math as m

a = int (input('Enter value for a :'))
b = int (input('Enter value for b :'))
c = int (input('Enter value for c :'))

if a==0:
    print('Invalid input values')
else:
    disc = (b*b) - (4*a*c)
    sqroot = m.sqrt(disc)
    x = sqroot / (4*a)




#=======================================================================


#=======================================================================

#=======================================================================