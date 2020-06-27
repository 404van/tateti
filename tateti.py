#FALTA HACER QUE PASE DE UN JUGADOR A OTRO!!!!



tablero=["-","-","-",
			 "-","-","-",
			 "-","-","-"]

winner_cond1 = ["X","X","X"]

winner_cond2 = ["O","O","O"]


def mostrar_tablero():
	print("|",tablero[0],"|",tablero[1],"|",tablero[2],"|		|0|1|2|")
	print("|",tablero[3],"|",tablero[4],"|",tablero[5],"|		|3|4|5|")
	print("|",tablero[6],"|",tablero[7],"|",tablero[8],"|		|6|7|8|")
	jugar()

def jugar():
	caracter = input("Ingrese X o O: ")
	posicion = int(input("posicion: "))
	tablero[posicion] = caracter
	check_filas()
	

def check_filas():
	fila1 = [tablero[0],tablero[1],tablero[2]]
	fila2 = [tablero[3],tablero[4],tablero[5]]
	fila3 = [tablero[6],tablero[7],tablero[8]]
	
	if fila1 == winner_cond1 or fila2 == winner_cond1 or fila3 == winner_cond1:
		print("GANADOR LAS X")
		print(tablero)
	elif fila1 == winner_cond2 or fila2 == winner_cond2 or fila3 == winner_cond2:
		print("GANADOR LAS O")
		print(tablero)
	else: check_columnas()
	

def check_columnas():
	'''checkeo las columnas'''

	columna1 = [tablero[0],tablero[3],tablero[6]]
	columna2 = [tablero[1],tablero[4],tablero[7]]
	columna3 = [tablero[2],tablero[5],tablero[8]]

	if columna1 == winner_cond1 or columna2 == winner_cond1 or columna3 == winner_cond1:
		print("GANADOR LAS X")
		print(tablero)
	elif columna1 == winner_cond2 or columna2 == winner_cond2 or columna3 == winner_cond2:
		print("GANADOR LAS O")
		print(tablero)
	else: check_diagonales()

def check_diagonales():
	'''checkeo las columnas'''
	diagonal1 = [tablero[0],tablero[4],tablero[8]]
	diagonal2 = [tablero[2],tablero[4],tablero[6]]

	if diagonal1 == winner_cond1 or diagonal2 == winner_cond1:
		print("GANADOR LAS X")
		print(tablero)
	elif diagonal1 == winner_cond2 or diagonal2 == winner_cond2:
		print("GANADOR LAS O")
		print(tablero)
	else: mostrar_tablero()

check_filas()







