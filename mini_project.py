#Name:
#Mini-Project - Build Your Own Game!
'''
This is YOUR game. You are the designer. There are only two requirements:

  1. Your game must use USER INPUT — typed answers, key strokes, mouse clicks, etc.
  2. Your game must keep track of and DISPLAY A SCORE.

You have everything you need from Modules 1-6: variables, input(), if/elif/else,
while loops, for loops, lists, random, and turtle graphics.

======================= NEED AN IDEA? PICK ONE OF THESE =======================

  TERMINAL GAMES (use input(), great with while loops + random):
    - Number guessing: score points for guessing in fewer tries, play 5 rounds
    - Math quiz: random questions, +1 per right answer, show the final score
    - Rock, paper, scissors: first to 3 wins, show the running score
    - Trivia: store questions and answers in lists, loop through them

  TURTLE GAMES (use the mouse or keyboard, see the reminder below):
    - Click the turtle: it jumps to a random spot every time you click it
    - Turtle race: press a key to make your turtle dash to the finish line
    - Falling catch: move a paddle with the arrow keys to catch a falling dot

  ...or invent something completely new. Weird ideas are welcome.

============================ HELPFUL SNIPPETS ================================

  Typed input:
      guess = int(input("Your guess: "))

  Turtle keyboard input:
      screen = turtle.Screen()
      screen.onkey(move_left, "Left")     # calls move_left() on the left arrow
      screen.listen()

  Turtle mouse input:
      screen.onclick(jump)                # calls jump(x, y) on every click
      my_turtle.onclick(caught)           # only when the turtle itself is clicked

  Keeping and showing a score:
      score = 0
      score = score + 1                   # when the player earns a point
      print("Score:", score)              # terminal
      pen.write("Score: " + str(score))   # turtle (use a separate pen turtle)

  REMINDER for turtle games — to see your game in Codespaces: run it, open the
  PORTS tab, click port 6080 ("Turtle Desktop"), Connect, password: vscode

========================== LEVEL-UP IDEAS (optional) ==========================

  - Add lives: the game ends after 3 misses
  - Add difficulty: harder questions or a faster game as the score goes up
  - Add a high score: remember the best score across rounds with a variable
  - Add sound-off flair: ASCII art title screens, victory messages, emoji

==============================================================================
Build your game below. Delete this line and start coding!
'''
import random
import turtle
import time
screen = turtle.Screen()
lace = turtle.Turtle()
phan = turtle.Turtle()
horn = turtle.Turtle()

def move_up():
  lace.speed(0)
  lace.setheading(90)
  lace.speed(5)
  lace.fd(50)

def move_left():
  lace.speed(0)
  lace.setheading(180)
  lace.speed(5)
  lace.fd(50)

def move_down():
  lace.speed(0)
  lace.setheading(270)
  lace.speed(5)
  lace.fd(50)

def move_right():
  lace.speed(0)
  lace.setheading(0)
  lace.speed(5)
  lace.fd(50)


def square_helper(count):
  #randomly place squares and increase score when the turtle enters one (unless turtle is already in the square location)
  phan.speed(0)
  phan.hideturtle()
  score_up = 0
  while count == 0:
    phan.penup()
    phan.goto(random.randint(-225,225),random.randint(-225,225))
    phan.pendown()
    phan.fd(50)
    phan.lt(90)
    phan.fd(50)
    phan.lt(90)
    phan.fd(50)
    phan.lt(90)
    phan.fd(50)
    count = count + 1

  if lace.pos()[0] > phan.pos()[0] and lace.pos()[1] > phan.pos()[1] and lace.pos()[0] < (phan.pos()[0]+50) and lace.pos()[1] < (phan.pos()[1]+50):
    phan.clear()
    phan.penup()
    phan.goto(random.randint(-225,225),random.randint(-225,225))
    phan.pendown()
    phan.setheading(0)
    phan.fd(50)
    phan.lt(90)
    phan.fd(50)
    phan.lt(90)
    phan.fd(50)
    phan.lt(90)
    phan.fd(50)
    score_up = score_up + 1
  if count == 1:
    return count
  if count > 1:
    return score_up


def score_writer(score):
  horn.penup()
  horn.hideturtle()
  horn.goto(240,240)
  horn.clear()
  horn.write(f'SCORE: {score:.0f}',font=('Courier', 12, 'normal'))



def main():

  print('WASD to move')
  lace.penup()
  count = 0
  loop_var = 0
  score = 0
  while loop_var == 0:
    screen.onkey(move_up, "w")
    screen.onkey(move_left, "a")
    screen.onkey(move_down, "s")
    screen.onkey(move_right, "d")
    screen.listen()

    if count == 0:
      count = square_helper(count)
    count = count + 1
    if square_helper(count) == 1:
      score = score + 1

    print(count)
    print('scoreis'+str(score))
    score_writer(score)

    
main()
turtle.done()