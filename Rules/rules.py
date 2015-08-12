import board
import cards

from random import randint

class DealDamage():
	def __init__(self, number_of_damage, player):
		for i in range(number_of_damage):
			if len(player.opponent.deck.cards) == 0:
				player.opponent.loss = True
				player.win = True
				break
			destroyed_card = player.opponent.deck.pop_top_card()
			player.opponent.discard_pile.add_card(destroyed_card)
		

class DrawCard():
	def __init__(self, number_of_cards, player):
		
		for i in range(number_of_cards):
			if len(player.deck.cards) == 0:
				player.loss = True
				player.opponent.win = True
				break
			drawn_card = player.deck.pop_top_card()
			player.hand.add_card(drawn_card)

class DrawPhase():
	def __init__(self, player, turn):
		if player.loss == True or player.win == True:
			pass
		else:
			DrawCard(1, player)

class MonsterDamagePhase():
	def __init__(self, player, turn):
		if player.loss == True or player.win == True:
			pass
		damage = player.inplay.count_creature_damage()
		DealDamage(damage, player.opponent)
		

class PlayPhase():
	def __init__(self, player, turn):
		for action in range(player.actions):
			if player.loss == True or player.win == True:
				pass
			else:
				if len(player.hand.cards) >= 1:
					index = self.pick_card_to_play(player)
					if index == -1:
						DrawCard(1, player)
					else:
						PlayCard(index, player)
				else:
					DrawCard(1, player)

	def pick_card_to_play(self, player):

		###############This function does not work properly, or the 
		#code calling it does not work. Some card is chosen and shown valid, but som other card is played.
		self.viable_card = False
		viable_cards = len(player.hand.cards)
		viable_cards_list = range(viable_cards)
		viable_card = False
		for card_index in range(viable_cards-1,0,-1):
			pick = viable_cards_list.pop(randint(0, card_index))

			viable_card = self.check_validity(player, player.hand.cards[pick])
			print player.hand.cards[pick].name, player.hand.cards[pick].cost
			if viable_card == True:
				return pick
		return -1

	def check_validity(self, player, card):
		if card.cost == 0:
			return True
		else:
			mana_list = player.inplay.count_mana()
			print "Mana list: ", mana_list
			if card.cost > mana_list[0]:
				return False
			else:
				if mana_list[1] != 0 and card.color == "c":
					return True
				elif mana_list[2] != 0 and card.color == "t":
					return True
				elif mana_list[3] != 0 and card.color == "f":
					return True
				elif mana_list[4] != 0 and card.color == "p":
					return True
				elif mana_list[5] != 0 and card.color == "q":
					return True
				else: 
					return False



class EndPhase():
	def __init__(self, player, turn):
		if player.loss == True or player.win == True:
			pass

class Actions():
	def __init__(self):
		action_count = 2

class PlayCard():
	def __init__(self, card_index, player):
		card_to_be_played = player.hand.cards.pop(card_index)
		if isinstance(card_to_be_played, cards.Spell):
			CardAbility(player, card_to_be_played.number, card_to_be_played.series)
			player.discard_pile.cards.append(card_to_be_played)
		else:
			player.inplay.cards.append(card_to_be_played)
		
class DiscardFromHand():
	def __init__(self, player, card_index = 0):
		print "%s discards!" % player.name
		if len(player.hand.cards) == 0:
			pass
		elif card_index >= len(player.hand.cards):
			pass
		else:
			player.discard_pile.cards.append(player.hand.cards.pop(card_index))

class DiscardFromPlay():
	def __init__(self, player, card_index = 0):
		if len(player.inplay.cards) == 0:
			pass
		elif card_index >= len(player.inplay.cards):
			pass
		else:
			player.discard_pile.cards.append(player.inplay.cards.pop(card_index))

class Heal():
	def __init__(self, number):
		pass

class Turn():
	def __init__(self):
		self.next_turn = None
		self.monster_damage = True

class CardAbility():
	def __init__(self, player, card_index, series="Basic"):
		if series == "Basic":
			if card_index == 14:
				self.basic014(player)
			else:
				pass

	def basic014(self, player):
		
		for number in range(len(player.opponent.hand.cards)):
			DiscardFromHand(player.opponent)

	def basic032(self, player):
		print "%s played Platform 9 3/4!"






