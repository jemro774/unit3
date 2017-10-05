#Jack Robey
#10/5/17
##dotsDemo.py - Making some dots

from ggame import *

red = Color(0xFF0000,1)

dot = CircleAsset(20,LineStyle(1,red),red)

for j in range(10): #prints the row 10 times
    for i in range(100): #prints one row of dots
        Sprite(dot,(200+100*i,200+100*j))
App().run()
