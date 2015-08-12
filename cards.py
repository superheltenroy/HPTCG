class card():
	def __init__(self, name, course, card_type, unique, healing):
		self.name = name
		self.course = course #potions, charms, transfiguration, Care of Magical Creatures, none(adventure, character)
		self.card_type = card_type #spell, creature, lesson, adventure, item, character
		self.unique = unique
		self.healing = healing
		
		self.damage = None
		self.max_hp = None

		provides_power = None



card_16 = card("Professor Severus Snape", None, "character", True, True)

		
