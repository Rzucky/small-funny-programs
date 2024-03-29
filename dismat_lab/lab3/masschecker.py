import linecache
import random

print('Started')

#Greedy algorith goes over nodes/vertices in a given order,
# checks if his neighbours which with whom it shares an edge are colored
# and colores it with the lowest possible colour it can,
# can produce a larger number then the lowest chromatic number
def greedy(listalista, current, n, colors):
	
	tempcolor = []
	
	#touched colours
	for j in range(n):
		if listalista[current][j] == 1:

			tempcolor.append(j)

	zabranjeneboje = set()
	#iterating through touched colours
	for j in range(len(tempcolor)):

		#if the node is colored
		if colors[int(tempcolor[j])] != 0:

			#adding all touched colours
			zabranjeneboje.add(colors[int(tempcolor[j])])

	#adding the smallest possible 
	for i in range(1,n):
		if i not in zabranjeneboje:
			colors[current] = i
			break


#only for full graph where every node touches every other one
def full(listalista, n):
	
	for i in range(n):
		for j in range(n):
			if listalista[i][j] != 1 and i != j:
				return False

	return True

#main function
def mein(path):

	file = open(path, 'r')

	#loading number of nodes
	n = int(file.readline())

	#skipping empty line
	file.readline() 

	#loading a list of lists of the adjacency matrix
	listalista = []

	for i in range(n):
		line = file.readline().split(' ')

		#each individual line
		lista = []

		#filling them with zeroes so we can change it later
		for j in range(n):
			lista.append(0)

		for j in range(n):
			lista[j] += int(line[j])

		listalista.append(lista)

	#if printing of whole matrix is necessary
	#print(listalista)

#######list loading over

	#main inputing to greedy starts here
	colors = []
	min = -1
	for i in range(n):
		colors.append(0)

	#sufle is used for shuffling 
	sufle = []
	for i in range(n):
		sufle.append(i)

	#testing greedy with normal 0->n order
	for j in range(n):
		greedy(listalista, j, n, colors)

	#firstly finding a minimal one in order 0->n
	min = max(colors)
	
	#shuffling m times for a permutation where there is a chance
	#for a better number, with the high enough number of m 
	m = 1000
	for i in range(m):
		colors = []
		for i in range(n):
			colors.append(0)

		#trying with random shuffles
		random.shuffle(sufle)
		for j in sufle:
			greedy(listalista, j, n, colors)

		k = max(colors)

		#finding the smallest one 
		if k < min:
			min = k

	#checking for the full graph
	if (full(listalista,n)):
		min = n

	#returning the smallest number of m permutations
	return min
	
#function for comparing solutions, needed when taking different paths
def checker(path, i):

	#reading solution from file
	line = linecache.getline('kromatskiBrojevi.txt', i)
	s = line[6:].strip()
	k = mein(path)
	#comparing results
	rez = 'Yes' if int(s) == k else 'No'
	print(f'File {path} - solution: {s} - mine: {k} - Correct: {rez}')


#going through 01-44 files, first 35 by ZPM; 36-44 by kluki
for i in range(1,44):
	path = str(i)
	k = 0
	#number 1-9 need 0 in front
	if i < 10:
		path = '0' + path

	path += '.txt'
	checker(path, i)

#checking through hardcore examples
hc_list = ['hc15.txt','hc20.txt','hc30.txt','hc37.txt','hc64.txt']
i = 46
for h in hc_list:
	checker(h, i)
	i+=1
