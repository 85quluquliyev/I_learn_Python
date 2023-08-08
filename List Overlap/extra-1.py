import random

a = []
b = []

for i in range(5):
    a.append(random.randint(0,9))
    i += 1

for i in range(5):
    b.append(random.randint(0,9))
    i += 1

print(a)
print(b)

new_a=[]
new_b=[]

same=[]

for i in a:
    if i not in new_a:
        new_a.append(i)
for i in b:
    if i not in new_b:
        new_b.append(i)

print('This list for the same number')
for i in new_b:
    for j in new_a:
        if i == j:
            same.append(i)

print(same)