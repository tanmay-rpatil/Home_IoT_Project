import paho.mqtt.subscribe as subscribe

msg = subscribe.simple("debug", hostname="tanmay-g3")
print("%s %s" % (msg.topic, msg.payload))