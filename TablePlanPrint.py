from random import shuffle
import sys
import random
import printer


table=["Yergus 'Stupid Yerger' O'Keefe", 'Izzy Mckellar', 'Tom Jewson', 'Charlotte Pender', 'Jim Bruges', "George 'meme' Watton", 'Tom Middleton', "Sophie 'Nietszche' Ashley", "Horatio 'meme man' Lovering", 'Imi Colla', 'Bigmac Macmullen', 'Emily Stainer', "Arron 'Weeb' Oliphant", 'Princess Fiona Bennett', "James 'NUT' Gardiner", 'Alice Walton-Knight', "Will 'It shows' Gough", 'Charlotte Ashley']


def NextTo(self, person):
		
		i = table.index(person)
		current_pos = i
		if i - 1 < 0:
			last_pos = len(table)-1
				
		else:
				last_pos = i-1
		if i+1 >= len(table)-1:
			next_pos = 0
		else:
			next_pos = i+1
		return [table[last_pos], table[current_pos], table[next_pos]]

#x=input('Press ENTER to continue')


p=printer.ThermalPrinter(serialport="/dev/ttyAMA0")

p.linefeed()
for i in range(0, len(table)):
	
	nextto = NextTo(table[i])
	p.underlineOn(1)
	p.print_text("Seating Plan organised by a computer\n")
	p.linefeed()
	p.underlineOn(0)
	p.print_text("Welcome, %s. You're sitting next to:\n" % nextto[1])
	p.linefeed()
	p.print_text("%s and %s\n" % (nextto[0], nextto[2]))
	p.linefeed()
	p.print_text(random.choice(["Be nice and make conversation.", "Don't be a meme", "It shows.", "Make a speech", "No Brexit chat", "Blame the computer for who you're sitting next to", "If Jim failed his driving test expect nothing from tonight."]))
	
	p.linefeed()
	p.linefeed()
	p.linefeed()



