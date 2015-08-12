import rules

class Card():
	def __init__(self, name, color=None, cost=0, card_number=0, series="Basic"):
		self.name = str(name)
		self.color = color
		self.cost = cost
		self.number = card_number
		self.series = series

class Cost(): #Experimental class to contain card costs
	def __init__(self, mana, number):
		self.mana = mana

class Mana():
	def __init__(self):
		pass

class Lesson(Card):
	def __init__(self, name, mana, card_number, series):
		Card.__init__(self, name, card_number=card_number, series=series)
		self.mana = mana
	
class Transfiguration(Mana):
	def __init__(self):
		Mana.__init__(self)

class Charms(Mana):
	def __init__(self):
		Mana.__init__(self)

class CareOfMagicalCreatures(Mana):
	def __init__(self):
		Mana.__init__(self)

class Potions(Mana):
	def __init__(self):
		Mana.__init__(self)

class Quidditch(Mana):
	def __init__(self):
		Mana.__init__(self)

class Creature(Card):
	def __init__(self, name, cost, card_number, series, health, attack = 0):
		Card.__init__(self, name, "f", cost, card_number, series)
		self.attack = attack
		self.health = health

class Spell(Card):
	def __init__(self, name, color, cost, card_number, series):
		Card.__init__(self, name, color, cost, card_number, series)

	def check_cost(self):
		self.extra_cost()

	def extra_cost(self):
		pass

##########################################################################################################
########################### SPELL CARDS ##################################################################
##########################################################################################################


class ElixirOfLife(Spell):
	def __init__(self):
		Spell.__init__(self, name="Elixir of Life", 
			color="c", cost=12, card_number=5, series="Basic")
		self.text = """To play this card, discard 2 of your P Lessons from play. 
						Shuffle up to 16 Non-Healing cards 
						from your discard pile into your deck."""

class Obliviate(Spell):
	def __init__(self):
		Spell.__init__(self, name="Obliviate", 
			color="c", cost=12, card_number=14, series="Basic")
		self.text = "Your opponent discards his or her hand."

##########################################################################################################
########################### CREATURE CARDS ###############################################################
##########################################################################################################

class ViciousWolf(Creature):
	def __init__(self):
		Creature.__init__(self, name="Vicious Wolf", 
			cost=6, card_number=110, series="Basic", 
			health=3, attack=3)
		self.text = ""

class BoaConstrictor(Creature):
	def __init__(self):
		Creature.__init__(self, name="Boa Constrictor", 
			cost=4, card_number=76, series="Basic", 
			health=2, attack=2)
		self.text = ""

class CuriousRaven(Creature):
	def __init__(self):
		Creature.__init__(self, name="CuriousRaven", 
			cost=2, card_number=80, series="Basic", 
			health=1, attack=1)
		self.text = ""

class SurlyHound(Creature):
	def __init__(self):
		Creature.__init__(self, name="Surly Hound", 
			cost=3, card_number=107, series="Basic", 
			health=3, attack=1)
		self.text = ""

class MountainTroll(Creature):
	def __init__(self):
		Creature.__init__(self, name="Mountain Troll", 
							cost=8, card_number=28, series="Basic", 
							health=4, attack=4)
		self.text = ""



##########################################################################################################
########################### LESSON CARDS #################################################################
##########################################################################################################

class CareOfMagicalCreaturesLesson(Lesson):
	def __init__(self):
		Lesson.__init__(self, "Care of Magical Creatures", CareOfMagicalCreatures(), 113, "Basic")

class CharmsLesson(Lesson):
	def __init__(self):
		Lesson.__init__(self, "Charms", Charms(), 114, "Basic")

class PotionsLesson(Lesson):
	def __init__(self):
		Lesson.__init__(self, "Potions", Potions(), 115, "Basic")

class TransfigurationLesson(Lesson):
	def __init__(self):
		Lesson.__init__(self, "Transfiguration", Transfiguration(), 116, "Basic")




