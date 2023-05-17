people = [
    {
        'name' : 'Foo Bear',
        'email' : 'abcd@gmail.com'

    },
    {
        'name' : 'Qux Bar',
        'email' : 'dcba@gmail.com',
        'address' : 'Borg, Country',
        'children' : [
            'Alpha',
            'Beta'
        ]
    }

]

print(people)
print(people[0]['name'])
print(people[1]['children'][0])

print(list(map(lambda p: p['name'], people)))