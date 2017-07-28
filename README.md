# Solar-Pi-Platter-UX (instructions in progress)

This is a web interface to interact with the <a href="http://danjuliodesigns.com/products/solar_pi_platter/solar_pi_platter.html">Solar Pi Platter</a> offered by <a href="http://danjuliodesigns.com/">Dan Julio Designs</a> which can be purchased on <a href="https://www.tindie.com/products/globoy/solar-pi-platter/">Tindie</a>.  This is an excellent add-on(? or add-to) for the Raspberry Pi Zero (W) to provide full power managment for your project.  It is packed full of useful features like: managed shutdown and power-up of the Pi based on battery voltage, switchable USB ports for further power management, and also I/O like PWM outputs and analog inputs.  There is also a breakout for an ethernet expansion port.  Check out <a href="http://danjuliodesigns.com/products/solar_pi_platter/solar_pi_platter.html">Dan's site</a> for more details.

<div style="display: inline;">
<img src="https://github.com/ccirone2/Solar-Pi-Platter-UX/blob/master/static/img/dan-julio-image_2849.png" height="220">
<img src="https://github.com/ccirone2/Solar-Pi-Platter-UX/blob/master/static/img/desktop-UX-screenshot.png" height="220" hspace="10">
<img src="https://github.com/ccirone2/Solar-Pi-Platter-UX/blob/master/static/img/mobile-UX-screenshot.png" height="220">
</div>

<ol>
<li> Install Raspbian-Jessie or Raspbian Jessie-Lite on your Pi Zero (W) -- not covered here
<li> Download/install talkpp binary from Dan Julio's github.
<li> Download/install Solar-Pi-Platter-UX
<li> Set-up UX to start-up as a service on RPi0 or RPi0-W
</ol>

## Download/install talkpp binary
This is a command line utility to interact with the Solar Pi Platter.  While command lines are useful, web interfaces are more user friendly.  That is the motivation behind this project!  Instructions for this process can be found <a href="https://github.com/danjulio/rocketblue-automation/tree/master/pi_platter/unix_applets/talkpp">here</a>.

### Instructions
Begin by downloading the binarys using:
``` 
wget ... 
```
Then move them to the `/usr/local/bin` directory:
``` 
sudo mv talkpp /usr/local/bin
```
Set the file permissions to be executable:
```
sudo chmod 775 /usr/local/bin/talkpp 
```
Finally test the command line utility to ensure all was successful:
```
talkpp -h
```

## Download/install Solar-Pi-Platter-UX
One you have the command-line utility installed, now we want to install a few package dependencies and get the UX installed.
```
#install bottle
```
Next, install the files from this repository:
```
wget ...
```
Set the permissions of the serve_my_platter.py to be executable (required for next step):
```
chmod +x ~/pi_platter/serve_my_platter.py
```

## Set-up Solar-Pi-Platter-UX to run as service
Final step is to set-up the web server to run as a service and starts up automatically with boot.

instructions will be elaborated from <a href="http://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/">here</a>.

### If you have suggestions/comments, I welcome them toward the improvment of this project and documentation. Im not a developer by trade, but I'll do my best to accommodate them as I continue on this learning experience.
