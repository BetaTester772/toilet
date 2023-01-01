//
// Created by 안호성 on 2022-11-02.
//

// include
#include "Arduino.h"

//set pinNumber
int Sensor = 1, Electromagnet = 2;

void setup() {
//    Set pin mode
    pinMode(Sensor, INPUT);
    pinMode(Electromagnet, OUTPUT);

//    Open serial
    Serial.begin(9600);
}

void loop() {
//    make and set Sen var with Sensor value
    int Sen = digitalRead(Sensor);

//    Set Electromagnet On/Off with Sensor value
    if (Sen == 1)
        digitalWrite(Electromagnet, HIGH);
    else
        digitalWrite(Electromagnet, LOW);

//    Delay
    delay(100);
}
