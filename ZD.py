ab = {'Swaroop' : 'swaroopch@byteofpython.info',
      'Larry' : 'larry@wall.org',
      'Matsumoto' : 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'}

print ("1、Swaroop's address is %s" %ab['Swaroop'])
# Adding a key/value pair


ab['Guido'] = 'guido@python.org'
# Deleting a key/value pair
del ab['Spammer']
print ('\n2、There are %s contacts in the address-book\n' % len(ab))


for name, address in ab.items():
    print ('3、Contact %s at %s' % (name, address))


if 'Guido' in ab: # OR ab.has_key('Guido')
    print ("\n4、Guido's address is %s" % ab['Guido'])