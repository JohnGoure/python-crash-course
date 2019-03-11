pepperoni = 'pepperoni'
sausage = 'sasauge'
toppings = ["pepperoni", "sasauge", "supreme", "mushrooms"]

print("Is pizza topping == 'pepperoni'? I predict True.")
print(pepperoni == 'pepperoni')
print(pepperoni == 'sasuage')

if (len(toppings) > 3):
    print("There are a lot of toppings.")

if (pepperoni in toppings and sausage in toppings):
    print(pepperoni + " and " + sausage + " in toppings")

if ("anchovie" not in toppings):
    print("I hate anchovies!")
