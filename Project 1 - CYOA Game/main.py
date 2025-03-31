import time
from storylines import outside_library, before_selection, knowledge_path, power_path, freedom_path
from art import logo, gameover

opening_doors = False
choosing_path = False
start_game = False
restart_input = False


def invalid_input():
  print("Invalid input, Please try again.")


def gameplay():
  global opening_doors, choosing_path
    # Main storyline
  for n in outside_library:
    time.sleep(1.2)
    print(n)

  print("\n")
  while not opening_doors:
    time.sleep(1.4)
    door_action = input("Type [open] to open the door, type [leave] to leave the library. \n").lower()
    if door_action == "leave" or door_action == "open":
      if door_action == "leave":
        print("After deep consideration, you have chosen to leave the Library.")
        time.sleep(1.2)
        print("While the allure of knowledge and power is strong, you realize that some doors are better left unopened.")
        time.sleep(1.2)
        print("You turn away from the Midnight Library, stepping back into the world you know.")
        gameover = True
        return
    
    else:
      invalid_input()
      continue
    opening_doors = True
  
  print("\n")
  for text in before_selection["entering_library"]:
    time.sleep(1.2)
    print(text)
  
  print("\n")
  for text in before_selection["inside_library"]:
    time.sleep(1.2)
    print(text)

  print("\n")
  for text in before_selection["librarian_encounter"]:
    time.sleep(1.2)
    print(text)

  print("\n")
  for text in before_selection["path_selection"]:
    time.sleep(1.2)
    print(text)
  
  while not choosing_path:
    time.sleep(1.4)
    print("\n")
    selection = input("Type [knowledge] for the path of knowledge, type [power] for the path of power, type [freedom] for the path of freedom.\n").lower()
    if selection == "knowledge" or selection == "power" or selection == "freedom":
      print(f"You have chosen the path of {selection}.")
      if selection == "knowledge":
        for text in knowledge_path:
          time.sleep(1.2)
          print(text)
        time.sleep(1.4)
        print("You have gained ultimate knowledge, but lost your existence.")
      elif selection == "power":
        for text in power_path:
          time.sleep(1.2)
          print(text)
        time.sleep(1.4)
        print("You have gained ultimate strength, but you can never leave.")
      elif selection == "freedom":
        for text in freedom_path:
          time.sleep(1.2)
          print(text)
        time.sleep(1.4)
        print("You have escaped, but at the cost of never knowing what could have been.")
    else:
      invalid_input()
      continue
    choosing_path = True
    time.sleep(1.5)


def start():
  global start_game
  print(logo)
  print("Welcome to The Midnight Library.")
  while not start_game:
    start = input("Do you have what it takes to explore the Midnight Library? (yes/no)\n").lower()
    if start == "yes":
      print("Great! Let's begin your adventure.")
      print("\n")
      time.sleep(1.2)
      start_game = True
      gameplay()
    elif start == "no":
      print("That's okay! Maybe another time.")
      print("\n")
      return
    else:
      invalid_input()
      continue

start()
start_game = False
restart_input = False
time.sleep(1.2)
print(gameover)
print("\n")
time.sleep(1.2)

while not restart_input:
  restart = input("Do you want to play again? (yes/no)\n").lower()
  if restart == "yes" or restart == "no":
    if restart == "yes":
      opening_doors = False
      choosing_path = False
      restart_input = True
      start()
    elif restart == "no":
      print("Thank you for playing!")
      restart_input = True
      break
  else:
    invalid_input()
    continue
