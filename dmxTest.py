from DMXEnttecPro import Controller
import time

dmx = Controller('/dev/ttyUSB0',auto_submit=True)

dmx.set_channel(512,0)

time.sleep(1)

dmx.set_channel(512,255)

# dmx.set_all_channels(val)
# dmx.clear_channels()
# dmx.all_channels_on()
