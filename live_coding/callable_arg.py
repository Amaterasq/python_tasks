import random

COUNT = 10


class Spam:
  def __init__(self, value):
    self.data = value

  def __repr__(self):
    return f'{self.__class__.__name__}({self.data})'


spams = [Spam(n) for n in random.choices(range(COUNT), k=COUNT)]
print(spams)

spams.sort(key=lambda x: x.data)
print(spams)
# Что нужно сделать, чтобы отсортировать лист spams по значениям self.data?
# Код можно редактировать.