from random import shuffle
import sys
import random
import printer
import time


table=["Horatio 'meme man' Lovering", 'Imi Colla', 'Bigmac Macmullen', 'Emily Stainer', "Arron 'Weeb' Oliphant", 'Princess Fiona Bennett', "James 'NUT' Gardiner", 'Izzy Mckellar', 'Tom Jewson', 'Charlotte Pender', "Yergus 'Stupid Yerger' O'Keefe", 'Charlotte Ashley', "Will 'It shows' Gough", 'Alice Walton-Knight', 'Tom Middleton', "Sophie 'Nietszche' Ashley", 'Jim Bruges', "George 'meme' Watton"]

def NextTo(person):
		
		i = table.index(person)
		current_pos = i
		if i - 1 < 0:
			last_pos = 17
				
		else:
				last_pos = i-1
		if i+1 >= len(table):
			next_pos = 0
		else:
			next_pos = i+1
		return [table[last_pos], table[current_pos], table[next_pos]]

#x=input('Press ENTER to continue')


p=printer.ThermalPrinter(serialport="/dev/ttyAMA0")

p.linefeed()
for i in range(0,18):
	nextto = NextTo(table[i])
	print(i)
	print(nextto)
	p.justify("C")
	p.barcode("Oct2016")
	p.linefeed()
	p.print_text("  ")
	p.linefeed()
	p.inverse_on()

	p.print_text("PARTY PARTY 11")


	p.inverse_off()
	p.font_b_on()
	p.linefeed()
	p.print_text("organised by robot overlords")
	p.linefeed()
	p.print_text("-------------------------")
	p.linefeed()	
	p.print_text("Welcome, ")
	p.bold_on()
	p.print_text(nextto[1])
	p.bold_off()
	p.print_text(" \nYou're sitting next to:")
	p.linefeed()
	p.bold_on()
	p.print_text(nextto[0])
	p.bold_off()
	p.print_text(" and ")
	p.bold_on()
	p.print_text(nextto[2])
	p.bold_off()
	p.linefeed()
	p.font_b_off()
	p.bold_off()
	p.print_text("-------------------------")
	p.linefeed()	
	p.print_text('"')
	p.print_text(random.choice(["realising that there is no point can be fun","I'm not well informed about space I'm just a fan", "crack out some booze but not welsh lads style","It's all going to be fine","I'd explain but the meme is too edgy","I don't want to sound like a massive nerd but...","Ask Arron about his primary school days","Take a photo with the instant camera","Don't spill wine on the carpet.","It's a meme, don't worry.","Don't mention Shillary or Trump","Be nice and make conversation.", "Don't be a meme", "It shows.", "Make a speech", "No Brexit chat", "Blame the computer for who you're sitting next to", "If Jim failed his driving test expect nothing from tonight."]))
	p.print_text('"')
	p.linefeed()
	p.linefeed()
	p.linefeed()
	p.linefeed()
	time.sleep(4)



