class Cat:
  def __init__(self, name, preferred_food, meal_time):
    self.name = name
    self.preferred_food = preferred_food
    self.meal_time = meal_time

  def __str__(self):
    return f"Name: {self.name} \nPreferred Food: {self.preferred_food}"

  def eats_at(self):
    if self.meal_time < 12:
      return f"{self.meal_time} AM"
    else:
      return f"{self.meal_time - 12} PM"

  def meow(self):
    return f"My name is {self.name}, and my favourite food is {self.preferred_food.lower()}. You can feed me at {self.eats_at()}"

charlie = Cat('Charlie', 'Tuna', 17)
jazzy = Cat('Jazzy', 'Everything', 8)

print()
print(charlie)
print(jazzy)

print()
print(charlie.eats_at())
print(jazzy.eats_at())

print()
print(charlie.meow())
print(jazzy.meow())