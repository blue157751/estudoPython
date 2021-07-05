from math import hypot
co = float(input('cumprimento do cateto oposto'))
ca = float(input('cumprimento do cateto adjacente'))
hi =hypot(co,ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))
