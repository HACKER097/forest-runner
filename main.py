import pygame

SCREEN_HEIGHT = 600
SCREEN_LENGTH = 600

camerax = 0
cameray = 0

win = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_LENGTH))
pygame.display.flip()
pygame.mixer.init()

jump = pygame.mixer.Sound("res/powerup.wav")
hurt = pygame.mixer.Sound("res/hurt.wav")
pygame.mixer.music.load('res/music.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
run = True

class Hero:

	def __init__(self, x, y):
		self.health = 10
		self.healthimg = pygame.image.load("res/health.png")
		self.isani = False
		self.anispeed = 0.1
		self.aninum = 0
		self.imgnum = 0
		self.yvel = 5
		self.y = y
		self.x = x
		self.vel = 0
		self.HERO_IMG = [[pygame.image.load("res/hero.png"),pygame.image.load("res/hero2.png"),pygame.image.load("res/hero3.png"),pygame.image.load("res/hero4.png"), pygame.image.load("res/hero5.png"), pygame.image.load("res/hero6.png")],
						 [pygame.transform.flip(pygame.image.load("res/hero.png"), True, False), pygame.transform.flip(pygame.image.load("res/hero2.png"), True, False), pygame.transform.flip(pygame.image.load("res/hero3.png"), True, False), pygame.transform.flip(pygame.image.load("res/hero4.png"), True, False), pygame.transform.flip(pygame.image.load("res/hero5.png"), True, False), pygame.transform.flip(pygame.image.load("res/hero6.png"), True, False)]]



	def move(self):
		self.yvel += 2
		self.y += self.yvel
		self.x += self.vel
		if self.y < -25:
			self.y = -25
		if self.yvel > 20:
			self.yvel = 20
		if self.y > rock1.y-self.HERO_IMG[0][0].get_height()/2 +30:
			self.y = rock1.y-self.HERO_IMG[0][0].get_height()/2 + 30

		if self.x < SCREEN_LENGTH/2:
			self.x = SCREEN_LENGTH/2

	def jump(self):
		pygame.mixer.Sound.play(jump)
		self.aninum = 4
		self.yvel = -25

	def walk(self):
		if self.isani:
			self.aninum += self.anispeed
			if self.aninum >= 3:
				self.aninum = 0



	def movement(self):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.isani = True
				self.vel = -2
				self.imgnum = 1
			if event.key == pygame.K_RIGHT:
				self.isani = True
				self.vel = 2
				self.imgnum = 0
			if event.key == pygame.K_UP:
				hero1.jump()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				self.isani = False
				self.aninum = 0
				self.vel = 0
			if event.key == pygame.K_RIGHT:
				self.isani = False
				self.aninum = 0
				self.vel = 0

	def colission(self, objx, objy, objlenth, objwidth):
		currenthealth = round(self.health)
		if self.x + self.HERO_IMG[0][0].get_width() > objx and self.x < objx+objlenth and self.y + self.HERO_IMG[0][0].get_height() > objy and self.y < objy+objwidth:
			self.health -= 0.1
		for i in  range(round(self.health)):
			win.blit(self.healthimg, (10+(i-1)*10, 10))
		if self.health < 0:
			self.health = 0
		if not currenthealth == round(self.health):
			self.aninum = 5
			pygame.mixer.Sound.play(hurt)
		pygame.display.update()


	def display(self):
		win.blit(self.HERO_IMG[self.imgnum][round(self.aninum)], (self.x - self.HERO_IMG[0][0].get_width()/2 -camerax, self.y - self.HERO_IMG[0][0].get_height()/2 -cameray))



class tile:
	def __init__(self, x, y, typ, tiling, cameraref):
		self.x = x
		self.y = y
		self.typ = typ
		self.tiling = tiling
		self.cameraref = cameraref

		if self.typ == "rock":
			self.tileimg = pygame.image.load("res/rock.png") 

		if self.typ == "grass":
			self.tileimg = pygame.image.load("res/grass.png")

		if self.typ == "bg":
			self.tileimg = pygame.image.load("res/forest.png")

		if self.typ == "bgg":
			self.tileimg = pygame.image.load("res/bgg.png")

	def display(self):
		if self.typ == "bg" or self.typ == "bgg":
			for i in range(self.tiling):
				win.blit(self.tileimg, (self.x - camerax*self.cameraref + self.tileimg.get_width() * 2 * i, self.y -cameray))
				win.blit(pygame.transform.flip(self.tileimg, True, False), (self.x -camerax*self.cameraref+self.tileimg.get_width()*2*i + self.tileimg.get_width() , self.y -cameray)) 
		else:
			for i in range(self.tiling):
				win.blit(self.tileimg, (self.x-camerax+self.tileimg.get_width()*i, self.y-cameray))


def display():
	bg2.display()
	bg1.display()
	hero2.display()
	hero1.display()
	rock1.display()
	pygame.display.update()



hero1 = Hero(SCREEN_LENGTH/2, SCREEN_HEIGHT/3*2)
hero2 = Hero(400, 400)
rock1 = tile(0, SCREEN_HEIGHT/8*7, "rock", 100, 1)
bg1 = tile(0, 0, "bg", 3, 0.2)
bg2 = tile(0, 0, "bgg", 2, 0.1)
clock = pygame.time.Clock()
while run:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		hero1.movement()

	if hero1.x > SCREEN_LENGTH/2:
		camerax += hero1.vel
	
	if hero1.x < SCREEN_LENGTH/2:
		camerax += hero1.vel

	hero1.move()
	hero1.walk()
	display()
	hero1.colission(hero2.x, hero2.y, hero2.HERO_IMG[0][0].get_height(), hero2.HERO_IMG[0][0].get_width())




