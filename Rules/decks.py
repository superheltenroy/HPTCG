import cards

# def lesson_test_deck(deck):
# 	for i in range(15):
# 		deck.cards.append(cards.Lesson("Transfiguration",cards.Transfiguration()))
# 		deck.cards.append(cards.Lesson("Potions",cards.Potions()))
# 		deck.cards.append(cards.Lesson("Charms",cards.Charms()))
# 		deck.cards.append(cards.Lesson("Care Of Magical Creatures",cards.CareOfMagicalCreatures()))

def creature_test_deck(deck):
	for i in range(5):
		deck.cards.append(cards.CareOfMagicalCreaturesLesson())
		deck.cards.append(cards.CharmsLesson())
	for i in range(50):
		deck.cards.append(cards.MountainTroll())


def obliviate_test_deck(deck):
	for i in range(40):
		deck.cards.append(cards.CharmsLesson())
	for i in range(20):
		deck.cards.append(cards.Obliviate())


