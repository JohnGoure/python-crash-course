sandwich_orders = [
    'turkey', 'ham', 'roast beef',
    'pastarami', 'pastarami', 'pastarami']
finished_sandwiches = []
print("The restraunt has ran out of pastarami sandwiches!")

while 'pastarami' in sandwich_orders:
    sandwich_orders.remove('pastarami')

for sandwich in sandwich_orders:
    print("I made your " + sandwich + ".")
    finished_sandwiches.append(sandwich)

print("The orders I finished are:")
for sandwich in finished_sandwiches:
    print(sandwich + " sandwich")
