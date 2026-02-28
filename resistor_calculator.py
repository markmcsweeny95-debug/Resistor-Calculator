import time 
import turtle
from turtle import *
digit_to_colour = {
   0: "black",
   1: "brown",
   2: "red",
   3: "orange",
   4: "yellow",
   5: "green",
   6: "blue",
   7: "violet",
   8: "grey",
   9: "white"
}
colour_to_digit = {
   "black": 0,
   "brown":1,
   "red":2,
   "orange":3,
   "yellow":4,
   "green":5,
   "blue":6,
   "violet":7,
   "grey": 8,
   "white":9,
}
multiplier_values = {
   "black":1,
   "brown":10, 
   "red":100,
   "orange":1000,
   "yellow":10000,
   "green":100000,
   "blue": 1000000,
   "gold":0.1,
   "silver":0.01
}
time.sleep(0.2)
message = "Welcome to the resistor calculator"
for char in message:
       print (char, end = '', flush = True)
       time.sleep(0.05)
time.sleep(0.2)
print("")
print("-------------------------------------")
time.sleep(0.2)
x = 1 
while x == 1:
    print("Select a mode")
    time.sleep(0.2)
    print("1 - Calculate resistor value (Text based)")
    time.sleep(0.2)
    print("2 - Visualise a resistor using turtle")
    time.sleep(0.2)
    message = ">>>"
    for char in message:
       print (char, end = '', flush = True)
       time.sleep(0.5)
    print()
    print("")
    print("")
    time.sleep(0.2)
    mode = input("Enter 1 or 2 to begin.")
    if mode == "1":
       time.sleep(0.2)
       print("Welcome to the text based resistor value calculator...")
       print("")
       time.sleep(0.2)
       print("We will assume the tolerance is 5%, Gold")
       time.sleep(0.2)
       message = ">>>"
       for char in message:
          print (char, end = '', flush = True)
          time.sleep(0.5)
       print("")
       print("")
       time.sleep(0.2)
       print("Example input: RED RED BLACK GOLD")
       time.sleep(0.2)
       Rcolours = input("Enter the colours of your resistor.(orientation doesn't matter) ")
       message = ">>>>>>>>>>"
       for char in message:
          print (char, end = '', flush = True)
          time.sleep(0.5)
       print("")
       print("")
       colours = Rcolours.strip().lower().split()
       if len(colours)>0 and colours [0] == "gold":
          colours.reverse()
       organisedcolours = (" ".join(colours))
       first = colour_to_digit[colours[0]]
       second = colour_to_digit[colours[1]]
       multiplier = multiplier_values[colours[2]]
       goldvalue = [colours[3]]
       value = (first * 10 + second) * multiplier 
       time.sleep(0.2)
       print("The resistor value is... ")
       time.sleep(0.2)
       print (value,"Ω")
       time.sleep(20)
       print("Code will restart in 5")
       time.sleep(1)
       print("Code will restart in 4")
       time.sleep(1)
       print("Code will restart in 3")
       time.sleep(1)
       print("Code will restart in 2")
       time.sleep(1)
       print("Code will restart in 1")
       time.sleep(1)

    elif mode == "2":
       time.sleep(0.2)
       print("Welcome to the resistor visualizer")
       time.sleep(0.2)
       print("Enter resistor value in number form with no letters")
       time.sleep(0.2)
       print("For example a 200k ohm resitor you would enter as 200000")
       time.sleep(0.2)
       message = ">>>"
       for char in message:
          print (char, end = '', flush = True)
          time.sleep(0.5)
       print("")
       print("")
       value = input("Enter your resistor value")
       message = ">>>"
       for char in message:
          print (char, end = '', flush = True)
          time.sleep(0.5)
       print("")
       print("")
       first_digit = int(value[0])
       second_digit = int(value[1])
       multiplier = len(value)- 2 
       band1 = digit_to_colour[first_digit]
       band2 = digit_to_colour[second_digit]
       band3 = digit_to_colour[multiplier]
       print("Your resistor is being drawn in turtle...")
       t = turtle.Turtle()
       t.speed(3)
       t.hideturtle()
       screen = turtle.Screen()
       screen.title("Resistor visualiser")
       screen.setup(width=800, height = 600, startx = 420, starty=90)
       screen.bgcolor("lightgrey")
       t.pencolor("grey")
       t.pensize(30)
       t.backward(200)
       t.forward(400)
       t.backward(200)
       t.pensize(70)
       t.pencolor("lightblue")
       t.backward(100)
       t.forward(200)
       t.backward(100)
       t.penup()
       t.backward (75)
       t.right(90)
       t.pencolor(band1)
       t.pensize(30)
       t.pendown()
       t.forward(30)
       t.backward(60)
       t.forward(30)
       t.left(90)
       t.penup()
       t.pencolor(band2)
       t.forward(50)
       t.right(90)
       t.pendown()
       t.forward(30)
       t.backward(60)
       t.forward(30)
       t.left(90)
       t.penup()
       t.pencolor(band3)
       t.forward(50)
       t.right(90)
       t.pendown()
       t.forward(30)
       t.backward(60)
       t.forward(30)
       t.left(90)
       t.penup()
       t.pencolor("gold")
       t.forward(50)
       t.right(90)
       t.pendown()
       t.forward(30)
       t.backward(60)
       t.forward(30)
       t.penup()
       t.goto(0,100)
       t.pendown()
       t.pencolor("black")
       t.write(f"{value}\u2126",align= "center", font = ("Arial",50,"bold"))
       t.penup()
       turtle.done()
       print("Your resistor colours are:")
       time.sleep(0.2)
       band_a = band1.upper()
       band_b = band2.upper()
       band_c = band3.upper()
       print("",band_a, band_b, band_c, "GOLD")

       time.sleep(20)
       print("Code will restart in 5")
       time.sleep(1)
       print("Code will restart in 4")
       time.sleep(1)
       print("Code will restart in 3")
       time.sleep(1)
       print("Code will restart in 2")
       time.sleep(1)
       print("Code will restart in 1")
       time.sleep(1)

    elif mode != "1" or mode != "2" :
       print("You have entered an incorrect value")
if x > 1:
   print(" ")
   x = x - 1 
