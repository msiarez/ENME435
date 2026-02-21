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
w = float(input("Input value for w: "))
x = float(input("Input value for x: "))
y = float(input("Input value for y: "))
z = float(input("Input value for z: "))

min1 = min(w, x)
min2 = min(y, z)

if w == min1:
    w = min2
else:
    x = min2

if y == min2:
    y = min1
else:
    z = min1

print("Final values: w =", w, "x =", x, "y =", y, "z =", z)
