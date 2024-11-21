import string, random
import sys

start="r"


print()
print("Version 1.1.2")
print()
print()
print()
print()
while start != "e":

  O=input("do you want to generate a password, find a password, or view patch notes?(g/f/p): ")
  print()

  while O!="g" and O!="f" and O!="p":
    print()
    print("misinput, try again")
    print()
    O=input("do you want to generate a password, find a password, or view patch notes?(g/f/p): ")
    

  if O=="g": 
  

    u = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    def random_char(y):
         return ''.join(random.choice(u) for w in range(y))

    b = (random_char(13))
  

    s = str(input("What is this password for? (eg. Google, Steam, Bank, etc.): "))
    print("Password: " + b)
    s = s + ".txt"


    n = open(s, "w")
    n.write(b)
    n.close()

  if O=="f":
   passCor = False
   while passCor == False: 
     c=input("What is the password for? (eg. Google, Steam, Bank, etc.): ")

     c = c + ".txt"
     try: 
       n = open(c, "r")
       print()
       print()
       print("-------------------------")
       print(n.read())
       print("-------------------------")
       passCor = True
     except:
       print("File not found. Make sure the name is correct.")
      
       b = input("Do you want to try again? (y/n): ")
       while b != "y" and b != "n":
         print("Misinput, try again")
         b = input("Do you want to try again? (y/n): ")
       if b == "n":
         passCor = True

  if O=="p": 
    print("-Added version number")
    print("-Spaced out lines more")
    print("-looped program")
    print("-added patch notes page")
    print("-improved code efficiency and organization ")
    print()
    print("Made by polp7")
    print()
    print("Latest update: t.ly/ytyR")
    print()
    print()
	
  start = input("Return to start or exit?(r/e): ")
  while start != "r" and start != "e":
    print()
    print("misinput, try again")
    print()
    start = input("Return to start or exit?(r/e): ")    
  if start=="e":
    sys.exit()
    






 
