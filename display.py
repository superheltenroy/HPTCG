

class Display():
	def __init__(self):
		self.version = 0.01
		self.author = "Grunde H. Wesenberg"

		self.opening_screen()



	def opening_screen(self):
		print ("Welcome to Harry Potter Trading Card Game.")
		print ("This is version %d") % self.version
		print ("Made by %s") % self.author