import pygame
import sys
from game import Game

text_color = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()

game = Game('assets/bird.png', 'assets/pipe.png', 'assets/background.png', 'assets/floor.png')
game.resize_images()
game.set_font('assets/Baloo-Regular.ttf', 48)

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1800)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit() # shutdown game completely
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE and game.active:
        game.flap()
        
      if event.key == pygame.K_SPACE and game.active == False:
        game.restart()
      
    if event.type == SPAWNPIPE:
      game.add_pipe()
      
  game.show_background(screen)
  
  if game.active:
    game.show_bird(screen)
    game.update_bird()
    game.move_pipes()
    game.draw_pipes(screen)
    game.check_collision()
    game.update_score()
    game.show_score('main_game', screen, text_color)
  else:
    game.game_over(screen, text_color)

  game.draw_floor(screen)
  game.move_floor()
  
  pygame.display.update()
  clock.tick(120) # set the framerate