import main
from Rules import board
from Rules import rules

class Test():
	def __init__(self):
		self.game = main.Game()

	def test_deckbuilding(self):
		try:
			hei = board.Deck()
			#print (hei.cards)
			hei.create_deck()
			#print (hei.cards)
			if hei.cards[59].name == 59:
				print "Deckbuilding successful"
		except Exception, e:
			raise e

	def test_deckshuffling(self):
		try:
			hei2 = board.Deck()
			hei2.create_deck()
			hei2.shuffle_deck()

			if len(hei2.cards) == 60:
				for i in range(60):
					counter = 0
					for card in hei2.cards:
						if card.name == i:
							counter += 1
					if counter != 1:
						print "Card number %d exists in %d copies" % (i, counter)
						break
				if counter == 1:
					print "Deck shuffled successfully"
			else:
				print "Deck has increased in size! Current size is %d" % len(hei2.cards)


		except Exception, e:
			raise e

	def test_start_game(self):
		#Checks that start_game initiates successfully
		self.game = main.Game()
		self.game.start_game()
		try:
			self.game.players[1]
			print "Game and players initiated"
		except Exception, e:
			raise e
		#game.players[]

	def test_draw_cards(self):
		if self.game.players[1].hand.get_size_hand() == 7:
			print "7 cards drawn successfully"
		else:
			print "Card drawing error!"

	def test_turns(self, number_of_turns):
		self.game.start_game()

		while self.game.loss == False and self.game.turn_counter < number_of_turns:
			self.game.new_turn(self.game.players[self.game.active_player], self.game.turn.next_turn)
			self.game.next_player()

		if self.game.turn_counter == number_of_turns:
			print "%d number of turns executed successfully" % self.game.turn_counter
		elif self.game.loss == True:
			print "Win condition reached!"
		else:
			print "what happened to the turns"

	def test_lessons(self):
		self.test_turns(20)

		print self.game.players[0].inplay
		print self.game.players[0].hand
		print self.game.players[0].inplay.cards[3].mana
		print self.game.players[0].inplay.count_mana()

	def test_damage(self):
		self.test_turns(30)
		self.game.players[0].inplay.count_creature_damage()
		print "The game ended in turn %d" % self.game.turn_counter

	def test_card_cost(self):
		self.test_turns(30)
		print self.game.players[0].hand
		print self.game.players[0].inplay
		print "mana: %d, creature damage: %d, deck size: %d, discard pile: %d"  % (self.game.players[0].inplay.count_mana()[0], self.game.players[0].inplay.count_creature_damage(), self.game.players[0].deck.get_size_deck(), self.game.players[0].discard_pile.get_size_discard_pile())

		print self.game.players[1].hand
		print self.game.players[1].inplay
		print "mana: %d, creature damage: %d, deck size: %d, discard pile: %d" % (self.game.players[1].inplay.count_mana()[0], self.game.players[1].inplay.count_creature_damage(), self.game.players[1].deck.get_size_deck(), self.game.players[1].discard_pile.get_size_discard_pile())
		



		

dummy = Test() 
#dummy.test_deckbuilding()
#dummy.test_deckshuffling()
#dummy.test_start_game()
#dummy.test_draw_cards()
#dummy.test_turns(10)
#dummy.test_lessons()
#dummy.test_damage()
dummy.test_card_cost()

