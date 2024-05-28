from machine import Pin
from time import sleep
import dht 

#sensor = dht.DHT22(Pin(14))
sensor = dht.DHT11(Pin(23))
led=Pin(14,Pin.OUT)
while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    if  70<=hum<=80:
        led.on()
    elif hum <70:
        led.off()
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
  except OSError as e:
    print('Failed to read sensor.')
