

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  float dataRead = analogRead(A0);
  dataRead = (dataRead/1024.0)*5;
  String dataToSend = String(dataRead);
  Serial.println(dataToSend);
  delay(300);
}
