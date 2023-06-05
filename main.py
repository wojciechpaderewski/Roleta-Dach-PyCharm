from machine import Pin
from servo import move_forward, move_backward, stop

up_button = Pin(20, Pin.IN, Pin.PULL_DOWN)
down_button = Pin(21, Pin.IN, Pin.PULL_DOWN)
mode_button = Pin(22, Pin.IN, Pin.PULL_DOWN)

hommed = False
endstop = Pin(1, Pin.IN, Pin.PULL_UP)

def endstop_reached(p):
    print("Endstop reached")
    global hommed
    hommed = True
    
endstop.irq(trigger=Pin.IRQ_FALLING, handler=endstop_reached)

while True:
    if hommed:
        # stop()
        if endstop.value():
            hommed = False
            print("Endstop released")
    else: 
        if up_button.value():
            print("Up button pressed")
            move_forward()
        elif down_button.value():
            print("Down button pressed")
            move_backward()
        elif mode_button.value():
            print("Mode button pressed")
        else:
            stop()
            pass
