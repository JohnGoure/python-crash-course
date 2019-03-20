try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
    filename = "error_log.txt"
    with open(filename, 'a') as file_object:
        file_object.write("User tried dividing by zero.\n")
