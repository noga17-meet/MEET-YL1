import meet
import random
import time
import turtle
colors=["blue", "red", "pale green", "purple", "yellow", "brown", "maroon", "grey", "gold"]
cells=[]
user_cell= {"radius": 20, "x": 50, "y": -50, "dy": 1, "dx": 2, "color": "black"}
user_cell1= meet.create_cell(user_cell)
cells.append(user_cell1)
z=0
while(z<15):
	ball1= {"radius": random.randint(10,30), "x":random.randint(-50,100), "y":random.randint(30,100), "dy":random.random(), "dx": random.random(), "color": colors[random.randint(0, len(colors)-1)]}
	circle1= meet.create_cell(ball1)
	cells.append(circle1)
	z+=1
playing=True

def borders(cells):
	for cell in cells:
		width = meet.get_screen_width()
		height = meet.get_screen_height()
		x = cell.xcor()
		y = cell.ycor()
		if (x > width):
			cell.set_dx(-cell.get_dx())
		if (x < -width):
			cell.set_dx(-cell.get_dx())
		if (y > height):
			cell.set_dy(-cell.get_dy())
		if (y < -height):
			cell.set_dy(-cell.get_dy())

def collision(cells):
	global playing
	for i in cells:
		for j in cells:
			distance=((i.xcor()-j.xcor())**2 + (i.ycor()-j.ycor())**2)**0.5
			if distance<=i.get_radius() + j.get_radius():
				if i.get_radius()>j.get_radius():
					i.set_radius(i.get_radius() + 2)
					x=meet.get_random_x()
					y=meet.get_random_y()
					j.goto(x,y)
				if i == user_cell1 and i.get_radius()<j.get_radius():
					turtle.write('Game Over',align='center',font=('ariel',50,'bold'))
					time.sleep(3)
					turtle.bye()
meet.move_cells(cells)
time.sleep(3)						
 
                                               
while playing:
	meet.move_cells(cells)
	borders(cells)
	collision(cells)
	xdir,ydir = meet.get_user_direction(user_cell1)
	user_cell1.set_dx(xdir)
	user_cell1.set_dy(ydir)
meet.mainloop()
