#include <Servo.h>
Servo myservo;
int servoPin = 9;
const int trigpin = 8;
const int echopin = 7;
long duration;
long distance;
void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(9600);
  myservo.attach(servoPin);
  pinMode(trigpin,OUTPUT);
  pinMode(echopin,INPUT);
  myservo.writeMicroseconds(700);                  // Initial setting for servo motor for its angle
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(1000);
  for(int i=0;i<=180;i++){
    digitalWrite(trigpin,HIGH);
    delayMicroseconds(10);
    digitalWrite(trigpin,LOW);
    duration=pulseIn(echopin,HIGH);
    distance = duration*0.034/2;                     // 0.034 for speed of wave
    myservo.write(i);                                // roatation of sevro motor
    Serial.println(String(i)+" "+String(distance)); 
    delay(500);
  }
  delay(5000);
  
}
