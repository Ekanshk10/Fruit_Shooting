import pgzrun
from random import randint
score = 0 
orange = Actor("orange")
apple = Actor("apple")
def draw():
    screen.clear()
    screen.draw.text("Score:"+ str(score),color="white",topleft=(10,10))
    apple.draw()
    orange.draw()

def place_apple():
    apple.x = randint(10,600)
    apple.y = randint(10,400)

def place_orange():
    orange.x = randint(10,600)
    orange.y = randint(10,400)

def on_mouse_down(pos): # on_mouse_down is built in function which run every time we hit the mouse and pos is position of the cursor
    global score
    if apple.collidepoint(pos): #This function checks if the cursor is in same position as an apple
        print("GOOD SHOT :D")
        score += 1
        place_apple()
        place_orange()
    elif orange.collidepoint(pos):
        print("Wrong Fruit")
        score -=1
        place_apple()
        place_orange()
    else:
        print("YOU MISSED :(")
        #score -= 1
        print("Total Score:",score)
        quit()
place_apple()
place_orange()
pgzrun.go()