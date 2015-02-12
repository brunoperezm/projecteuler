def isprime(n):
	if n!=2 and n%2==0:
		return False
		pass
	if n!=3 and n%3==0:
		return False
		pass
	if n!=5 and n%5==0:
		return False
		pass
	if n!=7 and n%7==0:
		return False
		pass
	if n!=11 and n%11==0:
		return False
		pass
	if n!=13 and n%13==0:
		return False
		pass
	if n!=17 and n%17==0:
		return False
		pass
	if n!=19 and n%19==0:
		return False
		pass
	#check if integer n is a prime
	# range starts with 2 and only needs to go up the squareroot of n
	for x in range(2, int(n**0.5)+1):
		if n % x == 0:
			return False
	return True
x = 2
ultimo_num_triangular = 0
condition = True
factores = 1
factoresanterior = 1
factoresfinal = 1
while factoresfinal <= 500:
	factores = 1
	y=2
	while y<=x:
		z = 1
		if y == 2 and x%2==0:
			z = 0
			pass
		if isprime (y) and x!=1:
			division = x
			while division%y == 0:
				division = division/y
				z += 1
				pass
			pass
		y+=1
		factores = z * factores
		pass
	factoresfinal=factores*factoresanterior
	factoresanterior = factores
	x += 1
	pass
print ((x-2)*(x-1)/2)