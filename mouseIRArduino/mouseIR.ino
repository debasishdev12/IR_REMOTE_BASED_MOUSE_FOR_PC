#include <IRremote.h>
int RECV_PIN = 11;
IRrecv irrecv(RECV_PIN);
decode_results results;


void setup()
{
  Serial.begin(115200);
  irrecv.enableIRIn();
}


void loop() {
  if (irrecv.decode(&results)) 
  {
    
    switch(results.value)
    {
      case 2080:
        Serial.println("F");
        break;
      case 32:
        Serial.println("F");
        break;
      case 2081:
        Serial.println("D");
        break;
      case 33:
        Serial.println("D");
        break;
      case 2065:
        Serial.println("L");
        break;
      case 17:
        Serial.println("L");
        break;
      case 2064:
        Serial.println("R");
        break;
      case 16:
        Serial.println("R");
        break;
      case 2104:
        Serial.println("x");      //diagonal left-down
        break;
      case 56:
        Serial.println("x");
        break;
      
      case 10:
        Serial.println("1");    //double click left
        break;
      case 2058:
        Serial.println("1");
        break;
        
      case 0:
        Serial.println("3");    //middle click
        break;
      case 2048:
        Serial.println("3");
        break;
        
      case 14:
        Serial.println("2");    //right click
        break;
      case 2062:
        Serial.println("2");
        break;
        
      case 2086:
        Serial.println("w");     //diagonal right-down
        break;
      case 38:
        Serial.println("w");
        break;
     
      case 41:
        Serial.println("v");     //diagonal left-up
        break;
      case 2089:
        Serial.println("v");
        break;
        
      case 34:
        Serial.println("c");     //diagonal right-up
        break;
      case 2082:
        Serial.println("c");
        break;
        
      case 1:
        Serial.println("q");    //(0,0) co_ordinate
        break;
      case 2049:
        Serial.println("q");    //(0,0) co_ordinate
        break;
      case 3:
        Serial.println("p");    //(1366,0) co_ordinate
        break;
      case 2051:
        Serial.println("p");    //(1366,0) co_ordinate
        break;
      case 2:
        Serial.println("t");    //(683,0) co_ordinate
        break;
      case 2050:
        Serial.println("t");    //(683,0) co_ordinate
        break;
      case 4:
        Serial.println("f");    //(0,384) co_ordinate
        break;
      case 2052:
        Serial.println("f");    //(0,384) co_ordinate
        break;
      case 5:
        Serial.println("h");    //(683,384) co_ordinate
        break;
      case 2053:
        Serial.println("h");    //(683,384) co_ordinate
        break;
      case 6:
        Serial.println("l");    //(1366,384) co_ordinate
        break;
      case 2054:
        Serial.println("l");    //(1366,384) co_ordinate
        break;
      case 7:
        Serial.println("z");    //(0,768) co_ordinate
        break;
      case 2055:
        Serial.println("z");    //(0,768) co_ordinate
        break;
      case 8:
        Serial.println("b");    //(683,768) co_ordinate
        break;
      case 2056:
        Serial.println("b");    //(683,768) co_ordinate
        break;
      case 9:
        Serial.println("m");    //(1366,768) co_ordinate
        break;
      case 2057:
        Serial.println("m");    //(1366,768) co_ordinate
        break;
      
      default:
        break;
    }
    irrecv.resume(); // Receive the next value
    
  }
}
