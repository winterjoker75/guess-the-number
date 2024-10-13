import random

class SingleGame:
  def __init__(self):
    self._secret_number = random.randint(1, 100)
    self._attempt_count = 0
    self.current_number = 1
    self.result = ""
  
  def submit_number(self, number):
    try:
      self.result = self._evaluate_guess(number)
      self._attempt_count += 1
      self.current_number = number
    except Exception as e:
      print(e)
  
  def receive_data(self):
    return {
      "current_number": self.current_number,
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
    return f"{number} {"UP" if self._secret_number>number else "DOWN"}"
