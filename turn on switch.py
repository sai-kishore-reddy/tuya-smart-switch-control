import sys
import pytuya
import socket


if(len(sys.argv)!=5):
	print("usage: " + sys.argv[0] + " <IP> <DevID> <Local key> <DPS value>")
	exit(1)

ip        = sys.argv[1]    # The ip address to which you are connecting the bulb with
devid     = sys.argv[2]	   # The id of the device switch
localkey  = sys.argv[3]    # Local key can be found in tuya api device info
dps_value = sys.argv[4]    # dsp value

device    = pytuya.OutletDevice(devid,ip,localkey)

try:
	
	payload = device.generate_payload('set', {str(dps_value):True})
	device._send_receive(payload)
	
except (ConnectionResetError, socket.timeout, OSError)  as e:
	print("A problem occur please retry...")
	exit(1)
