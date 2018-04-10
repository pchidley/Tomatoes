from OmegaExpansion import onion12C 
import time

i2c	=	onionI2C.OnionI2C()

status	= i2c.writeByte(0X20, 0, 0)
status	= i2c.writeByte(0X21, 0, 0)
status	= i2c.writeByte(0X20, 9, 0)
status 	= i2c.writeByte(0X21, 9, 0) 
time. sleep (1)

status	= i2c.writeByte(0X20, 9, 255)
status	= i2c.writeByte(0X21, 9, 255) 
time. sleep (1)

status  = i2c.writeByte(0X20,	9, 0)
status  = i2c.writeByte(0X21,	9, 0)
time. sleep(l) 

print "Done"
