import blynklib

BLYNK_AUTH = 'S8ZOg-Xxto0CiWJGh7MUUZYdTMGl_UlY'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

# register handler for virtual pin V1 write event
@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    

# infinite loop that waits for event
while True:
    blynk.run()