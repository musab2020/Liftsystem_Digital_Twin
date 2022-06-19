import paho.mqtt.client as paho
from paho import mqtt
import urllib.requests
import time

API="https://api.thingspeak.com/update?api_key=8DWB83IOVOABHYFC&field1=0"


# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)


# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    pass
    # print("mid: " + str(mid))
# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
# print message, useful for checking if it was successful
def on_message(client, userdata, msg):

    #print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    # Example on how to select a topic and extract the value from the topic
    if "Door_Position" in msg.topic:
        door_position = msg.payload.decode('utf8')  # This is a string

        print(f"The door is {door_position}% opened.")
        door_position = msg.payload.decode("utf-8")
        door_position= speed.replace(" ", "%20")
        door_position= speed.replace(" ", "%0A")
        urllib.request.urlopen("https://api.thingspeak.com/update?api_key=8DWB83IOVOABHYFC&field1=0{}&field1={}".format(API,door_position))
    if "Door_Status" in msg.topic:
        door_status = msg.payload.decode("utf-8")
        print("Door status: {}".format(door_status.split("Position")[0]))
        door_status = msg.payload.decode("utf-8")
        door_status= speed.replace(" ", "%20")
        door_status= speed.replace(" ", "%0A")
        urllib.request.urlopen("https://api.thingspeak.com/update?api_key=8DWB83IOVOABHYFC&field1=0{}&field2={}".format(API, door_status))
    if "State" in msg.topic:
        state = msg.payload.decode("utf-8")
        print("State: {}".format(state))
        state = msg.payload.decode("utf-8")
        state= speed.replace(" ", "%20")
        state= speed.replace(" ", "%0A")
        
        urllib.request.urlopen("https://api.thingspeak.com/update?api_key=8DWB83IOVOABHYFC&field1=0{}&field3={}".format(API, state))
    if "building/Position" in msg.topic:
        elevator_position = msg.payload.decode("utf-8")
        elevator_position = msg.payload.decode("utf-8")
        elevator_position= speed.replace(" ", "%20")
        elevator_position= speed.replace(" ", "%0A")
        print("Elevator position: {}".format(elevator_position))
        urllib.request.urlopen("https://api.thingspeak.com/update?api_key=8DWB83IOVOABHYFC&field1=0{}&field4={}".format(API, elevator_position))
    if "Speed" in msg.topic:
        speed = msg.payload.decode("utf-8")
        speed= speed.replace(" ", "%20")
        speed= speed.replace(" ", "%0A")
        print("Speed: {}".format(speed))
        urllib.request.urlopen("https://api.thingspeak.com/update?api_key=8DWB83IOVOABHYFC&field1=0{}&field5={}".format(API, speed))
    if "Queue" in msg.topic:
        Queue = msg.payload.decode("utf-8")
        print("Queue: {}".format(Queue))
        Queue = msg.payload.decode("utf-8")
        Queue= speed.replace(" ", "%20")
        Queue= speed.replace(" ", "%0A")
        urllib.request.urlopen("https://api.thingspeak.com/update?api_key=8DWB83IOVOABHYFC&field1=0{}&field6={}".format(API, Queue))

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("SotA2_Elevator", "z^!nENKNNDR4!Wj37SR3")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("33856ce158b64045a33edfdfe1bb55e8.s2.eu.hivemq.cloud", 8883)
# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish
# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("building/#", qos=1)
# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_forever()