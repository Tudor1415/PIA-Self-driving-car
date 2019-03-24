 #define trigPin 10
 #define echoPin 13
 #define ledOne 12

 float duration, distance;

 void setup() {
     Serial.begin (9600);
     pinMode(trigPin, OUTPUT);
     pinMode(echoPin, INPUT);

 
 }

 void loop(){

     digitalWrite(trigPin, LOW);
     delayMicroseconds(2);
     digitalWrite(trigPin, HIGH);
     delayMicroseconds(10);
     digitalWrite(trigPin, LOW);

     duration = pulseIn(echoPin, HIGH);

     distance = (duration/2)*0.0343;

     Serial.print("Distance =");
     if(distance >= 400 || distance <= 2){
       Serial.println("Out of range");
     }
     else{
       Serial.print(distance);
       Serial.println("cm");
//       delay(500);
     }
     if(distance < 20){
       digitalWrite(ledOne, HIGH);   
     }
     else{
       digitalWrite(ledOne, LOW);
     }
   
 //    delay(500);
 }

// Second method
