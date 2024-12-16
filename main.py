print("The Guessing Game")
counter = 0
number = 950
while True:
  value = int(input("Guess the chosen number:"))
  if value == number:
    print("That's correct!!")
    exit()
    counter+=1
  elif value < number:
    print("Incorrect,that's low")
    counter+=1
  elif value > number:
      print ("That's too high")
      counter+=1
  elif value <1:
      break
print ("You got the answer in",counter,"times")