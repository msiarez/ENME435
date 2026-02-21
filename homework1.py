#Question 3
import random
doubles = 1
for i in range(10000):
  roll1 = random.randint(1,6)
  roll2 = random.randint(1,6)
  if roll1 == roll2:
    doubles += 1
percentage = (doubles / 10000) * 100
print("Percentage of doubles out of 10000 rolls is:{0:0.2f}%".format(percentage))
