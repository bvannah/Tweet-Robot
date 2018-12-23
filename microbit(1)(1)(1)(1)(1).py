from microbit import *
from struct import *
import time

display.show(Image.HAPPY)
uart.init(tx=pin0, rx=pin1)
accelold = [accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()] #is this an int or float?
accelnew = accelold
threshold =300
standcount=0
timecount=0
while(1):
    timecount+=1
    if(timecount >7000):
        display.scroll("Follow me on twitter @LPC17681", delay=100)
        timecount=0
        display.show(Image.HAPPY)
    if(button_a.is_pressed() | button_b.is_pressed()):
        uart.write('4'+'/n/r') #4=button, do I need /n/r?
        display.scroll("!", delay=30)
        display.show(Image.SAD)
        standcount=0
        sleep(3)
        continue
    accelold = accelnew
    accelnew = [accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()]
    changedaxes=0
    if(abs(accelnew[0]-accelold[0]) > threshold): 
        changedaxes+=1
    if(abs(accelnew[1]-accelold[1]) > threshold): 
        changedaxes+=1
    if(abs(accelnew[2]-accelold[2]) > threshold): 
        changedaxes+=1
    if(abs(accelnew[0]-accelold[0]) > threshold*2): 
        changedaxes+=1
    if(abs(accelnew[1]-accelold[1]) > threshold*2): 
        changedaxes+=1
    if(abs(accelnew[2]-accelold[2]) > threshold*2): 
        changedaxes+=1
    if(changedaxes >= 4):
        uart.write('1'+'/n/r') #1=shake
        standcount=0
        display.scroll("!", delay=30)
        display.show(Image.CONFUSED)
        time.sleep(3)
        continue
    if(changedaxes >= 1):
        uart.write('2'+'/n/r') #2=slide
        display.scroll("!", delay=30)
        display.show(Image.SILLY)
        time.sleep(3)
        standcount=0
        continue
    if(abs(accelerometer.get_y()-1024) < 30 ):
        standcount+=1
        if(standcount>600): 
            uart.write('3'+'/n/r') #3=stand
            standcount=-999999
            display.scroll("!", delay=30)
            display.show(Image.HAPPY)
            sleep(3)
            continue
    sleep(.1)