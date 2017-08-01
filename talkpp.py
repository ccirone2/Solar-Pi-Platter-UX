import requests 
import subprocess 
import os

# Get info from Pi_Platter
def command(arg):
	if arg=='-s' or arg=='-t' or arg=='-f' or arg=='-a' or arg=='-d' or arg=='-w':
		stout = subprocess.check_output(['talkpp', arg]).strip()
	else:
		stout = subprocess.check_output(['talkpp', '-c', arg]).strip()
	return stout

# Write to Pi_Platter
def write2pp(bitname, value):
        os.system("talkpp -c {}={}".format(bitname,value))
        check = command(bitname)
        return check

# Decode the integer status code
def status_info():
	bit_desc=['USB Fault Detected', 
        	  'Reserved', 
	          'powerup_1', 
        	  'powerup_2', 
	          'Battery Charging', 
	          'USB Supplying Power', 
        	  'Battery Critical', 
	          'Battery Low']

	int_code = command('S')	

	status = [{bit_desc[i]:bit} for i, bit in enumerate('{0:08b}'.format(int(int_code)))]
	
	# combine powerup bits and decode
	powerup = status[2]['powerup_1']+status[3]['powerup_2']

	if powerup == '00':
		powerup_txt = 'by alarm'
	elif powerup == '01':
		powerup_txt = 'by button'
	elif powerup == '10':
		powerup_txt = 'battery restart'
	elif powerup == '11':
		powerup_txt = 'watchdog restart'    
    
	# add decoded powerup reason to status list
	status.insert(2,{'Power Up': powerup_txt})

	# remove individual power up bits from status list
	status.pop(4)
	status.pop(3)

	return status

# Decode the analog setting code
def analog_info(arg):

        if arg == '0':
                amode = 'PMIC/RTC VCC'
        elif arg == '1':
                amode = '1.024 V'
        elif arg == '2':
                amode = '2.048 V'
        elif arg == '3':
                amode = '4.096 V'
        else:
        		# return info for debugging
                amode = [arg, type(arg)] 
        return amode

# Decode the PWM setting code
def PWM_info(arg):
	
	if arg == '0':
		pwmmode = 'Fast, 46875 Hz'
	elif arg == '1':
		pwmmode = 'Medium, 2930 Hz'
	elif arg == '2':
		pwmmode = 'Slow, 732 Hz'
	elif arg == '3':
		pwmmode = 'Servo Mode'
	else:
		# return info for debugging
		pwmmode = [arg, type(arg)]
	return pwmmode


def pp_configs(arg):

	if arg == 'general':
		return [
			{'device time':{'setting':command('-f'),'control':{'set':'-s'}}},
			{'version':command('V')},
			{'battery voltage':command('B')},
                      	] + status_info()
	
        elif arg == 'timers':
		return [
			{'current time':command('T')},
			{'power off':command('O')},
			{'wakeup':command('W')},
			{'wakeup pretty':command('-w')},
                        {'wakeup repeat':command('R')},
			]

        elif arg == 'io':
		return [
			{'USB-2':command('U1')},
                        {'USB-3':command('U2')},
    		        {'analog-1':command('A1')},
                        {'analog-2':command('A2')},
                        {'PWM-1':command('P1')},
                        {'PWM-2':command('P2')},
	               ]

        elif arg == 'control':
		return [
			{'C0: Wakeup Enable':command('C0')},
                        {'C1: Low Battery Warning Enable':command('C1')},
                        {'C2: Critical Battery Warning Enable':command('C2')},
                        {'C3: USB Fault Warning Enable':command('C3')},
                        {'C4: Analog 1 Reference':analog_info(command('C4'))},
                        {'C5: Analog 2 Reference':analog_info(command('C5'))},
                        {'C6: PWM Mode':PWM_info(command('C6'))},
                        {'C7: Restart Enable':command('C7')},
                        {'C8: Watchdog Control':command('C8')},
		       ]

        elif arg == 'eeprom':
		return [
			{'E0: Battery Low Warn Threshold':round(float(command('E0'))*0.00423783877,2)},
                        {'E1: Battery Critical Threshold':round(float(command('E1'))*0.00423783877,2)},
                        {'E2: Battery Start Under-voltage Threshold':round(1/(float(command('E2'))/1023)*1.024+0.15,2)},
                        {'E3: Battery Restart Threshold':round(1/(float(command('E3'))/1023)*1.024+0.15,2)},
                        {'E4: Battery Critical to Turn-off Timeout':command('E4')},
                        {'E5: Battery Warn Message Enable':command('E5')},
                        {'E6: Battery Critical Message Enable':command('E6')},
                        {'E7: Battery Restart Enable':command('E7')},
                        {'E8: USB Fault Message Enable':command('E8')},
                        {'E9: USB Port 2 Default Power Enable':command('E9')},
                        {'E10: USB Port 3 Default Power Enable':command('E10')},
                        {'E11: Analog 1 Default Reference':analog_info(command('E11'))},
                        {'E12: Analog 2 Default Reference':analog_info(command('E12'))},
                        {'E13: PWM Mode':PWM_info(command('E13'))},
                       ]

def main():
	print "library of functions to speak to the pi platter"

if __name__ == "__main__":
	main()
