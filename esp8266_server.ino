#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "vivo123";
const char* password = "1234567890";

ESP8266WebServer server(80);

// Pin configuration for lights (GPIO5 = D1, GPIO4 = D2)

#define relay1 D1  // GPIO5
#define relay2 D2  // GPIO4
void setup() {
  Serial.begin(115200);

  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  // Configure pins
 pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  digitalWrite(relay1,HIGH);
  digitalWrite(relay2, HIGH);


  

  // Unified endpoint to receive commands from Python script
  server.on("/command", HTTP_GET, []() {
    String light1 = server.arg("light1");
    String light2 = server.arg("light2");

    if (light1 == "1") {
      digitalWrite(relay1, LOW);
     
     
    } 
    if(light1 == "0") {
      digitalWrite(relay1, HIGH);
    }

    if (light2 == "1") {
      digitalWrite(relay2, LOW);
    }
     if(light2 == "0") {
      digitalWrite(relay2, HIGH);
    }

    String response = "Light states updated: light1=" + light1 + ", light2=" + light2;
    server.send(200, "text/plain", response);
  });

  server.begin();
  Serial.println("Server started");
}

void loop() {
  server.handleClient();
}







