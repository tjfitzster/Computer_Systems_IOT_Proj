import blynklib

BLYNK_AUTH = 'S8ZOg-Xxto0CiWJGh7MUUZYdTMGl_UlY'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

# register handler for virtual pin V2(temperature) reading
@blynk.handle_event('read V2')
def read_virtual_pin_handler(pin):
    temp=round(sense.get_temperature(),2)
    blynk.virtual_write(pin, temp)
    

# infinite loop that waits for event
while True:
    blynk.run()
