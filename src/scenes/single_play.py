import sys
import pygame
from pygame.locals import *
from scripts.utils import Text, TextBox
from scripts.game import Container

def single_play(screen, clock, game):
  attempt = Text("", 40, (0, 0, 0), [200, 100])
  container = Container([270, 200])
  text_box = TextBox([160, 100], (0, 0, 255), [240, 300], text_size=80)

  running = True
  while running:
    data = game.receive_data()

    if data["result"]=="ok":
      running = False

    attempt.update(f"Tried {data["attempt_count"]} times")
    container.update(data["result"])

    screen.fill((255, 255, 255))
    attempt.draw(screen)
    container.draw(screen)
    text_box.draw(screen)

    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type==pygame.KEYDOWN:
        if event.key==K_RETURN:
          flushed_number = text_box.flush_number()
          if flushed_number and container.left<=flushed_number<=container.right:
            container.set_next(flushed_number)
            game.submit_number(flushed_number)
        elif event.key==K_BACKSPACE:
          text_box.erase_number()
        elif event.unicode.isdigit():
          text_box.write_number(event.unicode)

    pygame.display.update()
    clock.tick(60)
