# string and nubers code in folder youtube \file(2,3)

print(10 > 9) # true 
print(10 == 9)
print(10 < 9) # false

#========================= eg. ============================

a = 330
b = 20

if a > b:
    print(f'{a} is greater than {b}')
else:
    print(f"{b} is greater than {a}")
print('-----------------------------')
#=============================================================
a = 'adi'
b = ''
c = 12 # false if c = 0

print(bool(a)) #if contain value then returns TRUE
print(bool(b)) # FALSE if variable empty
print(bool(c))
print('-----------------------------')

# false
print(bool(False))
print(bool(0))
print(bool(None))
print(bool([]))
print(bool({}))
print('-----------------------------')

#==============================================================
class myclass():
    def __len__(self):
        return 0
myobj= myclass()
print(bool(myobj))    # false because class o\p is 0
print('-----------------------------')

#==============================================================
def myfun():
    return True
print(myfun())
print('-----------------------------')
#============================== eg. =============================================

def myabc():
    return False # if True o\p: (Yes)
if myabc():
    print('Yes')
else:
    print('No')

print('-----------------------------')
#=======================================================================
a = 10
print(isinstance(a , int)) # true a is an integer

print('-----------------------------')

#===================================================================

