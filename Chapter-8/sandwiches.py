def sandwich_toppings(**toppings):
    sandwich = {}
    for key, topping in toppings.items():
        sandwich[key] = topping
    print("The customer would like a sandwich with:")
    print(sandwich)

toppings = {
    'meat': 'turkey', 'vegies': ['onion', 'lettuce'],
    'cheese': 'american', 'sauce': 'mayo'
    }
sandwich_toppings(
    meat='turkey', vegies=['onion', 'lettuce'],
    cheese='american', sauce='mayo'
    )
