filename = 'alice.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " was not found."
    print(msg)
else:
    print(filename + " contains " + str(len(contents.split())) + " words.")
