# Python HOME,Intro,Get started
# print("Hello,Almaty!")


# Python Syntax
# if 10>3:
#  print("Ten is greater than three!")

# x=10
# y="Hello,Kazakhstan!"


# Python Comments
# comment hi

# print("Hello,Almaty!)
# print("Hello,Zhetisu!")

# Hello gays its a comment
# 1231
# 332

# and another way to commenting

"""
Hello gays its a comment
1231
332
"""

# Python Variables

"""
 x=7
y="Marat"
print(x)
print(y) 
"""

"""
x = 6
x = "Janna"
print(x)
"""

"""
x = str(2)
y = int(2)
z = float(2)
"""

"""
x = 7
y = "Marat"
print(type(x))
print(type(y))
"""

"""
x = "Marat"
#is the same as
x = 'Marat'
"""

"""
a = 4
A = "Janna"
"""

"""
myVariableName = "Serik"
MyVariableName = "Serik"
my_variable_name = "Serik" 
myvar = "Serik"
"""

"""
x, y, z = "Tomato" , "Melon", "Strawberry"
print(x)
print(y)
print(z)

"""

"""
x = y = z = "Melon"
print(x)
print(y)
print(z)

"""

"""
fruits = [ "apple" , "cherry" , "banana" ]
x , y , z = fruits
print(x)
print(y)
print(z)

"""

"""
x = "Almaty "
y = "is "
z = "wonderful"
print(x, y , z)

"""

"""

x=3
y=13
print(x + y)

"""

""" 

x = 5
y= "Janna"
print(x, y)


"""

"""

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

"""

"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
"""

"""
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

"""

"""

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

"""

# Python data types

"""
x = 3
print(type(x))
"""

"""
x = 4
y = 5.7
z = 6f

print(type(x))
print(type(y))
print(type(z))

"""

"""
x = 2.3
y = 4.0
z = -56.89

print(type(x))
print(type(y))
print(type(z))
"""

"""
x = 2+6j
y = 6j
z = -6j

print(type(x))
print(type(y))
print(type(z))

"""

"""


x = float(2)


y = int(3.9)


z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

"""

# Python Casting

"""
x=int(1)
y=float(3.0)
z=str("d2")
print(x)
print(y)
print(z)

"""

# Python Strings
"""
a = "Hello"
print(a)

"""

"""
a = "Hello, World!"
print(a[1])

"""

"""
for x in "potato":
  print(x)
"""

"""
a = "Hello,Almaty"
print(len(a))
"""

"""
txt = "The best things in life are free!"
print("free" in txt)
"""

"""
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
"""

"""
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
"""

"""
b = "Hello, Almaty!"
print(b[2:5])
"""

"""
b = "Hello, Almaty!"
print(b[:5])
"""

"""
a = "Hello, Kazakhstan!"
print(a.upper())

"""

"""
a = "Hello, Kazakhstan!"
print(a.lower())
"""

"""
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
"""

"""
a = "Hello, Almaty!"
print(a.replace("H", "A"))
"""

"""
a = "Hello, Almaty!"
print(a.split(",")) # returns ['Hello', ' Almaty!']
"""

"""
a = "Hello"
b = "World"
c = a + " " + b
print(c)
"""

"""
age = 27
txt = "My name is Saken, and I am {}"
print(txt.format(age))
"""

"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
"""

"""
txt = "We are the so-called \"Vikings\" from the north."
"""

# Python Booleans
"""
print(10 > 9)
print(10 == 9)
print(10 < 9)
"""

"""
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
"""

"""
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

"""

"""
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
"""

"""
x = 200
print(isinstance(x, int))
"""

# Python Operators
"""
print(10+5)
"""

# Python Lists
"""
thislist = ["strawberry", "banana", "cherry", "strawberry", "cherry"]
print(thislist)
"""

"""
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
"""

"""
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
"""

"""
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
"""

"""
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
"""

"""
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
"""

"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
"""

"""
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
"""

"""
thislist = ["apple", "banana", "cherry"]
thislist[1] = "strawberry"
print(thislist)
"""

"""
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
"""

"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
"""

"""
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
"""

"""
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
"""

"""
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
"""

"""
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
"""

"""
thislist = ["apple", "banana", "cherry"]
del thislist
"""

"""
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
"""

"""
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

"""

"""
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
"""

"""
fruits = ["apple", "banana", "cherry"]
print(
fruits[1])

"""

"""
fruits = ["apple", "banana", "cherry"]
fruits[0]
 = 
"kiwi"
"""

"""
fruits = ["apple", "banana", "cherry"]
fruits[0]
 = 
"kiwi"

"""

"""
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

"""

"""
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,
 "lemon")
"""

"""
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

"""

"""
fruits = ["apple", "banana", "cherry"]
print(
fruits[-1])
"""

"""
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[
2:5])
"""

"""
fruits = ["apple", "banana", "cherry"]
print(
len(fruits))
"""

# Python Tuples
"""
fruits = ("apple", "banana", "cherry")
print(
fruits[0])
"""

"""
fruits = ("apple", "banana", "cherry")
print(
len(fruits))
"""

"""
fruits = ("apple", "banana", "cherry")
print(
fruits[-1])
"""

"""
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[
2:5])
"""

# Python Sets
"""
fruits = {"apple", "banana", "cherry"}
if "apple" 
in
 fruits:
  print("Yes, apple is a fruit!")
"""

"""
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

"""

"""
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

"""

"""
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

"""

"""
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

"""

# Python Dictionaries
"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(
car.get("model"))
"""

"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]
 = 
2020

"""

"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]

=

"red"

"""

"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

"""

"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

"""

# Python If...else
"""
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

"""

"""
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
"""

"""
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
"""

"""
if a > b: print("a is greater than b")
"""

"""
a = 2
b = 330
print("A") if a > b else print("B")
"""

"""
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
"""

"""
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
"""

"""
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
"""

"""
x = 65

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
"""

"""
a = 33
b = 200

if b > a:
  pass
"""
