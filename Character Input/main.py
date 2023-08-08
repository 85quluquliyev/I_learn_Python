# This data is consist of Guests' name.

guests = [
    'Oliver','Jake','Noah','Amelia','Emily','Ava',
    'George','David','Mary','David','Susan',
    'Isla','Oscar','Ethan','Linda'
    ]

# We can get response from user and our response has to be flexible.
name = input('Please, Can you say your name to us: ').capitalize()

# This is our boolean variables which is used for informing user.
answer = False

# Loop help us to check that there is user's response in our data.
for guest in guests:
    if guest == name:
        answer = True
    else:
        answer = False

if answer == True:
    print('Ooo Welcome, It is nice to see you here.')
else:
    print("Sorry, your name is not in our Guests' list. You cannot join us")