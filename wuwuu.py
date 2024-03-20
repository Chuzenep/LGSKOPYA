from machine import Pin, SoftI2C
import ssd1306
from machine import Pin, ADC
from time import sleep

# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

pot = ADC(0)



while True:
    oled.fill(0)
    pot_value = pot.read()
    oled.text(str(pot_value),0,10)
    oled.show()
    print(pot_value)
    sleep(0.1)
    
    
oled.show()
