#!/usr/bin/env python

import RPi.GPIO as GPIO
import requests
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

# UID for card with free access.
ADMIN_CARDS = {
    '3C:2F:4F:0:2D': 'Admin 1',
}

GAME_CONTROLLER = False

while(True):
    print('Show your card RFID')
 
    try:
        id = reader.read()
        print(id)
        loginAPI()
        # Request to API
        # Start Game
    finally:
        GPIO.cleanup()


def loginAPI():
    r = requests.get('https://hockey-api.lappis.rocks')
    print(r.status_code)