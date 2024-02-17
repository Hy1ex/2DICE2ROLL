import random as rand
import sys
import os
import time

def exit():
	print("\nAUTHOR:")
	print("""┏┓ ┏┓┏┓  ┏┓ ┏┓ ┏━━━┓┏━┓┏━┓
┃┃ ┃┃┃┗┓┏┛┃┏┛┃ ┃┏━━┛┗┓┗┛┏┛
┃┗━┛┃┗┓┗┛┏┛┗┓┃ ┃┗━━┓ ┗┓┏┛
┃┏━┓┃ ┗┓┏┛  ┃┃ ┃┏━━┛ ┏┛┗┓
┃┃ ┃┃  ┃┃  ┏┛┗┓┃┗━━┓┏┛┏┓┗┓
┗┛ ┗┛  ┗┛  ┗━━┛┗━━━┛┗━┛┗━┛""")
	input("\nPress ENTER to EXIT!!")
	sys.exit()


def gameMenu():
	global selectedMenu

	os.system("cls")
	print("Welcome to 2DICE2ROLL\n1.PLAY\n2.Tutorial\n3.Credits")
	selectedMenu = input("CHOOSE: [1/2/3] > ")

	if selectedMenu == "r":
		main()
	elif selectedMenu == "e":
		exit()

	if selectedMenu == "1" or selectedMenu == "2" or selectedMenu == "3":
		pass
	else:
		input("\nInvalid OPTION!! : Please choose with [1/2/3]")
		gameMenu()

	selectedMenu = int(selectedMenu)

	if selectedMenu == 2:
		print("""\n\244 2DICE2ROLL: or Two Dice to Roll is game all based on chance.
	TUTURIAL: Explaining the Gamemodes: 1.Normal(In this game-
	mode you play as normal, guess the number, get point &
	break the records) & 2.DUEL(In this gamemode, There is
	Two players, guess the number, get points & check who won)
	Explaining the Difficultys: 0.Super Easy(1 DICE), 1.Easy(
	2 DICE), 2.Normal(3 DICE), 3.Hard(4 DICE), 4.EXTREME(10 DICE)
	Other things are clear, LET'S GO PLAY.
	COMMANDS: (e)for exit & (r)for restart.""")

		input("\nPress ENTER to EXIT!!")
		gameMenu()
	elif selectedMenu == 3:
		print("\nAUTHOR:")
		print("""┏┓ ┏┓┏┓  ┏┓ ┏┓ ┏━━━┓┏━┓┏━┓
┃┃ ┃┃┃┗┓┏┛┃┏┛┃ ┃┏━━┛┗┓┗┛┏┛
┃┗━┛┃┗┓┗┛┏┛┗┓┃ ┃┗━━┓ ┗┓┏┛
┃┏━┓┃ ┗┓┏┛  ┃┃ ┃┏━━┛ ┏┛┗┓
┃┃ ┃┃  ┃┃  ┏┛┗┓┃┗━━┓┏┛┏┓┗┓
┗┛ ┗┛  ┗┛  ┗━━┛┗━━━┛┗━┛┗━┛""")

		input("\nPress ENTER to EXIT!!")
		gameMenu()
	elif selectedMenu == 1:
		gamemode()


def gamemode():
	global gameMode

	os.system("cls")
	print("GAMEMODES: \n1.Normal Mode\n2.DUEL Mode aka Multiplayer")
	gameMode = input("CHOOSE: [1/2] > ")

	if gameMode == "r":
		main()
	elif gameMode == "e":
		exit()

	if gameMode == "1" or gameMode == "2":
		pass
	else:
		input("\nInvalid GAMEMODE!! : Please choose with [1/2]")
		gamemode()

	gameMode = int(gameMode)


def difficulty():
	global difficultyLvl

	os.system("cls")
	print("DIFFICULTY LEVEL: \n0.SUPER EASY\n1.EASY\n2.NORMAL\n3.HARD\n4.EXTREME")
	difficultyLvl = input("CHOOSE: [0/1/2/3/4] > ")

	if difficultyLvl == "r":
		main()
	elif difficultyLvl == "e":
		exit()

	if difficultyLvl == "0" or difficultyLvl == "1" or difficultyLvl == "2" or difficultyLvl == "3" or difficultyLvl == "4":
		pass
	else:
		input("\nInvalid DIFFICULTY LEVEL!! : Please choose with [0/1/2/3/4]")
		difficulty()

	difficultyLvl = int(difficultyLvl)


def EXTDifficultyCheck():
	EXTDifficultyChecker = input("\nAre you sure about playing EXTREME Mode?(!!10 Dice!!) [y/n] > ")

	if EXTDifficultyChecker == "r":
		main()
	elif EXTDifficultyChecker == "e":
		exit()

	if EXTDifficultyChecker == "y" or EXTDifficultyChecker == "Y" or EXTDifficultyChecker == "yes" or EXTDifficultyChecker == "Yes" or EXTDifficultyChecker == "YES" or EXTDifficultyChecker == "yEs" or EXTDifficultyChecker == "yeS" or EXTDifficultyChecker == "YEs" or EXTDifficultyChecker == "yES" or EXTDifficultyChecker == "YeS" or EXTDifficultyChecker == "yeah":
		print("Ok")
	else:
		difficulty()


def rounds():
	global roundNum
	roundNum = input("\nHow many rounds do you want to play: > ")

	if roundNum == "r":
		main()
	elif roundNum == "e":
		exit()

	roundNum = int(roundNum)


def normalDifficultySuperEasy():
	point = 0
	pointX = 0
	os.system("cls")
	for x in range(roundNum):
		time.sleep(1.5)

		print("")
		for i in range(5):
			sys.stdout.write("\rROLLING THE DICE{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.55)

		dice = rand.randrange(1, 6)
		guess = input("\n\nGuess the NUMBER: [1 - 6] > ")

		if guess == "r":
			main()
		elif guess == "e":
			exit()

		if guess == "1" or guess == "2" or guess == "3" or guess == "4" or guess == "5" or guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		result = dice - int(guess)
		result = abs(result)

		if result == 0:
			point = 10 + point
			pointX = 10
		elif result <= 2:
			point = 7 + point
			pointX = 7
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0

		time.sleep(1.1)
		print("Your DICE was", dice, "and You guessed", guess)
		print("You got", pointX, "point")
		print("\nOverall Point:", point)

		time.sleep(1.5)


def normalDifficultyEasy():
	point = 0
	pointX = 0
	os.system("cls")
	for x in range(roundNum):
		time.sleep(1.5)

		print("")
		for i in range(5):
			sys.stdout.write("\rROLLING THE DICEs{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.55)

		dice = rand.randrange(1, 6)
		dice2 = rand.randrange(1, 6)
		
		guess = input("\n\nGuess the 1st NUMBER: [1 - 6] > ")
		if guess == "r":
			main()
		elif guess == "e":
			exit()
		if guess == "1" or guess == "2" or guess == "3" or guess == "4" or guess == "5" or guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess2 = input("Guess the 2nd NUMBER: [1 - 6] > ")
		if guess2 == "r":
			main()
		elif guess2 == "e":
			exit()
		if guess2 == "1" or guess2 == "2" or guess2 == "3" or guess2 == "4" or guess2 == "5" or guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		result = dice - int(guess)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10
		elif result <= 2:
			point = 7 + point
			pointX = 7
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0

		result = dice2 - int(guess2)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		time.sleep(1.1)
		print("\nYour 1st DICE was", dice, "and You guessed", guess)
		print("Your 2nd DICE was", dice2, "and You guessed", guess2)
		print("You got", pointX, "point")
		print("\nOverall Point:", point)

		time.sleep(1.5)


def normalDifficultyNormal():
	point = 0
	pointX = 0
	os.system("cls")
	for x in range(roundNum):
		time.sleep(1.5)

		print("")
		for i in range(5):
			sys.stdout.write("\rROLLING THE DICEs{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.55)

		dice = rand.randrange(1, 6)
		dice2 = rand.randrange(1, 6)
		dice3 = rand.randrange(1, 6)
		
		guess = input("\n\nGuess the 1st NUMBER: [1 - 6] > ")
		if guess == "r":
			main()
		elif guess == "e":
			exit()
		if guess == "1" or guess == "2" or guess == "3" or guess == "4" or guess == "5" or guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess2 = input("Guess the 2nd NUMBER: [1 - 6] > ")
		if guess2 == "r":
			main()
		elif guess2 == "e":
			exit()
		if guess2 == "1" or guess2 == "2" or guess2 == "3" or guess2 == "4" or guess2 == "5" or guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess3 = input("Guess the 3rd NUMBER: [1 - 6] > ")
		if guess3 == "r":
			main()
		elif guess3 == "e":
			exit()
		if guess3 == "1" or guess3 == "2" or guess3 == "3" or guess3 == "4" or guess3 == "5" or guess3 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		result = dice - int(guess)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10
		elif result <= 2:
			point = 7 + point
			pointX = 7
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0

		result = dice2 - int(guess2)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice3 - int(guess3)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		time.sleep(1.1)
		print("\nYour 1st DICE was", dice, "and You guessed", guess)
		print("Your 2nd DICE was", dice2, "and You guessed", guess2)
		print("Your 3rd DICE was", dice3, "and You guessed", guess3)
		print("You got", pointX, "point")
		print("\nOverall Point:", point)

		time.sleep(1.5)


def normalDifficultyHard():
	point = 0
	pointX = 0
	os.system("cls")
	for x in range(roundNum):
		time.sleep(1.5)

		print("")
		for i in range(5):
			sys.stdout.write("\rROLLING THE DICEs{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.55)

		dice = rand.randrange(1, 6)
		dice2 = rand.randrange(1, 6)
		dice3 = rand.randrange(1, 6)
		dice4 = rand.randrange(1, 6)
		
		guess = input("\n\nGuess the 1st NUMBER: [1 - 6] > ")
		if guess == "r":
			main()
		elif guess == "e":
			exit()
		if guess == "1" or guess == "2" or guess == "3" or guess == "4" or guess == "5" or guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess2 = input("Guess the 2nd NUMBER: [1 - 6] > ")
		if guess2 == "r":
			main()
		elif guess2 == "e":
			exit()
		if guess2 == "1" or guess2 == "2" or guess2 == "3" or guess2 == "4" or guess2 == "5" or guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess3 = input("Guess the 3rd NUMBER: [1 - 6] > ")
		if guess3 == "r":
			main()
		elif guess3 == "e":
			exit()
		if guess3 == "1" or guess3 == "2" or guess3 == "3" or guess3 == "4" or guess3 == "5" or guess3 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess4 = input("Guess the 4th NUMBER: [1 - 6] > ")
		if guess4 == "r":
			main()
		elif guess4 == "e":
			exit()
		if guess4 == "1" or guess4 == "2" or guess4 == "3" or guess4 == "4" or guess4 == "5" or guess4 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		result = dice - int(guess)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10
		elif result <= 2:
			point = 7 + point
			pointX = 7
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0

		result = dice2 - int(guess2)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice3 - int(guess3)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice4 - int(guess4)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		time.sleep(1.1)
		print("\nYour 1st DICE was", dice, "and You guessed", guess)
		print("Your 2nd DICE was", dice2, "and You guessed", guess2)
		print("Your 3rd DICE was", dice3, "and You guessed", guess3)
		print("Your 4th DICE was", dice4, "and You guessed", guess4)
		print("You got", pointX, "point")
		print("\nOverall Point:", point)

		time.sleep(1.5)


def normalDifficultyEXTREME():
	point = 0
	pointX = 0
	os.system("cls")
	for x in range(roundNum):
		time.sleep(1.5)

		print("")
		for i in range(5):
			sys.stdout.write("\rROLLING THE DICEs{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.55)

		dice = rand.randrange(1, 6)
		dice2 = rand.randrange(1, 6)
		dice3 = rand.randrange(1, 6)
		dice4 = rand.randrange(1, 6)
		dice5 = rand.randrange(1, 6)
		dice6 = rand.randrange(1, 6)
		dice7 = rand.randrange(1, 6)
		dice8 = rand.randrange(1, 6)
		dice9 = rand.randrange(1, 6)
		dice10 = rand.randrange(1, 6)
		
		guess = input("\n\nGuess the 1st NUMBER: [1 - 6] > ")
		if guess == "r":
			main()
		elif guess == "e":
			exit()
		if guess == "1" or guess == "2" or guess == "3" or guess == "4" or guess == "5" or guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess2 = input("Guess the 2nd NUMBER: [1 - 6] > ")
		if guess2 == "r":
			main()
		elif guess2 == "e":
			exit()
		if guess2 == "1" or guess2 == "2" or guess2 == "3" or guess2 == "4" or guess2 == "5" or guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess3 = input("Guess the 3rd NUMBER: [1 - 6] > ")
		if guess3 == "r":
			main()
		elif guess3 == "e":
			exit()
		if guess3 == "1" or guess3 == "2" or guess3 == "3" or guess3 == "4" or guess3 == "5" or guess3 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess4 = input("Guess the 4th NUMBER: [1 - 6] > ")
		if guess4 == "r":
			main()
		elif guess4 == "e":
			exit()
		if guess4 == "1" or guess4 == "2" or guess4 == "3" or guess4 == "4" or guess4 == "5" or guess4 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess5 = input("Guess the 5th NUMBER: [1 - 6] > ")
		if guess5 == "r":
			main()
		elif guess5 == "e":
			exit()
		if guess5 == "1" or guess5 == "2" or guess5 == "3" or guess5 == "4" or guess5 == "5" or guess5 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess6 = input("Guess the 6th NUMBER: [1 - 6] > ")
		if guess6 == "r":
			main()
		elif guess6 == "e":
			exit()
		if guess6 == "1" or guess6 == "2" or guess6 == "3" or guess6 == "4" or guess6 == "5" or guess6 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess7 = input("Guess the 7th NUMBER: [1 - 6] > ")
		if guess7 == "r":
			main()
		elif guess7 == "e":
			exit()
		if guess7 == "1" or guess7 == "2" or guess7 == "3" or guess7 == "4" or guess7 == "5" or guess7 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess8 = input("Guess the 8th NUMBER: [1 - 6] > ")
		if guess8 == "r":
			main()
		elif guess8 == "e":
			exit()
		if guess8 == "1" or guess8 == "2" or guess8 == "3" or guess8 == "4" or guess8 == "5" or guess8 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess9 = input("Guess the 9th NUMBER: [1 - 6] > ")
		if guess9 == "r":
			main()
		elif guess9 == "e":
			exit()
		if guess9 == "1" or guess9 == "2" or guess9 == "3" or guess9 == "4" or guess9 == "5" or guess9 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess10 = input("Guess the 10th NUMBER: [1 - 6] > ")
		if guess10 == "r":
			main()
		elif guess10 == "e":
			exit()
		if guess10 == "1" or guess10 == "2" or guess10 == "3" or guess10 == "4" or guess10 == "5" or guess10 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		result = dice - int(guess)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10
		elif result <= 2:
			point = 7 + point
			pointX = 7
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0

		result = dice2 - int(guess2)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice3 - int(guess3)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice4 - int(guess4)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice5 - int(guess5)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice6 - int(guess6)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice7 - int(guess7)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice8 - int(guess8)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice9 - int(guess9)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice10 - int(guess10)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		time.sleep(1.1)
		print("\nYour 1st DICE was", dice, "and You guessed", guess)
		print("Your 2nd DICE was", dice2, "and You guessed", guess2)
		print("Your 3rd DICE was", dice3, "and You guessed", guess3)
		print("Your 4th DICE was", dice4, "and You guessed", guess4)
		print("Your 5th DICE was", dice5, "and You guessed", guess5)
		print("Your 6th DICE was", dice6, "and You guessed", guess6)
		print("Your 7th DICE was", dice7, "and You guessed", guess7)
		print("Your 8th DICE was", dice8, "and You guessed", guess8)
		print("Your 9th DICE was", dice9, "and You guessed", guess9)
		print("Your 10th DICE was", dice10, "and You guessed", guess10)
		print("You got", pointX, "point")
		print("\nOverall Point:", point)

		time.sleep(1.5)


def multiplayer():
	global multiplayerMode

	os.system("cls")
	print("DUEL MODES: \n1.vs Bot\n2.vs Friend\n3.Online")
	multiplayerMode = input("CHOOSE: [1/2/3] > ")

	if multiplayerMode == "r":
		main()
	elif multiplayerMode == "e":
		exit()

	if multiplayerMode == "1" or multiplayerMode == "2" or multiplayerMode == "3":
		pass
	else:
		input("Invalid DUEL MODE : Please choose with [1/2/3]")
		multiplayer()

	multiplayerMode = int(multiplayerMode)

	if multiplayerMode == 3:
		input("Currently Online Mode is not avaliable!!")
		multiplayer()


def userName():
	if multiplayerMode == 3:
		global uN
		uN = str(input("\nEnter your Username: > "))
	elif multiplayerMode == 2:
		global p1Un
		global p2Un
		p1Un = str(input("\n1st Player: Enter your Username > "))
		p2Un = str(input("2nd Player: Enter your Username > "))
		
		if p1Un == p2Un:
			input("\nPlayers Username can not be same!!")
			userName()


def finalResult():
	print("\nFinal Result: ")
	if multiplayerMode == 1:
		if point == botPoint:
			print("!! TIE !!")
		elif point > botPoint:
			print("!! WIN !!")
		elif point < botPoint:
			print("!! LOST !!")
	elif multiplayerMode == 2:
		pWin = "!! {} WIN !!"
		if p1Point == p2Point:
			print("!! TIE !!")
		elif p1Point > p2Point:
			print(pWin.format(p1Un))
		elif p1Point < p2Point:
			print(pWin.format(p2Un))


def duelBotDifficultySuperEasy():
	global point
	global botPoint
	point = 0
	pointX = 0
	botPoint = 0
	botPointX = 0
	os.system("cls")
	for x in range(roundNum):
		time.sleep(1.5)

		print("")
		for i in range(5):
			sys.stdout.write("\rROLLING THE DICE{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.55)

		dice = rand.randrange(1, 6)
		guess = input("\n\nGuess the NUMBER: [1 - 6] > ")

		if guess == "r":
			main()
		elif guess == "e":
			exit()

		if guess == "1" or guess == "2" or guess == "3" or guess == "4" or guess == "5" or guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		for i in range(5):
			sys.stdout.write("\rBot is Guessing{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.25)

		botGuess = rand.randrange(1, 6)

		result = dice - int(guess)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10
		elif result <= 2:
			point = 7 + point
			pointX = 7
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0

		botResult = dice - int(botGuess)
		botResult = abs(botResult)
		if botResult == 0:
			botPoint = 10 + botPoint
			botPointX = 10
		elif botResult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7
		if botResult <= 2:
			pass
		else:
			if botResult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4
		if botResult <= 4:
			pass
		else:
			if botResult == 5:
				botPoint = 0 + botPoint
				botPointX = 0

		time.sleep(1.1)
		print("\n\nDICE was", dice)
		print("You guessed", guess)
		print("You got", pointX, "point")
		print("Bot guessed", botGuess)
		print("Bot got", botPointX, "point")
		print("\nOverall Point:", point)
		print("Bot's Overall Point:", botPoint)

		print("\nResult: ")
		if pointX == botPointX:
			print("!! TIE !!")
		elif pointX > botPointX:
			print("!! WIN !!")
		elif pointX < botPointX:
			print("!! LOST !!")

		time.sleep(1.5)


def duelBotDifficultyEasy():
	global point
	global botPoint
	point = 0
	pointX = 0
	botPoint = 0
	botPointX = 0
	os.system("cls")
	for x in range(roundNum):
		time.sleep(1.5)

		print("")
		for i in range(5):
			sys.stdout.write("\rROLLING THE DICEs{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.55)

		dice = rand.randrange(1, 6)
		dice2 = rand.randrange(1, 6)

		guess = input("\n\nGuess the 1st NUMBER: [1 - 6] > ")
		if guess == "r":
			main()
		elif guess == "e":
			exit()

		if guess == "1" or guess == "2" or guess == "3" or guess == "4" or guess == "5" or guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess2 = input("Guess the 2nd NUMBER: [1 - 6] > ")
		if guess2 == "r":
			main()
		elif guess2 == "e":
			exit()

		if guess2 == "1" or guess2 == "2" or guess2 == "3" or guess2 == "4" or guess2 == "5" or guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		for i in range(5):
			sys.stdout.write("\rBot is Guessing{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.25)

		botGuess = rand.randrange(1, 6)
		botGuess2 = rand.randrange(1, 6)

		result = dice - int(guess)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10
		elif result <= 2:
			point = 7 + point
			pointX = 7
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0

		result = dice2 - int(guess2)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		botResult = dice - int(botGuess)
		botResult = abs(botResult)
		if botResult == 0:
			botPoint = 10 + botPoint
			botPointX = 10
		elif botResult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7
		if botResult <= 2:
			pass
		else:
			if botResult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4
		if botResult <= 4:
			pass
		else:
			if botResult == 5:
				botPoint = 0 + botPoint
				botPointX = 0

		botresult = dice2 - int(botGuess2)
		botresult = abs(botresult)
		if botresult == 0:
			botPoint = 10 + botPoint
			botPointX = 10 + botPointX
		elif botresult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7 + botPointX
		if botresult <= 2:
			pass
		else:
			if botresult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4 + botPointX
		if botresult <= 4:
			pass
		else:
			if botresult == 5:
				botPoint = 0 + botPoint
				botPointX = 0 + botPointX

		time.sleep(1.1)
		print("\n\n1st DICE was", dice)
		print("2nd DICE was", dice2)
		print("\n1st: You guessed", guess)
		print("2nd: You guessed", guess2)
		print("You got", pointX, "point")
		print("\n1st: Bot guessed", botGuess)
		print("2nd: Bot guessed", botGuess2)
		print("Bot got", botPointX, "point")
		print("\nOverall Point:", point)
		print("Bot's Overall Point:", botPoint)

		print("\nResult: ")
		if pointX == botPointX:
			print("!! TIE !!")
		elif pointX > botPointX:
			print("!! WIN !!")
		elif pointX < botPointX:
			print("!! LOST !!")

		time.sleep(1.5)


def duelBotDifficultyNormal():
	global point
	global botPoint
	point = 0
	pointX = 0
	botPoint = 0
	botPointX = 0
	os.system("cls")
	for x in range(roundNum):
		time.sleep(1.5)

		print("")
		for i in range(5):
			sys.stdout.write("\rROLLING THE DICEs{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.55)

		dice = rand.randrange(1, 6)
		dice2 = rand.randrange(1, 6)
		dice3 = rand.randrange(1, 6)

		guess = input("\n\nGuess the 1st NUMBER: [1 - 6] > ")
		if guess == "r":
			main()
		elif guess == "e":
			exit()

		if guess == "1" or guess == "2" or guess == "3" or guess == "4" or guess == "5" or guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess2 = input("Guess the 2nd NUMBER: [1 - 6] > ")
		if guess2 == "r":
			main()
		elif guess2 == "e":
			exit()

		if guess2 == "1" or guess2 == "2" or guess2 == "3" or guess2 == "4" or guess2 == "5" or guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess3 = input("Guess the 3rd NUMBER: [1 - 6] > ")
		if guess3 == "r":
			main()
		elif guess3 == "e":
			exit()

		if guess3 == "1" or guess3 == "2" or guess3 == "3" or guess3 == "4" or guess3 == "5" or guess3 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		for i in range(5):
			sys.stdout.write("\rBot is Guessing{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.25)

		botGuess = rand.randrange(1, 6)
		botGuess2 = rand.randrange(1, 6)
		botGuess3 = rand.randrange(1, 6)

		result = dice - int(guess)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10
		elif result <= 2:
			point = 7 + point
			pointX = 7
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0

		result = dice2 - int(guess2)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice3 - int(guess3)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		botResult = dice - int(botGuess)
		botResult = abs(botResult)
		if botResult == 0:
			botPoint = 10 + botPoint
			botPointX = 10
		elif botResult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7
		if botResult <= 2:
			pass
		else:
			if botResult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4
		if botResult <= 4:
			pass
		else:
			if botResult == 5:
				botPoint = 0 + botPoint
				botPointX = 0

		botresult = dice2 - int(botGuess2)
		botresult = abs(botresult)
		if botresult == 0:
			botPoint = 10 + botPoint
			botPointX = 10 + botPointX
		elif botresult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7 + botPointX
		if botresult <= 2:
			pass
		else:
			if botresult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4 + botPointX
		if botresult <= 4:
			pass
		else:
			if botresult == 5:
				botPoint = 0 + botPoint
				botPointX = 0 + botPointX

		botresult = dice3 - int(botGuess3)
		botresult = abs(botresult)
		if botresult == 0:
			botPoint = 10 + botPoint
			botPointX = 10 + botPointX
		elif botresult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7 + botPointX
		if botresult <= 2:
			pass
		else:
			if botresult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4 + botPointX
		if botresult <= 4:
			pass
		else:
			if botresult == 5:
				botPoint = 0 + botPoint
				botPointX = 0 + botPointX

		time.sleep(1.1)
		print("\n\n1st DICE was", dice)
		print("2nd DICE was", dice2)
		print("3rd DICE was", dice3)
		print("\n1st: You guessed", guess)
		print("2nd: You guessed", guess2)
		print("3rd: You guessed", guess3)
		print("You got", pointX, "point")
		print("\n1st: Bot guessed", botGuess)
		print("2nd: Bot guessed", botGuess2)
		print("3rd: Bot guessed", botGuess3)
		print("Bot got", botPointX, "point")
		print("\nOverall Point:", point)
		print("Bot's Overall Point:", botPoint)

		print("\nResult: ")
		if pointX == botPointX:
			print("!! TIE !!")
		elif pointX > botPointX:
			print("!! WIN !!")
		elif pointX < botPointX:
			print("!! LOST !!")

		time.sleep(1.5)


def duelBotDifficultyHard():
	global point
	global botPoint
	point = 0
	pointX = 0
	botPoint = 0
	botPointX = 0
	os.system("cls")
	for x in range(roundNum):
		time.sleep(1.5)

		print("")
		for i in range(5):
			sys.stdout.write("\rROLLING THE DICEs{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.55)

		dice = rand.randrange(1, 6)
		dice2 = rand.randrange(1, 6)
		dice3 = rand.randrange(1, 6)
		dice4 = rand.randrange(1, 6)

		guess = input("\n\nGuess the 1st NUMBER: [1 - 6] > ")
		if guess == "r":
			main()
		elif guess == "e":
			exit()

		if guess == "1" or guess == "2" or guess == "3" or guess == "4" or guess == "5" or guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess2 = input("Guess the 2nd NUMBER: [1 - 6] > ")
		if guess2 == "r":
			main()
		elif guess2 == "e":
			exit()

		if guess2 == "1" or guess2 == "2" or guess2 == "3" or guess2 == "4" or guess2 == "5" or guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess3 = input("Guess the 3rd NUMBER: [1 - 6] > ")
		if guess3 == "r":
			main()
		elif guess3 == "e":
			exit()

		if guess3 == "1" or guess3 == "2" or guess3 == "3" or guess3 == "4" or guess3 == "5" or guess3 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess4 = input("Guess the 4th NUMBER: [1 - 6] > ")
		if guess4 == "r":
			main()
		elif guess4 == "e":
			exit()

		if guess4 == "1" or guess4 == "2" or guess4 == "3" or guess4 == "4" or guess4 == "5" or guess4 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		for i in range(5):
			sys.stdout.write("\rBot is Guessing{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.25)

		botGuess = rand.randrange(1, 6)
		botGuess2 = rand.randrange(1, 6)
		botGuess3 = rand.randrange(1, 6)
		botGuess4 = rand.randrange(1, 6)

		result = dice - int(guess)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10
		elif result <= 2:
			point = 7 + point
			pointX = 7
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0

		result = dice2 - int(guess2)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice3 - int(guess3)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice4 - int(guess4)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		botResult = dice - int(botGuess)
		botResult = abs(botResult)
		if botResult == 0:
			botPoint = 10 + botPoint
			botPointX = 10
		elif botResult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7
		if botResult <= 2:
			pass
		else:
			if botResult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4
		if botResult <= 4:
			pass
		else:
			if botResult == 5:
				botPoint = 0 + botPoint
				botPointX = 0

		botresult = dice2 - int(botGuess2)
		botresult = abs(botresult)
		if botresult == 0:
			botPoint = 10 + botPoint
			botPointX = 10 + botPointX
		elif botresult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7 + botPointX
		if botresult <= 2:
			pass
		else:
			if botresult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4 + botPointX
		if botresult <= 4:
			pass
		else:
			if botresult == 5:
				botPoint = 0 + botPoint
				botPointX = 0 + botPointX

		botresult = dice3 - int(botGuess3)
		botresult = abs(botresult)
		if botresult == 0:
			botPoint = 10 + botPoint
			botPointX = 10 + botPointX
		elif botresult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7 + botPointX
		if botresult <= 2:
			pass
		else:
			if botresult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4 + botPointX
		if botresult <= 4:
			pass
		else:
			if botresult == 5:
				botPoint = 0 + botPoint
				botPointX = 0 + botPointX

		botresult = dice4 - int(botGuess4)
		botresult = abs(botresult)
		if botresult == 0:
			botPoint = 10 + botPoint
			botPointX = 10 + botPointX
		elif botresult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7 + botPointX
		if botresult <= 2:
			pass
		else:
			if botresult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4 + botPointX
		if botresult <= 4:
			pass
		else:
			if botresult == 5:
				botPoint = 0 + botPoint
				botPointX = 0 + botPointX

		time.sleep(1.1)
		print("\n\n1st DICE was", dice)
		print("2nd DICE was", dice2)
		print("3rd DICE was", dice3)
		print("4th DICE was", dice4)
		print("\n1st: You guessed", guess)
		print("2nd: You guessed", guess2)
		print("3rd: You guessed", guess3)
		print("4th: You guessed", guess4)
		print("You got", pointX, "point")
		print("\n1st: Bot guessed", botGuess)
		print("2nd: Bot guessed", botGuess2)
		print("3rd: Bot guessed", botGuess3)
		print("4th: Bot guessed", botGuess4)
		print("Bot got", botPointX, "point")
		print("\nOverall Point:", point)
		print("Bot's Overall Point:", botPoint)

		print("\nResult: ")
		if pointX == botPointX:
			print("!! TIE !!")
		elif pointX > botPointX:
			print("!! WIN !!")
		elif pointX < botPointX:
			print("!! LOST !!")

		time.sleep(1.5)


def duelBotDifficultyEXTREME():
	global point
	global botPoint
	point = 0
	pointX = 0
	botPoint = 0
	botPointX = 0
	os.system("cls")
	for x in range(roundNum):
		time.sleep(1.5)

		print("")
		for i in range(5):
			sys.stdout.write("\rROLLING THE DICEs{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.55)

		dice = rand.randrange(1, 6)
		dice2 = rand.randrange(1, 6)
		dice3 = rand.randrange(1, 6)
		dice4 = rand.randrange(1, 6)
		dice5 = rand.randrange(1, 6)
		dice6 = rand.randrange(1, 6)
		dice7 = rand.randrange(1, 6)
		dice8 = rand.randrange(1, 6)
		dice9 = rand.randrange(1, 6)
		dice10 = rand.randrange(1, 6)

		guess = input("\n\nGuess the 1st NUMBER: [1 - 6] > ")
		if guess == "r":
			main()
		elif guess == "e":
			exit()

		if guess == "1" or guess == "2" or guess == "3" or guess == "4" or guess == "5" or guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess2 = input("Guess the 2nd NUMBER: [1 - 6] > ")
		if guess2 == "r":
			main()
		elif guess2 == "e":
			exit()

		if guess2 == "1" or guess2 == "2" or guess2 == "3" or guess2 == "4" or guess2 == "5" or guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess3 = input("Guess the 3rd NUMBER: [1 - 6] > ")
		if guess3 == "r":
			main()
		elif guess3 == "e":
			exit()

		if guess3 == "1" or guess3 == "2" or guess3 == "3" or guess3 == "4" or guess3 == "5" or guess3 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess4 = input("Guess the 4th NUMBER: [1 - 6] > ")
		if guess4 == "r":
			main()
		elif guess4 == "e":
			exit()

		if guess4 == "1" or guess4 == "2" or guess4 == "3" or guess4 == "4" or guess4 == "5" or guess4 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess5 = input("Guess the 5th NUMBER: [1 - 6] > ")
		if guess5 == "r":
			main()
		elif guess5 == "e":
			exit()

		if guess5 == "1" or guess5 == "2" or guess5 == "3" or guess5 == "4" or guess5 == "5" or guess5 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess6 = input("Guess the 6th NUMBER: [1 - 6] > ")
		if guess6 == "r":
			main()
		elif guess6 == "e":
			exit()

		if guess6 == "1" or guess6 == "2" or guess6 == "3" or guess6 == "4" or guess6 == "5" or guess6 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess7 = input("Guess the 7th NUMBER: [1 - 6] > ")
		if guess7 == "r":
			main()
		elif guess7 == "e":
			exit()

		if guess7 == "1" or guess7 == "2" or guess7 == "3" or guess7 == "4" or guess7 == "5" or guess7 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess8 = input("Guess the 8th NUMBER: [1 - 6] > ")
		if guess8 == "r":
			main()
		elif guess8 == "e":
			exit()

		if guess8 == "1" or guess8 == "2" or guess8 == "3" or guess8 == "4" or guess8 == "5" or guess8 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess9 = input("Guess the 9th NUMBER: [1 - 6] > ")
		if guess9 == "r":
			main()
		elif guess9 == "e":
			exit()

		if guess9 == "1" or guess9 == "2" or guess9 == "3" or guess9 == "4" or guess9 == "5" or guess9 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		guess10 = input("Guess the 10th NUMBER: [1 - 6] > ")
		if guess10 == "r":
			main()
		elif guess10 == "e":
			exit()

		if guess10 == "1" or guess10 == "2" or guess10 == "3" or guess10 == "4" or guess10 == "5" or guess10 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		for i in range(5):
			sys.stdout.write("\rBot is Guessing{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.25)

		botGuess = rand.randrange(1, 6)
		botGuess2 = rand.randrange(1, 6)
		botGuess3 = rand.randrange(1, 6)
		botGuess4 = rand.randrange(1, 6)
		botGuess5 = rand.randrange(1, 6)
		botGuess6 = rand.randrange(1, 6)
		botGuess7 = rand.randrange(1, 6)
		botGuess8 = rand.randrange(1, 6)
		botGuess9 = rand.randrange(1, 6)
		botGuess10 = rand.randrange(1, 6)

		result = dice - int(guess)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10
		elif result <= 2:
			point = 7 + point
			pointX = 7
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0

		result = dice2 - int(guess2)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice3 - int(guess3)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice4 - int(guess4)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice5 - int(guess5)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice6 - int(guess6)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice7 - int(guess7)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice8 - int(guess8)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice9 - int(guess9)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		result = dice10 - int(guess10)
		result = abs(result)
		if result == 0:
			point = 10 + point
			pointX = 10 + pointX
		elif result <= 2:
			point = 7 + point
			pointX = 7 + pointX
		if result <= 2:
			pass
		else:
			if result <= 4:
				point =	4 + point
				pointX = 4 + pointX
		if result <= 4:
			pass
		else:
			if result == 5:
				point = 0 + point
				pointX = 0 + pointX

		botResult = dice - int(botGuess)
		botResult = abs(botResult)
		if botResult == 0:
			botPoint = 10 + botPoint
			botPointX = 10
		elif botResult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7
		if botResult <= 2:
			pass
		else:
			if botResult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4
		if botResult <= 4:
			pass
		else:
			if botResult == 5:
				botPoint = 0 + botPoint
				botPointX = 0

		botresult = dice2 - int(botGuess2)
		botresult = abs(botresult)
		if botresult == 0:
			botPoint = 10 + botPoint
			botPointX = 10 + botPointX
		elif botresult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7 + botPointX
		if botresult <= 2:
			pass
		else:
			if botresult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4 + botPointX
		if botresult <= 4:
			pass
		else:
			if botresult == 5:
				botPoint = 0 + botPoint
				botPointX = 0 + botPointX

		botresult = dice3 - int(botGuess3)
		botresult = abs(botresult)
		if botresult == 0:
			botPoint = 10 + botPoint
			botPointX = 10 + botPointX
		elif botresult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7 + botPointX
		if botresult <= 2:
			pass
		else:
			if botresult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4 + botPointX
		if botresult <= 4:
			pass
		else:
			if botresult == 5:
				botPoint = 0 + botPoint
				botPointX = 0 + botPointX

		botresult = dice4 - int(botGuess4)
		botresult = abs(botresult)
		if botresult == 0:
			botPoint = 10 + botPoint
			botPointX = 10 + botPointX
		elif botresult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7 + botPointX
		if botresult <= 2:
			pass
		else:
			if botresult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4 + botPointX
		if botresult <= 4:
			pass
		else:
			if botresult == 5:
				botPoint = 0 + botPoint
				botPointX = 0 + botPointX

		botresult = dice5 - int(botGuess5)
		botresult = abs(botresult)
		if botresult == 0:
			botPoint = 10 + botPoint
			botPointX = 10 + botPointX
		elif botresult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7 + botPointX
		if botresult <= 2:
			pass
		else:
			if botresult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4 + botPointX
		if botresult <= 4:
			pass
		else:
			if botresult == 5:
				botPoint = 0 + botPoint
				botPointX = 0 + botPointX

		botresult = dice6 - int(botGuess6)
		botresult = abs(botresult)
		if botresult == 0:
			botPoint = 10 + botPoint
			botPointX = 10 + botPointX
		elif botresult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7 + botPointX
		if botresult <= 2:
			pass
		else:
			if botresult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4 + botPointX
		if botresult <= 4:
			pass
		else:
			if botresult == 5:
				botPoint = 0 + botPoint
				botPointX = 0 + botPointX

		botresult = dice7 - int(botGuess7)
		botresult = abs(botresult)
		if botresult == 0:
			botPoint = 10 + botPoint
			botPointX = 10 + botPointX
		elif botresult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7 + botPointX
		if botresult <= 2:
			pass
		else:
			if botresult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4 + botPointX
		if botresult <= 4:
			pass
		else:
			if botresult == 5:
				botPoint = 0 + botPoint
				botPointX = 0 + botPointX

		botresult = dice8 - int(botGuess8)
		botresult = abs(botresult)
		if botresult == 0:
			botPoint = 10 + botPoint
			botPointX = 10 + botPointX
		elif botresult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7 + botPointX
		if botresult <= 2:
			pass
		else:
			if botresult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4 + botPointX
		if botresult <= 4:
			pass
		else:
			if botresult == 5:
				botPoint = 0 + botPoint
				botPointX = 0 + botPointX

		botresult = dice9 - int(botGuess9)
		botresult = abs(botresult)
		if botresult == 0:
			botPoint = 10 + botPoint
			botPointX = 10 + botPointX
		elif botresult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7 + botPointX
		if botresult <= 2:
			pass
		else:
			if botresult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4 + botPointX
		if botresult <= 4:
			pass
		else:
			if botresult == 5:
				botPoint = 0 + botPoint
				botPointX = 0 + botPointX

		botresult = dice10 - int(botGuess10)
		botresult = abs(botresult)
		if botresult == 0:
			botPoint = 10 + botPoint
			botPointX = 10 + botPointX
		elif botresult <= 2:
			botPoint = 7 + botPoint
			botPointX = 7 + botPointX
		if botresult <= 2:
			pass
		else:
			if botresult <= 4:
				botPoint =	4 + botPoint
				botPointX = 4 + botPointX
		if botresult <= 4:
			pass
		else:
			if botresult == 5:
				botPoint = 0 + botPoint
				botPointX = 0 + botPointX

		time.sleep(1.1)
		print("\n\n1st DICE was", dice)
		print("2nd DICE was", dice2)
		print("3rd DICE was", dice3)
		print("4th DICE was", dice4)
		print("5th DICE was", dice5)
		print("6th DICE was", dice6)
		print("7th DICE was", dice7)
		print("8th DICE was", dice8)
		print("9th DICE was", dice9)
		print("10th DICE was", dice10)
		print("\n1st: You guessed", guess)
		print("2nd: You guessed", guess2)
		print("3rd: You guessed", guess3)
		print("4th: You guessed", guess4)
		print("5th: You guessed", guess5)
		print("6th: You guessed", guess6)
		print("7th: You guessed", guess7)
		print("8th: You guessed", guess8)
		print("9th: You guessed", guess9)
		print("10th: You guessed", guess10)
		print("You got", pointX, "point")
		print("\n1st: Bot guessed", botGuess)
		print("2nd: Bot guessed", botGuess2)
		print("3rd: Bot guessed", botGuess3)
		print("4th: Bot guessed", botGuess4)
		print("5th: Bot guessed", botGuess5)
		print("6th: Bot guessed", botGuess6)
		print("7th: Bot guessed", botGuess7)
		print("8th: Bot guessed", botGuess8)
		print("9th: Bot guessed", botGuess9)
		print("10th: Bot guessed", botGuess10)
		print("Bot got", botPointX, "point")
		print("\nOverall Point:", point)
		print("Bot's Overall Point:", botPoint)

		print("\nResult: ")
		if pointX == botPointX:
			print("!! TIE !!")
		elif pointX > botPointX:
			print("!! WIN !!")
		elif pointX < botPointX:
			print("!! LOST !!")

		time.sleep(1.5)


def duelFriendDifficultySuperEasy():
	global p1Point
	global p2Point
	p1Point = 0
	p1PointX = 0
	p2Point = 0
	p2PointX = 0
	os.system("cls")
	for x in range(roundNum):
		time.sleep(1.5)

		print("")
		for i in range(5):
			sys.stdout.write("\rROLLING THE DICE{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.55)

		dice = rand.randrange(1, 6)
		pGuessTxt = "{}: Guess the NUMBER: [1 - 6] > "

		p1Guess = input("\n\n" + pGuessTxt.format(p1Un))
		if p1Guess == "r":
			main()
		elif p1Guess == "e":
			exit()

		if p1Guess == "1" or p1Guess == "2" or p1Guess == "3" or p1Guess == "4" or p1Guess == "5" or p1Guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess = input("\n" + pGuessTxt.format(p2Un))
		if p2Guess == "r":
			main()
		elif p2Guess == "e":
			exit()

		if p2Guess == "1" or p2Guess == "2" or p2Guess == "3" or p2Guess == "4" or p2Guess == "5" or p2Guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		time.sleep(1.25)

		p1Result = dice - int(p1Guess)
		p1Result = abs(p1Result)
		if p1Result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10
		elif p1Result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7
		if p1Result <= 2:
			pass
		else:
			if p1Result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4
		if p1Result <= 4:
			pass
		else:
			if p1Result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0

		p2Result = dice - int(p2Guess)
		p2Result = abs(p2Result)
		if p2Result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10
		elif p2Result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7
		if p2Result <= 2:
			pass
		else:
			if p2Result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4
		if p2Result <= 4:
			pass
		else:
			if p2Result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0

		time.sleep(1.1)
		print("\n\nDICE was", dice)
		guessedTxt = "{} guessed"
		gotTxt = "{} got"
		opTxt = "{} Overall Point:"
		print("\n" + guessedTxt.format(p1Un), p1Guess)
		print(gotTxt.format(p1Un), p1PointX, "point")
		print(opTxt.format(p1Un), p1Point)
		print("\n" + guessedTxt.format(p2Un), p2Guess)
		print(gotTxt.format(p2Un), p2PointX, "point")
		print(opTxt.format(p2Un), p2Point)

		print("\nResult: ")
		pWin = "!! {} WIN !!"
		if p1PointX == p2PointX:
			print("!! TIE !!")
		elif p1PointX > p2PointX:
			print(pWin.format(p1Un))
		elif p1PointX < p2PointX:
			print(pWin.format(p2Un))

		time.sleep(1.5)


def duelFriendDifficultyEasy():
	global p1Point
	global p2Point
	p1Point = 0
	p1PointX = 0
	p2Point = 0
	p2PointX = 0
	os.system("cls")
	for x in range(roundNum):
		time.sleep(1.5)

		print("")
		for i in range(5):
			sys.stdout.write("\rROLLING THE DICEs{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.55)

		dice = rand.randrange(1, 6)
		dice2 = rand.randrange(1, 6)
		pGuessTxt = "{}"

		p1Guess = input("\n\n" + pGuessTxt.format(p1Un) + ": Guess the 1st NUMBER: [1 - 6] > ")
		if p1Guess == "r":
			main()
		elif p1Guess == "e":
			exit()

		if p1Guess == "1" or p1Guess == "2" or p1Guess == "3" or p1Guess == "4" or p1Guess == "5" or p1Guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p1Guess2 = input(pGuessTxt.format(p1Un) + ": Guess the 2nd NUMBER: [1 - 6] > ")
		if p1Guess2 == "r":
			main()
		elif p1Guess2 == "e":
			exit()

		if p1Guess2 == "1" or p1Guess2 == "2" or p1Guess2 == "3" or p1Guess2 == "4" or p1Guess2 == "5" or p1Guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess = input("\n" + pGuessTxt.format(p2Un) + ": Guess the 1st NUMBER: [1 - 6] > ")
		if p2Guess == "r":
			main()
		elif p2Guess == "e":
			exit()

		if p2Guess == "1" or p2Guess == "2" or p2Guess == "3" or p2Guess == "4" or p2Guess == "5" or p2Guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess2 = input(pGuessTxt.format(p2Un) + ": Guess the 2nd NUMBER: [1 - 6] > ")
		if p2Guess2 == "r":
			main()
		elif p2Guess2 == "e":
			exit()

		if p2Guess2 == "1" or p2Guess2 == "2" or p2Guess2 == "3" or p2Guess2 == "4" or p2Guess2 == "5" or p2Guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		time.sleep(1.25)

		p1Result = dice - int(p1Guess)
		p1Result = abs(p1Result)
		if p1Result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10
		elif p1Result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7
		if p1Result <= 2:
			pass
		else:
			if p1Result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4
		if p1Result <= 4:
			pass
		else:
			if p1Result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0

		p1result = dice2 - int(p1Guess2)
		p1result = abs(p1result)
		if p1result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10 + p1PointX
		elif p1result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7 + p1PointX
		if p1result <= 2:
			pass
		else:
			if p1result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4 + p1PointX
		if p1result <= 4:
			pass
		else:
			if p1result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0 + p1PointX

		p2Result = dice - int(p2Guess)
		p2Result = abs(p2Result)
		if p2Result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10
		elif p2Result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7
		if p2Result <= 2:
			pass
		else:
			if p2Result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4
		if p2Result <= 4:
			pass
		else:
			if p2Result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0

		p2result = dice2 - int(p2Guess2)
		p2result = abs(p2result)
		if p2result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10 + p2PointX
		elif p2result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7 + p2PointX
		if p2result <= 2:
			pass
		else:
			if p2result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4 + p2PointX
		if p2result <= 4:
			pass
		else:
			if p2result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0 + p2PointX


		time.sleep(1.1)
		print("\n\n1st DICE was", dice)
		print("2nd DICE was", dice2)
		guessedTxt = "{} guessed"
		gotTxt = "{} got"
		opTxt = "{} Overall Point:"
		print("\n1st:", guessedTxt.format(p1Un), p1Guess)
		print("2nd:", guessedTxt.format(p1Un), p1Guess2)
		print(gotTxt.format(p1Un), p1PointX, "point")
		print(opTxt.format(p1Un), p1Point)
		print("\n1st:", guessedTxt.format(p2Un), p2Guess)
		print("2nd:", guessedTxt.format(p2Un), p2Guess2)
		print(gotTxt.format(p2Un), p2PointX, "point")
		print(opTxt.format(p2Un), p2Point)

		print("\nResult: ")
		pWin = "!! {} WIN !!"
		if p1PointX == p2PointX:
			print("!! TIE !!")
		elif p1PointX > p2PointX:
			print(pWin.format(p1Un))
		elif p1PointX < p2PointX:
			print(pWin.format(p2Un))

		time.sleep(1.5)


def duelFriendDifficultyNormal():
	global p1Point
	global p2Point
	p1Point = 0
	p1PointX = 0
	p2Point = 0
	p2PointX = 0
	os.system("cls")
	for x in range(roundNum):
		time.sleep(1.5)

		print("")
		for i in range(5):
			sys.stdout.write("\rROLLING THE DICEs{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.55)

		dice = rand.randrange(1, 6)
		dice2 = rand.randrange(1, 6)
		dice3 = rand.randrange(1, 6)
		pGuessTxt = "{}"

		p1Guess = input("\n\n" + pGuessTxt.format(p1Un) + ": Guess the 1st NUMBER: [1 - 6] > ")
		if p1Guess == "r":
			main()
		elif p1Guess == "e":
			exit()

		if p1Guess == "1" or p1Guess == "2" or p1Guess == "3" or p1Guess == "4" or p1Guess == "5" or p1Guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p1Guess2 = input(pGuessTxt.format(p1Un) + ": Guess the 2nd NUMBER: [1 - 6] > ")
		if p1Guess2 == "r":
			main()
		elif p1Guess2 == "e":
			exit()

		if p1Guess2 == "1" or p1Guess2 == "2" or p1Guess2 == "3" or p1Guess2 == "4" or p1Guess2 == "5" or p1Guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p1Guess3 = input(pGuessTxt.format(p1Un) + ": Guess the 3rd NUMBER: [1 - 6] > ")
		if p1Guess3 == "r":
			main()
		elif p1Guess3 == "e":
			exit()

		if p1Guess3 == "1" or p1Guess3 == "2" or p1Guess3 == "3" or p1Guess3 == "4" or p1Guess3 == "5" or p1Guess3 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess = input("\n" + pGuessTxt.format(p2Un) + ": Guess the 1st NUMBER: [1 - 6] > ")
		if p2Guess == "r":
			main()
		elif p2Guess == "e":
			exit()

		if p2Guess == "1" or p2Guess == "2" or p2Guess == "3" or p2Guess == "4" or p2Guess == "5" or p2Guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess2 = input(pGuessTxt.format(p2Un) + ": Guess the 2nd NUMBER: [1 - 6] > ")
		if p2Guess2 == "r":
			main()
		elif p2Guess2 == "e":
			exit()

		if p2Guess2 == "1" or p2Guess2 == "2" or p2Guess2 == "3" or p2Guess2 == "4" or p2Guess2 == "5" or p2Guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess3 = input(pGuessTxt.format(p2Un) + ": Guess the 3rd NUMBER: [1 - 6] > ")
		if p2Guess3 == "r":
			main()
		elif p2Guess3 == "e":
			exit()

		if p2Guess3 == "1" or p2Guess3 == "2" or p2Guess3 == "3" or p2Guess3 == "4" or p2Guess3 == "5" or p2Guess3 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		time.sleep(1.25)

		p1Result = dice - int(p1Guess)
		p1Result = abs(p1Result)
		if p1Result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10
		elif p1Result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7
		if p1Result <= 2:
			pass
		else:
			if p1Result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4
		if p1Result <= 4:
			pass
		else:
			if p1Result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0

		p1result = dice2 - int(p1Guess2)
		p1result = abs(p1result)
		if p1result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10 + p1PointX
		elif p1result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7 + p1PointX
		if p1result <= 2:
			pass
		else:
			if p1result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4 + p1PointX
		if p1result <= 4:
			pass
		else:
			if p1result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0 + p1PointX

		p1result = dice3 - int(p1Guess3)
		p1result = abs(p1result)
		if p1result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10 + p1PointX
		elif p1result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7 + p1PointX
		if p1result <= 2:
			pass
		else:
			if p1result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4 + p1PointX
		if p1result <= 4:
			pass
		else:
			if p1result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0 + p1PointX

		p2Result = dice - int(p2Guess)
		p2Result = abs(p2Result)
		if p2Result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10
		elif p2Result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7
		if p2Result <= 2:
			pass
		else:
			if p2Result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4
		if p2Result <= 4:
			pass
		else:
			if p2Result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0

		p2result = dice2 - int(p2Guess2)
		p2result = abs(p2result)
		if p2result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10 + p2PointX
		elif p2result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7 + p2PointX
		if p2result <= 2:
			pass
		else:
			if p2result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4 + p2PointX
		if p2result <= 4:
			pass
		else:
			if p2result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0 + p2PointX

		p2result = dice3 - int(p2Guess3)
		p2result = abs(p2result)
		if p2result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10 + p2PointX
		elif p2result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7 + p2PointX
		if p2result <= 2:
			pass
		else:
			if p2result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4 + p2PointX
		if p2result <= 4:
			pass
		else:
			if p2result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0 + p2PointX


		time.sleep(1.1)
		print("\n\n1st DICE was", dice)
		print("2nd DICE was", dice2)
		print("3rd DICE was", dice3)
		guessedTxt = "{} guessed"
		gotTxt = "{} got"
		opTxt = "{} Overall Point:"
		print("\n1st:", guessedTxt.format(p1Un), p1Guess)
		print("2nd:", guessedTxt.format(p1Un), p1Guess2)
		print("3rd:", guessedTxt.format(p1Un), p1Guess3)
		print(gotTxt.format(p1Un), p1PointX, "point")
		print(opTxt.format(p1Un), p1Point)
		print("\n1st:", guessedTxt.format(p2Un), p2Guess)
		print("2nd:", guessedTxt.format(p2Un), p2Guess2)
		print("3rd:", guessedTxt.format(p2Un), p2Guess3)
		print(gotTxt.format(p2Un), p2PointX, "point")
		print(opTxt.format(p2Un), p2Point)

		print("\nResult: ")
		pWin = "!! {} WIN !!"
		if p1PointX == p2PointX:
			print("!! TIE !!")
		elif p1PointX > p2PointX:
			print(pWin.format(p1Un))
		elif p1PointX < p2PointX:
			print(pWin.format(p2Un))

		time.sleep(1.5)


def duelFriendDifficultyHard():
	global p1Point
	global p2Point
	p1Point = 0
	p1PointX = 0
	p2Point = 0
	p2PointX = 0
	os.system("cls")
	for x in range(roundNum):
		time.sleep(1.5)

		print("")
		for i in range(5):
			sys.stdout.write("\rROLLING THE DICEs{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.55)

		dice = rand.randrange(1, 6)
		dice2 = rand.randrange(1, 6)
		dice3 = rand.randrange(1, 6)
		dice4 = rand.randrange(1, 6)
		pGuessTxt = "{}"

		p1Guess = input("\n\n" + pGuessTxt.format(p1Un) + ": Guess the 1st NUMBER: [1 - 6] > ")
		if p1Guess == "r":
			main()
		elif p1Guess == "e":
			exit()

		if p1Guess == "1" or p1Guess == "2" or p1Guess == "3" or p1Guess == "4" or p1Guess == "5" or p1Guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p1Guess2 = input(pGuessTxt.format(p1Un) + ": Guess the 2nd NUMBER: [1 - 6] > ")
		if p1Guess2 == "r":
			main()
		elif p1Guess2 == "e":
			exit()

		if p1Guess2 == "1" or p1Guess2 == "2" or p1Guess2 == "3" or p1Guess2 == "4" or p1Guess2 == "5" or p1Guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p1Guess3 = input(pGuessTxt.format(p1Un) + ": Guess the 3rd NUMBER: [1 - 6] > ")
		if p1Guess3 == "r":
			main()
		elif p1Guess3 == "e":
			exit()

		if p1Guess3 == "1" or p1Guess3 == "2" or p1Guess3 == "3" or p1Guess3 == "4" or p1Guess3 == "5" or p1Guess3 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p1Guess4 = input(pGuessTxt.format(p1Un) + ": Guess the 4th NUMBER: [1 - 6] > ")
		if p1Guess4 == "r":
			main()
		elif p1Guess4 == "e":
			exit()

		if p1Guess4 == "1" or p1Guess4 == "2" or p1Guess4 == "3" or p1Guess4 == "4" or p1Guess4 == "5" or p1Guess4 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess = input("\n" + pGuessTxt.format(p2Un) + ": Guess the 1st NUMBER: [1 - 6] > ")
		if p2Guess == "r":
			main()
		elif p2Guess == "e":
			exit()

		if p2Guess == "1" or p2Guess == "2" or p2Guess == "3" or p2Guess == "4" or p2Guess == "5" or p2Guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess2 = input(pGuessTxt.format(p2Un) + ": Guess the 2nd NUMBER: [1 - 6] > ")
		if p2Guess2 == "r":
			main()
		elif p2Guess2 == "e":
			exit()

		if p2Guess2 == "1" or p2Guess2 == "2" or p2Guess2 == "3" or p2Guess2 == "4" or p2Guess2 == "5" or p2Guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess3 = input(pGuessTxt.format(p2Un) + ": Guess the 3rd NUMBER: [1 - 6] > ")
		if p2Guess3 == "r":
			main()
		elif p2Guess3 == "e":
			exit()

		if p2Guess3 == "1" or p2Guess3 == "2" or p2Guess3 == "3" or p2Guess3 == "4" or p2Guess3 == "5" or p2Guess3 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess4 = input(pGuessTxt.format(p2Un) + ": Guess the 4th NUMBER: [1 - 6] > ")
		if p2Guess4 == "r":
			main()
		elif p2Guess4 == "e":
			exit()

		if p2Guess4 == "1" or p2Guess4 == "2" or p2Guess4 == "3" or p2Guess4 == "4" or p2Guess4 == "5" or p2Guess4 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		time.sleep(1.25)

		p1Result = dice - int(p1Guess)
		p1Result = abs(p1Result)
		if p1Result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10
		elif p1Result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7
		if p1Result <= 2:
			pass
		else:
			if p1Result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4
		if p1Result <= 4:
			pass
		else:
			if p1Result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0

		p1result = dice2 - int(p1Guess2)
		p1result = abs(p1result)
		if p1result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10 + p1PointX
		elif p1result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7 + p1PointX
		if p1result <= 2:
			pass
		else:
			if p1result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4 + p1PointX
		if p1result <= 4:
			pass
		else:
			if p1result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0 + p1PointX

		p1result = dice3 - int(p1Guess3)
		p1result = abs(p1result)
		if p1result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10 + p1PointX
		elif p1result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7 + p1PointX
		if p1result <= 2:
			pass
		else:
			if p1result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4 + p1PointX
		if p1result <= 4:
			pass
		else:
			if p1result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0 + p1PointX

		p1result = dice4 - int(p1Guess4)
		p1result = abs(p1result)
		if p1result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10 + p1PointX
		elif p1result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7 + p1PointX
		if p1result <= 2:
			pass
		else:
			if p1result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4 + p1PointX
		if p1result <= 4:
			pass
		else:
			if p1result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0 + p1PointX

		p2Result = dice - int(p2Guess)
		p2Result = abs(p2Result)
		if p2Result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10
		elif p2Result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7
		if p2Result <= 2:
			pass
		else:
			if p2Result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4
		if p2Result <= 4:
			pass
		else:
			if p2Result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0

		p2result = dice2 - int(p2Guess2)
		p2result = abs(p2result)
		if p2result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10 + p2PointX
		elif p2result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7 + p2PointX
		if p2result <= 2:
			pass
		else:
			if p2result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4 + p2PointX
		if p2result <= 4:
			pass
		else:
			if p2result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0 + p2PointX

		p2result = dice3 - int(p2Guess3)
		p2result = abs(p2result)
		if p2result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10 + p2PointX
		elif p2result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7 + p2PointX
		if p2result <= 2:
			pass
		else:
			if p2result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4 + p2PointX
		if p2result <= 4:
			pass
		else:
			if p2result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0 + p2PointX

		p2result = dice4 - int(p2Guess4)
		p2result = abs(p2result)
		if p2result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10 + p2PointX
		elif p2result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7 + p2PointX
		if p2result <= 2:
			pass
		else:
			if p2result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4 + p2PointX
		if p2result <= 4:
			pass
		else:
			if p2result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0 + p2PointX


		time.sleep(1.1)
		print("\n\n1st DICE was", dice)
		print("2nd DICE was", dice2)
		print("3rd DICE was", dice3)
		print("4th DICE was", dice4)
		guessedTxt = "{} guessed"
		gotTxt = "{} got"
		opTxt = "{} Overall Point:"
		print("\n1st:", guessedTxt.format(p1Un), p1Guess)
		print("2nd:", guessedTxt.format(p1Un), p1Guess2)
		print("3rd:", guessedTxt.format(p1Un), p1Guess3)
		print("4th:", guessedTxt.format(p1Un), p1Guess4)
		print(gotTxt.format(p1Un), p1PointX, "point")
		print(opTxt.format(p1Un), p1Point)
		print("\n1st:", guessedTxt.format(p2Un), p2Guess)
		print("2nd:", guessedTxt.format(p2Un), p2Guess2)
		print("3rd:", guessedTxt.format(p2Un), p2Guess3)
		print("4th:", guessedTxt.format(p2Un), p2Guess4)
		print(gotTxt.format(p2Un), p2PointX, "point")
		print(opTxt.format(p2Un), p2Point)

		print("\nResult: ")
		pWin = "!! {} WIN !!"
		if p1PointX == p2PointX:
			print("!! TIE !!")
		elif p1PointX > p2PointX:
			print(pWin.format(p1Un))
		elif p1PointX < p2PointX:
			print(pWin.format(p2Un))

		time.sleep(1.5)


def duelFriendDifficultyEXTREME():
	global p1Point
	global p2Point
	p1Point = 0
	p1PointX = 0
	p2Point = 0
	p2PointX = 0
	os.system("cls")
	for x in range(roundNum):
		time.sleep(1.5)

		print("")
		for i in range(5):
			sys.stdout.write("\rROLLING THE DICEs{0}".format("."*i))
			sys.stdout.flush()
			time.sleep(0.55)

		dice = rand.randrange(1, 6)
		dice2 = rand.randrange(1, 6)
		dice3 = rand.randrange(1, 6)
		dice4 = rand.randrange(1, 6)
		dice5 = rand.randrange(1, 6)
		dice6 = rand.randrange(1, 6)
		dice7 = rand.randrange(1, 6)
		dice8 = rand.randrange(1, 6)
		dice9 = rand.randrange(1, 6)
		dice10 = rand.randrange(1, 6)
		pGuessTxt = "{}"

		p1Guess = input("\n\n" + pGuessTxt.format(p1Un) + ": Guess the 1st NUMBER: [1 - 6] > ")
		if p1Guess == "r":
			main()
		elif p1Guess == "e":
			exit()

		if p1Guess == "1" or p1Guess == "2" or p1Guess == "3" or p1Guess == "4" or p1Guess == "5" or p1Guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p1Guess2 = input(pGuessTxt.format(p1Un) + ": Guess the 2nd NUMBER: [1 - 6] > ")
		if p1Guess2 == "r":
			main()
		elif p1Guess2 == "e":
			exit()

		if p1Guess2 == "1" or p1Guess2 == "2" or p1Guess2 == "3" or p1Guess2 == "4" or p1Guess2 == "5" or p1Guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p1Guess3 = input(pGuessTxt.format(p1Un) + ": Guess the 3rd NUMBER: [1 - 6] > ")
		if p1Guess3 == "r":
			main()
		elif p1Guess3 == "e":
			exit()

		if p1Guess3 == "1" or p1Guess3 == "2" or p1Guess3 == "3" or p1Guess3 == "4" or p1Guess3 == "5" or p1Guess3 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p1Guess4 = input(pGuessTxt.format(p1Un) + ": Guess the 4th NUMBER: [1 - 6] > ")
		if p1Guess4 == "r":
			main()
		elif p1Guess4 == "e":
			exit()

		if p1Guess4 == "1" or p1Guess4 == "2" or p1Guess4 == "3" or p1Guess4 == "4" or p1Guess4 == "5" or p1Guess4 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p1Guess5 = input(pGuessTxt.format(p1Un) + ": Guess the 5th NUMBER: [1 - 6] > ")
		if p1Guess5 == "r":
			main()
		elif p1Guess5 == "e":
			exit()

		if p1Guess5 == "1" or p1Guess5 == "2" or p1Guess5 == "3" or p1Guess5 == "4" or p1Guess5 == "5" or p1Guess5 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p1Guess6 = input(pGuessTxt.format(p1Un) + ": Guess the 6th NUMBER: [1 - 6] > ")
		if p1Guess6 == "r":
			main()
		elif p1Guess6 == "e":
			exit()

		if p1Guess6 == "1" or p1Guess6 == "2" or p1Guess6 == "3" or p1Guess6 == "4" or p1Guess6 == "5" or p1Guess6 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p1Guess7 = input(pGuessTxt.format(p1Un) + ": Guess the 7th NUMBER: [1 - 6] > ")
		if p1Guess7 == "r":
			main()
		elif p1Guess7 == "e":
			exit()

		if p1Guess7 == "1" or p1Guess7 == "2" or p1Guess7 == "3" or p1Guess7 == "4" or p1Guess7 == "5" or p1Guess7 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p1Guess8 = input(pGuessTxt.format(p1Un) + ": Guess the 8th NUMBER: [1 - 6] > ")
		if p1Guess8 == "r":
			main()
		elif p1Guess8 == "e":
			exit()

		if p1Guess8 == "1" or p1Guess8 == "2" or p1Guess8 == "3" or p1Guess8 == "4" or p1Guess8 == "5" or p1Guess8 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p1Guess9 = input(pGuessTxt.format(p1Un) + ": Guess the 9th NUMBER: [1 - 6] > ")
		if p1Guess9 == "r":
			main()
		elif p1Guess9 == "e":
			exit()

		if p1Guess9 == "1" or p1Guess9 == "2" or p1Guess9 == "3" or p1Guess9 == "4" or p1Guess9 == "5" or p1Guess9 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p1Guess10 = input(pGuessTxt.format(p1Un) + ": Guess the 10th NUMBER: [1 - 6] > ")
		if p1Guess10 == "r":
			main()
		elif p1Guess10 == "e":
			exit()

		if p1Guess10 == "1" or p1Guess10 == "2" or p1Guess10 == "3" or p1Guess10 == "4" or p1Guess10 == "5" or p1Guess10 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess = input("\n" + pGuessTxt.format(p2Un) + ": Guess the 1st NUMBER: [1 - 6] > ")
		if p2Guess == "r":
			main()
		elif p2Guess == "e":
			exit()

		if p2Guess == "1" or p2Guess == "2" or p2Guess == "3" or p2Guess == "4" or p2Guess == "5" or p2Guess == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess2 = input(pGuessTxt.format(p2Un) + ": Guess the 2nd NUMBER: [1 - 6] > ")
		if p2Guess2 == "r":
			main()
		elif p2Guess2 == "e":
			exit()

		if p2Guess2 == "1" or p2Guess2 == "2" or p2Guess2 == "3" or p2Guess2 == "4" or p2Guess2 == "5" or p2Guess2 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess3 = input(pGuessTxt.format(p2Un) + ": Guess the 3rd NUMBER: [1 - 6] > ")
		if p2Guess3 == "r":
			main()
		elif p2Guess3 == "e":
			exit()

		if p2Guess3 == "1" or p2Guess3 == "2" or p2Guess3 == "3" or p2Guess3 == "4" or p2Guess3 == "5" or p2Guess3 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess4 = input(pGuessTxt.format(p2Un) + ": Guess the 4th NUMBER: [1 - 6] > ")
		if p2Guess4 == "r":
			main()
		elif p2Guess4 == "e":
			exit()

		if p2Guess4 == "1" or p2Guess4 == "2" or p2Guess4 == "3" or p2Guess4 == "4" or p2Guess4 == "5" or p2Guess4 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess5 = input(pGuessTxt.format(p2Un) + ": Guess the 5th NUMBER: [1 - 6] > ")
		if p2Guess5 == "r":
			main()
		elif p2Guess5 == "e":
			exit()

		if p2Guess5 == "1" or p2Guess5 == "2" or p2Guess5 == "3" or p2Guess5 == "4" or p2Guess5 == "5" or p2Guess5 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess6 = input(pGuessTxt.format(p2Un) + ": Guess the 6th NUMBER: [1 - 6] > ")
		if p2Guess6 == "r":
			main()
		elif p2Guess6 == "e":
			exit()

		if p2Guess6 == "1" or p2Guess6 == "2" or p2Guess6 == "3" or p2Guess6 == "4" or p2Guess6 == "5" or p2Guess6 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess7 = input(pGuessTxt.format(p2Un) + ": Guess the 7th NUMBER: [1 - 6] > ")
		if p2Guess7 == "r":
			main()
		elif p2Guess7 == "e":
			exit()

		if p2Guess7 == "1" or p2Guess7 == "2" or p2Guess7 == "3" or p2Guess7 == "4" or p2Guess7 == "5" or p2Guess7 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess8 = input(pGuessTxt.format(p2Un) + ": Guess the 8th NUMBER: [1 - 6] > ")
		if p2Guess8 == "r":
			main()
		elif p2Guess8 == "e":
			exit()

		if p2Guess8 == "1" or p2Guess8 == "2" or p2Guess8 == "3" or p2Guess8 == "4" or p2Guess8 == "5" or p2Guess8 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess9 = input(pGuessTxt.format(p2Un) + ": Guess the 9th NUMBER: [1 - 6] > ")
		if p2Guess9 == "r":
			main()
		elif p2Guess9 == "e":
			exit()

		if p2Guess9 == "1" or p2Guess9 == "2" or p2Guess9 == "3" or p2Guess9 == "4" or p2Guess9 == "5" or p2Guess9 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		p2Guess10 = input(pGuessTxt.format(p2Un) + ": Guess the 10th NUMBER: [1 - 6] > ")
		if p2Guess10 == "r":
			main()
		elif p2Guess10 == "e":
			exit()

		if p2Guess10 == "1" or p2Guess10 == "2" or p2Guess10 == "3" or p2Guess10 == "4" or p2Guess10 == "5" or p2Guess10 == "6":
			pass
		else:
			input("\nInvalid input NUMBER!! : Please choose with [1 - 6]")
			main()

		time.sleep(1.25)

		p1Result = dice - int(p1Guess)
		p1Result = abs(p1Result)
		if p1Result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10
		elif p1Result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7
		if p1Result <= 2:
			pass
		else:
			if p1Result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4
		if p1Result <= 4:
			pass
		else:
			if p1Result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0

		p1result = dice2 - int(p1Guess2)
		p1result = abs(p1result)
		if p1result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10 + p1PointX
		elif p1result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7 + p1PointX
		if p1result <= 2:
			pass
		else:
			if p1result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4 + p1PointX
		if p1result <= 4:
			pass
		else:
			if p1result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0 + p1PointX

		p1result = dice3 - int(p1Guess3)
		p1result = abs(p1result)
		if p1result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10 + p1PointX
		elif p1result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7 + p1PointX
		if p1result <= 2:
			pass
		else:
			if p1result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4 + p1PointX
		if p1result <= 4:
			pass
		else:
			if p1result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0 + p1PointX

		p1result = dice4 - int(p1Guess4)
		p1result = abs(p1result)
		if p1result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10 + p1PointX
		elif p1result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7 + p1PointX
		if p1result <= 2:
			pass
		else:
			if p1result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4 + p1PointX
		if p1result <= 4:
			pass
		else:
			if p1result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0 + p1PointX

		p1result = dice5 - int(p1Guess5)
		p1result = abs(p1result)
		if p1result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10 + p1PointX
		elif p1result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7 + p1PointX
		if p1result <= 2:
			pass
		else:
			if p1result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4 + p1PointX
		if p1result <= 4:
			pass
		else:
			if p1result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0 + p1PointX

		p1result = dice6 - int(p1Guess6)
		p1result = abs(p1result)
		if p1result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10 + p1PointX
		elif p1result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7 + p1PointX
		if p1result <= 2:
			pass
		else:
			if p1result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4 + p1PointX
		if p1result <= 4:
			pass
		else:
			if p1result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0 + p1PointX

		p1result = dice7 - int(p1Guess7)
		p1result = abs(p1result)
		if p1result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10 + p1PointX
		elif p1result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7 + p1PointX
		if p1result <= 2:
			pass
		else:
			if p1result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4 + p1PointX
		if p1result <= 4:
			pass
		else:
			if p1result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0 + p1PointX

		p1result = dice8 - int(p1Guess8)
		p1result = abs(p1result)
		if p1result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10 + p1PointX
		elif p1result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7 + p1PointX
		if p1result <= 2:
			pass
		else:
			if p1result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4 + p1PointX
		if p1result <= 4:
			pass
		else:
			if p1result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0 + p1PointX

		p1result = dice9 - int(p1Guess9)
		p1result = abs(p1result)
		if p1result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10 + p1PointX
		elif p1result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7 + p1PointX
		if p1result <= 2:
			pass
		else:
			if p1result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4 + p1PointX
		if p1result <= 4:
			pass
		else:
			if p1result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0 + p1PointX

		p1result = dice10 - int(p1Guess10)
		p1result = abs(p1result)
		if p1result == 0:
			p1Point = 10 + p1Point
			p1PointX = 10 + p1PointX
		elif p1result <= 2:
			p1Point = 7 + p1Point
			p1PointX = 7 + p1PointX
		if p1result <= 2:
			pass
		else:
			if p1result <= 4:
				p1Point = 4 + p1Point
				p1PointX = 4 + p1PointX
		if p1result <= 4:
			pass
		else:
			if p1result == 5:
				p1Point = 0 + p1Point
				p1PointX = 0 + p1PointX

		p2Result = dice - int(p2Guess)
		p2Result = abs(p2Result)
		if p2Result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10
		elif p2Result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7
		if p2Result <= 2:
			pass
		else:
			if p2Result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4
		if p2Result <= 4:
			pass
		else:
			if p2Result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0

		p2result = dice2 - int(p2Guess2)
		p2result = abs(p2result)
		if p2result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10 + p2PointX
		elif p2result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7 + p2PointX
		if p2result <= 2:
			pass
		else:
			if p2result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4 + p2PointX
		if p2result <= 4:
			pass
		else:
			if p2result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0 + p2PointX

		p2result = dice3 - int(p2Guess3)
		p2result = abs(p2result)
		if p2result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10 + p2PointX
		elif p2result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7 + p2PointX
		if p2result <= 2:
			pass
		else:
			if p2result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4 + p2PointX
		if p2result <= 4:
			pass
		else:
			if p2result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0 + p2PointX

		p2result = dice4 - int(p2Guess4)
		p2result = abs(p2result)
		if p2result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10 + p2PointX
		elif p2result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7 + p2PointX
		if p2result <= 2:
			pass
		else:
			if p2result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4 + p2PointX
		if p2result <= 4:
			pass
		else:
			if p2result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0 + p2PointX

		p2result = dice5 - int(p2Guess5)
		p2result = abs(p2result)
		if p2result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10 + p2PointX
		elif p2result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7 + p2PointX
		if p2result <= 2:
			pass
		else:
			if p2result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4 + p2PointX
		if p2result <= 4:
			pass
		else:
			if p2result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0 + p2PointX

		p2result = dice6 - int(p2Guess6)
		p2result = abs(p2result)
		if p2result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10 + p2PointX
		elif p2result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7 + p2PointX
		if p2result <= 2:
			pass
		else:
			if p2result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4 + p2PointX
		if p2result <= 4:
			pass
		else:
			if p2result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0 + p2PointX

		p2result = dice7 - int(p2Guess7)
		p2result = abs(p2result)
		if p2result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10 + p2PointX
		elif p2result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7 + p2PointX
		if p2result <= 2:
			pass
		else:
			if p2result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4 + p2PointX
		if p2result <= 4:
			pass
		else:
			if p2result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0 + p2PointX

		p2result = dice8 - int(p2Guess8)
		p2result = abs(p2result)
		if p2result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10 + p2PointX
		elif p2result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7 + p2PointX
		if p2result <= 2:
			pass
		else:
			if p2result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4 + p2PointX
		if p2result <= 4:
			pass
		else:
			if p2result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0 + p2PointX

		p2result = dice9 - int(p2Guess9)
		p2result = abs(p2result)
		if p2result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10 + p2PointX
		elif p2result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7 + p2PointX
		if p2result <= 2:
			pass
		else:
			if p2result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4 + p2PointX
		if p2result <= 4:
			pass
		else:
			if p2result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0 + p2PointX

		p2result = dice10 - int(p2Guess10)
		p2result = abs(p2result)
		if p2result == 0:
			p2Point = 10 + p2Point
			p2PointX = 10 + p2PointX
		elif p2result <= 2:
			p2Point = 7 + p2Point
			p2PointX = 7 + p2PointX
		if p2result <= 2:
			pass
		else:
			if p2result <= 4:
				p2Point = 4 + p2Point
				p2PointX = 4 + p2PointX
		if p2result <= 4:
			pass
		else:
			if p2result == 5:
				p2Point = 0 + p2Point
				p2PointX = 0 + p2PointX


		time.sleep(1.1)
		print("\n\n1st DICE was", dice)
		print("2nd DICE was", dice2)
		print("3rd DICE was", dice3)
		print("4th DICE was", dice4)
		print("5th DICE was", dice5)
		print("6th DICE was", dice6)
		print("7th DICE was", dice7)
		print("8th DICE was", dice8)
		print("9th DICE was", dice9)
		print("10th DICE was", dice10)
		guessedTxt = "{} guessed"
		gotTxt = "{} got"
		opTxt = "{} Overall Point:"
		print("\n1st:", guessedTxt.format(p1Un), p1Guess)
		print("2nd:", guessedTxt.format(p1Un), p1Guess2)
		print("3rd:", guessedTxt.format(p1Un), p1Guess3)
		print("4th:", guessedTxt.format(p1Un), p1Guess4)
		print("5th:", guessedTxt.format(p1Un), p1Guess5)
		print("6th:", guessedTxt.format(p1Un), p1Guess6)
		print("7th:", guessedTxt.format(p1Un), p1Guess7)
		print("8th:", guessedTxt.format(p1Un), p1Guess8)
		print("9th:", guessedTxt.format(p1Un), p1Guess9)
		print("10th:", guessedTxt.format(p1Un), p1Guess10)
		print(gotTxt.format(p1Un), p1PointX, "point")
		print(opTxt.format(p1Un), p1Point)
		print("\n1st:", guessedTxt.format(p2Un), p2Guess)
		print("2nd:", guessedTxt.format(p2Un), p2Guess2)
		print("3rd:", guessedTxt.format(p2Un), p2Guess3)
		print("4th:", guessedTxt.format(p2Un), p2Guess4)
		print("5th:", guessedTxt.format(p2Un), p2Guess5)
		print("6th:", guessedTxt.format(p2Un), p2Guess6)
		print("7th:", guessedTxt.format(p2Un), p2Guess7)
		print("8th:", guessedTxt.format(p2Un), p2Guess8)
		print("9th:", guessedTxt.format(p2Un), p2Guess9)
		print("10th:", guessedTxt.format(p2Un), p2Guess10)
		print(gotTxt.format(p2Un), p2PointX, "point")
		print(opTxt.format(p2Un), p2Point)

		print("\nResult: ")
		pWin = "!! {} WIN !!"
		if p1PointX == p2PointX:
			print("!! TIE !!")
		elif p1PointX > p2PointX:
			print(pWin.format(p1Un))
		elif p1PointX < p2PointX:
			print(pWin.format(p2Un))

		time.sleep(1.5)


def main():
	gameMenu()
	if gameMode == 1:
		difficulty()
		if difficultyLvl == 4:
			EXTDifficultyCheck()
		rounds()
		if difficultyLvl == 0:
			normalDifficultySuperEasy()
		elif difficultyLvl == 1:
			normalDifficultyEasy()
		elif difficultyLvl == 2:
			normalDifficultyNormal()
		elif difficultyLvl == 3:
			normalDifficultyHard()
		elif difficultyLvl == 4:
			normalDifficultyEXTREME()
	elif gameMode == 2:
		multiplayer()
		userName()
		if multiplayerMode == 1:
			difficulty()
			if difficultyLvl == 4:
				EXTDifficultyCheck()
			rounds()
			if difficultyLvl == 0:
				duelBotDifficultySuperEasy()
			elif difficultyLvl == 1:
				duelBotDifficultyEasy()
			elif difficultyLvl == 2:
				duelBotDifficultyNormal()
			elif difficultyLvl == 3:
				duelBotDifficultyHard()
			elif difficultyLvl == 4:
				duelBotDifficultyEXTREME()
			finalResult()
		elif multiplayerMode == 2:
			difficulty()
			if difficultyLvl == 4:
				EXTDifficultyCheck()
			rounds()
			if difficultyLvl == 0:
				duelFriendDifficultySuperEasy()
			elif difficultyLvl == 1:
				duelFriendDifficultyEasy()
			elif difficultyLvl == 2:
				duelFriendDifficultyNormal()
			elif difficultyLvl == 3:
				duelFriendDifficultyHard()
			elif difficultyLvl == 4:
				duelFriendDifficultyEXTREME()
			finalResult()
		elif multiplayer == 3:
			pass

main()


def restart():
	restart = input("\nRestart the Game? [y/n] > ")

	if restart == "y" or restart == str("Y") or restart == str("yes") or restart == str("Yes") or restart == str("YES") or restart == str("yES") or restart == str("YEs") or restart == str("yeS") or restart == str("yEs") or restart == str("Yeah"):
		main()
	else:
		exit()

restart()