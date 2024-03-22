#include <DHT.h>

#define DHTPIN 2
#define PIRPIN 3
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

const int photoPin = A0;
const int gasSensorPin = A1;
const int soilMoisturePin = A2;
const int flamePin = 4;
const int tiltPin = 5;

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(PIRPIN, INPUT);
  pinMode(flamePin, INPUT);
  pinMode(tiltPin, INPUT);
  Serial.print("Temperature");
  Serial.print(",");
  Serial.print("Humidity");
  Serial.print(",");
  Serial.print("Motion");
  Serial.print(",");
  Serial.print("Light Intensity");
  Serial.print(",");
  Serial.print("Fire State");
  Serial.print(",");
  Serial.print("Air Quality");
  Serial.print(",");
  Serial.print("Soil Moisture");
  Serial.print(",");
  Serial.print("Rack Stability");
  Serial.println("");
}

void loop() {
  delay(2000);
  
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  
  int pirState = digitalRead(PIRPIN);
  int photoValue = analogRead(photoPin); 
  int flameState = digitalRead(flamePin); 
  int sensorValueGas = analogRead(gasSensorPin);
  int sensorValueSoil = analogRead(soilMoisturePin);
  int tiltState = digitalRead(tiltPin);
  
  Serial.print(t);
  Serial.print(",");
  Serial.print(h);
  Serial.print(",");
  Serial.print(pirState);
  Serial.print(",");
  Serial.print(photoValue);
  Serial.print(",");
  Serial.print(flameState);
  Serial.print(",");
  Serial.print(sensorValueGas);
  Serial.print(",");
  Serial.print(map(sensorValueSoil, 0, 1023, 0, 100));
  Serial.print(",");
  Serial.println(tiltState);
}
