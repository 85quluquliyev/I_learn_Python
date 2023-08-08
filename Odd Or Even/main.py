# We will get number for finding it is odd or even

print('Hi! Today we will try to find number which you write for us is odd or even')
number = int(input('Write number: '))

#There is Modulus in Math. We can use this topic for solving current problem 

if number % 2 == 0:
    print(str(number) + " is even")
else:
    print(str(number) + " is odd")

