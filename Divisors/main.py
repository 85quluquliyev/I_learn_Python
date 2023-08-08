number = int(input('Number: '))

divisor = list(range(2, number+1))
result = []

for i in divisor:
    if number % i == 0:
        result.append(i)
print(result)
