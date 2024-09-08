#dictionaries

capitals = {'USA':'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

#print(capitals['Germany'])

#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
print(capitals.items())

for x,y in capitals.items():
    print(x, y)

capitals.update({'Germany':'Berlin'})
capitals.pop('China')
capitals.clear()    