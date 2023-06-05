import network
import time
from machine import Pin
from umqtt.simple import MQTTClient

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Moria","Barahir6")
time.sleep(5)
print(wlan.isconnected())

sensor = Pin(16, Pin.IN)

mqtt_server = 'broker.hivemq.com'
client_id = 'bigles'
topic_pub = b'TomsHardware'
topic_msg = b'Movement Detected'

def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()

try:
    client = mqtt_connect()
except OSError as e:
    reconnect()
while True:
    if sensor.value() == 0:
        client.publish(topic_pub, topic_msg)
        time.sleep(3)
    else:
        pass

# from machine import Pin
# from servo import move_forward, move_backward, stop
#
# up_button = Pin(20, Pin.IN, Pin.PULL_DOWN)
# down_button = Pin(21, Pin.IN, Pin.PULL_DOWN)
# mode_button = Pin(22, Pin.IN, Pin.PULL_DOWN)
#
# hommed = False
# endstop = Pin(1, Pin.IN, Pin.PULL_UP)

# def endstop_reached(p):
#     print("Endstop reached")
#     global hommed
#     hommed = True
#
# endstop.irq(trigger=Pin.IRQ_FALLING, handler=endstop_reached)
#
# while True:
#     if hommed:
#         # stop()
#         if endstop.value():
#             hommed = False
#             print("Endstop released")
#     else:
#         if up_button.value():
#             print("Up button pressed")
#             move_forward()
#         elif down_button.value():
#             print("Down button pressed")
#             move_backward()
#         elif mode_button.value():
#             print("Mode button pressed")
#         else:
#             stop()
#             pass
