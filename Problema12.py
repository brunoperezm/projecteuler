def is_prime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		print '\t',f
	if n%f == 0: return False
	if n%(f+2) == 0: return False
	f +=6
	return True

x = 1
ultimo_num_triangular = 0
factores = 1
while factores<15:
	ultimo_num_triangular = ultimo_num_triangular + x
	for y in range(1,ultimo_num_triangular):
		z = 1
		if is_prime (y):
			division = ultimo_num_triangular
			
			while division%y==0:
				division =division/y
				z += 1
				pass
			pass
		factores = z * factores
		pass
	x += 1
	pass
print ultimo_num_triangular

