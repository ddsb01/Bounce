#!/usr/bin/python3

# game 'B O U N C E'.



from tkinter import *
import random
import time



# the  W I N D O W : 
# create the main window object
root = Tk()
root.title(" ^^ BOUNCE ^^ ")

root.resizable(0,0)                 # it means that we'll not be able to resize the window. (0,0) :: (height, width)=(False, False)

root.wm_attributes("-topmost",1)    # the window containing our canvas will always remain on top of all other windows.

canvas = Canvas(root, width = 500, height = 500, bd = 0, highlightthickness =0)
canvas.pack()

root.update()











# Required C L A S S E S :
# creating the class ball :
class ball :
    def __init__(self, canvas, paddle, color) :
        self.canvas = canvas
        self.paddle = p

        self.id = canvas.create_oval(10,10,25,25, fill = color) #(top, left, bottom, right)
        
        self.canvas.move(self.id, 245, 100)                # (x, y) : top-left corner is (0,0)    
                                                           # moving the ball to the middle of the canvas.
        
        start = [-3, -2, -1, 0, 1, 2, 3]
        random.shuffle(start)
        
        self.x = start[0]
        self.y = -3         # in the game, the paddle is going to be at the bottom so the ball should initially go upwards so that the user has time to react.
        
        self.canvas_height = self.canvas.winfo_height()
        self. canvas_width = self.canvas.winfo_width()

        self.hits_bottom = False



    def paddle_ctrl(self, pos) :
        paddle_pos = self.canvas.coords(self.paddle.id)     # paddle_pos is an array containing the co-ordinates of the paddle.


        # [x1, y1, x2, y2] : [left, top, right, bottom]
    
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] :        # i.e., if the ball's rightmost  co-ordinate >= paddle's leftmost co-ordinate AND the ball's leftmost co-ordinate <= paddle's rightmost co-ordinate :: the ball touches the paddle. 
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3] :    # i.e., if the ball is above the paddle.
                return True
            return False
         




    def draw(self) :
        self.canvas.move(self.id, self.x, self.y)               # x : move horizontally, if self.y = -1 : move one pixel up.
        pos = self.canvas.coords(self. id) # [x1, y1, x2, y2]      # coords returns the coordinates of the ball.
        
        # print(pos)

        # to keep the ball inside the window :
        # vertically :
        if pos[1] <= 0 :                  # y1 is top boundary
            self.y = 3                    # greater magnitude : the ball moves faster.
        
        if pos[3] >= self.canvas_height : # y2 is bottom boundary
            self.hits_bottom = True
            canvas.create_text(245,100, text = " ' G A M E   O V E R ' ", font = ("Arial 20 bold"), fill = "red")

        # horizontally :
        if pos[0] <= 0 :                  # x1 is left boundary
            self.x = 3
        if pos[2] >= self.canvas_width :  # x2 is right boundary
            self.x = -3 

        # self.x < 0 : move left, self.y < 0 : move up

        if self.paddle_ctrl(pos) == True :  # if ball hits the paddle, it should go up.
            self.y = -3
        





# creating the paddle class :
class paddle :
    def __init__(self, canvas, color) :
        self.canvas = canvas
        
        self.id = canvas.create_rectangle(0,0,100,10, fill = color)
        
        self.canvas.move(self.id, 200, 450)     # (x, y) : top-left corner is (0,0)
        
        # since the paddle has to move only in horizontal direction so we just have to take care of that.
        self.x = 0
        
        self.canvas_width = self.canvas.winfo_width()

        # binding keyboard input keys and direction of motion of the paddle.
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

        

    def draw(self) :
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        
        if pos[0] <= 0 :
            self.x = 0
        if pos[2] >= self.canvas_width :
            self.x = 0
    

    def turn_left(self, event) :
        self.x = -2
    def turn_right(self, event) :
        self.x = 2













# Required  O B J E C T S :
# creating the paddle (object) :
p = paddle(canvas, 'brown')

# creating the ball (object) :      
b = ball(canvas, paddle, 'orange')

# the paddle object should, obviously, be called first as ball object takes paddle as a parameter.










# E X E C U T E :
while(1) :
    if b.hits_bottom == False :
        b.draw()                    # to move the ball (actual animation)
        p.draw()                    # to move the paddle 
    
    root.update_idletasks()     # updating the background tasks
    root.update()               # updating the foreground tasks
    
    time.sleep(0.01)            # it takes 0.01 seconds to update the screen.

    # to kill the window object after game is over.
    if b.hits_bottom == True :
        time.sleep(5)   # holds the screen for 5 seconds (so that user sees 'GAME OVER')
        root.destroy()  # closes the tkinter window automatically.
