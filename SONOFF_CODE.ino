#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

ESP8266WebServer server(80);

const char* ssid = "switcher01";
const char* pass = "switchmeister";

int RelaisPin = 12;


void switcher() {
  if(server.arg("state") == "1") digitalWrite(RelaisPin, HIGH);
  if(server.arg("state") == "0") digitalWrite(RelaisPin, LOW);
  server.send(204,"");
}


void setup() {
  pinMode(RelaisPin, OUTPUT);
  Serial.begin(115200);
  WiFi.softAP(ssid, pass);
  server.on("/", switcher);
  server.begin();
}


void loop() {
  server.handleClient();
}
