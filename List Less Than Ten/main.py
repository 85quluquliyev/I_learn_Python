list = [

]

for i in range(5):
    i += 1
    number = int(input("For creating data, you have to write number: "))
    list.append(number)

for part in list:
    if part < 5:
        list.remove(part) 

print(list)

