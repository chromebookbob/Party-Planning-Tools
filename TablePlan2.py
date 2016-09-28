import random
boys = ["Jim Bruges", "Will 'It shows' Gough", "James 'NUT' Gardiner", "Yergus 'Stupid Yerger' O'Keefe", "Tom Jewson", "Tom Middleton", "Horatio 'meme man' Lovering", "Bigmac Macmullen", "Arron 'Weeb' Oliphant"]
girls= ["Charlotte Pender", "Charlotte Ashley", "Princess Fiona Bennett", "Emily Stainer", "Sophie 'Nietszche' Ashley", "Izzy Mckellar", "Imi Colla", "Alice Walton-Knight", "George 'meme' Watton"]
rules= [["Bigmac Macmullen","Imi Colla", "next"], ["Arron 'Weeb' Oliphant", "Princess Fiona Bennett", "next"], ["Arron 'Weeb' Oliphant", "Emily Stainer", "next"], ["Bigmac Macmullen", "Emily Stainer", "next"], ["Tom Jewson", "Charlotte Pender", "next"], ["Jim Bruges", "George 'meme' Watton", "next"], ["Yergus 'Stupid Yerger' O'Keefe", "Charlotte Pender", "next"], ["James 'NUT' Gardiner", "Princess Fiona Bennett", "next"],["James 'NUT' Gardiner", "Princess Fiona Bennett", "notnext"] ]
table=[None] * 18
'''

Pick boy from list
pick girl from list, check that rules apply to all of them
if not pick another person

'''
boys = random.shuffle(boys)
girls = random.shuffle(girls)
rulescorrect=False
while rulescorrect = False
    n=0
    for i in range(len(boys)):
        boy = boys.pop(i)
        girl = girls.pop(i)
        notnext = False
        nextto = False
        for i in len(rules):
            ruletemp = [boy, girl, "notnext"]
            if rule[i] == ruletemp:
                girltemp = girl
                girl = girls[i]
                girls[i] = girltemp
            ruletemp = [boy, girl, "next"]
            if rule[i] == ruletemp:
                nextto = True
        table[n]=boy
        table[n+1]=girl
        

