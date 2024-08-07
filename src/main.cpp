#include <Arduino.h>
#include <Servo.h>


const int echoPin = 7;
const int trigPin = 8;
const int servoPin = 9;

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
  if (distance > 400 || distance < 2) {
    distance = 9999;
  }
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
  pinMode(servoPin, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600); // debugging
  for (int i = 0; i < 5; i++) {
    flash(LED_BUILTIN, 100);
  }
}

void loop() {
  Serial.println(getDistance());
  flash(LED_BUILTIN, 100);
}
