motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'harley')
print(motorcycles)
print('Deleting Honda at position 0')
del motorcycles[0]
print(motorcycles)
print(motorcycles.pop(0))
if motorcycles.__contains__('yamaha'):
    motorcycles.remove('yamaha')
    print(motorcycles)