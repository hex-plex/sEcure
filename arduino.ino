
#include <AddicoreRFID.h>
#include <SPI.h>

#define	uchar	unsigned char
#define	uint	unsigned int

uchar fifobytes;
uchar fifoValue;

AddicoreRFID myRFID;
const int chipSelectPin = 10;
const int NRSTPD = 5;

#define MAX_LEN 16

void setup() {
   Serial.begin(9600);


  SPI.begin();

  pinMode(chipSelectPin,OUTPUT);
    digitalWrite(chipSelectPin, LOW);
  pinMode(NRSTPD,OUTPUT);
    digitalWrite(NRSTPD, HIGH);

  myRFID.AddicoreRFID_Init();
}

void loop()
{
  	uchar i, tmp, checksum1;
	uchar status;
        uchar str[MAX_LEN];
        uchar RC_size;
        uchar blockAddr;
        String mynum = "";

        str[1] = 0x4400;


	status = myRFID.AddicoreRFID_Anticoll(str);
	if (status == MI_OK)
	{
          Serial.print("!!");
    	    Serial.print(str[0]);
    	    Serial.print(str[1]);
    	    Serial.print(str[2]);
    	    Serial.println(str[3]);
          Serial.println();
          delay(1000);
	}

        myRFID.AddicoreRFID_Halt();

}
