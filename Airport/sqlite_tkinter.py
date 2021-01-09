from tkinter import *
from tkinter.messagebox import *
import sqlite3

conn = sqlite3.connect('ZračnaLuka.db')
c = conn.cursor()


#obicne klase zbog lakšeg unosa novih putnika ili letova
class Putnik:
	def __init__(self,  ime, prezime, brLet, klasa):
		
		self.ime = ime
		self.prezime = prezime
		self.brLet = brLet
		self.klasa = klasa
	
	@classmethod
	def insert_putnik(self, putnik):
		c.execute("INSERT INTO Putnici (ime, prezime, brLet, klasa) VALUES('{}', '{}', {}, '{}')".format( putnik.ime, putnik.prezime, putnik.brLet, putnik.klasa))


class Let:
	def __init__(self, brLet, vrsta, kapacitet, vrijeme):
		self.brLet = brLet
		self.vrsta = vrsta
		self.kapacitet = kapacitet
		self.vrijeme = vrijeme

	@classmethod
	def insert_let(self, let):
		c.execute("INSERT INTO Letovi VALUES({},'{}',{},'{}')".format(let.brLet, let.vrsta, let.kapacitet, let.vrijeme))


#3 tablice koje koristimo - više info na dnu programa
c.execute("""CREATE TABLE if not exists Letovi (
			brLet integer,
			vrsta text,
			kapacitet integer,
			vrijeme text
			)""")


c.execute("""CREATE TABLE if not exists Putnici(
			id integer primary key,
			ime text,
			prezime text,
			brLet integer,
			klasa text
			)""")

c.execute("""CREATE TABLE if not exists Cijene(
			dom_econ integer,
			dom_bus integer,
			dom_first integer,

			me_econ integer,
			me_bus integer,
			me_first integer
			)""")


	
print("Pokrenut GUI")
#setup cijena uzeto sa CroatiaAirlines domaći Zagreb-Split, međunarodni Zagreb-New York zaokruženo da bude lijepše				
c.execute("INSERT INTO Cijene VALUES(400 , 600 , 900 , 3000 , 15000 , 40000 )")


#setup jednostavne baze podataka
let1= Let(113, 'Domaci', 100, '14:25' )
Let.insert_let(let1)
let2 = Let(792, 'Medunarodni', 200, '07:45')
Let.insert_let(let2)
let3 = Let(440, 'Medunarodni', 300, '22:15')
Let.insert_let(let3)
let4 = Let(651, 'Domaci', 150, '19:00')
Let.insert_let(let4)

put1 = Putnik('Pero', 'Perić', 113, 'Economy')
Putnik.insert_putnik(put1)
put2 = Putnik('Marija', 'Horvat', 792, 'First')
Putnik.insert_putnik(put2)
put3 = Putnik('Luka', 'Horvat', 792, 'First')
Putnik.insert_putnik(put3)
put4 = Putnik('Ivana', 'Knežević', 113, 'Business')
Putnik.insert_putnik(put4)
put5 = Putnik('Ante', 'Knežević', 113, 'Business')
Putnik.insert_putnik(put5)
put6 = Putnik('Maja', 'Kovačić', 440, 'Economy')
Putnik.insert_putnik(put6)
put7 = Putnik('Petar', 'Svačić', 440, 'Economy')
Putnik.insert_putnik(put7)
put8 = Putnik('Lucija', 'Matić', 651, 'First')
Putnik.insert_putnik(put8)


def dodaj_putnika():
	global imevar
	global prezvar
	global brlvar
	global klasavar

	#dobiva vrijednosti iz textboxeva i stavlja ih u klasu i dodaje u tablicu
	imep = imevar.get()
	prezimep = prezvar.get()
	brLetp = brlvar.get()
	klasap = klasavar.get()
	
	put = Putnik(imep, prezimep, int(brLetp), klasap)

	#nakon unosa mijenja textbox u prazno
	imevar.set("")
	prezvar.set("")
	brlvar.set("")
	klasavar.set("")

	Putnik.insert_putnik(put)

def dodaj_let():
	global brlvar
	global vrstavar
	global kapvar
	global vrijvar

	#dobiva vrijednosti iz textboxeva i stavlja ih u klasu i dodaje u tablicu
	brLetl = blvar.get()
	vrstal = vrstavar.get()
	kapacitetl = kapvar.get()
	vrijemel = vrijvar.get()

	let = Let(int(brLetl), vrstal, int(kapacitetl), vrijemel)
	Let.insert_let(let)

	#nakon unosa mijenja textbox u prazno
	blvar.set("")
	vrstavar.set("Domaci")
	kapvar.set("")
	vrijvar.set("")
	
def brisi_putnika():
	global idvar

	#uzima id iz textboxa, ulazi u tablicu i obriše ga iz tablice
	id_put = idvar.get()
	c.execute("DELETE FROM Putnici WHERE rowid = {}".format(id_put))
	idvar.set("")
	
def lista_putnika():
	global lst

	#uzima sve putnike iz tablice i ispisuje ih u listbox
	k = c.execute("SELECT rowid,ime, prezime, brLet, klasa FROM Putnici").fetchall()
	tmp = []
	for i in k:
		tmp += ['ID {:2} -  {:10} {:10} - let {} - {} class'.format(i[0], i[1], i[2], i[3],i[4])]
	lst.set(tmp)


def lista_letova():
	global lst

	#uzima sve letove iz tablice i ispisuje ih u listbox
	letvar = c.execute("SELECT * FROM Letovi").fetchall()
	tmp = []
	for i in letvar:
		tmp += [' Let {:3}  - vrsta:  {} - polazak {} sati - kapacitet {} sjedala'.format(i[0], i[1], i[3], i[2])]
	lst.set(tmp)

def cijena():
	global lst

	#uzima sve id iz tablice
	id_putnika = c.execute("SELECT rowid From Putnici"). fetchall();

	tmp = []
	for i in range (len(id_putnika)):

		#uzima sva imena, prezime, broj leta i klasu iz Putnika, vrstu i vrijeme iz letova, spaja ih 
		#na način da pomoću broja leta iz putnika, traži taj let u bazi, gleda da li je domaći ili međunarodni i
		#spaja klasu putnika i vrstu leta sa tablicom cijena da bi odredio kolika je cijena leta
		ime_prezime = c.execute("SELECT ime, prezime From Putnici WHERE rowid = {} ".format(id_putnika[i][0])).fetchone()
		temp = c.execute("SELECT brLet, klasa FROM Putnici WHERE rowid = {} ".format(id_putnika[i][0])).fetchone()

		vrstaLeta = c.execute("SELECT vrsta FROM Letovi WHERE brLet = {}".format(str(temp[0]))).fetchone()
		vrijeme = c.execute("SELECT vrijeme FROM letovi WHERE brLet = {}".format(str(temp[0]))).fetchone()

		cijena = ""

		#spajanje vrste leta(domaci/medunarodni) i klase putnika u cijenu
		if(vrstaLeta[0] == 'Domaci'):
			if(temp[1] == 'Economy'):
				cijena = 'dom_econ'
			elif(temp[1] == 'Business'):
				cijena = 'dom_bus'
			else:
				cijena = 'dom_first'

		elif(vrstaLeta[0] == 'Medunarodni'):
			if(temp[1] == 'Economy'):
				cijena = 'me_econ'
			elif(temp[1] == 'Business'):
				cijena = 'me_bus'
			else:
				cijena = 'me_first'
		else:
			print("Greška")

		cijenaLeta = c.execute("SELECT {} FROM Cijene".format(cijena)).fetchone()

		#generalni ispis cijene
		tmp += ['{:8} {} - let broj: {} u {} sati, cijena leta: {:5} kuna'.format(ime_prezime[0], ime_prezime[1], temp[0], vrijeme[0], cijenaLeta[0])]

		lst.set(tmp)

#Tkinter prozor generalni setup
win = Tk()
win.title("Zracna luka")
win.geometry("800x600")

font = ('Arial', 14)

#rađenje buttona za početne odabire
bput = Button(win, text="Putnici", command=lambda:lista_putnika(), font=font)
bput.grid(row=0, column=0, columnspan=2, sticky="nwe")

blet = Button(win, text="Letovi", command=lambda:lista_letova(), font=font)
blet.grid(row=1, column=0, columnspan=2, sticky="nwe")

bcij = Button(win, text="Cijene", command=lambda:cijena(), font=font)
bcij.grid(row=2, column=0, columnspan=2, sticky="nwe")

fr1 = Frame(win)
fr1.grid(row=3, column=0, sticky="nswe", pady=5)

#Lijevi dio, dodavanje putnika, 4 Labela, 4 Entry i njihovi StringvVarovi u koje se sprema upis
Label(fr1, text="Ime:", font=font).grid(row=0, column=0, sticky="nswe")
Label(fr1, text="Prezime:", font=font).grid(row=1, column=0, sticky="nswe")
Label(fr1, text="Broj leta:", font=font).grid(row=2, column=0, sticky="nswe")
Label(fr1, text="Klasa:", font=font).grid(row=3, column=0, sticky="nswe")

imevar = StringVar()
prezvar = StringVar()
brlvar = StringVar()
klasavar = StringVar()
Entry(fr1, textvariable=imevar, font=font).grid(row=0, column=1, sticky="nswe")
Entry(fr1, textvariable=prezvar, font=font).grid(row=1, column=1, sticky="nswe")
Entry(fr1, textvariable=brlvar, font=font).grid(row=2, column=1, sticky="nswe")
Entry(fr1, textvariable=klasavar, font=font).grid(row=3, column=1, sticky="nswe")

Button(fr1, text="Dodaj putnika", font=font, command=lambda:dodaj_putnika()).grid(row=4, column=0, sticky="nswe", columnspan=2)

#configurira da se malo rasire polja da popune prostor
for i in range(4):
	fr1.rowconfigure(i, weight=1)
for i in range(2):
	fr1.columnconfigure(i, weight=1)

fr2 = Frame(win)
fr2.grid(row=3, column=1, sticky="nswe", pady=5)

#Desni dio, dodavanje leta, isto kao s putnikom, 4 Labela, 3 Entrya i 2 radiobuttona za izbor vrste leta
Label(fr2, text="Br. leta:", font=font).grid(row=0, column=0, sticky="nswe")
Label(fr2, text="Vrsta:", font=font).grid(row=1, column=0, sticky="nswe")
Label(fr2, text="Kapacitet:", font=font).grid(row=3, column=0, sticky="nswe")
Label(fr2, text="Vrijeme:", font=font).grid(row=4, column=0, sticky="nswe")
blvar = StringVar()
vrstavar = StringVar()
kapvar = StringVar()
vrijvar = StringVar()
Entry(fr2, textvariable=blvar, font=font).grid(row=0, column=1, sticky="nswe")
Radiobutton(fr2, text="Domaci", variable=vrstavar, value="Domaci", font=font).grid(row=1, column=1, sticky="nswe")
Radiobutton(fr2, text="Medunarodni", variable=vrstavar, value="Medunarodni", font=font).grid(row=2, column=1, sticky="nswe")
Entry(fr2, textvariable=kapvar, font=font).grid(row=3, column=1, sticky="nswe")
Entry(fr2, textvariable=vrijvar, font=font).grid(row=4, column=1, sticky="nswe")

#postavi da je radiobutton po defaultu domaci
vrstavar.set("Domaci")

Button(fr2, text="Dodaj let", font=font, command=lambda:dodaj_let()).grid(row=5, column=0, columnspan=2, sticky="nswe")
#isto configurira da se polja rasire
for i in range(6):
	fr2.rowconfigure(i, weight=1)
for i in range(2):
	fr2.columnconfigure(i, weight=1)

#listbox u kojem se ispisuju putnici/letovi/cijene
lst = StringVar()
lbox = Listbox(win, listvariable=lst, font = font)
lbox.grid(row=4, column=0, columnspan=3, sticky="nswe")

#za opciju brisanja putnika
fr3 = Frame(win)
fr3.grid(row=5, column=0, columnspan=2, sticky="nswe", pady=5)
Label(fr3, text="ID putnika:", font=font).grid(row=0, column=0, sticky="nswe")
idvar = StringVar()
Entry(fr3, textvariable=idvar, font=font).grid(row=0, column=1, sticky="nswe")
Button(fr3, text="Obrisi putnika", command=lambda:brisi_putnika()).grid(row=0, column=2, sticky="nswe")

fr3.rowconfigure(0, weight=1)
for i in range(3):
	fr3.columnconfigure(i, weight=1)

win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=1)

win.mainloop()

#brise sve tablice na kraju programa
#c.execute("DROP TABLE Letovi")
#c.execute("DROP TABLE Putnici")
#c.execute("DROP TABLE Cijene")

conn.commit()
conn.close()