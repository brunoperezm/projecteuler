a = 9
for x in range(1,11):
	b = 9
	for y in range(1,11):
		c = 9
		for z in range(1,11):
			palindromo = 1100*c+10010*b+100001*a
			m = 999
			while m>= palindromo**(0.5):
				if palindromo%m == 0:
					print (palindromo)
					print (m)
					import sys
					sys.exit('listo')
					pass
				m-=1
				pass
			c -= 1
			pass
		b -= 1
		pass
	a -= 1
	pass
'''
b = 9
for y in range(1,11):
	c = 9
	for z in range(1,11):
		palindromo = 110*c+1001*b
		m = 99
		while m>= palindromo**(0.5):
			if palindromo%m == 0:
				print (palindromo)
				print (m)
				import sys
				sys.exit('listo')
				pass
			m-=1
			pass
		c -= 1
		pass
	b -= 1
	pass
	'''