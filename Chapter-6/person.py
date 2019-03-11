person_I_Know = {
    'first': 'Destiny',
    'last': 'Deleon',
    'age': 22,
    'city': 'san antonio'
    }

person2 = {
    'first': 'Roy',
    'last': 'Deleon',
    'age': 54,
    'city': 'victoria'
}
person3 = {
    'first': 'Tina',
    'last': 'Deleon',
    'age': 52,
    'city': 'victoria'
}

people = [person_I_Know, person2, person3]

for person in people:
    print('\n')
    for trait, value in person.items():
        print(trait.title() + ': ' + str(value).title())

print('\n')

buddy = {
    'kind': 'dog',
    'owner': 'felicia'
    }

duke = {
    'kind': 'dog',
    'owner': 'jeff'
    }

wiggles = {
    'kind': 'dog',
    'owner': 'john'
    }

pets = [buddy, duke, wiggles]

for pet in pets:
    for kind, owner in pet.items():
        print(kind + ' ' + owner)

print('\n')

cities = {
    'austin': {
        'country': 'united states',
        'population': '7 million',
        'fact': 'texas state capital'
    },
    'la': {
        'country': 'united states',
        'population': '12 million',
        'fact': 'by the beach'
    },
    'tahoe': {
        'country': 'united states',
        'population': '5000',
        'fact': 'it is beautiful'
    }
}

for city, info in cities.items():
    print(city.title() + ':')
    for key, value in info.items():
        print('\t' + key.title() + ': ' + value.title())
