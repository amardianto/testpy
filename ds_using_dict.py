# 'ab' is short for 'a'ddress'b'ook

ab = {
    'Agus' : 'agus@agustus.com',
    'Bayu' : 'bayu@angin.net',
    'Chika' : 'chika@makmur.co.id',
    'Dewi' : 'dewilaras@merbabu.com'
    }

print("Agus's address is", ab['Agus']) #Agus haruf A kapital

# Deleting a key-value pair

del ab['Dewi']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# Adding key-value pair
ab['Diana'] = 'diana@muslimah.com'

if 'Diana' in ab:
    print("\nDiana's address is", ab['Diana'])
