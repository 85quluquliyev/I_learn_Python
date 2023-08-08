a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_a=[]
new_b=[]

for i in a:
    if i not in new_a:
        new_a.append(i)
for i in b:
    if i not in new_b:
        new_b.append(i)


for i in new_b:
    for j in new_a:
        if i == j:
            print(i)