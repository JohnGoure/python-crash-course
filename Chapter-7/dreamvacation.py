dream_vacation = {}

active = True

while active:
    username = input("What is your name? ")
    dream_vacation[username] = input(
        "If you could visit one place in the world, where would you go? "
    )
    more_users = input("Any more users? Yes/No ")
    if more_users.lower() == 'no':
        active = False

for user, place in dream_vacation.items():
    print(user + ": " + place)
