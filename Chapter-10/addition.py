print("This program will add together 2 numbers.")
print("Input q when you want to quit the program.")

while(True):
    numberOne = input()
    if numberOne == 'q':
        break
    numberTwo = input()
    if numberTwo == 'q':
        break
    try:
        int(numberOne)
    except ValueError:
        print(numberOne + " did not contain only numbers.")
    else:
        try:
            int(numberTwo)
        except ValueError:
            print(numberTwo + " did not contain only numbers.")
        else:
            print(int(numberOne) + int(numberTwo))
