# =============================Dictionary==============================
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

d = {1: "Aditya",
      2: "Kale" ,
      3: 500}
print(d)

print("---------------------------------")
# Dictionary items are presented in key:value pairs, and can be referred to 
# by using the key name.

# Example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
print("---------------------------------")

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(len(thisdict))
print(type(thisdict))
print(thisdict)
print("---------------------------------")

# =====================The dict() Constructor============================\

# It is also possible to use the dict() constructor to make a dictionary.
# Example
# Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
print("---------------------------------")


d = dict(name = 'aditya', lname = 'kale' , div = 'b_final year')
print(len(d))
print(type(d))

x = d["name"]
print(x.upper())  # convert value of name to upper case 
print("---------------------------------")

y = d.get('div')
print(y)
print("---------------------------------")

# The keys() method will return a list of all the keys in the dictionary.

print(d.keys())
print("---------------------------------")

# Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print("---------------------------------")

#====================================================================
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

a = car.keys() # prints keys in dictonary
print(a) 
print("---------------------------------")

b = car.values() # prints values in dictonary
print(b)
print("---------------------------------")

c = car.items() # prints key-value pairs of dictonary
print(c)
print('----------------------------------')

#===================================================================
car["colour"] = 'white'  # adding key pair in dictonary
print(a)
print("---------------------------------")

car["model"] = "fortuner" # change the value of a key
print(car)
print("---------------------------------")

print ('brand' in car) # checks the key is in dictonry or not
print("---------------------------------")

# =======================Python - Remove Dictionary Items===============================

#The pop() method removes the item with the specified key name:
c = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

a = c.pop("model")
print(a)
print("---------------------------------")

print(c.popitem())  # popitem() only display/remove last item from dictonary
print("---------------------------------")

# delete entire list 
# d = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del d
# print(d)  # rise error
print("---------------------------------")

# The clear() method empties the dictionary:
d = {
    "name" : "aditya",
    "lname": "kale",
    "age" : 22
}
print(d)

d.clear()
print(d)
print("---------------------------------")

# ======================Loop Dictionaries=================================

# Print all key names in the dictionary, one by one:
d = {
    "name" : "aditya",
    "lname": "kale",
    "age" : 22
}
for x in d:
    print(x)
print("---------------------------------")

# Print all values in the dictionary, one by one:
d = {
    "name" : "aditya",
    "lname": "kale",
    "age" : 22
}
for x in d:
    print(d[x])
print("---------------------------------")

# Print all values in the dictionary, one by one:
for x in d.values() :
    print(x)
print("---------------------------------")

# Loop through both keys and values, by using the items() method:
for x,y in d.items() :
    print(x,y)
print("---------------------------------")

# or 
for x in d.items():
    print(x)
print("---------------------------------")


print("---------------------------------")

print("---------------------------------")

print("---------------------------------")

print("---------------------------------")

print("---------------------------------")

