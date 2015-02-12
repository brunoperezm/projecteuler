n = 2
mayor = 0
mayorn = 0
while n<=1000000:
	x=0
	proximon = n
	while proximon > 1:
		if proximon%2 == 0:
			proximon = proximon /2
		else :
			proximon = proximon+proximon+proximon+1
			pass
		x+=1
		pass
	print (n,x)
	if x>mayor:
		mayor = x
		mayorn = n
		pass
	n+=1
	pass
print (mayor)
print (mayorn)