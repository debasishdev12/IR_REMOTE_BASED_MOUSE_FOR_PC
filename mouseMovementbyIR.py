import serial
import time
from pymouse import PyMouse
import pyautogui

ser = serial.Serial('COM5',115200,timeout=0)
m = PyMouse()
pos = m.position()

while 1:
    var = ser.read(1)
   
    if var == "F":
        m.move(pos[0],pos[1]-15)
        pos = m.position()
        
    elif var == "D":
        m.move(pos[0],pos[1]+15)
        pos = m.position()

    elif var == "R":
        m.move(pos[0]+15,pos[1])
        pos = m.position()
        
    elif var == "L":
        m.move(pos[0]-15,pos[1])
        pos = m.position()

    elif var == "3":
        m.click(pos[0],pos[1],button=1)
        time.sleep(.1)
        m.position()
        
    elif var == "1":
        m.press(pos[0],pos[1],1)
        m.position()
        time.sleep(.2)

    elif var == "2":
        m.click(pos[0],pos[1],button=2)
        m.position()

    elif var == "q":
        m.move(0,0)
        pos = m.position()
        
    elif var == "p":
        m.move(1366,0)
        pos = m.position()
        
    elif var == "t":
        m.move(683,0)
        pos = m.position()

    elif var == "f":
        m.move(0,384)
        pos = m.position()

    elif var == "h":
        m.move(683,384)
        pos = m.position()

    elif var == "l":
        m.move(1366,384)
        pos = m.position()

    elif var == "z":
        m.move(0,768)
        pos = m.position()

    elif var == "b":
        m.move(683,768)
        pos = m.position()
        
    elif var == "m":
        m.move(1366,768)
        pos = m.position()

    elif var == "v":
        m.move(pos[0]-10,pos[1]-10)
        pos = m.position()

    elif var == "w":
        m.move(pos[0]+10,pos[1]+10)
        pos = m.position()
        
    elif var == "x":
        m.move(pos[0]-10,pos[1]+10)
        pos = m.position()

    elif var == "c":
        m.move(pos[0]+10,pos[1]-10)
        pos = m.position()
