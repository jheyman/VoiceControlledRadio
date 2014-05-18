#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import os

#adjust for where your switch is connected
buttonPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)

while True:
  #assuming the script to call is long enough we can ignore bouncing
  if (not GPIO.input(buttonPin)):
    #this is the script that will be called (as root)
    os.system("""  arecord -D plughw:0,0 -f cd -t wav -d 3 -r 16000 | flac - -f --best --sample-rate 16000 -o out.flac; wget -O - -o /dev/nu
ll --post-file out.flac --header="Content-Type: audio/x-flac; rate=16000" http://www.google.com/speech-api/v1/recognize?lang=fr | sed -e 's/
[{}]/''/g' | awk -v k="text" '{n=split($0,a,","); for (i=1; i<=n; i++) print a[i]; exit }' | awk -F: 'NR==3 { print $3; exit }' | xargs ./te
a5767.py """)
    time.sleep(0.5)
  time.sleep(0.05)
