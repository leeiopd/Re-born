String sig;
char Ard1[5]={0};
char Ard2[5]={0};
char check[1];
int value_1=0;
int value_2=0;


void setup()
{
  Serial.begin(9600);
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);
}

void loop()
{ 
  /* 문자열로 저장*/
  while(Serial.available()) 
   {
     char wait = Serial.read();
     sig.concat(wait);
   } 
  
    /* 입력 문자열 슬라이싱 */
    sig.substring(0,1).toCharArray(check,2);

    if(check[0] == 'Q')
      {
      if (sig.length()==9)
        {
          sig.substring(1,5).toCharArray(Ard1,5);
          sig.substring(5,9).toCharArray(Ard2,5);
          value_1 = atoi(Ard1);
          value_2 = atoi(Ard2);
          sig = "";
        }
       else if (sig.length()>9)
        {sig = "";}
       }
     else if (check[0] != 'Q')
      {sig = "";}

     /* 수신 확인*/
    if(value_1 == 1111 && value_2 == 5678)
      {
        Serial.println(value_1);
        digitalWrite(A0, 255);
        digitalWrite(A1, 0);
        digitalWrite(A2, 0);
      }
    else {
        digitalWrite(A0, 0);
        digitalWrite(A1, 0);
        digitalWrite(A2, 0);
    }
}
