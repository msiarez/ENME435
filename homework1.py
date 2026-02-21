#Question 3
import random

doubles = 1
for i in range(10000): #rolls the dice 10000 times
  roll1 = random.randint(1,6) #random roll for dice 1
  roll2 = random.randint(1,6) # random roll for dice 2
  if roll1 == roll2: #compares the rolls to see if there is a double
    doubles += 1
    
percentage = (doubles / 10000) * 100 #calculates the percentage of doubles out of 10000
print("Percentage of doubles out of 10000 rolls is: {0:0.2f}%".format(percentage))

#Question 4
w = int(input("Input value for w: "))
x = int(input("Input value for x: "))
y = int(input("Input value for y: "))
z = int(input("Input value for z: "))

if w < x: #checks if w is less than x and if so sets w as the first min value
  min1 = w
else: #sets x as the first min value if x is smaller
  min1 = x
  
if y < z: #checks if y is less than z and if so sets y as the second min value
  min2 = y
else: #sets z as the second min value if z is smaller
  min2 = z

min1, min2 = min2, min1 #switches the min values

#now sets the switched min value back to the smallest variables
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

#puts the 10 values entered into the numbers list
for i in range(10):
  num = int(input(f"Enter number {i+1}/10: "))
  numbers.append(num)

numbers = sorted(set(numbers)) #set gets rid of the duplicates and sorted returns the set back to a list from least to greatest

print("The 2 smallest numbers are:", numbers[:2]) #prints the first 2 values of the list

#Question 6
x = int(input("Enter a number: "))

#prints all of the As for how large x is on the same line
for i in range(x):
    print("A", end="")
print()

#Question 7
import random

for i in range(50): #does 50 lines
  line = 10 + i #first line starts at 10 but adds one more digit for each line ending with the last line having 59 digits
  for n in range(line): #prints the number of random values either 0 or 1 for how long the line should be
    print(random.randint(0,1), end="")
  print()

#Question 8
count = 0 #counts number of values entered
less = False

while True: #allows user to keep entering values from 1-10 until 5 is entered
  num = int(input("Enter number from 1 to 10: "))
  count += 1
  if num == 5: #stops the loop if 5 is entered
    break
  if num < 3: #if a value entered is less than 3 changes boolean to True
    less = True

#checks if boolean is False and if so prints no, prints yes if boolean is True, also prints the number of values entered
if less == False:
  print("Numbers entered: ", count, "no")
else:
  print("Numbers entered: ", count, "yes")
