motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[0])

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'shineray')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

poped_motorcycles = motorcycles.pop()
print(motorcycles)
print(poped_motorcycles)
