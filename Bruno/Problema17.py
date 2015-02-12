"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

numeros_1_20 = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19:"nineteen"}
numeros_20_90 = {0: "", 10: "ten",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
def contar_letras(n):
	ultima_palabra = ""
	for x in range(n):
		if x<20:
			ultima_palabra += numeros_1_20[x]#+"\n"
		elif x<100 and x%10 == 0:
			#es 10 20 30 40 etc
			ultima_palabra += numeros_20_90[x]#+"\n"
		elif x<100:
			ultima_palabra += numeros_20_90[int(str(x)[0])*10] + numeros_1_20[int(str(x)[1])]#+"\n"
		elif x<1000 and x%100 == 0:
			ultima_palabra += numeros_1_20[int(str(x)[0])]+"hundred"#+"\n"
		elif x<1000 and x-(int(str(x)[0])*100) < 20:
			ultima_palabra += numeros_1_20[int(str(x)[0])]+"hundredand"+numeros_1_20[x-(int(str(x)[0])*100)]#+"\n"
		elif x<1000: 
			ultima_palabra += numeros_1_20[int(str(x)[0])]+"hundredand"+numeros_20_90[int(str(x)[1])*10] + numeros_1_20[int(str(x)[2])]#+"\n"
		elif x==1000:
			ultima_palabra += "onethousand"
	return ultima_palabra
print len(contar_letras(1001))