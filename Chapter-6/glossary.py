python_terms = {
    'statment': 'The value assigned to a variable.',
    'list': 'A sequential group of objects.',
    'datatype': 'A definition for the value stored in an object.',
    'assigment': 'When a value is set to a variable.',
    'variable': 'An object that stores a value.'
}

for key, value in python_terms.items():
    print(key + ': ' + value)

major_rivers = {
    'nile': 'egypt',
    'colorado': 'united states of america',
    'missippi': 'united states of america'
}

for river, country in major_rivers.items():
    print('The ' + river.title() + ' runs through ' + country.title())

for river in major_rivers.keys():
    print(river)

for country in major_rivers.values():
    print(country)
