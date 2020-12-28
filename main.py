answer = input("Are you ready to play? (yes/no ")
if answer.lower().strip() == "yes":
  answer = input("You are on crossroad, would you like to turn left or right? ")
  if answer == "left":
    answer = input("you encounter a bear , would you like to run or attack?")
    if answer == "attack":
      print("bad idea, cant fight a bear, you lost")
    else:
      print("Good idea, you made it out safely")
      answer = input ("you see a car and boat, which one you choose?")
      if answer == "boat":
        print("you do not know how to operate a boat, you lost")
      else:
          print("you won! have a great day")

  elif answer == "right":
        print("you walk aimlessly in to a forest and get lost, game over")

  else: 
     Print("Oops , bad choice !You lost the game")

else:
    print("Okay! see you another day ")
