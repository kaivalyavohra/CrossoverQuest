#Kaivalya Vohra 2018
#import libraries
from time import sleep
from random import randint

# initialize monster classes


class Monster():
    def __init__(self, name, attackPower, attackName, defenseName):
        self._attackPower = attackPower
        self._attackName = attackName
        self._defenseName = defenseName
        self._name = name
        self._health = 100

    def setHealth(self, changeHealth):
        self._health = changeHealth

    def getHealth(self):
        return(self._health)

    def getAttackPower(self):
        return(self._attackPower)

    def getAttackName(self):
        return(self._attackName)

    def getDefenseName(self):
        return(self._defenseName)

    def getName(self):
        return(self._name)

    def playTurn(self):
        moves = [self._attackName, self._defenseName]
        turnNum = randint(1, 2)

        if turnNum % 2:
            print(self._name, "used", moves[0])
            return(self._attackPower)
        else:
            print(self._name, "used", moves[1])
            return(-1)


class Vogon(Monster):
    def __init__(self):
        super().__init__("Vogon", 25, "Vogon Attack", "Block")


class Dementor(Monster):
    def __init__(self):
        super().__init__("Dementor", 25, "Dementor's Kiss", "Block")


class Dragon(Monster):
    def __init__(self):
        super().__init__("Dragon", 25, "FireBreath", "Block")


class Voldemort(Monster):
    def __init__(self):
        super().__init__("Voldemort", 30, "Crucio", "Expelliarmus(Block)")


# initialize race classes
class Race():
    def __init__(self, health, intellect, strength, speed, specialAttackName):
        self._health = health
        self._intellect = intellect
        self._strength = strength
        self._speed = speed
        self._specialAttackName = specialAttackName

    def setHealth(self, changeHealth):
        self._health = changeHealth

    def getHealth(self):
        return(self._health)

    def getIntellect(self):
        return(self._intellect)

    def getStrength(self):
        return(self._strength)

    def getSpeed(self):
        return(self._speed)

    def getSpecialAttackName(self):
        return(self._specialAttackName)

    def specialAttack(self):
        print(self._specialAttackName, "was used.")
        damage = (self._intellect + self._strength) / 2
        self.setHealth(self.getHealth() - 20)
        return(damage)

    def getSpecialAttackPower(self):
        return((self._intellect + self._strength) / 2)


class Wookie(Race):
    def __init__(self):
        super().__init__(100, 25, 100, 25, "Wookie Scream")


class Human(Race):
    def __init__(self):
        super().__init__(100, 50, 50, 50, "Humanoid Attack")


class Droid(Race):
    def __init__(self):
        super().__init__(100, 100, 25, 25, "CyberStrike")

# initialize class classes


class CharacterClass():
    def __init__(self, attackPower, healPower, attackName, defenseName):
        self._attackPower = attackPower
        self._healPower = healPower
        self._attackName = attackName
        self._defenseName = defenseName

    def defense(self):
        return(-1)

    def getAttackPower(self):
        return(self._attackPower)

    def getHealPower(self):
        return(self._healPower)

    def getAttackName(self):
        return(self._attackName)

    def getDefenseName(self):
        return(self._defenseName)


class Fighter(CharacterClass):
    def __init__(self):
        super().__init__(35, 20, "Slice", "Block")


class Marksman(CharacterClass):
    def __init__(self):
        super().__init__(40, 20, "Shoot Arrow", "Block")


class Mage(CharacterClass):
    def __init__(self):
        super().__init__(45, 20, "Imperio Curse", "Patronus Charm")

# initialize player class- uses composition for the race


class Player():
    def __init__(self, theClass):

        self.Class = theClass
        sleep(0.7)
        print("\nThere are 3 races.\nWookie-Intellect:25, Strength:100, Speed:25")
        print("Human-Intellect:50, Strength:50, Speed:50\nDroid-Intellect:100, Strength:25, Speed:25")
        print("Note: All these attributes will influence the game in some way.")
        while True:
            try:
                playerRaceInput = int(
                    input("\nEnter 1 for Wookie, 2 for Human, or 3 for Droid: "))
                if playerRaceInput in [1, 2, 3]:
                    break
                else:
                    print("Invalid")
            except ValueError:
                print("Invalid")
        raceList = ["", Wookie(), Human(), Droid()]
        self.Race = raceList[playerRaceInput]

    def doMove(self):
        print("\n\n")
        moves = [self.Class.getAttackName() + " (Damage: " + str(self.Class.getAttackPower()) + ")", self.Class.getDefenseName(),
                 "Heal. Increase your health by 20", self.Race.getSpecialAttackName() + " (Damage: " + str(self.Race.getSpecialAttackPower()) + ")"]
        for i in range(1, len(moves) + 1):
            print("Enter", i, "for", moves[i - 1])
        print("Note:", self.Race.getSpecialAttackName(),
              "will take away 20 of your health.")
        while True:
            try:
                playerChoice = int(input("\nEnter your choice: "))
                if playerChoice in range(1, len(moves) + 1):
                    break
                else:
                    print("Invalid")
            except ValueError:
                print("Invalid")
        if playerChoice == 1:
            print("You used", self.Class.getAttackName())
            return(self.Class.getAttackPower())
        elif playerChoice == 2:
            print("You used Block.")
            return(-1)
        elif playerChoice == 3:
            print("You used Heal.")
            self.Race.setHealth(self.Race.getHealth() +
                                self.Class.getHealPower())
            return(0)
        else:
            return(self.Race.specialAttack())
