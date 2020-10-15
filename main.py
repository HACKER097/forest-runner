import pygame

SCREEN_HEIGHT = 600
SCREEN_LENGTH = 600

camerax = 0
cameray = 0

win = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_LENGTH))
pygame.display.flip()

run = True

bgimg = pygame.image.load("res/forest.png")
bggimg = pygame.image.load("res/bgg.png")

class Hero:

	def __init__(self, x, y):
		self.anispeed = 1
		self.aninum = 0
		self.imgnum = 0
		self.yvel = 5
		self.y = y
		self.x = x
		self.vel = 0
		self.HERO_IMG = [[pygame.image.load("res/hero.png"),pygame.image.load("res/hero2.png"),pygame.image.load("res/hero3.png"),pygame.image.load("res/hero4.png")],
						 [pygame.transform.flip(pygame.image.load("res/hero.png"), True, False), pygame.transform.flip(pygame.image.load("res/hero2.png"), True, False), pygame.transform.flip(pygame.image.load("res/hero3.png"), True, False), pygame.transform.flip(pygame.image.load("res/hero4.png"), True, False)]]


	def display(self):
		win.blit(self.HERO_IMG[self.imgnum][self.aninum], (self.x - self.HERO_IMG[0][0].get_width()/2 -camerax, self.y - self.HERO_IMG[0][0].get_height()/2 -cameray))

	def move(self):
		self.yvel += 2
		self.y += self.yvel
		self.x += self.vel
		if self.y < -25:
			self.y = -25
		if self.yvel > 20:
			self.yvel = 20
		if self.y > rock1.y-self.HERO_IMG[0][0].get_height()/2 and self.x + self.HERO_IMG[0][0].get_width()/2 > rock1.x and self.HERO_IMG[0][0].get_width()/2 < rock1.x*rock1.tiling:
			self.y = rock1.y-self.HERO_IMG[0][0].get_height()/2

	def jump(self):
		self.yvel = -25

	def walk(self):
		self.aninum= round(self.aninum + self.anispeed)
		if self.aninum == 0:
			self.anispeed = -self.anispeed
		if self.aninum == 3:
			self.anispeed = -self.anispeed

class tile:
	def __init__(self, x, y, typ, tiling):
		self.x = x
		self.y = y
		self.typ = typ
		self.tiling = tiling

		if self.typ == "rock":
			self.tileimg = pygame.image.load("res/rock.png") 

		if self.typ == "grass":
			self.tileimg = pygame.image.load("res/grass.png")

	def display(self):
		for i in range(self.tiling):
			win.blit(self.tileimg, (self.x-camerax+self.tileimg.get_width()*i, self.y-cameray))




def display():
	win.blit(bggimg, (0-camerax*0.1,0-cameray))
	win.blit(bgimg, (0-camerax*0.3,0-cameray))
	hero2.display()
	hero1.display()
	rock1.display()
	pygame.display.update()



hero1 = Hero(SCREEN_LENGTH/2, SCREEN_HEIGHT/3*2)
hero2 = Hero(200, 200)
rock1 = tile(SCREEN_LENGTH/2, SCREEN_HEIGHT/8*7, "grass", 20)
clock = pygame.time.Clock()
while run:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				hero1.vel = -5
				hero1.imgnum = 1
			if event.key == pygame.K_RIGHT:
				hero1.vel = 5
				hero1.imgnum = 0
			if event.key == pygame.K_UP:
				hero1.jump()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				hero1.vel = 0
			if event.key == pygame.K_RIGHT:
				hero1.vel = 0

	if hero1.x > SCREEN_LENGTH/2:
		camerax += hero1.vel
	
	if hero1.x < SCREEN_LENGTH/2:
		camerax += hero1.vel

	hero1.move()
	hero1.walk()
	display()




