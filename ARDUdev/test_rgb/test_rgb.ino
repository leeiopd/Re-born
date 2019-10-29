#include <Servo.h>

Servo myservo;
Servo myservoH;  // create servo object to control a servo
Servo myservoV;
int posH = 90;
int posV = 90;

int trigPin = 11;
int echoPin = 10;
int trigPinTrash = 9;
int echoPinTrash = 8;
int trigPinPlastic = 7;
int echoPinPlastic = 6;
int trigPinPaper = 5;
int echoPinPaper = 4;
int trigPinCan = 3;
int echoPinCan = 2;

void setup() {
    // 파이썬과 통신
    Serial.begin(9600);
    
    // 초음파 핀 선언
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    pinMode(trigPinCan, OUTPUT);
    pinMode(echoPinCan, INPUT);
    pinMode(trigPinPlastic, OUTPUT);
    pinMode(echoPinPlastic, INPUT);
    pinMode(trigPinPaper, OUTPUT);
    pinMode(echoPinPaper, INPUT);
    pinMode(trigPinTrash, OUTPUT);
    pinMode(echoPinTrash, INPUT);

    // LED 핀 선언
    pinMode(A0, OUTPUT);
    pinMode(A1, OUTPUT);
    pinMode(A2, OUTPUT);

    // 서보모터 선언
    myservo.attach(12); // 360 서보모터
    myservoH.attach(A3);  // 서보모터를 쉴드의 10번에 연결한다.
    myservoV.attach(A4);
}
 
void loop()
{
  if (wavesensor(0)) {
    // 순서는 캔 1, 페이퍼 2, 플라스틱 3, 트래쉬 4
    // 색깔은  Red ,   Green ,   Blue,   Purple
    if (wavesensor(1)){
      return;
    }
    if (wavesensor(2)){
      return;
    }
    int res = 3; // 라즈베리로 받은 값이 플라스틱일경우 가정하고
    if (res == 1) {
      Serial.println("mode 1");
      servomotor(1);
      delay(1000);
      // 위에 덮개 열어주는 함수 실행

      delay(1000);
      // 쓰레기를 360도 회전으로 쓸어준다.
      servo360();

      delay(5000);
      Serial.println("mode 2");
      servomotor(2);
    }
    else if (res == 2) {
      Serial.println("mode 2");
      servomotor(2);
      delay(1000);
      // 위에 덮개 열어주는 함수 실행

      delay(1000);
      // 쓰레기를 360도 회전으로 쓸어준다.
      servo360();
      delay(5000);
      Serial.println("mode 1");
      servomotor(1);
    }
    else if (res == 3) {
      Serial.println("mode 3");
      servomotor(3);
      delay(1000);
      // 위에 덮개 열어주는 함수 실행

      delay(1000);
      // 쓰레기를 360도 회전으로 쓸어준다.
      servo360();
      delay(5000);
      Serial.println("mode 4");
      servomotor(4);
    }
    else if (res == 4) {
      Serial.println("mode 4");
      servomotor(4);
      delay(1000);
      // 위에 덮개 열어주는 함수 실행

      delay(1000);
      // 쓰레기를 360도 회전으로 쓸어준다.
      servo360();
      delay(5000);
      Serial.println("mode 3");
      servomotor(3);
    }
  }
}



