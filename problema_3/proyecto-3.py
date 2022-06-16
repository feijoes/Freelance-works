#!/usr/bin/env python3
import sys
import time
import random
from operator import itemgetter
from copy import deepcopy
from collections import Counter
from datetime import datetime

# TODO: Estudien el uso de Counter y Counter.most_common(...), el siguiente link es la referencia
# https://docs.python.org/3/library/collections.html#collections.Counter

# INSTRUCCIONES:
#     Sólamente deben implementar el código que falta donde
#     están las instrucciones TODO: <instrucciones...>
# NOTA:
#     Se recomienda que estudien el código para que aprendan más cosas
#     sobre el lenguaje Python.
	
CRLF = "\n"
SP = " "

dice = [ '1', '2', '3', '4', '5', '6' ]

def get_ones(dices, counter, most_common):
	cnt = 0
	# TODO: calcular el score para 'dices' según esta categoría
	#       y asignarlo a la variable cnt
	
	cnt += counter["1"] // most_common
	return cnt

def get_twos(dices, counter, most_common):
	cnt = 0
	# TODO: calcular el score para 'dices' según esta categoría
	#       y asignarlo a la variable cnt
	cnt += counter["2"]
	return cnt

def get_threes(dices, counter, most_common):
	cnt = 0
	# TODO: calcular el score para 'dices' según esta categoría
	#       y asignarlo a la variable cnt
	cnt += counter["3"]
	return cnt

def get_fours(dices, counter, most_common):
	cnt = 0
	# TODO: calcular el score para 'dices' según esta categoría
	#       y asignarlo a la variable cnt
	cnt += counter[most_common] * 4
	return cnt

def get_fives(dices, counter, most_common):
	cnt = 0
	# TODO: calcular el score para 'dices' según esta categoría
	#       y asignarlo a la variable cnt
	cnt += counter[most_common] *5
	return cnt

def get_sixes(dices, counter, most_common):
	cnt = 0
	# TODO: calcular el score para 'dices' según esta categoría
	#       y asignarlo a la variable cnt
	cnt += counter[most_common]
	return cnt

def get_chance(dices, counter, most_common):
	cnt = 0
	# TODO: calcular el score para 'dices' según esta categoría
	#       y asignarlo a la variable cnt
	return cnt

def get_three_of_a_kind(dices, counter, most_common):
	cnt = 0
	# TODO: calcular el score para 'dices' según esta categoría
	#       y asignarlo a la variable cnt
	return cnt

def get_four_of_a_kind(dices, counter, most_common):
	cnt = 0
	# TODO: calcular el score para 'dices' según esta categoría
	#       y asignarlo a la variable cnt
	return cnt

def get_five_of_a_kind(dices, counter, most_common):
	cnt = 0
	# TODO: calcular el score para 'dices' según esta categoría
	#       y asignarlo a la variable cnt
	return cnt

def get_short_straight(dices, counter, most_common):
	cnt = 0
	# TODO: calcular el score para 'dices' según esta categoría
	#       y asignarlo a la variable cnt
	if len(counter) == 4 and sorted(dices) == list(range(min(dices), max(dices)+1)): cnt+= 35
	return cnt

def get_long_straight(dices, counter, most_common):
	cnt = 0
	# TODO: calcular el score para 'dices' según esta categoría
	#       y asignarlo a la variable cnt
	if len(counter) == 6:
		if sorted(dices) == list(range(min(dices), max(dices)+1)):
			cnt+= 35
	return cnt

def get_full_house(dices, counter, most_common):
	cnt = 0
	# TODO: calcular el score para 'dices' según esta categoría
	#       y asignarlo a la variable cnt
	if most_common == 3:
		if len(counter) == 2:
			cnt += 40
	return cnt

# esta lista contiene las funciones para calcular los scores
# según cada categoría
scorefn = [ \
	get_ones, \
	get_twos, \
	get_threes, \
	get_fours, \
	get_fives, \
	get_short_straight, \
	get_three_of_a_kind, \
	get_chance, \
	get_four_of_a_kind, \
	get_sixes, \
	get_long_straight, \
	get_full_house, \
	get_five_of_a_kind \
]

# esta lista contiene el orden de valor de cada categoría
catfn = [0,1,2,3,4,10,7,6,8,5,11,12,9]

# s:       scores en la solución parcial actual
# r:       lista con rondas escogidas y no escogidas
# c:       lista con categorías escogidas y no escogidas
# i:       índice de categoría actual a considerar
# scores:  lista de listas con todos los scores de ronda posibles por categoría
# max_sum: lista con las sumas de scores máximos desde cada categoría hasta la última
# score:   mejor score actual
# choice:  scores de la mejor escogencia actual
# total:   score de la solución parcial actual a comparar con la mejor escogencia
#          que se ha encontrado hasta ahora
def find_score(s, r, c, i, scores, max_sum, score, choice, total):
	if i == 13:
		# si ya se escogieron todas las categorías
		if total > score:
			# si el total actual es mejor que el mejor score
			# entonces se sustituye este total como el mejor score
			# y la escogencia como los scores que lo componen
			score = total
			choice = deepcopy(s)
		# si no, el mejor score y la escogencia no cambian
		return score, choice

	# si el total actual no tiene posibilidad de superar el mejor score actual
	if total + max_sum[i] <= score:
		# se suspende la búsqueda en esta dirección y
		# el mejor score y la escogencia no cambian
		return score, choice
		# TIP: esto se hizo para optimizar la velocidad de la búsqueda

	# n = cantidad de scores en categoría actual
	n = len(scores[i])
	# indica si la categoría no se utilizó
	skipped_cat = True
	# iterar sobre los scores (idx) en la categoría actual (i)
	for idx in range(n):
		# obtener score->scr para ronda i->rnd y categoría idx->cat
		scr, rnd, cat = scores[i][idx]
		# si no se han agregado a la solución ni la ronda ni la categoría
		if not r[rnd] and not c[cat]:
			skipped_cat = False # se registra que la categoría sí se utiliza
			# se agregan a la solución 
			r[rnd] = True
			c[cat] = True
			# se agrega el score a la lista (scr, rnd, cat)
			s.append(scores[i][idx])
			# se acumula el score total de la solución parcial actual
			total += scr
			# se continúa buscando con las categorías que faltan (uso de i+1)
			score, choice = find_score(s, r, c, i + 1, scores, max_sum, score, choice, total)
			# como hay que intentar con los scores restantes para esta categoría
			# se deshacen los cambios previos a: total, s, r y c
			total -= scr
			s.pop()
			r[rnd] = False
			c[cat] = False
	# Si la categoría no se utilizó
	if skipped_cat:
		# intentar con las categorías restantes (por eso se usa i+1)
		score, choice = find_score(s, r, c, i + 1, scores, max_sum, score, choice, total)

	# retornar el mejor score encontrado
	return score, choice

def find_best_scores(dices):
	# listas de scores por categoría inicialmente vacías
	scores = [[] for x in range(13)]

	# iterar sobre las rondas
	for rnd in range(13):
		# obtener objeto Counter para la ronda
		cnt = Counter(dices[rnd])
		# obtener las veces que aparece el dado más común
		mc = cnt.most_common(1)[0][1]
		# iterar sobre las categorías
		for cat in range(13):
			# calcular el score para la ronda según cada categoría 
			score = scorefn[cat](dices[rnd], cnt, mc) # esto invoca funciones en la lista scorefn
			# si el score es positivo se agrega a la lista de scores de la categoría
			if (score > 0):
				scores[cat].append((score, rnd, cat))

	# iterar sobre las categorías
	for cat in range(13):
		# ordenar los scores de cada categoría por ronda (creciente) y score (descendiente)
		scores[cat].sort(key=itemgetter(1))
		scores[cat].sort(key=itemgetter(0), reverse=True)

	# calcular las sumas de los scores más altos desde cada categoría hasta la última categoría
	# TIP: esto es para evitar cálculos que no proporcionarán un score final mejor, porque ya
	#      se tiene una solución que supera cualquier solución aún no considerada
	max_sum = [0] * 13
	max_sum[12] = max(scores[12], key=itemgetter(0))[0] if len(scores[12]) > 0 else 0
	for i in range(11, -1, -1):
		m = max(scores[i], key=itemgetter(0))[0] if len(scores[i]) > 0 else 0
		max_sum[i] = max_sum[i+1] + m

	# buscar el mejor score posible
	max_score, best_choice = find_score([], [False]*13, [False]*13, 0, scores, max_sum, 0, [], 0)
	# recuperar el orden original de las categorías
	best_choice = [(s, r, catfn[c]) for (s, r, c) in best_choice]
	# ordenar por categorías
	best_choice.sort(key=itemgetter(2))
	# calcular bonificación
	choice = [0] * 15
	for ch in best_choice:
		choice[ch[2]] = ch[0]
	choice[13] = 35 if sum(choice[:6]) > 62 else 0
	# sumar los scores en el total
	choice[14] = sum(choice)
	# devolver la línea del mejor score para las rondas y categorías
	return " ".join([str(ch) for ch in choice]) + CRLF

def solve_games(input_file, output_file):
	n = 0
	scorefn.reverse()
	catfn.reverse()
	with open(input_file, "r") as inp:
		out = open(output_file, "w")
		games = inp.readlines()
		n = len(games) // 13
		for g in range(n):
			dices = [list(game[:-1]) for game in games[g * 13:g * 13 + 13]]
			choice = find_best_scores(dices)
			out.write(choice)
			out.flush()
		out.close()
	return n
		
def evaluate_games(solucion_txt, correcta_txt, n):
	with open(solucion_txt, "r") as resp, open(correcta_txt, "r") as sol:
		resp_lines = resp.readlines()
		sol_lines = sol.readlines()
		cnt = 0
		for i in range(len(resp_lines)):
			if (resp_lines[i] == sol_lines[i]):
				cnt += 1
		print("Nota = " + str(cnt * 100 / n) + "%")

def main(problema_txt, solucion_txt, correcta_txt):
	n = solve_games(problema_txt, solucion_txt)
	evaluate_games(solucion_txt, correcta_txt, n)

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2], sys.argv[3])

# Para sus pruebas puede descomentar la siguiente línea y
# sustituir las rutas de los archivos correspondientes
# main("ruta de problema.txt", "ruta de solucion.txt", "ruta de correcta.txt")
