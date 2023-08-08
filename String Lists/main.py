string = input("Write something: ").upper()

reverse_string = string[::-1]

if reverse_string == string:
    print('This string is a Palindrome')
else:
    print('This string is not a Palindrome')
