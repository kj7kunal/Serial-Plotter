/*
 Test Serial plotter using different test scenarios
 modified on 29 Dec 2016

 by Kunal Jain
 https://github.com/kj7kunal
*/

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
Serial.println(random(10,50));
delay(50);
}
