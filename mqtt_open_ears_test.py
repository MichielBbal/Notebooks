import paho.mqtt.client as mqtt
mqtt_topic = 'open_ears_test'
mqtt_server_ip="mqtt.eclipseprojects.io" #use external broker
mqttsid = 'servalhr'

def on_connect(client, userdata, flags, rc):
    print('verbonden')
    client.subscribe(mqtt_topic)
def on_message(client, userdata, msg):
    print(msg.topic +" "+ str(msg.payload))
client = mqtt.Client(mqttsid)
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_server_ip, 1883, 60)
client.loop_forever()
client.disconnect