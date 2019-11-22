#!/usr/bin/env python

import RPi.GPIO as GPIO
#import requests
#import json
from mfrc522 import SimpleMFRC522
import time
import os
from audio import Audio
from api  import Api

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Goal Sensor
GPIO.setup(26, GPIO.IN) # Goal sensor 1
GPIO.setup(20, GPIO.IN) # Goal sensor 2

# Reles
GPIO.setup(23, GPIO.OUT) # Rele in 1
GPIO.setup(24, GPIO.OUT) # Rele in 2
GPIO.output(23, GPIO.HIGH) # Rele 1 output
GPIO.output(24, GPIO.HIGH) # Rele 2 output

# Scoreboard
GPIO.setup(6, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.output(6, GPIO.LOW)
GPIO.output(12, GPIO.LOW)

reader = SimpleMFRC522()
sound = Audio()

# UID for card with free access.
ADMIN_CARDS = {
    '3C:2F:4F:0:2D': 'Admin 1',
}


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
    GPIO.output(23, GPIO.LOW) # Turn on air
    sound.play_background()

    while(True):
        #input_goal_player = GPIO.input(26)
        #input_goal_robot = GPIO.input(20)
        #print(input_goal_player)
        #print(input_goal_robot)
        input_goal_player = 0
        input_goal_robot = 0

        count = 0
        
        GPIO.setup(26, GPIO.OUT)
        GPIO.output(26, GPIO.LOW)
        time.sleep(0.01)
        GPIO.setup(26, GPIO.IN)

        while (GPIO.input(26) == GPIO.LOW):
            count += 1

        
        if count >= 10:
            input_goal_robot = 1
        
        #TODO: Code robot player goal

        os.system('clear')
        
        if score_player >= 3:
            print("Player Wins")
            GPIO.output(23, GPIO.HIGH) # Turn off air
            break
        
        if score_robot >= 3:
            print("Robot Wins")
            GPIO.output(23, GPIO.HIGH) # Turn off air
            break

        if input_goal_player == 1:
            score_player += 1
            sound.play_player_point()
            #send_scoreboard_point(False)
        elif input_goal_robot == 1:
            score_robot += 1
            sound.play_robot_point()
            #send_scoreboard_point(True)
        
        print("Player: ", score_player)
        print("Robot: ", score_robot)
        print(count) 
     
        """
        time.sleep(.3)
        """


def main():
    api = Api()
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


if __name__ == "__main__":
    main()
