import random

wildpokemon = ['zubat','vulpix','staryu','sandshrew']
ledgpokemon = ['articuno','zapdos','moltres','mewtwo']

class Pokemon(object) :
	def __init__(self,xHP,xAtk,xDef) :
		self.name = 'missingno'
		self.lvl = 0
		self.xHP = xHP
		self.xAtk = xAtk
		self.xDef = xDef
	def calcHP(self) :
		return self.lvl * self.xHP
	def calcAtk(self) :
		return self.lvl * self.xAtk
	def calcDef(self) :
		return self.lvl * self.xDef

class WildPokemon(Pokemon) :
	def __init__(self) :
		super(WildPokemon,self).__init__(50,2,1)
		self.name = wildpokemon[random.randint(0,3)]
		self.lvl = random.randint(5,15)

class LedgPokemon(Pokemon) :
	def __init__(self) :
		super(LedgPokemon,self).__init__(100,5,4)
		self.name = ledgpokemon[random.randint(0,3)]
		self.lvl = random.randint(75,90)

		

p = LedgPokemon()
print('a wild', p.name, 'has appeared!')
print('Level:',p.lvl)
print('HP:',p.calcHP())
print('Atk:',p.calcAtk())
print('Def:',p.calcDef())
