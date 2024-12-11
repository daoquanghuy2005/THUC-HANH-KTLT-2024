#include <Servo.h>
#include <SoftWire.h>  // Thư viện SoftWire để sử dụng SDA/SCL tùy chỉnh
#include <LiquidCrystal_I2C.h>

// Khởi tạo đối tượng SoftWire với các chân A1 (SDA) và A2 (SCL)
SoftWire myWire(A1, A2);  // SDA -> A1, SCL -> A2

// Khởi tạo LCD với đối tượng SoftWire
LiquidCrystal_I2C lcd(0x27, 16, 2);  // 0x27 là địa chỉ I2C mặc định

Servo servo_9;  // Tạo đối tượng servo trên chân 9
int led1 = 2;    
int led2 = 3;
int led3 = 4;
int led4 = 5;
int led5 = 6;
int led6 = 7;
int led7 = 8;
int green = 11;
int yellow = 12;
int red = 13;

void setup() {
  // Khởi tạo LCD
  lcd.begin(16, 2);
  lcd.backlight();

  // Hiển thị dòng 1 và dòng 2 ở giữa
  String line1 = "TRUONG!";
  int startCol1 = (16 - line1.length()) / 2;  
  lcd.setCursor(startCol1, 0);
  lcd.print(line1);

  String line2 = "DAI HOC VINH";
  int startCol2 = (16 - line2.length()) / 2;
  lcd.setCursor(startCol2, 1);
  lcd.print(line2);

  // Khởi tạo các chân LED
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
  pinMode(led7, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(red, OUTPUT);

  // Khởi tạo servo
  servo_9.attach(9, 500, 2500);  
}

void loop() {
  dong();
  dendo();
  chin();
  delay(1000);
  tam();
  delay(1000);
  bay();
  delay(1000);
  sau();
  delay(1000);
  nam();
  delay(1000);
  bon();
  delay(1000);
  denvang();
  ba();
  delay(1000);
  hai();
  delay(1000);
  mot();
  delay(1000);
  khong();
  delay(1000);
  denxanh();
  mo();
  chin();
  delay(1000);
  tam();
  delay(1000);
  bay();
  delay(1000);
  sau();
  delay(1000);
  nam();
  delay(1000);
  bon();
  delay(1000);
  ba();
  delay(1000);
  hai();
  delay(1000);
  mot();
  delay(1000);
  khong();
  delay(1000);
}

// Các hàm điều khiển khác không thay đổi
void dong() {
  for (int pos = 90; pos <= 180; pos++) {
    servo_9.write(pos);
    delay(10);
  }
}

void mo() {
  for (int pos = 180; pos >= 90; pos--) {
    servo_9.write(pos);
    delay(10);
  }
}

void chin() {
  digitalWrite(led1, 1);
  digitalWrite(led2, 1);
  digitalWrite(led3, 1);
  digitalWrite(led4, 1);
  digitalWrite(led5, 0);
  digitalWrite(led6, 1);
  digitalWrite(led7, 1);
  delay(1000);
}

void tam() {
  digitalWrite(led1, 1);
  digitalWrite(led2, 1);
  digitalWrite(led3, 1);
  digitalWrite(led4, 1);
  digitalWrite(led5, 1);
  digitalWrite(led6, 1);
  digitalWrite(led7, 1);
  delay(1000);
}

void bay() {
  digitalWrite(led1, 1);
  digitalWrite(led2, 1);
  digitalWrite(led3, 1);
  digitalWrite(led4, 0);
  digitalWrite(led5, 0);
  digitalWrite(led6, 0);
  digitalWrite(led7, 0);
  delay(1000);
}

void sau() {
  digitalWrite(led1, 1);
  digitalWrite(led2, 0);
  digitalWrite(led3, 1);
  digitalWrite(led4, 1);
  digitalWrite(led5, 1);
  digitalWrite(led6, 1);
  digitalWrite(led7, 1);
  delay(1000);
}

void nam() {
  digitalWrite(led1, 1);
  digitalWrite(led2, 0);
  digitalWrite(led3, 1);
  digitalWrite(led4, 1);
  digitalWrite(led5, 0);
  digitalWrite(led6, 1);
  digitalWrite(led7, 1);
  delay(1000);
}

void bon() {
  digitalWrite(led1, 0);
  digitalWrite(led2, 1);
  digitalWrite(led3, 1);
  digitalWrite(led4, 0);
  digitalWrite(led5, 0);
  digitalWrite(led6, 1);
  digitalWrite(led7, 1);
  delay(1000);
}

void ba() {
  digitalWrite(led1, 1);
  digitalWrite(led2, 1);
  digitalWrite(led3, 1);
  digitalWrite(led4, 1);
  digitalWrite(led5, 0);
  digitalWrite(led6, 0);
  digitalWrite(led7, 1);
  delay(1000);
}

void hai() {
  digitalWrite(led1, 1);
  digitalWrite(led2, 1);
  digitalWrite(led3, 0);
  digitalWrite(led4, 1);
  digitalWrite(led5, 1);
  digitalWrite(led6, 0);
  digitalWrite(led7, 1);
  delay(1000);
}

void mot() {
  digitalWrite(led1, 0);
  digitalWrite(led2, 1);
  digitalWrite(led3, 1);
  digitalWrite(led4, 0);
  digitalWrite(led5, 0);
  digitalWrite(led6, 0);
  digitalWrite(led7, 0);
  delay(1000);
}

void khong() {
  digitalWrite(led1, 1);
  digitalWrite(led2, 1);
  digitalWrite(led3, 1);
  digitalWrite(led4, 1);
  digitalWrite(led5, 1);
  digitalWrite(led6, 1);
  digitalWrite(led7, 0);
  delay(1000);
}

void dendo() {
  digitalWrite(red, 1);
  digitalWrite(yellow, 0);
  digitalWrite(green, 0);
}

void denxanh() {
  digitalWrite(red, 0);
  digitalWrite(yellow, 0);
  digitalWrite(green, 1);
}

void denvang() {
  digitalWrite(red, 0);
  digitalWrite(yellow, 1);
  digitalWrite(green, 0);
}
