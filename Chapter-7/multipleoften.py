user_number = input(
    "Please enter a number and" +
    " I will see if it is a multiple of ten: "
)

if int(user_number) % 10 == 0:
    print(user_number + " is a multiple of ten.")
else:
    print(user_number + " is not a multiple of ten.")
