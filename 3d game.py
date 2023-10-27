import pygame
#ide Project zomboid likt spill
#fin ut allt med object og sånt
class GO(pygame.sprite.Sprite):
    pass
class Player():
    #init er brukt for å gi attributes
    def __init__(self,name,hitpoints,health,position):

        self.name =name
        self.hitpoints=hitpoints
        self.position=position
        self.health=health
    def update():
        print("update")
    def printStats(self):
        print(self.name,self.hitpoints,self.position)
    def fight(slef,hitpoints):
        print("You are fighting"+str(health))
        health = health -1
        print("actual health"+str(health))
    class Human(pygame.sprite.Sprite):
        #constructor
        def __init__(self,name,weight,age):
            self.name=name
            self.weihgt=weight
            self.age=age
        def printStats(self):
            print(self.name,self,weight,self,age)
        def update(self):
                print("update")
        def calculatepos(self,position):
                print(position)
class SuperHuman(Human):
    def __init__(self, name, weight, age):
        #super human caller stuff til mamma klassen
        super().__init__(name, weight, age)
        super().printStats()
        self.specialability=specialability


position =[100,10]
player1 = Player("Peter Parker",100,100,position)
#player1.update()
player1.printStats
player1.fight(100,200)


human1= Human("Arthur",72,100)
hulk =SuperHuman("bruce banner",300,55)
#pygame.init()

#pygame.display()
#pygame.sprite.Sprite.
#pygame.image.
pygame.image.load
while True:
    human1.update()

