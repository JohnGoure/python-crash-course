threes = list(range(3, 31, 3))
print("The first three items in the list are: ")
for x in threes[:3]:
    print(x)

print("Three items from the middle of the list are: ")
for x in threes[len(threes)//2 - 2:len(threes)// 2 + 1]:
    print(x)
print("The last three items in the list are: ")
for x in threes[-3:]:
    print(x)