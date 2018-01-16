read the newone python code attentively.
It uses serial module and somewhere in the code there is an option for COM port
After plugging in the arduino cable watch your and change in the code.
if not willing to change then go to the device manager and change the com port of 
arduino to the given one. 
Because doing this one can run the .exe application file from dist folder as console
and control everything via remote.
In this case Philips TV remote is used.....
If other remote is used then at first decode the button function using arduino IR
library and then re code the arduino with the following button code.
  