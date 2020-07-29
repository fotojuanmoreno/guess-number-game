import random

def main():
	fails = 0
	number = 0
	cifra = 0
	
	number = random.randint(0, 100)
	
	print("He escogido un número entre 1 y 100.¿Podrás adivinar cual es?\nTienes 4 intentos:")
	
	while cifra != str(number):
		cifra = input("Introduce una cifra: ")
		try:
			if cifra == str(number):
				if fails == 0:
					print("\n¡WOW! A la primera. Impresionante.\n")
				else:
					print("¡Has acertado!")
			elif int(cifra) > number and fails < 3:
				print("Te has pasado. Intentalo otra vez.\n")
				fails = fails + 1
			elif int(cifra) < number and fails < 3:
				print("Demasiado bajo. Intentalo otra vez.\n")
				fails = fails + 1
			elif fails == 3:
				print("Has fallado 3 veces. Lo siento, pero el numero era " + str(number))
				break
		except ValueError:
			print("Error")
	rep = input("¿Quieres volver a intentarlo? y/n: \n")
	if rep != "n":
		main()

if __name__ == '__main__':
	main()