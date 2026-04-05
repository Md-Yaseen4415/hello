import pygame,sys,random
pygame.init()
clock = pygame.time.Clock()
FPS =60
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("sand simulation")
blocks = []
filled_blocks = []


class Block:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.fill = 0
  
  def draw(self):
    pygame.draw.rect(screen,'yellow',(self.x,self.y,10,10))
  
for i in range(60):
  rows = []
  for j in range(60):
    rows.append(Block(i*10,j*10))
  blocks.append(rows)

def update_blocks(block):
  if block.y//10 < 59:
    nex_blk = blocks[(block.x//10)][(block.y//10)+1]
    if nex_blk not in filled_blocks:
      filled_blocks.append(blocks[(block.x//10) ][(block.y//10) + 1])
      #print(block.x/10,block.y/10 + 1) 
      filled_blocks.remove(block)


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print(len(filled_blocks))
      pygame.quit()
      sys.exit()
    
    mou_evnt = pygame.mouse.get_pressed()
    if mou_evnt[0] == True:
      gr_y = pygame.mouse.get_pos()[1]//10
      gr_x = pygame.mouse.get_pos()[0]//10
      blk = blocks[gr_x][gr_y]
      filled_blocks.append(blk)



  screen.fill("black")
  #pygame.draw.rect(screen,'yellow',(gr_x *10,gr_y *10,20,20))
  for block in filled_blocks:
    block.draw()
    update_blocks(block)
  pygame.display.update()
  clock.tick(FPS)