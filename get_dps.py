import sys
import pytuya
import socket #needed for socket.timeout exception


if(len(sys.argv)!=3):
	print("usage: " + sys.argv[0] + " <IP> <DevID>")
	exit(1)

ip        = sys.argv[1]    # The ip address to which you are connecting the bulb with
devid     = sys.argv[2]	   # The id of the device switch


device   = pytuya.OutletDevice(devid,ip,"")

data = 0 #stub for the try except
try:
	data = device.status()
except (ConnectionResetError, socket.timeout, OSError)  as e:
	print("A problem occur please retry...")
	exit(1)

print("\nPlug State Information:")
print(data)

print("\nPlug DPS List:")

dps_list = ""
first=True
for key in data['dps'].keys():
	
	if(type (data['dps'][key]) is bool):
		if(not first):
			dps_list += ";"
		dps_list += str(int(key))
		first=False
				
print(dps_list)
