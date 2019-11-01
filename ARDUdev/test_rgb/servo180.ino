void servomotor(int val){  
  int backUpH = posH;
  int backUpV = posV;
  switch (val) {
    case 1:
      posH += 90;
      Serial.println("+90");    
      break;
    case 2:
      posH -= 90;
      Serial.println("-90");
      break;
    case 3:
      posV -= 90;
      Serial.println("-90");    
      break;
    case 4:
      posV += 90;
      Serial.println("+90");
      break;
  }
  myservoH.write(posH);
  myservoV.write(posV);
  delay(600);  
  return;
}