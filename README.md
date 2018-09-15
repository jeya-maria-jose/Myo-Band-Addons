# Myo-Band-Addon-Virtual-Keyboard

Myo armband, reads the electrical activity of your muscles to control technology with gestures and motion, hands-free. It is an open source research hardware provided the thalmic labs.

Using <a href="https://market.myo.com/app/559adc2ee4b0f2c8982c9138/pyoconnect"> Pyoconnect </a> , a open source tool made to support operations of the myo band in linux, few addon codes and functions have been writted for usage of myoband in linux.

Data.py has the functions needed to display the realtime Accelerometer, Gyro, Orientation angles of the myoband.

Virtualkeyboard.py maps the current location of the band to a letter in the keyboard. The code has been calibtrated so as to match the order of the letters found in the normal keyboard. So for each postition of the hand an alphabet will be displayed in the screen accordingly.

Both these codes can be easily plugged in to the PyoConnect and be made to use.
