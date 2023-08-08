number = int(input('Number: '))

divisor = list(range(2, number+1))
result = []

for i in divisor:
    if number % i == 0:
        result.append(i)

if len(result) == 1:
    print('This is Prime number')
else:
    print('This is not prime number')
    print(result)
