import sys
import pygame
from scripts.game import SingleGame
from scripts.utils import Text, Button
from scenes.single_play import single_play
from scenes.game_over import game_over

def main_menu(screen, clock):
  title = Text("Up Down Game", 50, (0, 0, 255), [320, 150])
  title.move_center()

  play_btn = Button("PLAY", [100, 50], (0, 255, 0), [200, 300], text_size=30)
  exit_btn = Button("EXIT", [100, 50], (255, 0, 0), [340, 300], text_size=30)

  click = False
  while True:
    mx, my = pygame.mouse.get_pos()

    if play_btn.is_collided((mx, my)) and click:
      game = SingleGame()
      single_play(screen, clock, game)
      game_over(screen, clock, game)
    
    if exit_btn.is_collided((mx, my)) and click:
      pygame.quit()
      sys.exit()

    screen.fill((255, 255, 255))
    title.draw(screen)
    play_btn.draw(screen)
    exit_btn.draw(screen)

    click = False
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type==pygame.MOUSEBUTTONDOWN:
        click = True
    
    pygame.display.update()
    clock.tick(60)
