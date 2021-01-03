import blynklib
import serial

BLYNK_AUTH = 'S8ZOg-Xxto0CiWJGh7MUUZYdTMGl_UlY'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

# register handler for virtual pin V2(temperature) reading
@blynk.handle_event('read V2')
def read_virtual_pin_handler(pin):
    moisture=round(moisturevalue)
    print('V2 Read: ' + str(moisturevalue))  # print temp to console
    blynk.virtual_write(pin, moisturevalue)

if __name__ == '__main__':
   ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
   ser.flush()
   while True:
        if ser.in_waiting > 0:
            moisturemessage = ser.readline().decode('utf-8').rstrip()
            moisturevalue = moisturemessage[15:]
            print(moisturevalue)
          
          
  
