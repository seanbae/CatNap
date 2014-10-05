#include <Servo.h> 
 
Servo myservo; // pump servo
Servo myservo2; // bleed servo
 
int pos = 0;    // variable to store the servo position 
 
void setup() 
{ 
  Serial.begin(9600);
  myservo.attach(9);  // pump servo
  myservo2.attach(10); // bleed servo
  
  pinMode(7, INPUT); // pump
  pinMode(8, INPUT); // bleed

  /*
  pos = 180;
  myservo.write(pos);
  myservo.write(pos);
  /*
  delay(10000);
  pos -= 90;
  myservo.write(pos);*/
} 

void neutral() {
  myservo.write(180);
  myservo2.write(85);
}

void inflate() {
  myservo.write(80);
  myservo2.write(85);
}

void deflate() {
  myservo.write(180);
  myservo2.write(180);
}
 
void loop() 
{ 
   
  int x = 0;
  int y = 0;
  
  x = digitalRead(13);
  y = digitalRead(12);
  Serial.print(x);
  Serial.print("|");
  Serial.print(y);
  Serial.print("\n");
  
  if (digitalRead(7) == LOW && digitalRead(8) == LOW) {
    neutral();
  } else if (digitalRead(7) == HIGH && digitalRead(8) == LOW) {
    inflate();
  } else {
    deflate();
  }
  /*
  for(pos = 0; pos < 180; pos += 10)  // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 1 degree 
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  } 
  delay(100);
  for(pos = 180; pos>=1; pos-=10)     // goes from 180 degrees to 0 degrees 
  {                                
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  } */
}
