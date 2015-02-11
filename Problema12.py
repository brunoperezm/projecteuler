def is_prime(n):
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

#encontrar los factores de un numero
def factores(numero_original):
	n = numero_original
	post_n = numero_original
	divisor = 2
	factors = []
	if is_prime(numero_original) or numero_original == 1:
		return 2
	while True:
		if (is_prime(divisor) and n%divisor == 0):
			n = n/divisor
			factors.append(divisor)
		if (n%divisor != 0):
			divisor+=1
		if n==1:
			# Tenemos todos los factores primos
			# Ahora hay que averiguar la cantidad de veces que se repiten los factores, su multiplicidad
			last_divisor = sorted((factors))[0]
			multiplicidad = {}
			for x in sorted(factors):
				last_divisor = x
				if x==last_divisor:
					if x in multiplicidad:
						multiplicidad[x] += 1
					else:
						multiplicidad[x] = 1
			divisores_totales = 1
			for nums, exponentes in multiplicidad.iteritems():
				divisores_totales *= (exponentes+1)
			#print multiplicidad
			break
	return divisores_totales

x = 1
ultimo_num_triangular = 0
divisores = 1
while True:
	ultimo_num_triangular = ultimo_num_triangular + x
	x += 1
	if (factores(ultimo_num_triangular) > 499):
		print ultimo_num_triangular, divisores, factores(ultimo_num_triangular)
		break
