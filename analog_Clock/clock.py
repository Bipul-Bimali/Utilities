import turtle
import math
import time
import pygame

# Enter your  GMT value [HH:MM] in the format [HH,MM]
GMT = [0,0]


# Uncomment one  to enable or disable Alarm
Alarm = True #Alarm ON
# Alarm = False  # Alarm OFF


# Set Alarm Time HH,MM 
Alarm_time = [ 1 , 1]


# Initialize pygame mixer for playing the alarm sound
pygame.mixer.init()


# Method to undo hand drawings
def undo():
    hours.undo()
    minutes.undo()
    seconds.undo()


#Alarm configuration
def alarm(ALarm_state):
    if(ALarm_state):
        # Change file variable to set a custom alarm tone
        file = "alarm.mp3"
        # file = "C:/Users/Bipul Bimali/OneDrive/Desktop/html_trial/first_step/clock/a.mp3"
        
        #Load and play alarm sound
        pygame.mixer.music.load(file)
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()


# Method to Draw Clock 
def draw_clock():
    turtle.penup()
    turtle.goto(00 ,-45)
    turtle.pendown()
    turtle.shape()
    turtle.speed(450)
    turtle.pensize(.3)
    turtle.circle(45)
    turtle.fillcolor('white')
    turtle.filling()
    turtle.end_fill()
    turtle.penup()
    for i in range (12):
        turtle.pensize(1)
        turtle.goto(math.sin(math.pi*(i*30)/180)*45,math.cos(math.pi*(i*30)/180)*45)
        turtle.pendown()
        turtle.goto(math.sin(math.pi*(i*30)/180)*32*1.5,math.cos(math.pi*(i*30)/180)*32*1.5)
        turtle.penup()
        turtle.pensize(.3)


def display_time(hr ,min ,sec):
    speed = 10
    x_hr = math.cos(hr)
    y_hr = math.sin(hr)
    x_min = math.cos(min)
    y_min = math.sin(min)
    x_sec = math.cos(sec)
    y_sec = math.sin(sec)
    global hours
    global minutes
    global seconds
    hours.pensize(4)
    hours.pendown()
    hours.speed(speed)
    minutes.pensize(2)
    minutes.pendown()
    minutes.speed(speed)
    seconds.pensize(.15)
    seconds.pendown()
    seconds.speed(speed)
    hours.goto(y_hr*23*1.5 ,x_hr*23*1.5)
    minutes.goto(y_min*26*1.5,x_min*26*1.5)
    seconds.goto(y_sec*29*1.5,x_sec*29*1.5)    


#  change coordinates below to make window larger of smaller
turtle.setup(150 , 150)
turtle.ht()
hours = turtle.Turtle()
minutes = turtle.Turtle()
seconds = turtle.Turtle()
hours.ht()
minutes.ht()
seconds.ht()
turtle.screensize(90,120)  
draw_clock()
# turtle.hideturtle()
# turtle.up()
# turtle.seth(0)
while True:        
    Time = list(time.gmtime())        
    hr = (Time[3]+GMT[0])%12+1
    
    if GMT[0] < 0 :
        min = (Time[4]-GMT[1])%60
        if(GMT[1]>Time[4]):
            hr=hr-1
    else:
        min = (Time[4]+GMT[1])%60
    sec = Time[5]  

    h = math.pi * (hr * 30) / 180
    m = math.pi * (min * 6) / 180
    s = math.pi * (sec * 6) / 180 

    if(Alarm_time[0] == hr and Alarm_time[1] == min) :
        alarm(Alarm)    
        
    start = time.time()  # Record the start time
    display_time(h, m, s)  # Display the time
    end = time.time()  # Record the end time
        
    # Sleep for the remainder of the second
    time.sleep(max(0, 1 - (end - start)))
    undo()