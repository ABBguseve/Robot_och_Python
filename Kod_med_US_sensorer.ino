#include <Servo.h> // Inkluderar Servot
#include "EspMQTTClient.h" //Inkluderar Clienten till MQTT
#define echoPin 14 
#define trigPin 12 // Definerar pinnar till US sensorn
#define echoPin1 13
#define trigPin1 15
Servo My_Servo; //Ger ett namn till servot

byte eng = 5; //Motor     // Bestämmer vilka
byte Dir1 = 0; //Fram     // portar de olika 
byte Dir2 = 4; //Bak      // koponenterna ska ha

int duration;    // definerar variabler
int duration1;
int distance;
int distance1;
int count = 0;

typedef enum DriveStates {fram, hoger, vanster, stuck, fixV, fixH}; //Skaoar alla staten som behövs

DriveStates DState; 
 
void dir(int hastighet, int state){ //funktion som gör det enkelt att styra motorn
  if(state == 1){ //säger vadsom ska hända om state 1 är aktiverat
    digitalWrite(Dir1, HIGH); //Gör så att motorn backar
    digitalWrite(Dir2, LOW);
    analogWrite(eng,hastighet); //Bestämmer hastigheten
  }
   else if(state == 2){ //säger vad som ska hända om state=2
    digitalWrite(Dir1, LOW);
    digitalWrite(Dir2, HIGH);
    analogWrite(eng,hastighet);
  }
  else if(state == 3){
    digitalWrite(Dir1, LOW);
    digitalWrite(Dir2, LOW);
    analogWrite(eng,hastighet);
  } 
}

void onConnectionEstablished(); //Funktion för MQTT
EspMQTTClient client(
  "ABBIndgymIoT_2.4GHz",              // Wifi ssid
  "ValkommenHit!",                   // Wifi password
  "192.168.0.113",                  // MQTT broker ip
  1883,                            // MQTT broker port
  "jocke",                        // MQTT username
  "apa",                         // MQTT password
  "lyssnarlasse",               // Client name
  onConnectionEstablished,     // Connection established callback
  true,                       // Enable web updater
  true                       // Enable debug messages
);

void onConnectionEstablished(){} 

void US(){ //Funktion för ena US sensorn
digitalWrite(trigPin, LOW); //Resetar trigPin
delayMicroseconds(2); //Delay på 2 microsekunder
digitalWrite(trigPin, HIGH); //Sätter trigPin på HIGH så att den kan läsa av
delayMicroseconds(10); //delay på 10 microsekunder
digitalWrite(trigPin, LOW); // Stänger av så att echoPin kan läsa av värdet
duration = pulseIn(echoPin, HIGH); //Läser av värdet i microsekunder
distance= duration*0.034/2; //Gör om värdet till centimeter
}

void US1(){ //Funnktion för den andra US sensorn, fungerar på samma sätt som ovan
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);
  duration1 = pulseIn(echoPin1, HIGH);
  distance1=duration1*0.034/2;
}

void setup() {
  My_Servo.attach(2); //Säger att Servot ska ha utgång 4
  pinMode(eng, OUTPUT); //Bestämmer att motorn ska vara en output
  pinMode(Dir1, OUTPUT);
  pinMode(Dir2, OUTPUT);
  pinMode(trigPin, OUTPUT);  //Sätter trigPin till output
  pinMode(echoPin, INPUT);   //Sätter echoPin till input
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  Serial.begin(9600); //Startar serial monitor på 9600
}

void loop() {
  client.loop(); //Startar anslutningen till clienten
  Serial.print("Distance Fram: ");
  Serial.println(distance);            //Skriver ut värden i Serial monitor(9600)
  Serial.print("Distance Vänster:");
  Serial.println(distance1);
  US(); //Kör funktionerna till US sensorerna
  US1();
  switch(DState) { //Startar Casen
    case fram: //Definerar att det är case fram
    Serial.println("Fram");
    Serial.print("Distance Fram: ");
    Serial.println(distance);
    Serial.print("Distance Vänster:");  //Skriver ut värden i Serial monitor
    Serial.println(distance1);
    My_Servo.write(70); //Styr servot så att det står i mitten
    US(); //Kör US sensorerna igen
    US1();
    dir(400,2); //Kör funktionen för att stuyra motorn
    if (distance1 > 25){ //Denna lopp säger att om vänstersensorn int känner av någon vägg så går den till case vanster
      DState = vanster;
    }
    else if (distance < 10 && distance > 0 && distance1 < 15){ //Här säger loopen att om det finns en vägg på vänster sida och en vägg framför
      DState = hoger;                                          //så ska den köra case hoger
    }
    else if (distance < 10 && distance > 0 && distance1 < 25){ //Här är det nästan samma förhållanden men distansen till vänster måste vara
      DState = stuck;                                          //längre och då kör den case stuck
    }
    else if (distance1 > 5){ //De två nästa looparna gör så att bilen håller sig på rätt avstånd till väggen.
      DState = fixV;         //Den kommer alltid att försöka hålla samma värde.
    }
    else if (distance1 < 5){
      DState = fixH;
    }
    else{} //Om ingen av dessa påståenden är sanna så kommer "Case Fram" att köras igen.
    break; //Avslutar caset

    case hoger:
    count == 0; //Sätter variabeln count till 0 viktigt senare i koden.
    Serial.println("Höger");
    Serial.print("Distance Fram: ");
    Serial.println(distance);
    Serial.print("Distance Vänster:");
    Serial.println(distance1);
    client.publish("mess", "Backar");
    dir(400,1); //Kör motorfunmktionen igen
    delay(800); //Sätter ett delay på 800 millisekunder
    client.publish("mess", "Höger"); //Skickar ett meddelande till MQTT clientenf
    My_Servo.write(180); //Ställer servo så långt till höger som det går
    dir(400,2);
    delay(1300);
    client.publish("mess", "Kör framåt"); //Skickar ett annat meddelande ill clienten
    DState = fram; //Säger att programmet nu ska köra case frammåt
    break;

    case vanster: //Kör case vänster
    if (count == 5){ //Denna lopp säger att om variabeln "count = 5" så ska programmet köra DState hoger istället
      DState = hoger;
    }
    Serial.println("Vänster");
    Serial.print("Distance Fram: ");
    Serial.println(distance);
    Serial.print("Distance Vänster:");
    Serial.println(distance1);
    client.publish("mess", "Backar");
    dir(400,1);
    delay(800);
    client.publish("mess", "Vänster");
    My_Servo.write(0); //Sätter servot längst till vänster
    dir(400,2);
    delay(600);
    if (distance < 250){//Kollar om det finns någon vägg i närheten framför bilen
      My_Servo.write(120);
      dir(400,2);
      delay(600);
    }
    else{ //om det inte finns någon vägg så ska den fortsätta svängen
      dir(400,2);
      delay(600);
    }
    client.publish("mess", "Kör framåt");//Skickar meddelande till clienten
    My_Servo.write(70);
    delay(500);
    DState = fram;
    count += 1;//Lägger till 1 på variabeln "count"
    break;
    
    case stuck: //Detta case använde jag när jag fastnade på ett hörn med höger fram då bilen förr trodde att den åkte frammåt
    client.publish("mess", "Stuck!");
    Serial.println("IM STUCK!");
    My_Servo.write(70);
    dir(400,1);//Använder köfunktionen, kör bakåt med hastigheten 400
    delay(800);
    My_Servo.write(0);
    dir(400,2);
    delay(1000);
    My_Servo.write(180);
    delay(1050);
    client.publish("mess", "Kör frammåt");
    DState = fram;
    break;

    case fixV:
    Serial.println("Fixar vänster");
    My_Servo.write(50);
    dir(400,2);
    delay(100);//Sätter ett kort delay så att bilen bara ändrar riktning lite.
    DState = fram;
    break;

    case fixH:
    Serial.println("Fixar höger");
    My_Servo.write(130);
    dir(400,2);
    delay(100);
    DState = fram;
    break;
  }
  client.loop();//Loopar clienten så att den körs hela tiden när koden körs
}
