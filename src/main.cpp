#include <Arduino.h>

const int echoPin = 7;
const int trigPin = 8;
const int buttonPin = 2;

int distance;
long duration; // using long to ensure precision

int getDistance() {

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.0343 / 2; // speed of sound in air is 0.0343 cm/um
  return distance;
}

void flash(int pin, int delayTime = 1000) {
  digitalWrite(pin, HIGH);
  delay(delayTime);
  digitalWrite(pin, LOW);
  delay(delayTime);
}

void setup() {
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buttonPin, INPUT_PULLUP);

  Serial.begin(1200); // debugging

}

void loop() {
  if (distance < 50) {
    flash(LED_BUILTIN, distance*10);
    digitalWrite(LED_BUILTIN, LOW);
  }
  Serial.println(getDistance());
}
