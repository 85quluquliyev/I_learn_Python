# We will get number for finding it is odd or even

print('Hi! Today we will try to find number which you write for us is odd or even')
number = int(input('Write number: '))

#There is Modulus in Math. We can use this topic for solving current problem 

#If the number is a multiple of 4, I will print out a different message.
signal = False

if number % 4 == 0:
    print('I will give you extra information, this number is a multiple of 4 ')
    signal = True

if number % 2 == 0:
    if signal is True:
        print(str(number) + " is also even")
    else:
        print(str(number) + " is even")
else:
    print(str(number) + " is odd")

