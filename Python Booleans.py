print(bool("HellO"))
print(bool(15))

x = "Hello!"
y = 15
print(bool(x))
print(bool(y))

a = str(input("Enter the string : "))
b = str(input("Enter the Integre : "))
print(bool(a))
print(bool(b))

c=int(input("Enter fist number : "))
d=int(input("Enter second number : "))

if d>c:
    print("d is greatter than c")
else:
    print("c is greatter than d")

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#The following will return Ffalse:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#Functions can Return a Boolean

#You can create functions that returns a Boolean Value:
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False: 
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


x = 200
print(isinstance(x, int)) 