#include <AFMotor.h>

AF_DCMotor motor(4); //motor kiri

AF_DCMotor motor2(3); //motor kanan

unsigned long previousMillis = 0; 
int set_kecepatan = 220;
float Kp = 0.5;
const long interval = 1000;  
void setup() {
  Serial.begin(115200);           // set up Serial library at 9600 bps
  Serial.println("Motor test!");
  motor.run(RELEASE);
  motor2.run(RELEASE);
  // turn on motor
//  motor.setSpeed(255);
//  motor2.setSpeed(255); 
  
}

void loop() {
  int data_1m;
  int data_2m;
  int set_point_sensor = 0;
  int pv;
  int Error;
  float P;
  if (Serial.available()) 
  {
    unsigned long currentMillis = millis();
    String data = Serial.readStringUntil('\n');
    int data_in = data.toInt();
    if (data_in == 0 )
    {
      data_1m = 255;
      data_2m = 255;
    }
    else if (data_in > 0)
    {
      pv = -30;
      Error = set_point_sensor - pv;
      P = Kp * Error;
      data_1m = set_kecepatan + P;
      data_2m = set_kecepatan - P;
    }
    else if (data_in < 0)
    {
      pv = 30;
      Error = set_point_sensor - pv;
      P = Kp * Error;
      data_1m = set_kecepatan + P;
      data_2m = set_kecepatan - P;      
    }   
    
    motor.setSpeed(data_1m);
    motor2.setSpeed(data_2m);
    
    Serial.print("Motor ki Speed: ");
    Serial.print(data_1m);
    Serial.print("=====");
    Serial.print("Motor ka Speed: ");
    Serial.println(data_2m);
    
    motor.run(FORWARD);
    motor2.run(FORWARD);
    delay(100);
  }
  else
  {
    motor.run(RELEASE);
    motor2.run(RELEASE);
    delay(1);    
  }
  
  
  
}

//    String data_1 = data.substring(0, data.indexOf("#"));
//    String data_2 = data.substring(data.indexOf("#")+1);
//    int data_1m = data_1.toInt();
//    int data_2m = data_2.toInt();
