a = input('Digite algo: ')
print('O tipo primitivo de {} é'.format(a), type(a))
print('Só tem espaços?',a.isspace())
print('É um número?',a.isnumeric())
print('É alfabetico?',a.isalpha())
print('É alfanumerico?',a.isalnum())
print('Está em maiusculo?',a.isupper())
print('Está em minusculo?',a.islower())
print('Está capitalizada?',a.istitle())