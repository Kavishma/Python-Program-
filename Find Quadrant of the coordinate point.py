from os import *
from sys import *
from collections import *
from math import *

#Your code goes here
def quadrant(x, y): 
    if (x > 0 and y > 0): 
        print ("1st Quadrant") 
  
    elif (x < 0 and y > 0): 
        print ("2nd Quadrant") 
          
    elif (x < 0 and y < 0): 
        print ("3rd Quadrant") 
      
    elif (x > 0 and y < 0): 
        print ("4th Quadrant") 
          
    elif (x == 0 and y > 0 or x == 0 and y < 0 ): 
        print ("y axis") 
      
    elif (y == 0 and x < 0 or y == 0 and x > 0): 
        print ("x axis") 

    else: 
        print ("Origin") 
  
# Driver code      
x, y = map(int, input().strip().split())

quadrant(x, y) 


























