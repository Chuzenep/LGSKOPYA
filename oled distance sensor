# Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/
from hcsr04 import HCSR04
from time import sleep


from machine import Pin, SoftI2C
import ssd1306
from time import sleep



# ESP8266 Pin assignment
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.show()
# ESP8266
sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

    
while True:
    distance = sensor.distance_cm()
    oled.fill(0)
    oled.text(str(distance),0,10)
    oled.show()
    sleep(0.1)
    
