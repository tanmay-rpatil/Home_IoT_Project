#include <EEPROM.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include "DHT.h"

DHT dht;
char tarr[10];
char harr[10];
// Connect to the WiFi
const char* ssid = "YourSSID"; //Replace YourSSID with your ssid
const char* password = "YourPass"; //Replace YourPass with your wifi password
const char* mqtt_server = "YourLocalIp"; // local IP for test broker is setup
 
WiFiClient espClient;
PubSubClient client(espClient);
 
void reconnect() {
 // Loop until we're reconnected
 while (!client.connected()) {
 Serial.print("Attempting MQTT connection...");
 // Attempt to connect
 if (client.connect("ESP8266 Client")) {
  Serial.println("connected");
  // ... and publish to topic
  client.publish("iot/temp","HI");
 } 
 else {
  Serial.print("failed, rc=");
  Serial.print(client.state());
  Serial.println(" try again in 5 seconds");
  // Wait 5 seconds before retrying
  delay(5000);
  }
 }
 
}
 
void setup()
{
  Serial.begin(9600);
  // Connect to WiFi
  delay(500);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) 
  {
     delay(500);
     Serial.print("*");
  }
  dht.setup(D1);   /* D1 is used for data communication */
  Serial.println("");
  Serial.println("WiFi connection Successful");
  Serial.print("The IP Address of ESP8266 Module is: ");
  Serial.print(WiFi.localIP());// Print the IP address
 
 client.setServer(mqtt_server, 1883);
 
 pinMode(LED_BUILTIN, OUTPUT);     // Initialize the LED_BUILTIN pin as an output
}
 
void loop()
{
 if (!client.connected()) {
  reconnect();
 }
 delay(2000);
 float temperature = dht.getTemperature();
 float humidity = dht.getHumidity();
 snprintf(tarr, sizeof(tarr), "%f", temperature );
 snprintf(harr, sizeof(harr), "%f", humidity );
 Serial.println(temperature, 1);
 client.publish("iot/temp",tarr);
 client.publish("iot/hum",harr);
 client.loop();
}
