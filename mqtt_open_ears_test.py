#a script to send and read data over MQTT
import paho.mqtt.client as mqtt
import config
mqtt_topic = 'test/test'
mqtt_server_ip="sensemakers-vm.dev.sda-projects.nl" #use external broker
mqttsid = 'michiel'
mqtt_user = config.oe_user
mqtt_password = config.oe_pw


def on_connect(client, userdata, flags, rc):
    print('verbonden')
    print(mqtt_user)
    client.subscribe(mqtt_topic)
def on_message(client, userdata, msg):
    print(msg.topic +" "+ str(msg.payload))
client = mqtt.Client(mqttsid)
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(mqtt_user, mqtt_password)
client.connect(mqtt_server_ip, 1883) #, 60
client.loop_forever()
client.disconnect