from math import floor
x = 2**1000
digito = 0
suma = 0
y = 301
resto = 0
digitoelevado = 0
while y >= 0:
	resto = x%10**y
	digitoelevado = x-resto
	digito = digitoelevado/10**y
	suma = digito + suma
	x = resto
	y-=1
	pass
print suma
