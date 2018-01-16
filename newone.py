import serial
import time
import pyautogui as m

ser = serial.Serial('COM5',115200,timeout=0)
size = m.size()
pos = m.position()
click = False

while 1:
    var = ser.read(1)
   
    if var == "F":
        if click == False:
            m.moveTo(pos[0],pos[1]-15)
            pos = m.position()
        else:
            m.moveTo(pos[0],pos[1]-15)
            pos = m.position()
        
    elif var == "D":
        if click == False:
            m.moveTo(pos[0],pos[1]+15)
            pos = m.position()
        else:
            m.moveTo(pos[0],pos[1]+15)
            pos = m.position()
            
    elif var == "R":
        if click == False:
            m.moveTo(pos[0]+15,pos[1])
            pos = m.position()
        else:
            m.moveTo(pos[0]+15,pos[1])
            pos = m.position()

    elif var == "L":
        if click == False:
            m.moveTo(pos[0]-15,pos[1])
            pos = m.position()
        else:
            m.moveTo(pos[0]-15,pos[1])
            pos = m.position()

    elif var == "2":
        m.click(pos[0],pos[1],button='right')
        time.sleep(.1)
        m.position()
        
    elif var == "1":
        m.click(pos[0],pos[1],button='left')
        m.position()
        time.sleep(.25)

    elif var == "3":
        m.doubleClick()
        m.position()
        time.sleep(.1)

    elif var == "q":
        m.moveTo(1,1)
        pos = m.position()
        
    elif var == "p":
        m.moveTo(1366,0)
        pos = m.position()
        
    elif var == "t":
        m.moveTo(683,0)
        pos = m.position()

    elif var == "f":
        m.moveTo(0,384)
        pos = m.position()

    elif var == "h":
        m.moveTo(683,384)
        pos = m.position()

    elif var == "l":
        m.moveTo(1366,384)
        pos = m.position()

    elif var == "z":
        m.moveTo(0,768)
        pos = m.position()

    elif var == "b":
        m.moveTo(683,768)
        pos = m.position()
        
    elif var == "m":
        m.moveTo(1366,768)
        pos = m.position()

    elif var == "v":
        if click == False:
            m.moveTo(pos[0]-10,pos[1]-10)
            pos = m.position()
        else:
            m.moveTo(pos[0]-10,pos[1]-10)
            pos = m.position()

    elif var == "w":
        if click == False:
            m.moveTo(pos[0]+10,pos[1]+10)
            pos = m.position()
        else:
            m.moveTo(pos[0]+10,pos[1]+10)
            pos = m.position()
        
    elif var == "x":
        if click == False:
            m.moveTo(pos[0]-10,pos[1]+10)
            pos = m.position()
        else:
            m.moveTo(pos[0]-10,pos[1]+10)
            pos = m.position()

    elif var == "c":
        if click == False:
            m.moveTo(pos[0]+10,pos[1]-10)
            pos = m.position()
        else:
            m.moveTo(pos[0]+10,pos[1]-10)
            pos = m.position()

    elif var == "9":
        m.scroll(20)
        time.sleep(.1)
        
    elif var == "8":
        m.scroll(-20)
        time.sleep(.1)

    elif var == "7":
        click = True
        m.mouseDown(button='right')

    elif var == "6":
        click = False
        m.mouseUp(button='right',x=pos[0],y=pos[1]);

    
