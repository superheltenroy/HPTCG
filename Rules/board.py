import cards
import decks

from random import randint



class Player ():
	def __init__(self, deck_option="creatures"):
		self.is_active = False
		self.name = ""
		self.loss = False
		self.win = False
		self.opponent = None
		self.actions = 2
		self.deck_option = deck_option

class Board():
	def __init__(self):
		pass

class Deck():
	def __init__(self):
		self.main_character = []
		self.cards = []

	def create_deck(self, deck_option):
		if deck_option == 1:
			decks.creature_test_deck(self)
		elif deck_option == 2:
			decks.obliviate_test_deck(self)

		if len(self.cards) != 60:
			print "Something's wrong with the deck! Start over! deck size: %d" % len(self.cards)

		# for i in range(14):
		# 	self.cards.append(cards.Lesson("Transfiguration",cards.Transfiguration()))
		# 	self.cards.append(cards.Lesson("Potions",cards.Potions()))
		# 	self.cards.append(cards.Lesson("Charms",cards.Charms()))
		# 	self.cards.append(cards.Lesson("Care Of Magical Creatures",cards.CareOfMagicalCreatures()))
		#self.cards.append(cards.Creature("Vicious Wolf", 3, 3))

	def shuffle_deck(self):
		shuffled_deck = []
		length = len(self.cards)
		for x in range(0,length):
			rand = randint(0,length-x-1)
			shuffled_deck.append(self.cards.pop(rand))
		self.cards = shuffled_deck

	def get_size_deck (self):
		return len(self.cards)

	def pop_top_card (self):
		return self.cards.pop(0)

class InPlay():
	def __init__(self):
		self.cards = []

	def __str__(self):
		x = "In Play: {"
		for card in self.cards:
			x = x + card.name + ", "
		x = x.strip(", ") + "}"
		return x

	def get_size_in_play(self):
		return len(self.cards)

	def count_mana(self):
		counter = 0
		c = 0
		t = 0 
		f = 0
		p = 0 
		q = 0

		for card in self.cards:
			try:
				if isinstance(card.mana, cards.Charms):
					counter += 1
					c += 1
				if isinstance(card.mana, cards.Transfiguration):
					counter += 1
					t += 1
				if isinstance(card.mana, cards.CareOfMagicalCreatures):
					counter += 1
					f += 1
				if isinstance(card.mana, cards.Potions):
					counter += 1
					p += 1
				if isinstance(card.mana, cards.Quidditch):
					counter += 1
					q += 1
			except:
				pass

		return [counter, c, t, f, p, q]

	def count_creature_damage(self):
		damage_counter = 0

		for card in self.cards:
			try:
				if isinstance(card, cards.Creature):
					damage_counter += card.attack
			except:
				pass

		return damage_counter


class ActiveEffects():
	#This class may be used to keep track of cards that maintain active effects.
	def __init__(self):
		self.cards = []

class DiscardPile():
	def __init__(self):
		self.cards = []

	def get_size_discard_pile (self):
		return len(self.cards)

	def add_card(self, card):
		self.cards.append(card)

class Hand():
	def __init__(self):
		self.cards = []

	def __str__(self):
		x = "Hand: {"
		for card in self.cards:
			x = x + card.name + ", "
		x = x.strip(", ") + "}"
		return x

	def get_size_hand(self):
		return len(self.cards)

	def add_card(self, card):
		self.cards.append(card)

class Adventure():
	def __init__(self):
		pass

