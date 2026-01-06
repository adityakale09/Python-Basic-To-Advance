# list [Ordared , changable , allow diff datatype, allowed duplicate]

# l = ['a', 1 , True,'a']
# print(l)
# print(type(l))
# print(len(l))
# print('------------------------')

# # ============list() constructor===========
# myl = list(('a', 1 ,True, 3+5j)) # here don't need to use [] to declare list
# print(myl)

# #===================list indexing(Accessing)=======================
# l = list(('a', 10 ,True, 3+5j))
# print(l[0])
# print(l[-1])
# print(l[0 : ])
# print(l[ : 5])
# print(l[-4 : 5])
# print('------------------------')

# # ============ check item if exist ===========
# l = list(('a', 10 ,True, 3+5j))
# if 3+5j in l:
#     print(f'item {l[3]} is present in list')

# print('------------------------')

# #====================== change item in list(replace item) ==============
# l = list(('a', 10 ,True, 3+5j))
# l[0] = 'Aditya'
# print(l)

# l[0:4] = 'Aditya'
# print(l)
# print(len(l))

# l[1:3] = 100,4044
# print(l)
# print('------------------------')

# #============= insert() ==========add new item(without replacing existing one)=============
# l = list(('a', 10 ,True, 3+5j))
# l.insert(2,'xyz')
# print(l)

# print('------------------------')

# #================= append() =========add new item to the end================
# l = list(('a', 10 ,True, 3+5j))
# l.append('aditya kale')
# print(l)
# print('------------------------')

# # ================= extend() ======use to merge two lists=================
# ## :note: by extend() we can add any set, tuple , dictonary
# l1 = list((22,'a', 10 ,True, 3+5j))
# l2 = [2,3,5,6754,4]
# l1.extend(l2)
# print(l1)
# print('------------------------') 

# #=============================================================================
# #===================remove() delete specific item ==============================

# l = list(('a', 10 ,True, 3+5j,10)) #removes first occurance of 10 (if multiple 10)
# l.remove(10) #or l.remove(l[1])
# print(l)
# print('------------------------')

# #================ pop() delete by index============
# l = list(('a', 10 ,True, 3+5j))
# l.pop(0)
# print(l)

# l.pop() #remove last item
# print(l)
# print('------------------------')

# #====================== del ======delete by index======================
# l = list(('a', 10 ,True, 3+5j))
# del l[0:2] #l[3]
# print(l)
# print('------------------------')

# # l = list(('a', 10 ,True, 3+5j))
# # del l
# # print(l) #error beause list is completely deleted and not in memory
# # print('------------------------')

# #=======================clear()======empty list but still remaning==============
# l = list(('a', 10 ,True, 3+5j))
# l.clear()
# print(l)
# print('------------------------')

# #=======================loop through a list====================
# l = ['a' ,True, 3+5j]
# for x in l:  #print all the items in a list by using loop
#     print(x)
# print('------------------------')

# #================== for loop ======== prints all items by using index =================
# l = list(('a', 10 ,True, 3+5j))
# print(range(len(l)))

# for i in range(len(l)):
#     print(l[i])
# print('------------------------')
# #============== while loop=======================
# l = ['a', 10 ,True, 3+5j]
# i = 0
# while i < (len(l)) :
#     print(l[i])
#     i += 1
# print('------------------------')
# #=========[Easy]========== loop using list comprehension ====================

# l2 = [23,5432,4,346,546654,3]
# [print(x) for x in l2]
# print('------------------------')
# #========================================================================
# #===============list comprehension===============

# # without list comprehension----------
# l = ['a','aditya'] # only char allowed
# newl = []
# for x in l:
#     if 'a' in x: #conditon
#         newl.append(x) # if exist then add in newl
# print(newl)
# print('------------------------')

# #------- with list comprehension ---------------
# l = ['a','aa','A','b','bb','CC','d','asd']

# new = [x for x in l if 'a' in x]  # simple code
# print(new)
# print('------------------------')

# l = [1,2,3,5,5,6]
# nl = [x for x in l]
# print(nl)
# print('------------------------')

# l = [1,2,3,5,5,6]
# nl = [x for x in range (9) if x <= 6 ]
# print(nl)
# print('------------------------')

# l1 =['apple','mango','banana','orange']
# for x in l1:
#     print(x.upper())  # nl1 = [x.upper() for x in l1]
