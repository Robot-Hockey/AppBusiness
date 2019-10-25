#!/usr/bin/env python
# -*- coding: utf8 -*-
 
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
 
# UID for card with free access.
ADMIN_CARDS = {
    '3C:2F:4F:0:2D': 'Admin 1',
}
 
try:
    # Init module RC522.
    LeitorRFID = MFRC522.MFRC522()
 
    print('Show your card RFID')
 
    while True:
        # Verify if there is one tag close to de module.
        status, tag_type = LeitorRFID.MFRC522_Request(LeitorRFID.PICC_REQIDL)
 
        if status == LeitorRFID.MI_OK:
            print('Card detected!')
 
            # Read Card UID.
            status, uid = LeitorRFID.MFRC522_Anticoll()
 
            if status == LeitorRFID.MI_OK:
                uid = ':'.join(['%X' % x for x in uid])
                print('Card UID: %s' % uid)
 
                # If you are an admin the game starts automatically.
                if uid in ADMIN_CARDS:
                    # Is a system admin
                else:
                    # Not a system admin
 
                print('nShow your card RFID')
 
        time.sleep(.25)
except KeyboardInterrupt:
    # If the user press Ctrl + C
    # exit the program.
    GPIO.cleanup()
    print('nExit.')