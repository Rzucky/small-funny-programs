# print('started')


#################Loadanje filea
print('Unesite ime datoteke:')
path = input()

# path += '.txt'


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

########################## trazenje najduljeg

def modifiedDFS(start, current, poss):
	#global poss

	#ako dodemu u istu ali da nije start odmah
	if current == start:
		for k in poss:
			if k == 1:
				return 0

	#jako malen broj zbog max funkcije
	output = -999999999999999999999999999999999

	# output = 0
	# counter = 0
	noviposs = []
	#prepisujemo da bi se izbjegle greske
	for z in range(n):
		noviposs.append(poss[z])

	#puni listu popunjenih koje smo obisli sa jedinicama
	if start != current:
		noviposs[current] = 1

	#prolazak po dodirnim tockama svakog nodea i pozivamo dfs nad svakim od njih
	for j in range(n):
		#ako su 1 u listalista i nisu posjeceni
		if listalista[current][j] == 1 and noviposs[j] == 0:

			# if start != current:
			# 	noviposs[j] = 1

			# counter += 1
			# if counter > output:
			# 	output = counter
			#output2 = max(output, modifiedDFS(start, j, noviposs))

			#provjera dal li su veci od max
			output = max(output, modifiedDFS(start, j, noviposs) + 1)

	return output

######## main



najjaci = 0
posjeceni = 0

#svaka startna tocka
for i in range(n):

	output = 0
	#punimo nulama
	posjeceni = [0 for i in range(n)]


	#output izlazak rezultat max 
	output = modifiedDFS(i, i, posjeceni)

	
	#posjeceni = None

	if output > najjaci:
		najjaci = output

	#ne smije imati najdulji ciklus od 2 tocke
	if najjaci == 2:
		najjaci = 0

print(najjaci)
#ostavljena velika kolicina pogresnog koda da se vidi proces testiranja
