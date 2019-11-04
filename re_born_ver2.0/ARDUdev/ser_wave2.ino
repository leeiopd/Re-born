#include <Servo.h>

Servo myservoH;  // create servo object to control a servo
Servo myservoV;
int posH = 90;
int posV = 90;
int trigPin = 8;
int echoPin = 7;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  myservoH.attach(10);  // 서보모터를 쉴드의 10번에 연결한다.
  myservoV.attach(11);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (wavesensor()== 1) {
    Serial.println("1번모드");
    servomotor(1);
    delay(5000);
    Serial.println("2번모드");
    servomotor(2);
  }
  else if (wavesensor() == 2) {
    Serial.println("2번모드");
    servomotor(2);
    delay(5000);
    Serial.println("1번모드");
    servomotor(1);
  }
  else if (wavesensor() == 3) {
    Serial.println("3번모드");
    servomotor(3);
    delay(5000);
    Serial.println("4번모드");
    servomotor(4);
  }
  else if (wavesensor() == 4) {
    Serial.println("4번모드");
    servomotor(4);
    delay(5000);
    Serial.println("3번모드");
    servomotor(3);
  }
}

int wavesensor(){
  long duration, distance;                   // 각 변수를 선언합니다.
  digitalWrite(trigPin, LOW);                 // trigPin에 LOW를 출력하고
  delayMicroseconds(2);                    // 2 마이크로초가 지나면
  digitalWrite(trigPin, HIGH);                // trigPin에 HIGH를 출력합니다.
  delayMicroseconds(100);                  // trigPin을 10마이크로초 동안 기다렸다가
  digitalWrite(trigPin, LOW);                // trigPin에 LOW를 출력합니다.
  duration = pulseIn(echoPin, HIGH);   // echoPin핀에서 펄스값을 받아옵니다.
/*
        trigPin핀에서 초음파를 발사하였고 그 초음파가 다시 돌아 올 때까지 기다립니다. 
        만약 벽이나 장애물에 닿아서 다시 echoPin으로 돌아왔다면 그동안의 시간을 duration에 저장합니다.
    */ 
  distance = (duration * 17) / 1000;          //  duration을 연산하여 센싱한 거리값을 distance에 저장합니다.
  delay(1000);
  if (distance >= 30 || distance <= 0)       // 거리가 200cm가 넘거나 0보다 작으면
    {
      Serial.println("거리를 측정할 수 없음");   // 에러를 출력합니다.
    }
    else                                                    // 거리가 200cm가 넘지 않거나 0보다 작지 않으면
    {
      // Serial.print(distance);                         // distance를 시리얼 모니터에 출력합니다.
      // Serial.println(" cm");  
      Serial.println(3);                         // cm를 출력하고 줄을 넘깁니다.
      return 3;
      // distance가 10이면 10 cm로 출력됩니다.
    }
    Serial.println("리턴 false");
    return 0;
}


void servomotor(int val){
  Serial.println("뭐가나올까?");    
  int backUpH = posH;
  int backUpV = posV;
  switch (val) {
    case 1:
      posH += 90;
      Serial.println("+90도");    
      break;
    case 2:
      posH -= 90;
      Serial.println("-90도");
      break;
    case 3:
      posV -= 90;
      Serial.println("-90도");    
      break;
    case 4:
      posV += 90;
      Serial.println("+90도");
      break;
  }
  myservoH.write(posH);
  myservoV.write(posV);
  delay(600);  
  return;
}
