import math
import pygame
import random
from scripts.utils import Text
import globals.values

class SingleGame:
  def __init__(self):
    globals.values.left = 1
    globals.values.right = 100
    self._secret_number = random.randint(globals.values.left, globals.values.right)
    self._attempt_count = 0
    self.result = ""
  
  def submit_number(self, number):
    try:
      self.result = self._evaluate_guess(number)
      self._attempt_count += 1
    except Exception as e:
      print(e)
  
  def receive_data(self):
    return {
      "result": self.result,
      "attempt_count": self._attempt_count
    }
  
  def receive_result(self):
    return {
      "secret_number": self._secret_number,
      "attempt_count": self._attempt_count
    }

  def _evaluate_guess(self, number):
    if self._secret_number==number:
      return "ok"
    return f"{"UP" if self._secret_number>number else "DOWN"}"

class Box:
  def __init__(self, size, color, location, text = "", text_size = 40, text_color = (0, 0, 0)):
    self.location = location
    
    text = Text(text, text_size, text_color, [0, 0])
    text_size = text.text.get_size()
    text.location = [(size[0]-text_size[0])/2, (size[1]-text_size[1])/2]

    self.surf = pygame.Surface(size)
    self.surf.fill(color)
    text.draw(self.surf)
    pygame.draw.rect(self.surf, (0, 0, 0), ((0, 0), (size)), 2)

  def update(self, speed):
    self.location[0] = (self.location[0]*10+speed*10)/10

  def draw(self, screen):
    screen.blit(self.surf, self.location)

class Container:
  def __init__(self, location, box_size = [100, 50], box_color = (255, 255, 255)):
    location[0] -= box_size[0]
    self.boxes = []
    for i in range(0, 102):
      self.boxes.append(Box(box_size, box_color, [location[0]+i*box_size[0], location[1]], text=str(i)))

    self.curr = 1
    self.set_next(1)

    self.speed = 0
    self.removable = False

  def update(self, result):
    if result=="":
      return
    if self.curr==self.next:
      return
    
    # left to right
    if self.curr<self.next and self.curr_box_location[0]>=self.next_box_location[0]:
      if self.removable:
        # self.boxes = self.boxes[(self.curr-1):]
        if result=="UP":
          globals.values.left = self.curr
        else:
          globals.values.right = self.curr
        self.removable = False
      self.curr_box_location[0] = math.floor(self.curr_box_location[0])
      self.speed = 0
      return
    
    # right to left
    if self.curr>self.next and self.curr_box_location[0]<=self.next_box_location[0]:
      if self.removable:
        # self.boxes = self.boxes[:(self.curr+2)]
        if result=="UP":
          globals.values.left = self.curr
        else:
          globals.values.right = self.curr
        self.removable = False
      self.curr_box_location[0] = math.floor(self.curr_box_location[0])
      self.speed = 0
      return
    
    if self.curr_box_location[0]<self.average:
      for i in range(len(self.boxes)):
        self.boxes[i].update(self.speed)
      self.speed = (self.speed*10+1)/10
    else:
      for i in range(len(self.boxes)-1):
        self.boxes[i].update(self.speed)
      self.speed = (self.speed*10-1)/10

  def draw(self, screen):
    # for i in range(1, len(self.boxes)-1):
    for i in range(globals.values.left, globals.values.right+1):
      self.boxes[i].draw(screen)

  def set_next(self, next):
    try:
      assert globals.values.left<=next<=globals.values.right

      self.next = self.curr
      self.curr = next

      self.curr_box = self.boxes[self.curr]
      self.next_box = self.boxes[self.next]

      self.curr_box_location = self.curr_box.location
      self.next_box_location = list(self.next_box.location)

      self.average = (self.curr_box_location[0]+self.next_box_location[0])/2

      self.removable = True
    except Exception as e:
      globals.values.myOF = 1
      print(e)
