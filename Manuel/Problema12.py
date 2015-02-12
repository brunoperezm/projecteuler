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
x = 1
ultimo_num_triangular = 0
condition = True
factores = 1
while factores <= 100:
	factores = 1
	ultimo_num_triangular = ultimo_num_triangular + x
	for y in range(2,ultimo_num_triangular+1):
		z = 1
		if isprime (y):
			division = ultimo_num_triangular
			while division%y == 0:
				division = division/y
				z += 1
				pass
			pass
		factores = z * factores
		pass
	x += 1
	pass
print (ultimo_num_triangular)
