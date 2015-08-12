#from board import Deck, Card
from Rules import rules 
from Rules import board
import display
import cards

class Main ():
	def __init__(self):
		pass

class Game():
	def __init__(self):
		self.players = [board.Player(), board.Player()]
		self.loss = False
		self.turn_counter = 0
		self.active_player = 0
		self.turn = rules.Turn()
		self.turn.next_turn = rules.Turn()

		# self.start_game()

		# while self.loss == False and self.turn_counter < 10:
			
		# 	self.new_turn(self.players[self.active_player])
		# 	self.next_player()


	def start_game(self):
		for player in self.players:
			player.deck = board.Deck()
			if player == self.players[0]:
				player.deck.create_deck(1)
			else:
				player.deck.create_deck(2)
			player.deck.shuffle_deck()
			player.deck.shuffle_deck()
			player.hand = board.Hand()
			player.inplay = board.InPlay()
			player.discard_pile = board.DiscardPile()
			rules.DrawCard(7,player)
		self.choose_player1()
		self.players[0].opponent = self.players[1]
		self.players[1].opponent = self.players[0]

	def new_turn(self, player, current_turn):
		self.turn_counter += 1
		self.turn = current_turn
		if isinstance(current_turn.next_turn, rules.Turn):
			pass
		else:
			self.turn.next_turn = rules.Turn()

		rules.DrawPhase(player, self.turn)

		rules.MonsterDamagePhase(player, self.turn)

		rules.PlayPhase(player, self.turn)

		rules.EndPhase(player, self.turn)

		self.victory_check()

	def choose_player1(self):
		self.players[0].is_active = True 
		self.players[0].name = "Player 1"
		self.players[1].name = "Player 2"

	def next_player(self):
		self.active_player += 1
		if self.active_player >= len(self.players):
			self.active_player = 0

	def victory_check(self):
		if self.players[0].loss == True:
			self.loss = True
			print "%s won!" % self.players[1].name
		elif self.players[1].loss == True:
			self.loss = True
			print "%s won!" % self.players[0].name

	def card_ability(self, card):
		pass

