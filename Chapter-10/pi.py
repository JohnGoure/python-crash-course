filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = '031587'
if birthday in pi_string:
    print("Your birthday is in pi")
else:
    print("Your birthday is not in the first million digits of pi")
