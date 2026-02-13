import random

def spin_twister_spinner():
  """
  Returns a list with a random color, side, and appendage
  
  colors: "red", "green", "yellow", or "blue"
  sides: "left" or "right"
  appendage: "hand" or "foot"
  """
  colors = ["red", "green", "yellow", "blue"]
  side = ["left", "right"]
  limb = ["hand", "foot"]
  print()
  print(f"{random.choice(side)} {random.choice(limb)} on {random.choice(colors)}!")
  print()

# Here's the function call. This should print a random assortment of twister commands
def spin():
  print(spin_twister_spinner())
  cont = input("would you like to spin again? (y/n): ")
  if cont == "y":
    spin()
  elif cont == "n":
    print("ok")
  else:
    print("im taking that as a yes")
    spin()

spin()