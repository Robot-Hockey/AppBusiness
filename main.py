#!/usr/bin/env python

import RPi.GPIO as GPIO
#import requests
#import json
from mfrc522 import SimpleMFRC522
import time
import os
from audio import Audio
from api import Api

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

GPIO.output(5, GPIO.HIGH)
GPIO.output(6, GPIO.LOW)
GPIO.output(12, GPIO.LOW)


reader = SimpleMFRC522()

# UID for card with free access.
ADMIN_CARDS = {
    '3C:2F:4F:0:2D': 'Admin 1',
}

sound = Audio()
api = Api()

def send_scoreboard_point(robot):
    if(robot):
        GPIO.output(6, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(6, GPIO.LOW)
    else:
        GPIO.output(12, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(12, GPIO.LOW)

def game():
    score_player = 0
    score_robot = 0
    game_max_score = 3
    GPIO.output(5, GPIO.LOW)
    sound.play_background()

    while(True):
        input_goal_player = GPIO.input(17)
        input_goal_robot = GPIO.input(18)
        
        os.system('clear')
        print("Player: ", score_player)
        print("Robot: ", score_robot)
        
        if score_player >= 3:
            print("Player Wins")
            GPIO.output(5, GPIO.HIGH)
            break
        
        if score_robot >= 3:
            print("Robot Wins")
            GPIO.output(5, GPIO.HIGH)
            break

        if input_goal_player == 1:
            score_player += 1
            sound.play_player_point()
            send_scoreboard_point(False)
        elif input_goal_robot == 1:
            score_robot += 1
            sound.play_robot_point()
            send_scoreboard_point(True)
        
        time.sleep(.3)
       

auth_token = api.login()

try:
    while(True):
        print('Show your card RFID')
        id, text = reader.read()
        print(hex(id))
        result = api.debit(auth_token, hex(id))
        if result:
            game()
        else:
            print("Error")
except KeyboardInterrupt:
    pass

GPIO.cleanup()
