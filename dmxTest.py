from DMXEnttecPro import Controller
import time
import random

dmx = Controller('/dev/ttyUSB0',auto_submit=True)
count = 0
testChannel = 5
while True:
	dmx.set_channel(testChannel,count)
	count = (count+1)%255
	time.sleep(0.01)


# dmx.set_all_channels(val)
# dmx.clear_channels()
# dmx.all_channels_on()
