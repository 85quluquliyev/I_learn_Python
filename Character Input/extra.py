# This data is consist of Guests' name.

guests = [
    'Oliver','Jake','Noah','Amelia','Emily','Ava',
    'George','David','Mary','David','Susan',
    'Isla','Oscar','Ethan','Linda'
    ]
new_guests = [

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
    print("Sorry, your name is not in our Guests' list. If you want, I can ask our Host")
    want = input("Dou you want to join us? If you answer is yes, write 1: ")
    if want == '1':
        print('Ooo Welcome, It is nice to see you here.')
        print('-----------------------------------------')
        print("Our Guests's list")
        new_guests.append(name)
        guests.extend(new_guests)
        for person in guests:
            print(person)
        chance = input('You are in our list. If you want we can remove you? Your answer is yes, write 1: ')
        if chance == '1':
            print('You were removed.')
            print('-----------------------------------------')
            print("Our Guests's list")
            guests.remove(name)
            for person in guests:
                print(person)  
        else:
            print('Have good day')  
    else:
        print('Have good day')
        
        