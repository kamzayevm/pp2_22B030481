# Lists exercises

# 1
"""
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

"""
# 2
"""
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)
"""
# 3
"""
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
"""
# 4
"""
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
print(fruits)
"""

# 5
"""
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)
"""

# 6
"""
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
"""

# 7
"""
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
"""

# 8
"""
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
"""

# Python Tuples

# 1
"""
fruits = ("apple", "banana", "cherry")
print(fruits[0])
"""

# 2
"""
fruits = ("apple", "banana", "cherry")
print(len(fruits))

"""

# 3
"""
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
"""

# 4
"""
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
"""

# Python Sets

# 1
"""
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
"""

# 2
"""
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
"""

# 3
"""
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)
"""

# 4
"""
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
"""

# 5
"""
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)
"""

# Python Dictionaries

# 1
"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
"""

# 2
"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
print(car)
"""

# 3
"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
print(car)
"""

# 4
"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)
"""

# 5
"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)
"""

# Python While

# 1
"""
i = 1
while i < 6:
 print(i)
 i += 1
"""

# 2
"""
i = 1
while i < 6:
  if i == 3:
    break
  i += 1
"""

# 3
"""
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
"""

# 4
"""
i = 1
while i < 6:
  print(i)
  i += 1
else:

  print("i is no longer less than 6")
"""

# Python For

# 1
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
 print(x)
"""

# 2
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":

continue

  print(x)
"""

# 3
"""
for x in range(6):
  print(x)
"""

# 4
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
   break
  print(x)
"""
