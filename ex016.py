n = input('nos diga seu nome')
d = int(input('a quantos dias você está com o carro?'))
km= float(input('quantos km você rodou com o carro nesses {} dias?'.format(d)))
di = 60*d
ki = 0.15*km
print ('{}, você irá pagar um total de R$:{}'.format(n, di+ki))