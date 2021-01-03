



// You could use a spare Hardware Serial on boards that have it (like Mega)
#include <SoftwareSerial.h>
SoftwareSerial DebugSerial(2, 3); // RX, TX

#include <BlynkSimpleStream.h>

// Application Token which was wmailed to me. 
char auth[] = "-8PpUZQ6o7gZTvCZ-Ek8Aub7Z76j-T_U";


void setup()
{
  // Debug console
  DebugSerial.begin(9600);


  Serial.begin(9600);
  Blynk.begin(Serial, auth);
}

void loop()
{
  Blynk.run();
}
