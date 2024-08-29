print ("Fake Fan Finder")
print()
superfan = input("Are you a superfan of 'Money Heist'? ")
if superfan == "yes":
  print("Oh really?")
  character = input("Name me any of the charecters? ")
  if character == "Professor" or character == "Tokyo" or character == "Rio" or character == "Berlin" or character == "Moscow":
    print("You got that by pure chance.")
    bank = input("Okay then, what is the name of the bank that the professor is robbing? ")
    if bank == "Bank of Spain":
      print("Hmph!")
      animal = input("What animal is in Money Heist? ")
      if animal == "ferret":
        print("You are a true fan!")
      else:
        print("Fake fan! Fake fan!")
    else:
      print("Fake fan!")
  else:
    print("See! Fake Money Heist fan!")
else:
  print("okay")