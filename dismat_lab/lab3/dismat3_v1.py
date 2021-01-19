import random	
#print('started')

#################Loadanje filea
print('Unesite ime datoteke:')
path = input()

#path += '.txt'


file = open(path, 'r')

##########loadnanje broja nodeova
n = int(file.readline())

file.readline() #preskakanje prazne linije

################Loadanje listi listi

listalista = []

for i in range(n):
	line = file.readline().split(' ')

	#micemo nove redove
	#line[n] = line[n].replace('\n', '')
	# print(line)
	# print('\n')

	#pojedinacni red
	lista = []

	# for j in range(n):
	# 	lista[j].append(line[j])
	# 	print(lista[j])

	#prvo ih punimo nulama da bi kasnije mogli dodavati
	for j in range(n):
		lista.append(0)

	for j in range(n):
		lista[j] += int(line[j])
		#print(lista[j])

	listalista.append(lista)
#print(listalista)

################Loadanje listi listi OVER

def full(n):
	for i in range(n):
		for j in range(n):
			if listalista[i][j] != 1 and i != j:
				return False

	return True


def greedy(current):
	lista = listalista[current]
	#print(f'Dodirne tocke vrha {current} su:')
	#print(lista)
	tempcolor = []
	# for j in range(n):
	# 	tempcolor.append(0)


	#dodirne tocke
	for j in range(n):
		if listalista[current][j] == 1:

			tempcolor.append(j)

	#print(f'pozicije koje tocka {current} dodiruje:')
	#print(tempcolor)
	zabranjeneboje = set()

	#idemo po svim dodirnim tockama
	for j in range(len(tempcolor)):

		#ako je tocka nepobojana
		if colors[int(tempcolor[j])] != 0:
			#dodajemo sve dodirne boje

			#zabranjeneboje.append(colors[int(tempcolor[j])])
			zabranjeneboje.add(colors[int(tempcolor[j])])

	#print(f'dodirne boje {zabranjeneboje}')
	#print(zabranjeneboje)
	#zabranjeneboje.sort()
	#print(zabranjeneboje)

	for i in range(1,n):
		#print(i)
		if i not in zabranjeneboje:
			colors[current] = i
			break


	#print(colors)
	#print('')


		# if int(tempcolor[j]) in colors:
		# 	print(f'{tempcolor[j]} is in colors')
		# else:
		# 	colors[int(tempcolor[j])] = int(tempcolor[j])
		# 	#colors.append(int(tempcolor[j]))
		# 	print(f'dodan {tempcolor[j]}')

	
	#colors[current] = str(current) + 'a'
	


#main

#colors
colors = []
min = -1
for i in range(n):
	colors.append(0)


sufle = []
for i in range(n):
	sufle.append(i)

for i in range(n):
	greedy(i)

min = max(colors)
#print(min)
for i in range(500):
	colors = []
	for i in range(n):
		colors.append(0)

	random.shuffle(sufle)
	for j in sufle:
		greedy(j)
	k = max(colors)
	#print(f'k je {k}')
	#print(f'min je {min}')
	if k < min:
		min = k

if (full(n)):
	min = n

#print(colors)
print(min)
#print('end')