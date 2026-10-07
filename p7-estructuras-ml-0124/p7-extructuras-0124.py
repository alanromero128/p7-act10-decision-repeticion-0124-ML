print("Alan Romero NC = 0124")

print("Python Conditions and If statements")
print("Ejemplo 1")
a = 33
b = 200
if b > a:
  print("b is greater than a")
print("Ejemplo 2")
number = 15
if number > 0:
  print("The number is positive")

#-------------------------------------------------
print("Python if elif")
print("Ejemplo 1")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
print("Ejemplo 2")
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
#-------------------------------------------------
print("Python if else")
print("Ejemplo 1")
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  a = 200
b = 33
print("Ejemplo 2")
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#-------------------------------------------------
print("Python loops")
print("Ejemplo 1")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  print("Ejemplo 2")
for x in "banana":
  print(x)
#-------------------------------------------------
print("Python while loops")
print("Ejemplo 1")
i = 1
while i < 6:
  print(i)
  i += 1
print("Ejemplo 2")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print("Alan Romero NC = 0124")