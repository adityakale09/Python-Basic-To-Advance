#============================ set ====================================
# A set is a collection which is unordered, unchangeable, and unindexed. on dupliate
# Sets are written with curly brackets {}.
#  Note: Set items are unchangeable, but you can remove items and add new items.

myset = {'apple', 'banana', 'cherry'}
print(myset)
print('-----------------------')

print(type(myset))
print('-----------------------')

# True and 1 is considered the same value:
# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
s = {10 ,0,0,1,2,3,4,4,5,5,6,7}
print(s)
print('-----------------------')

print(len(s))
print('-----------------------')

s = set(('aditya', 1, True))
print(s)
print('-----------------------')
#=======================================================================
#You cannot access items in a set by referring to an index or a key.
# (But you can loop through the set items using a for loop, or ask if
# a specified value is present in a set, by using the in keyword.)

s = set(('aditya', 1, True,"apple", "banana", "cherry", True, 1, 2))
for x in s:
    print(x)
print('-----------------------')

print('aditya' in s)
print('aditya' not in s)
print('-----------------------')

#=========================================================================
#====================Add an item to a set, using the add() method:========
s = {1,2,3}
s.add(344)
print(s)
print('-----------------------')

#===================================================================
#Add Any Iterable
#The object in the update() method does not have to be a set, 
# it can be any iterable object (tuples, lists, dictionaries etc.).

s = {1,2,3}
l = ['aditya', 'kale']

s.update(l)
print(s)
print('-----------------------')

# Note: If the item to remove does not exist, remove() will raise an error
s.remove('aditya')
print(s)
print('-----------------------')

# Note: If the item to remove does not exist, discard() will NOT raise an error.
s.discard('kale')
print(s)
print('-----------------------')

a = s.pop()
print(a)
print('-----------------------')

# The clear() method empties the set:
s.clear()
print(s)
print('-----------------------')

#The del keyword will delete the set completely:

# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset) # rise error
# print('-----------------------')

#========================= loop =========================
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print('-----------------------')

#=============================== imp =================================
# Join Sets
# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.

#--------------------------------------------------------------------------------
# The union() method returns a new set with all items from both sets \ no duplicates.
s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6,7,8,9}

s3 = s1.union(s2)
print(s3)
print('-----------------------')

# You can use the | operator instead of the union() method,
#  and you will get the same result.

# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
print('-----------------------')

# Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(len(myset))
print(myset)
print('----------------------------------------------------------------------')

myset = set1 | set2 | set3 |set4
print(myset)
print('----------------------------------------------------------------------')

# Note: The  | operator only allows you to join sets with sets, 
# and not with other data types like you can with the  union() method.
s11 = {1,2,3,4}
l11 = [22,2,223,343,45]

f = s11.union(l11)  
print(f)
print('----------------------------------------------------------------------')

#============================== update ===============================
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.

s1= {12,3,4,5}
s2= [12,23,3,445,50]
s1.update(s2)
print(s1)
print('----------------------------------------------------------------------')

# =======================Remove Item===================================
# To remove an item in a set, use the remove(), or the discard() method.

# Note: If the item to remove does not exist, remove() will raise an error.
ss = {12,12,14,15,17,16}
ss.remove(12)
print(ss)
print('----------------------------------------------------------------------')

# Note: If the item to remove does not exist, discard() will NOT raise an error.
s = {12,12,14,15,17,16}
s.discard(12)
print(s)
print('----------------------------------------------------------------------')


print('----------------------------------------------------------------------')


print('----------------------------------------------------------------------')


