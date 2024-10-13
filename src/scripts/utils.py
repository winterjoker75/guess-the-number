import math
import pygame
from enum import Enum

class Text:
  def __init__(self, text, size, color, location):
    self.color = color
    self.location = location

    self.font = pygame.font.SysFont("Arial", size)
    self.text = self._render(text)

  def update(self, text):
    self.text = self._render(text)

  def draw(self, screen):
    screen.blit(self.text, self.location)

  def _render(self, text):
    return self.font.render(text, True, self.color)
  
class State(Enum):
  wrong = (255, 0, 0)
  accept = (0, 255, 0)

class TextBox:
  def __init__(self, size, color, location, text_size = 100, text_color = (0, 0, 0), border = 5):
    self.size = size
    self.color = color
    self.location = location
    self.border = border

    self.text_width = [math.ceil(1.68*text_size), math.ceil(1.12*text_size)]
    self.text_location = [(size[0]-self.text_width[0])//2, (size[1]-self.text_width[1])//2]

    self.surf = pygame.Surface(size)
    self.text = Text("", text_size, text_color, self.text_location)

    self.surf.fill((255, 255, 255))
    pygame.draw.rect(self.surf, color, ((0, 0), (size)), border)

    self.number = ""
  
  def draw(self, screen):
    screen.blit(self.surf, self.location)

  def flush_number(self) -> int:
    try:
      flushed_number = int(self.number)
      assert 1<=flushed_number<=100
      self.number = ""
      pygame.draw.rect(self.surf, (255, 255, 255), (
        (self.text_location[0], self.text_location[1]),
        (self.text_width[0], self.text_width[1])
      ))
      pygame.draw.rect(self.surf, State.accept.value, ((0, 0), (self.size)), self.border)
      return flushed_number
    except:
      pygame.draw.rect(self.surf, State.wrong.value, ((0, 0), (self.size)), self.border)

  def write_number(self, digit):
    try:
      assert len(self.number)<3
      self.text.location = [
        self.text_location[0]+self.text_width[0]*len(self.number)/3,
        self.text_location[1]
      ]
      self.number += digit
      self.text.update(digit)
      self.text.draw(self.surf)
      pygame.draw.rect(self.surf, self.color, ((0, 0), (self.size)), self.border)
    except:
      pygame.draw.rect(self.surf, State.wrong.value, ((0, 0), (self.size)), self.border)

  def erase_number(self):
    self.number = self.number[:-1]
    pygame.draw.rect(self.surf, (255, 255, 255), (
      (self.text_location[0]+self.text_width[0]*len(self.number)/3, self.text_location[1]),
      (self.text_width[0]/3, self.text_width[1])
    ))
    pygame.draw.rect(self.surf, self.color, ((0, 0), (self.size)), self.border)