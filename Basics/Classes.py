import random

wildpokemon = ['zubat','vulpix','staryu','sandshrew']

class Pokemon() :
	def __init__(self) :
		self.name = wildpokemon[random.randint(0,3)]
		self.lvl = random.randint(5,15)
	def calcHP(self) :
		return self.lvl * 50
	def calcAtk(self) :
		return self.lvl * 2
	def calcDef(self) :
		return self.lvl * 1.5
		

p = Pokemon()
print('a wild', p.name, 'has appeared!')
print('Level:',p.lvl)
print('HP:',p.calcHP())
print('Atk:',p.calcAtk())
print('Def:',p.calcDef())
