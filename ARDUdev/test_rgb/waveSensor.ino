int wavesensor(int num){
  long duration, distance;                   // 각 변수를 선언합니다.
  if (num == 0) { // 물건이 있나 없나 체크
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
    // delay(1000);
    if (distance >= 30 || distance <= 0)       // 거리가 30cm가 넘으면
      {
        Serial.println("nothing");   // 물건이 없음
        return 0;
      }
    // 그렇지 않고 물건이 있다면
    Serial.print(distance);                         // distance를 시리얼 모니터에 출력합니다.
    Serial.println(" cm");                           // cm를 출력하고 줄을 넘깁니다.
    return 1;
    // distance가 10이면 10 cm로 출력됩니다.
    }
  else if (num == 1) {
    setColor(255, 0, 0); // red
    delay(1000);
    
    digitalWrite(trigPinCan, LOW);                 // trigPin에 LOW를 출력하고
    delayMicroseconds(2);                    // 2 마이크로초가 지나면
    digitalWrite(trigPinCan, HIGH);                // trigPin에 HIGH를 출력합니다.
    delayMicroseconds(100);                  // trigPin을 10마이크로초 동안 기다렸다가
    digitalWrite(trigPinCan, LOW);                // trigPin에 LOW를 출력합니다.
    duration = pulseIn(echoPinCan, HIGH);   // echoPin핀에서 펄스값을 받아옵니다.
  /*
          trigPin핀에서 초음파를 발사하였고 그 초음파가 다시 돌아 올 때까지 기다립니다. 
          만약 벽이나 장애물에 닿아서 다시 echoPin으로 돌아왔다면 그동안의 시간을 duration에 저장합니다.
      */ 
    distance = (duration * 17) / 1000;          //  duration을 연산하여 센싱한 거리값을 distance에 저장합니다.
    // delay(1000);
    if (distance >= 5)       // 거리가 5cm가 넘으면
      {
        Serial.println("great");   // 쓰레기통 여유 있음
      }
    else                                                    // 거리가 5보다 작으면
      {
        Serial.print(distance);                         // distance를 시리얼 모니터에 출력합니다.
        Serial.println(" cm");                           // cm를 출력하고 줄을 넘깁니다.
        
        // setColor(255, 0, 0); // red
        // delay(300);
        setColor(0, 0, 0); // off
        delay(300);
        setColor(255, 0, 0); // red
        delay(300);
        setColor(0, 0, 0); // off
        delay(300);
        setColor(255, 0, 0); // red
        delay(300);
        setColor(0, 0, 0); // off
        delay(300);
        setColor(255, 0, 0); // red
        delay(300);
        setColor(0, 0, 0); // off
        delay(300);
        setColor(255, 0, 0); // red
        delay(300);
        setColor(0, 0, 0); // off
        delay(300);
        setColor(255, 0, 0); // red
        delay(300);
        setColor(0, 0, 0); // off
        // 통이 가득차면 3초 깜빡이고 리턴
        return 1;
        // distance가 10이면 10 cm로 출력됩니다.
      }
    setColor(0, 0, 0); // off
    delay(1000);
    Serial.println("false");
    return 0;
  }
  else if (num == 2) {
    setColor(0, 255, 0); // green
    delay(1000);
    
    digitalWrite(trigPinPaper, LOW);                 // trigPin에 LOW를 출력하고
    delayMicroseconds(2);                    // 2 마이크로초가 지나면
    digitalWrite(trigPinPaper, HIGH);                // trigPin에 HIGH를 출력합니다.
    delayMicroseconds(100);                  // trigPin을 10마이크로초 동안 기다렸다가
    digitalWrite(trigPinPaper, LOW);                // trigPin에 LOW를 출력합니다.
    duration = pulseIn(echoPinPaper, HIGH);   // echoPin핀에서 펄스값을 받아옵니다.
  /*
          trigPin핀에서 초음파를 발사하였고 그 초음파가 다시 돌아 올 때까지 기다립니다. 
          만약 벽이나 장애물에 닿아서 다시 echoPin으로 돌아왔다면 그동안의 시간을 duration에 저장합니다.
      */ 
    distance = (duration * 17) / 1000;          //  duration을 연산하여 센싱한 거리값을 distance에 저장합니다.
    // delay(1000);
    if (distance >= 5)       // 거리가 5cm가 넘으면
      {
        Serial.println("great");   // 쓰레기통 여유 있음
      }
    else                                                    // 거리가 5보다 작으면
      {
        Serial.print(distance);                         // distance를 시리얼 모니터에 출력합니다.
        Serial.println(" cm");                           // cm를 출력하고 줄을 넘깁니다.
        
        setColor(0, 0, 0); // off
        delay(300);
        setColor(0, 255, 0); // green
        delay(300);
        setColor(0, 0, 0); // off
        delay(300);
        setColor(0, 255, 0); // green
        delay(300);
        setColor(0, 0, 0); // off
        delay(300);
        setColor(0, 255, 0); // green
        delay(300);
        setColor(0, 0, 0); // off
        delay(300);
        setColor(0, 255, 0); // green
        delay(300);
        setColor(0, 0, 0); // off
        delay(300);
        setColor(0, 255, 0); // green
        delay(300);
        setColor(0, 0, 0); // off
        // 통이 가득차면 3초 깜빡이고 리턴
        return 1;
        // distance가 10이면 10 cm로 출력됩니다.
      }
    setColor(0, 0, 0); // off
    delay(1000);
    Serial.println("false");
    return 0;
  }
  else if (num == 3) {
    setColor(0, 0, 255); // blue
    delay(1000);
    
    digitalWrite(trigPinPlastic, LOW);                 // trigPin에 LOW를 출력하고
    delayMicroseconds(2);                    // 2 마이크로초가 지나면
    digitalWrite(trigPinPlastic, HIGH);                // trigPin에 HIGH를 출력합니다.
    delayMicroseconds(100);                  // trigPin을 10마이크로초 동안 기다렸다가
    digitalWrite(trigPinPlastic, LOW);                // trigPin에 LOW를 출력합니다.
    duration = pulseIn(echoPinPlastic, HIGH);   // echoPin핀에서 펄스값을 받아옵니다.
  /*
          trigPin핀에서 초음파를 발사하였고 그 초음파가 다시 돌아 올 때까지 기다립니다. 
          만약 벽이나 장애물에 닿아서 다시 echoPin으로 돌아왔다면 그동안의 시간을 duration에 저장합니다.
      */ 
    distance = (duration * 17) / 1000;          //  duration을 연산하여 센싱한 거리값을 distance에 저장합니다.
    // delay(1000);
    if (distance >= 5)       // 거리가 5cm가 넘으면
      {
        Serial.println("great");   // 쓰레기통 여유 있음
      }
    else                                                    // 거리가 5보다 작으면
      {
        Serial.print(distance);                         // distance를 시리얼 모니터에 출력합니다.
        Serial.println(" cm");                           // cm를 출력하고 줄을 넘깁니다.
        
        setColor(0, 0, 255); // blue
        delay(300);
        setColor(0, 0, 0); // off
        setColor(0, 0, 255); // blue
        delay(300);
        setColor(0, 0, 0); // off
        setColor(0, 0, 255); // blue
        delay(300);
        setColor(0, 0, 0); // off
        setColor(0, 0, 255); // blue
        delay(300);
        setColor(0, 0, 0); // off
        setColor(0, 0, 255); // blue
        delay(300);
        setColor(0, 0, 0); // off
        // 통이 가득차면 일단 1.5초 깜빡이고 리턴
        return 1;
        // distance가 10이면 10 cm로 출력됩니다.
      }
    setColor(0, 0, 0); // off
    delay(1000);
    Serial.println("false");
    return 0;
  }
  else if (num == 4) {
    setColor(80, 0, 80); // purple
    delay(1000);
    
    digitalWrite(trigPinTrash, LOW);                 // trigPin에 LOW를 출력하고
    delayMicroseconds(2);                    // 2 마이크로초가 지나면
    digitalWrite(trigPinTrash, HIGH);                // trigPin에 HIGH를 출력합니다.
    delayMicroseconds(100);                  // trigPin을 10마이크로초 동안 기다렸다가
    digitalWrite(trigPinTrash, LOW);                // trigPin에 LOW를 출력합니다.
    duration = pulseIn(echoPinTrash, HIGH);   // echoPin핀에서 펄스값을 받아옵니다.
  /*
          trigPin핀에서 초음파를 발사하였고 그 초음파가 다시 돌아 올 때까지 기다립니다. 
          만약 벽이나 장애물에 닿아서 다시 echoPin으로 돌아왔다면 그동안의 시간을 duration에 저장합니다.
      */ 
    distance = (duration * 17) / 1000;          //  duration을 연산하여 센싱한 거리값을 distance에 저장합니다.
    // delay(1000);
    if (distance >= 5)       // 거리가 5cm가 넘으면
      {
        Serial.println("great");   // 쓰레기통 여유 있음
      }
    else                                                    // 거리가 5보다 작으면
      {
        Serial.print(distance);                         // distance를 시리얼 모니터에 출력합니다.
        Serial.println(" cm");                           // cm를 출력하고 줄을 넘깁니다.
        
        setColor(80, 0, 80); // purple
        delay(300);
        setColor(0, 0, 0); // off
        setColor(80, 0, 80); // purple
        delay(300);
        setColor(0, 0, 0); // off
        setColor(80, 0, 80); // purple
        delay(300);
        setColor(0, 0, 0); // off
        setColor(80, 0, 80); // purple
        delay(300);
        setColor(0, 0, 0); // off
        setColor(80, 0, 80); // purple
        delay(300);
        setColor(0, 0, 0); // off
        // 통이 가득차면 일단 1.5초 깜빡이고 리턴
        return 1;
        // distance가 10이면 10 cm로 출력됩니다.
      }
    setColor(0, 0, 0); // off
    delay(1000);
    Serial.println("false");
    return 0;
  }
}