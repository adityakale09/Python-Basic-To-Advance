import sys
print(sys.version) # or python --version

#============working with textual data========================
a = "Aditya's laptop"
b = 'Aditya\'s laptop'
print(a)
print(type(a)) # returns datatype

print(b)

print(len(b))

print(a[2]) #  [] to access the character by its location\index

print(b[14])
print(b[0:14]) # index 14=p is excluded(not include)

#----------------------------------------------------------------------------
print(a.lower())
print(b.upper())

#----------------------------------------------------------------------------
print(b.count('Adi')) # this function takes an argument\parameters in ""
                    #and print how many times the text or char appear in text

#----------------------------------------------------------------------------
print(a.find("laptop")) #o/p = 9 because starting character l is on index 9 
print(b.find ('abc')) # -1 because abc is not appear in text

#--------------------------------------------------------------------------
b.replace ("laptop","phone")

print(b) # not giving updated text because need to assign a new veriable 
           #to return a updated text with replace

abc = b.replace ("laptop","phone")
print (abc)

#-------------------------------------------------------------------------
#=======================(concatination) use to (combine\join\merge) text.
fname = 'Aditya'
lname = 'kale'

fullname = fname +' '+ lname #(this is not best way)
print(fullname)

full= '{} {} {} {}'. format('Mr.',fname,"Shrikrushna",lname) # {} is a place holder
                                    #(means :- it holds space for parameters\text)

print(full)

print(f"My name is {fname .upper()+' '+ lname.lower()} and I am 22 years old.")
print(f"My name is {fname.lower()} {lname.upper()} and I am 22 years old.") # best way

print('My name is {} {} and I am 22 years old.'.format(fname.upper(),lname) ) 

#----------------------------------------------------------------------------
#============================================
# dir() display different methods available to use
#============================================
print(dir(fname))
print('----------------------------------------------------------------------------------')
# this is imp function 
# (because of this we are able to know which functions have to apply on specific type)
#like
print(dir(3)) #int
print('----------------------------------------------------------------------------------')
print(dir(3.5))
print('----------------------------------------------------------------------------------')
print(dir([2,3,40])) #list

#------------------------------------------------------------------------------------
#============================================
# help() displays how to use it\methods\functions
#============================================
# print(help('aditya')) # Xwrong way
n = 'aditya'
print(help(str.lower))
print(help (list.append)) #explain how to use append method
# print("adiitya".__doc__) #in short explanation
#------------------------------------------------------------------------------------