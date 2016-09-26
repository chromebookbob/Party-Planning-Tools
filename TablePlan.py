from random import shuffle

boys = ["Jim", "Will", "James", "Fergus", "Tom-Jewson", "Tom-Middleton", "Horatio", "Bigmac", "Arron"]
girls= ["Pender", "Charlotte", "Hattie", "Emily", "Sophie", "Izzy", "Imi", "Alice", "Watton"]
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
		new_table=[]
		table = self.table
		#print(len(table))
		i=0
		while i <= len(table)-1:
			current_pos = i
			if i - 1 < 0:
				last_pos = len(table)-1
				
			else:
				last_pos = i-1
			if i+1 >= len(table)-1:
				next_pos = 0
			else:
				next_pos = i+1
			#print(last_pos , current_pos, next_pos, len(self.rules))
			#print(table[last_pos] , table[current_pos], table[next_pos])
			
			for n in range(0, len(self.rules)-1):
				if i % 2 == 0:
					if self.rules[n][2] == "next":
		
						
						if self.CheckNext(table[current_pos], table[last_pos]):
							new_table.append(table[current_pos])
							new_table.append(table[last_pos])
							if last_pos < current_pos:
								del table[current_pos]
								del table[last_pos]
							elif last_pos > current_pos:
								del table[last_pos]
								del table[current_pos]
							break
						elif self.CheckNext(table[current_pos], table[next_pos]):
							new_table.append(table[current_pos])
							new_table.append(table[next_pos])
							if next_pos < current_pos:
								del table[current_pos]
								del table[last_pos]
							elif next_pos > current_pos:
								del table[next_pos]
								del table[current_pos]
							break
					'''if self.rules[n][2] == "notnext":
						if self.CheckNext(table[current_pos], table[last_pos]):
							diff = last_pos +3
							if diff >17:
								diff = 18-diff
							new_table.append(table[diff])
							new_table.append(table[last_pos])
							
							if last_pos < current_pos:
								del table[current_pos]
								del table[last_pos]
							elif last_pos > current_pos:
								del table[last_pos]
								del table[current_pos]
								
								
							break
						if self.CheckNext(table[current_pos], table[next_pos]):
							diff =  current_pos+3
							if diff >17:
								diff = 18-diff
							new_table.append(table[current_pos])
							new_table.append(table[diff])
							if last_pos < current_pos:
								del table[current_pos]
								del table[last_pos]
							elif last_pos > current_pos:
								del table[last_pos]
								del table[current_pos]
								
								
							break'''
				else:
					if self.rules[n][2] == "next":
						if self.CheckNext(table[current_pos], table[last_pos]):
							
							new_table.append(table[last_pos])
							new_table.append(table[current_pos])
							if last_pos < current_pos:
								del table[current_pos]
								del table[last_pos]
							elif last_pos > current_pos:
								del table[last_pos]
								del table[current_pos]
								
								
							break
						elif self.CheckNext(table[current_pos], table[next_pos]):
							new_table.append(table[next_pos])
							new_table.append(table[current_pos])
							
							if next_pos < current_pos:
								del table[current_pos]
								del table[last_pos]
							elif next_pos > current_pos:
								del table[next_pos]
								del table[current_pos]
							break
					'''if self.rules[n][2] == "notnext":
						if self.CheckNext(table[current_pos], table[last_pos]):
							diff = last_pos +3
							if diff >17:
								diff = 18-diff
							new_table.append(table[last_pos])
							new_table.append(table[diff])
							if last_pos < current_pos:
								del table[current_pos]
								del table[last_pos]
							elif last_pos > current_pos:
								del table[last_pos]
								del table[current_pos]
								
								
							break
						if self.CheckNext(table[current_pos], table[next_pos]):
							diff =  current_pos+3
							if diff >17:
								diff = 18-diff
							new_table.append(table[diff])
							new_table.append(table[current_pos])
							
							if last_pos < current_pos:
								del table[current_pos]
								del table[last_pos]
							elif last_pos > current_pos:
								del table[last_pos]
								del table[current_pos]
								
								
							break'''
			
			i+=1
		tempboys=[]
		tempgirls=[]
		for i in range(0, len(table)):
			if i % 2 ==0:
				tempboys.append(table[i])
			else:
				tempgirls.append(table[i])
		shuffle(tempboys)
		shuffle(tempgirls)
		n=0
		for i in range(0, (len(tempboys)*2)):
			if i %2 == 0:
				new_table.append(tempboys[n])
				
			else:
				new_table.append(tempgirls[n])
				n+=1
		
		temptable = []
		m=0
		
		for i in range(0, int(len(new_table)/2)):
			temptable.append([new_table[m], new_table[m+1]])
			m+=2
		print(temptable)
		shuffle(temptable)
		new_table = flatten(temptable)
		
		self.table = new_table
	
	def CheckRules(self):
		alltrue = False
		while alltrue == False:
			alltrue = True
			for n in range(0, len(self.rules)-1):
				print(self.table)
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
		self.TablePlan()
		self.TableGenerate()
		x="\n"
		while x != "q":
			x=input("")
			self.CheckRules()
			
			self.DrawTable()
			
	def DrawTable(self):
		table=self.table
		for i in range(len(table)):
			print(table[i])
table=Table(boys, girls, [],[["Bigmac","Imi", "next"], ["Arron", "Hattie", "next"], ["Arron", "Emily", "next"], ["Bigmac", "Emily", "next"], ["Tom-Jewson", "Pender", "next"]])
table.AddRules()
table.TestTable()
input('Press ENTER to exit')