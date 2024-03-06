# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers
# for _ in range(10)

class Robot:
    
    def __init__(self, name, attack, hp):
      self.name = name
      self.attack = attack
      self.hp = hp

    def attack_enemy(self, enemy):
      value = randint(1, 2)
      print(value)
      enemy.hp -= self.attack * value
      print(f"{self.name} attacked {enemy.name} and dealt {self.attack * value} damage, multiplied by {value}")

    def regen(self,enemy):
      value= randint(10, 50)
      self.hp+=value
      print(f"{self.name} regenerated {value} hp")
      
    def giveup(self,enemy):
      self.hp=0

    def is_alive(self):
      return self.hp > 0

class Games:
    def __init__(self,robot1, robot2):
      self.rounds = 0
      self.robot1 = robot1
      self.robot2 = robot2

    def game(self):
      print(f"Welcome to the game!")
      #awalan game
      while self.robot1.is_alive() and self.robot2.is_alive():
        self.rounds  += 1
        print(f"Round {self.rounds}")
        print(f"Robot 1: {self.robot1.name} HP: {self.robot1.hp}")
        print("VS")
        print(f"Robot 2: {self.robot2.name} HP: {self.robot2.hp}")
        print("--------------------\n")

        print(f"{self.robot1.name}")
        print(f'1. Attack      2. HP Regen      3.Give Up')
        robot1C = int(input(f'Action:'))

        print(f"{self.robot2.name}")
        print(f'1. Attack      2. HP Regen      3.Give Up')
        robot2C = int(input(f'Action:'))

        if robot1C == 3 and robot2C == 3:
          print(f'Draw,{self.robot1.name} and {self.robot2.name} are give Ups')
          break
        else:
          if robot1C == 1:
            self.robot1.attack_enemy(self.robot2)
          elif robot1C == 2:
             self.robot1.regen(self.robot2)
          elif robot1C == 3:
            print(f'{self.robot1.name} is give up')
            self.robot1.giveup(self.robot2)
          else :
            print("Input not valid")
          if robot2C == 1:
              self.robot2.attack_enemy(self.robot1)
          elif robot2C == 2:
              self.robot2.regen(self.robot1)
          elif robot2C == 3:
              print(f'{self.robot2.name} is give up')
              self.robot2.giveup(self.robot1)
          else :
              print("Input not valid")
          if self.robot1.is_alive() == False and self.robot2.is_alive() == False:
            print(f"Draw, {self.robot1.name} and {self.robot2.name} are out of hp in same round")
          elif self.robot1.is_alive() == False :
            print(f"{self.robot2.name} wins in {self.rounds} rounds")
          elif self.robot2.is_alive() == False :
            print(f"{self.robot1.name} wins in {self.rounds} rounds")
            
Robot1 = Robot("Bocchi", 69, 350)
Robot2 = Robot("Ryo",50,500)
game = Games(Robot1, Robot2)
game.game()
