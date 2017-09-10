import random
import statistics

number_size = random.randint(15, 20)

numbers = list()

for _ in range(number_size):
    numbers.append(random.randint(10, 20))

print (numbers)
numbers.sort()
print ("numbers = ", numbers)
print ("number_size = ", number_size)

# half_size = len(numbers) // 2

median = None

if len(numbers) % 2 == 1:
    median = numbers[number_size // 2]
else:
    median = (numbers[number_size // 2] + numbers[number_size // 2 + 1]) / 2

print(median)
print(statistics.median(numbers))