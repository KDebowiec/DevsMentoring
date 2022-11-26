# Napisz program generujący wszystkie możliwe kombinacje liczb 4-cyfrowych, np. 1000, 1001, 1002, ..., 9999.
thousands = []
hundreds = []
tens = []
numbers = []
combinations = []


for i in range(1000, 10000, 1000):
    thousands.append(i)

for i in range(0, 1000, 100):
    hundreds.append(i)

for i in range(0, 100, 10):
    tens.append(i)

for i in range(0, 10):
    numbers.append(i)

for i in thousands:
    for y in hundreds:
        for z in tens:
            for x in numbers:
                combinations.append(i + y + z + x)
print(combinations)