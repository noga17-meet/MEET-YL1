from meet import *
import random
colors=["blue", "red", "plae green", "purple", "yellow", "brown", "black", "grey", "gold"]
cells=[]
z=0
while(z<20):
	ball1= {"radius": random.randint(1,20), "x":random.randint(1,20), "y":random.randint(1,20), "dy":random.randint(1,20), "dx": random.randint(1,20), "color": colors[random.colors(0,-1)]}
	circle1= create_cell(ball1)
	cells.append(circle1)
	z+=1

def borders(cells):
	for cell in cells:
		width = get_screen_width()
		height = get_screen_height()
		x = cell.xcor()
		y = cell.ycor()
		if (x > width):
			cell.set_dx(-cell.get_dx())
		#if (x > -width):
			#cell.set_dx(-cell.get_dx())
                                               
while (True):
	move_cells(cells)
	borders(cells)
	

