import pygame,sys,random
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
fps = 10
screen = pygame.display.set_mode((500,500))
snake_body = []
score = 0

eat_sound = pygame.mixer.Sound("eat_sound.mp3")

class SnakeBody:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.speed_x = 0
    self.speed_y = 0

  def draw(self):
    pygame.draw.rect(screen,'red',(self.x,self.y,16,16))

  
  def follow(self,lead,head):
    self.x = lead.x
    self.y = lead.y

class SnakeHead(SnakeBody):
  def __init__(self,x,y):
    super().__init__(x,y)
    self.speed_x = 0
    self.speed_y = 0

  def pos_update(self):
    self.x+=self.speed_x
    self.y+=self.speed_y

  def loc_check(self):
    if self.x >=512:
      self.x = 0
      return
    if self.x <= -15:
      self.x = 500
      return
    if self.y >= 512:
      self.y = 0
      return
    if self.y<=-15:
      self.y = 500
      return

class Snack:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  
  def draw(self):
    pygame.draw.ellipse(screen,'green',(self.x,self.y,12,12))

  def reappear(self):
    pygame.draw.ellipse(screen,'green',(random.randint(8,492),random.randint(8,492),12,12))

head = SnakeHead(50,50)
snake_body.append(head)
snack = Snack(300,400)



while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print(f"score is {score}")
      print(len(snake_body))
      print(body_rects)
      pygame.quit()
      sys.exit()

    keys = pygame.key.get_pressed()
  body_rects = [None]*len(snake_body)
  for snake in snake_body:
    if keys[pygame.K_RIGHT]:
      if head.speed_x == 0:
        snake.speed_x = 16
        snake.speed_y = 0

    if keys[pygame.K_LEFT]:
      if head.speed_x == 0:
        snake.speed_x = -16
        snake.speed_y = 0

    if keys[pygame.K_DOWN]:
      if head.speed_y == 0:
        snake.speed_x = 0
        snake.speed_y = 16

    if keys[pygame.K_UP]:
      if head.speed_y == 0:
        snake.speed_x = 0
        snake.speed_y = -16


  screen.fill("black")
  #head.draw()
  for i in range(len(snake_body)):
    snake_body[i].draw()
  snack.draw()
  head.loc_check()
  head.pos_update()

  snack_rect = pygame.Rect(snack.x,snack.y,12,12)
  head_rect = pygame.Rect(head.x,head.y,16,16)


  for j in range(len(snake_body)-1,0,-1):
    snake_body[j].follow(snake_body[j-1],head)
  
  for i in range(len(snake_body)):
    body_rects[i] = pygame.Rect(snake_body[i].x,snake_body[i].y,16,16)
      
  
      

  if head_rect.colliderect(snack_rect):
    eat_sound.play(maxtime=700)
    last_rect = snake_body[len(snake_body)-1]
    if last_rect.speed_y>0:
      newx = last_rect.x
      newy = last_rect.y-16
    if last_rect.speed_y<0:
      newx = last_rect.x
      newy = last_rect.y+16
    if last_rect.speed_x>0:
      newx = last_rect.x-16
      newy = last_rect.y
    if last_rect.speed_x<0:
      newx = last_rect.x+16
      newy = last_rect.y
    #body_rects.append([newx,newy,16,16])
    snake_body.append(SnakeBody(newx,newy))
    snack.x = random.randint(10,488)
    snack.y = random.randint(10,488)
    score+=1

  if len(body_rects)>3:
    for i in range(2,len(body_rects)):
      if head_rect.colliderect(body_rects[i]):
        print(f"your score is {score}")
        pygame.quit()
        sys.exit()
    


  pygame.display.update()
  clock.tick(fps)


  