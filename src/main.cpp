#include <Arduino.h>
#include <Servo.h>
#include <SoftwareSerial.h>

SoftwareSerial inputSerial(10, 11); // RX, TX
SoftwareSerial outputSerial(12, 13);   // RX, TX

const int echoPin = 7;
const int trigPin = 8;
const int servoPin = 9;

Servo servo;

int distance;
long duration; 

int angle = 90;

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

void flash(int pin, int numFlashes = 5, int delayTime = 1000) {
  for (int i = 0; i < numFlashes; i++) {
    digitalWrite(pin, HIGH);
    delay(delayTime);
    digitalWrite(pin, LOW);
    delay(delayTime);
  }
}

void setup() {
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(servoPin, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600);
  while (!Serial) {
    ; // Wait for the serial port to connect. Needed for native USB port only
  }

  Serial.println("Hardware serial ready");

  servo.attach(servoPin);
}

void loop() {
  if (Serial.available() > 0) {
    char inChar = Serial.read();
    if (inChar == '1') {
      angle = min(angle + 1, 180);
    } else if (inChar == '2') {
      angle = max(angle - 1, 0);
    } else if (inChar == '4') {
      angle = max(angle - 10, 0);
    } else if (inChar == '3') {
      angle = min(angle + 10, 180);
    }
    servo.write(angle);
  }
}
