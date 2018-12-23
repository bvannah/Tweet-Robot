#include "mbed.h"
#include <Serial.h>
#include <string>
Serial microbit(p9, p10); //tx, rx
DigitalOut redled(p21);
DigitalOut yellowled(p22);
Serial pc(USBTX, USBRX); // tx, rx
extern "C" void mbed_reset();

void lights(char x){
    if(x=='1'){
        redled=1;
        wait(.2);
        redled=0;
    }
        
    if(x=='2'){
        yellowled=1;
        wait(.2);
        yellowled=0;
    }
}

void callback(){
    char c=microbit.getc();
    pc.printf("%c", c);
    lights(c);
    mbed_reset();      
    }

int main() {
    microbit.attach(&callback);
    while(1){}
    }




