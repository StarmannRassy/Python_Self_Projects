# In this project we would use string concatenation
# these are few ways to use string concatenation

# name = Erasmus
# 1. print('i am called ' + name)
# 2. print('i am called {}'.format(name))
# 3. print(f'i am called {name}')

adj = input('Adjective: ')
verb1 = input('verb: ')
verb2 = input('verb: ')
famous_person = input('famous_person: ')

madlib = f"Computer programming is so {adj}! It makes me so exicited\
 all the time because I love to {verb1}. Stay hydrated and {verb2}\
 like you are {famous_person}!"

print(madlib)