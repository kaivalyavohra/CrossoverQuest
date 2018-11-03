from random import randint
from time import sleep
from scoring import *
from OOPClasses import *

textfile = open("highscores.txt", "r")
scores = sorted(literal_eval(textfile.read()).items(),
                key=lambda t: t[1], reverse=True)
printscores(scores)

print("\nWelcome to Crossover Quest. Mario just sent you an email from his holiday in Bali. Princess Peach has been kidnapped by Lord Voldemort.")
x = input("You must go on a quest to rescue her. Enter anything to begin: ")
sleep(0.7)
difficultyLevel = 0
monsterList = [Vogon(), Dementor(), Dragon()]
opponentList = []
while True:
    try:
        difficultyLevel = int(
            input("\nEnter 1 for Easy, 2 for Medium, or 3 for Hard: "))
        if difficultyLevel in [1, 2, 3]:
            break
        else:
            print("Invalid")
    except ValueError:
        print("Invalid")
monsterCounter = 0
for i in range(0,difficultyLevel):
    monsterCounter = randint(0, len(monsterList) - 1)
    opponentList.append(monsterList[monsterCounter])
opponentList.append(Voldemort())
print(opponentList)

sleep(0.75)
while True:
    try:
        playerClassInput = int(
            input("\nEnter 1 for Fighter, 2 for Marksman, or 3 for Mage: "))
        if playerClassInput in [1, 2, 3]:
            break
        else:
            print("Invalid")
    except ValueError:
        print("Invalid")
classList = ["", Fighter(), Marksman(), Mage()]
myPlayer = Player(classList[playerClassInput])


def makeMove(player, opponent):
    playerMove = player.doMove()
    oppMove = opponent.playTurn()
    sleep(0.7)
    if playerMove > 0:

        if oppMove == -1:
            print("\nOpponent succesully blocked your move.")
        else:
            attackChance = randint(1, myPlayer.Race.getSpeed())
            if attackChance > 10:
                print("\nYou succesfully attacked and dealt",
                      playerMove, "damage.")
                opponent.setHealth(opponent.getHealth() - playerMove)
            else:
                print("\nSorry. You were too slow. Attack Unsuccesful")

    if oppMove > 0:
        if playerMove == -1:
            blockChance = randint(1, myPlayer.Race.getSpeed())
            if blockChance > 15:
                print("\nYou blocked the opponents move.")
            else:
                print("Sorry. You were too slow.")
                print("\nOpponent succesfully attacked and dealt",
                      oppMove, "damage.")
                player.Race.setHealth(player.Race.getHealth() - oppMove)
        else:
            print("\nOpponent succesfully attacked and dealt", oppMove, "damage.")
            player.Race.setHealth(player.Race.getHealth() - oppMove)


opp1 = Dragon()


for i in range(0, len(opponentList)):
    opp1 = opponentList[i]
    print("\n\nYou are facing a", opp1.getName())
    opp1.setHealth(100 + (i * 5))
    while myPlayer.Race.getHealth() > 1 and opp1.getHealth() > 1:
        sleep(1)
        print("\n\nYour health:", myPlayer.Race.getHealth(),
              "\n" + opp1.getName(), "health:", opp1.getHealth())
        sleep(1)
        makeMove(myPlayer, opp1)
        if myPlayer.Race.getHealth() < 1:
            print("\nGame over. You have died.")
            quit()
        if opp1.getHealth() < 1:
            print(
                "\nYou have beaten your opponent. As a result, your health has increased by 40.")
            myPlayer.Race.setHealth(myPlayer.Race.getHealth() + 30)
            sleep(1)
            break
sleep(1)
print("\nCongratulations.\nYou have succesfully completed your quest and saved Princess Peach. Mario is eternally greatful.")
while True:
    username=input("Enter your 3 letter long gamer tag: ")
    if len(username)==3:
    	break
    
addscore(username,difficultyLevel*2*myPlayer.Race.getHealth(),scores)
