filename = 'user_responses.txt'

while(True):
    response = input(
        'Why do you like programming?' +
        '(enter Q, to quit the program) ')
    if response == 'Q':
        break
    with open(filename, 'a') as file_object:
        file_object.write(response + "\n")
