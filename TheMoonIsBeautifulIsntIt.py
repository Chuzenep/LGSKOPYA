from machine import Pin, SoftI2C
import ssd1306
from time import sleep
import dht

sensor = dht.DHT11(Pin(14))
relay=Pin(2, Pin.OUT)

i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C (oled_width, oled_height, i2c)
  

while True:
  try:
    sleep(2)
    oled.fill(0)
    oled.show()
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    tempStr = str(temp)
    humStr =  str(hum)
    temp_fStr = str(temp_f)
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
    
    if  hum>=65:
        relay.value(0)
        oled.text(tempStr, 0,10)
        oled.text(humStr, 0,20)
        oled.text(temp_fStr, 0,30)
        oled.show()
    else:
        relay.value(1)
        oled.text(tempStr, 0,10)
        oled.text(humStr, 0,20)
        oled.text(temp_fStr, 0,30)
        oled.show()
        
  except OSError as e:
    print('Failed to read sensor.')