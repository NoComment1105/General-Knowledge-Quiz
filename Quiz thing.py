#This is a quiz that takes in data of each player and records their highscore
print("Good Morning, Good evening, Good night, Good Day, Welcome to this fabulous general knowledge quiz i have concocted. It asks for your name and some other things and stores them so you can track your high score even when you close the program")
players=[]
with open("highscores.txt","r") as InFile:
     line=InFile.readline()
     while line:
          players.append(line.rstrip("\n").split(","))
          line=InFile.readline()
name = input("Please enter your name ")
age = input("Please enter your age ")
shoeSize = input("Enter your shoe size (yes) ")


counter = 0
print("In all questions start it with a capital, and grammar and stuff \n")
answerQ1 = input("Question 1: What year did the Titanic sink on April 15, on it's maiden voyage? ")
if answerQ1 == "1912":
     print("Correct\n")
     counter = counter + 1
else:
     print("Unlucky, Incorrect. The answer is 1912\n")

answerQ2 = input("What is the Chemical Symbol for Silver? is it a) S   b) K  c) Ag (answer with the letter) ")
if answerQ2 == "c":
     print("Correct\n")
     counter = counter + 1
else:
     print("Incorrect. The correct answer is Ag\n")

answerQ3 = input("What is the capital of Portugal? ")
if answerQ3 == "Lisbon":
     print("Correct\n")
     counter = counter + 1
else:
     print("Unlucky. The correct answer is Lisbon\n")

answerQ4 = input("Who created the police force? was it a) Alan Turing  b) Clint Eastwood c) Robert Peel  d) Bob Unwrap (answer with letter) ")
if answerQ4 == "c":
     print("Correct\n")
     counter = counter + 1
else:
     print("Incorrect. It was actually founded by Robert Peel\n")

answerQ5 = input("What is the name of the film starring Chris Hemsworth and Daniel Brühl, charts the formula 1 rivalry of James Hunt and Niki Lauda? ")
if answerQ5 == "Rush":
     print("Correct\n")
     counter = counter + 1
else:
     print("Incorrect. The answer is 'Rush'\n")

answerQ6 = int(input("If a = 7, B = 3 and C = 4 What is abcc? "))
if answerQ6 == 336:
     print("Correct!\n")
     counter = counter + 1
else:
     print("Unlucky the answer is 336. (You get the answer because abcc means a x b x c x c)\n ")

answerQ7 = input("Riddle Time: What question can you never answer yes to? (remember grammar) ")
if answerQ7 == "Are you asleep yet?":
     print("Correct. Well done\n")
     counter = counter + 1
else:
     print("Incorrect, the answer is: 'Are you asleep yet?\n'")

answerQ8 = input("The sun rises in the east and sets in the ____ ")
if answerQ8 == "west":
     print("Correct\n")
     counter = counter + 1
else:
     print("Unlucky. The answer is west\n")

answerQ9 = int(input("How many aces are there in a deck of cards? (enter integer)"))
if answerQ9 == 4:
     print("Well done, Correct\n")
     counter = counter + 1
else:
     print("Incorrect, the answer is 4, spades hearts clubs and diamonds")

answerQ10 = input("Round and round the ______ like a teddy bear one step two step tickly under there")
if answerQ10 == "garden":
     print("Correct :)\n")
     counter = counter + 1
else:
     print("Incorrect, the answer is garden")


counterstr = str(counter)
with open("highscores.txt","a") as file1:
               file1.write(name+","+age+","+shoeSize+","+counterstr+"\n")
               
print("Well Done! You have completed this quiz; you scored:", counter, "Whoop!")

for i in range(len(players)):
     if players[i][0] == name:
          print("Your previous highscore was",players[i][3])
          print("This time you scored", counter)
     else:
          toe = 1
