import sys
import pygame
from pygame.locals import *
from scripts.utils import Text, TextBox
from scripts.game import SingleGame

def single_play(screen, clock):
  game = SingleGame()

  attempt = Text("", 40, (0, 0, 0), [320, 100])
  result = Text("", 40, (0, 0, 0), [320, 200])
  text_box = TextBox([160, 100], (0, 0, 255), [240, 300], text_size=80)

  running = True
  while running:
    data = game.receive_data()

    attempt.update(str(data["attempt_count"]))
    result.update(data["result"])

    screen.fill((255, 255, 255))
    attempt.draw(screen)
    result.draw(screen)
    text_box.draw(screen)

    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type==pygame.KEYDOWN:
        if event.key==K_RETURN:
          game.submit_number(text_box.flush_number())
        elif event.key==K_BACKSPACE:
          text_box.erase_number()
        elif event.unicode.isdigit():
          text_box.write_number(event.unicode)

    pygame.display.update()
    clock.tick(60)
