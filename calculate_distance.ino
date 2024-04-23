#define echoPin 2 
#define trigPin 3 

long duration; // duration of sound wave travel
int distance; // distance measurement


int MeasureDistance() {
  // clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // sets the trigPin HIGH for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // reads the echoPin, so it returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  
  // calculating the distance
  distance = duration * 0.034 / 2; // speed of sound wave divided by 2
  
  return distance;
}

void setup() {
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT); 
  Serial.begin(9600);
}

void loop() {
  int distance = MeasureDistance(); // call the MeasureDistance Function
  
  // Send the distance to Python
  Serial.println(distance);
  delay(100);
}
