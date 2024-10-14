import sys
import pygame
from scripts.utils import Text, Button

def game_over(screen, clock, game):
  data = game.receive_result()

  secret_number = Text(f"The secret number was {data["secret_number"]}", 40, (0, 0, 0), [320, 150])
  attempt = Text(f"You tried {data["attempt_count"]} times", 30, (0, 0, 0), [320, 250])
  menu_btn = Button("MENU", [100, 50], (0, 255, 0), [270, 350], text_size=30)

  secret_number.move_center()
  attempt.move_center()

  click = False
  while True:
    mx, my = pygame.mouse.get_pos()
    if menu_btn.is_collided((mx, my)) and click:
      break

    screen.fill((255, 255, 255))
    secret_number.draw(screen)
    attempt.draw(screen)
    menu_btn.draw(screen)

    click = False
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type==pygame.MOUSEBUTTONDOWN:
        click = True
    
    pygame.display.update()
    clock.tick(60)
