import pygame,sys,random
pygame.init()
clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("A screensaver.")



class Box:
  def __init__(self,x,y,wid,heit):
    self.x = x
    self.y = y
    self.wid = wid
    self.heit = heit
    self.col = random.choice(['red','green','blue','purple','yellow','violet'])
    self.speed_x = random.randint(2,5)
    self.speed_y = random.randint(1,5)

 

  def draw(self,screen):
    pygame.draw.rect(screen,self.col,(self.x,self.y,self.wid,self.heit))

  def speed_update(self):
    self.x += self.speed_x
    self.y += self.speed_y
    if self.x>=600-self.wid: 
      self.speed_x = -self.speed_x
    if self.x<=0:
      if self.speed_x>=0:
        pass
      else:
        self.speed_x = -self.speed_x

    if self.y>=600-self.heit:
      self.speed_y = -self.speed_y
    if self.y<=0:
      if self.speed_y>=0:
        pass
      else:
        self.speed_y = -self.speed_y


boxes = []

mainBox = Box(random.randint(40,560),random.randint(40,560),40,40)
mainBox.speed_x = random.randint(3,6)
mainBox.speed_y = random.randint(3,6)


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()



  if mainBox.x >= 560 or mainBox.x <= 0:
    boxes.append(Box(mainBox.x,mainBox.y,10,10))
  if mainBox.y>=560 or mainBox.y<=0:
    boxes.append(Box(mainBox.x,mainBox.y,10,10)) 
    

  screen.fill("black")
  mainBox.draw(screen)
  mainBox.speed_update()
  for i in range(len(boxes)):
    boxes[i].draw(screen)
    boxes[i].speed_update()
    

  pygame.display.update()
  clock.tick(FPS)