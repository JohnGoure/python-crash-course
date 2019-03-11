dinner_group_size = input("How many people are in your dinner group, please? ")

if int(dinner_group_size) > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")
