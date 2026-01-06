#============================== tuple() =============================
#===============ordered , unchangeable , allow duplicate=============
t = (1,2,3,4,'r','adi')
print(t)
print(type(t))
print('-----------------------')

print(len(t))
print('-----------------------')

#=====================tuple constructur===========================
t1 = (('a','d','i'))  # imp: ((items))
print(t1)
print('-----------------------')

print(t1[0:3])
print('-----------------------')

#==========(imp)======== only way to change tuple is ===========

tt = (12,23,34,45,56,70)
l = list(tt) # convert tuple into list by constructor
print(l)
l[0] = 100   # change
# or l.append(100)
t = tuple(l)  # convert list into tuple
print(t)
print('-----------------------')

tt = (12,23,34,45,56,70)
l = list(tt) # convert tuple into list by constructor
l.remove(12)  # remove
t = tuple(l)
print(t)
print('-----------------------')

#=================== unpacking a tuple ============================
t = ('apple','banana', 'tomato')
(green, yellow , red) = t

print(yellow)
print(red)
print(red, yellow, green)
print('-----------------------')

t = ('apple','banana', 'tomato')
tt = t * 3 # repete 3 times 
print(tt)
print('-----------------------')

(a,*b,c) = tt  # assign the remaining items to *b
print(a)
print(b)
print(c)
print('-----------------------')

t = ('apple','banana', 'tomato')
tt =t.index('apple') # apple is at index 0
print(tt)
print('-----------------------')

tt = t.index('tomato')
print(tt)
# print('-----------------------')
# print('-----------------------')
# print('-----------------------')