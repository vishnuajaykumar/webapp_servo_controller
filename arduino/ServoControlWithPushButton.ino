#include <Servo.h>

Servo myServo;           
char inChar;              
int button = 9;
int buttonState;

void setup() {
  Serial.begin(9600);
  myServo.attach(8);  
}

void loop() {
  
  if (Serial.available()) {
    inChar = (char)Serial.read();
  }


  if (inChar == 'H') {
    rotateServo(90);  
  } else if (inChar == 'L') {
    rotateServo(180);  
  }

  
  int newState = digitalRead(button);
  if (buttonState != newState) {
    buttonState = newState;
    if(buttonState == HIGH){
      Serial.println("light");
    }
    else{
      Serial.println("dark");
    }
  }
  delay(500);
}

void rotateServo(int angle) {
  myServo.write(angle);  
  delay(500);  
}
