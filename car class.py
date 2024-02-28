# Car Class
from os import *
from sys import *
from collections import *
from math import *

from sys import stdin


class Car:

    #Write your constructor and printCarInfo method here.
    def __init__(self, noOfGear, color):
        self.noOfGear = noOfGear
        self.color = color
        
    def printCarInfo(self):
        print("noOfGear:", self.noOfGear)
        print("color:", self.color)  
        print("maxSpeed:", self.maxSpeed) 
        


class RaceCar(Car):
    
    #Write your constructor and printRaceCarInfo method here.
    def __init__(self, noOfGear, color, maxSpeed):
        super().__init__(noOfGear, color)
        self.maxSpeed = maxSpeed
        
    def printRaceCarInfo(self):
        print("noOfGear:", self.noOfGear)
        print("color:", self.color)
        print("maxSpeed:", self.maxSpeed)

        
#Driver's code

noOfGear = int(stdin.readline().rstrip())
color = stdin.readline().rstrip()
maxSpeed = int(stdin.readline().rstrip())
        
raceCar = RaceCar(noOfGear,color,maxSpeed)
raceCar.printCarInfo()
