from app.audio import Audio

sound = Audio()
sound.play_background()

try:
    while(True):
        number = input("")
        if(number == '1'):
            sound.play_robot_point()
        elif(number == '2'):
            sound.play_player_point()
        elif(number == '3'):
            sound.play_on()
        elif(number == '4'):
            sound.play_off()
except KeyboardInterrupt:
    pass
