#Question 3
import random

doubles = 1
for i in range(10000):
  roll1 = random.randint(1,6)
  roll2 = random.randint(1,6)
  if roll1 == roll2:
    doubles += 1
    
percentage = (doubles / 10000) * 100
print("Percentage of doubles out of 10000 rolls is: {0:0.2f}%".format(percentage))

#Question 4
w = int(input("Input value for w: "))
x = int(input("Input value for x: "))
y = int(input("Input value for y: "))
z = int(input("Input value for z: "))

if w < x:
  min1 = w
  max1 = x
else:
  min1 = x
  max1 = w
  
if y < z:
  min2 = y
  max2 = z
else:
  min2 = z
  max2 = y

min1, min2 = min2, min1

if w < x:
  w = min1
else:
  x = min1

if y < z:
  y = min2
else:
  z = min2

print("w =", w, "x =", x, "y =", y, "z =", z)

#Question 5
numbers = []

for i in range(10):
  num = int(input("Enter number {i+1}/10: "))
  list.append(num)

sort = sorted(sort(list))

print("The 2 smallest numbers are:", sort[:2])
