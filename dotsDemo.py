#Jack Robey
#10/5/17
##dotsDemo.py - Making some dots

from ggame import *

red = Color(0xFF0000,1)

dot = CircleAsset(20,LineStyle(1,red),red)

for i in range(100):
    Sprite(dot,(200+10*i,200))
App().run()
