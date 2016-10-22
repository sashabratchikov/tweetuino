// схема https://rm-content.s3.amazonaws.com/57024268467568d777fa4a53/623356/upload-b05cc610-9175-11e6-85c6-95b0dea6d9af.png

#define BUTTON_PIN 3
#define LED_PIN 13

boolean buttonWasUp = true;
boolean ledEnabled = false;

void setup()
{
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop()
{
  boolean buttonIsUp = digitalRead(BUTTON_PIN);
 
  if (buttonWasUp && !buttonIsUp) {
    delay(10);
    buttonIsUp = digitalRead(BUTTON_PIN);
    if (!buttonIsUp) {
      Serial.write('1');
      ledEnabled = !ledEnabled;
      digitalWrite(LED_PIN, ledEnabled);
    }
  }

  buttonWasUp = buttonIsUp;
}
