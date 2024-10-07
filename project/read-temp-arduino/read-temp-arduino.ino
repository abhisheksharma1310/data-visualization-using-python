#include <DHT.h>
 
#define DHTPIN 2     // DHT sensor pin
#define DHTTYPE DHT11 // DHT11 or DHT22
#define LEDPIN 13    // LED pin
 
DHT dht(DHTPIN, DHTTYPE);
String command = "";
 
void setup() {
    Serial.begin(9600); // Start serial communication
    dht.begin();        // Initialize DHT sensor
    pinMode(LEDPIN, OUTPUT);
    digitalWrite(LEDPIN, LOW); // Turn LED off initially
}
 
void loop() {
    if (Serial.available()) {
        command = Serial.readStringUntil('\n'); // Read command from serial
        if (command == "LED_ON") {
            digitalWrite(LEDPIN, HIGH); // Turn LED on
            Serial.println("LED is ON");
        } else if (command == "LED_OFF") {
            digitalWrite(LEDPIN, LOW); // Turn LED off
            Serial.println("LED is OFF");
        } else if (command == "READ_TEMP") {
            float temp = dht.readTemperature(); // Read temperature
            Serial.println("Temperature: " + String(temp) + "C");
        }
    }
    delay(500); // Wait before next command
}