from meet import *
import random
colors=["blue", "red", "pale green", "purple", "yellow", "brown", "maroon", "grey", "gold"]
cells=[]
user_cell= {"radius": 5, "x": 7, "y": 7, "dy": 1, "dx": 2, "color": "black"}
user_cell1= create_cell(user_cell)
cells.append(user_cell1)
z=0
while(z<15):
	ball1= {"radius": random.randint(10,30), "x":random.randint(1,100), "y":random.randint(1,100), "dy":random.randint(1,10), "dx": random.randint(1,10), "color": colors[random.randint(0, len(colors)-1)]}
	circle1= create_cell(ball1)
	cells.append(circle1)
	z+=1
