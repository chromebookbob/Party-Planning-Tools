from random import shuffle
import random


def flatten(input):
    new_list = []
    for i in input:
        for j in i:
            new_list.append(j)
    return new_list
class Table:
	def __init__(self, boys, girls, table, rules):
		self.boys=boys
		self.girls=girls
		self.table=table
		self.rules=rules


	def TablePlan(self):
		n=0
		shuffle(self.boys)
		shuffle(self.girls)
		for i in range(0, (len(self.boys)*2)):
			if i %2 == 0:
				self.table.append(self.boys[n])
				
			else:
				self.table.append(self.girls[n])
				n+=1
		return self.table
		
	def TableGenerate(self):
		boys=self.boys
		girls=self.girls
		table = []
		shuffle(boys)
		shuffle(girls)
		n=0
		while len(boys) != 0:
			boy = boys[n]
			if len(boys) >1:
				nextboy = boys[n+1] 
			nexttolist = self.NextTo(boy)
			print(nexttolist)
			if len(nexttolist) == 1:
				if nexttolist[0] in table:
					index = table.index(nexttolist[0])
					if table[index-1] in boys:
						table.insert(index+1, boy)
					else:
						table.insert(index, boy)
					boys.pop(boys.index(boy))
				else:
					table.append(None)
					table.append(boy)
					boys.pop(boys.index(boy))
					table.append(nexttolist[0])
					girls.pop(girls.index(nexttolist[0]))
			elif len(nexttolist)==2:
				if (nexttolist[0] in table) and (nexttolist[1] in table):
					i = table.index(nexttolist[0])
					i2 = table.index(nexttolist[1])
					if i<i2:
						table.insert(i2, boy)
					else: 
						table.insert(i, boy)
					boys.pop(boys.index(boy))
				elif nexttolist[0] in table:
					index = table.index(nexttolist[0])
					if table[index-1] in boys:
						table.insert(index, nexttolist[1])
						table.insert(index, boy)
					
					else:
						table.insert(index, boy)
						table.insert(index, nexttolist[1])
					boys.pop(boys.index(boy))
					girls.pop(girls.index(nexttolist[1]))
				elif nexttolist[1] in table:
					index = table.index(nexttolist[1])
					if table[index-1] in boys:
						table.insert(index, nexttolist[0])
						table.insert(index, boy)
					
					else:
						table.insert(index, boy)
						table.insert(index, nexttolist[0])
					boys.pop(boys.index(boy))
					girls.pop(girls.index(nexttolist[0]))
				else:
					table.append(nexttolist[0])
					table.append(boy)
					table.append(nexttolist[1])
					boys.pop(boys.index(boy))
					
					girls.pop(girls.index(nexttolist[0]))
					girls.pop(girls.index(nexttolist[1]))
			else:
				table.append(None)
				table.append(boy)
				table.append(None)
				boys.pop(boys.index(boy))
			n = boys.index(nextboy)
			
			print(table)		
		
		
	
	def CheckRules(self):
		alltrue = False
		while alltrue == False:
			alltrue = True
			for n in range(0, len(self.rules)-1):
				#print(self.table)
				if self.rules[n][2]=="next":
					
					if self.CheckNext(self.rules[n][0], self.rules[n][1])== False: 
						alltrue = False
				if self.rules[n][2]=="notnext":
				
					if self.CheckNext(self.rules[n][0],self.rules[n][1])== True: 
						alltrue = False
						
			if alltrue == True:
				break
			else:
				self.TableGenerate()
	
	def CheckNext(self, boy, girl):
		table = self.table
		if abs(table.index(boy) - table.index(girl)) == 1:
			return True
		else:
			return False
	def NextTo(self, name):
		
		if name in self.boys:
			nexttolist = []
			for n in range(0, len(self.rules)-1):
				rule = self.rules[n]
				if rule[0] ==name and rule[2] == 'next':
					nexttolist.append(rule[1])
		elif name in self.girls:
			nexttolist = []
			for n in range(0, len(self.rules)-1):
				rule = self.rules[n]
				if rule[0] ==name and rule[2] == 'next':
					nexttolist.append(rule[0])
		return nexttolist
	def NotNextTo(self, name):
		if name in self.boys:
			for n in range(0, len(self.rules)-1):
				if rule[0] ==name and rule[2] == 'notnext':
					return rule[1]
		elif name in self.girls:
			for n in range(0, len(self.rules)-1):
				if rule[0] ==name and rule[2] == 'notnext':
					return rule[0]
		return False
	def AddRules(self):
		print("Type quit to quit")
		while True:
			boy = input("Boy")
			
			if boy == "":
				break
				
			girl = input("Girl")
			
			if girl == "":
				break
			rule = input("Rule to apply (next, notnext)")
			if rule == "":
				break
			if boy in self.table:
				if girl in self.table:
					if rule in ["next", "notnext"]:
						self.rules.append([])
						self.rules.append([boy, girl, rule])
			else:
				print("sorry, those names or rules weren't applicable")
				
	def TestTable(self):
		#self.TablePlan()
		self.TableGenerate()
		#x="\n"
		#while x != "q":
		#	x=input("")
		#	self.CheckRules()
			
		#	self.DrawTable()
		
	def DrawTable(self):
		table=self.table
		print(table)
		
		for i in range(len(table)):
			print(table[i])
	def Old_NextTo(self, person):
		table = self.table
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
		return [self.table[last_pos], self.table[current_pos], self.table[next_pos]]
# Define table as Table( list of boys names, list of girls names, empty list, list of rules with the syntax [boy, girl, rule (which can be "next")])


boys = ["Jim Bruges", "Will 'It shows' Gough", "James 'NUT' Gardiner", "Yergus 'Stupid Yerger' O'Keefe", "Tom Jewson", "Tom Middleton", "Horatio 'meme man' Lovering", "Bigmac Macmullen", "Arron 'Weeb' Oliphant"]
girls= ["Charlotte Ashley", "Charlotte Pender", "Princess Fiona Bennett", "Emily Stainer", "Sophie 'Nietszche' Ashley", "Izzy Mckellar", "Imi Colla", "Alice Walton-Knight", "George 'meme' Watton"]
rules= [["Bigmac Macmullen","Imi Colla", "next"], ["Arron 'Weeb' Oliphant", "Princess Fiona Bennett", "next"], ["Arron 'Weeb' Oliphant", "Emily Stainer", "next"], ["Bigmac Macmullen", "Emily Stainer", "next"], ["Tom Jewson", "Charlotte Pender", "next"], ["Jim Bruges", "George 'meme' Watton", "next"], ["Yergus 'Stupid Yerger' O'Keefe", "Charlotte Pender", "next"], ["James 'NUT' Gardiner", "Princess Fiona Bennett", "next"],["James 'NUT' Gardiner", "Princess Fiona Bennett", "notnext"] ]



table=Table(boys, girls, [], rules)
table.AddRules()
table.TestTable()
print(table.table)
print(table.NextTo("Watton"))



'''for i in range(0, len(table.table)):
	
	nextto = table.NextTo(table.table[i])
	print("Seating Plan organised by a computer\n")
	print("Welcome, %s. You're sitting next to:\n" % nextto[1])
	print("%s and %s\n" % (nextto[0], nextto[2]))
	print(random.choice(["Be nice and make conversation.", "Don't be a meme", "It shows.", "Make a speech", "No Brexit chat", "Blame the computer for who you're sitting next to", "If Jim failed his driving test expect nothing from tonight."]))
	

'''

input('Press ENTER to continue')
