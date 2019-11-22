from pygame import mixer, time
import random
import sys

ROBOT_POINT_SOUNDS = [
    'ai-ai',
    'bambam-ajuda-o-maluco-ta-doente',
    'bambam-bora-caralho',
    'bambam-bora-cupadre',
    'bambam-nao-eh-agua-com-musculo',
    'bambam-nao-vai-dar',
    'carreta-furacao',
    'nao-teve-uma-boa-partida',
    'no-no-no-hahaha',
    'now-the-world-dont-move',
    'serjao-atirei-a-primeira',
    'serjao-mata-onca-mesmo',
    'serjao-matador-de-onca',
    'ta-pegando-fogo',
    'ta-sentindo-cansaco',
    'voar-nos-metros-finais',
    'e-agora-desliga',
    'e-agora-pra-desligar-essa-merda-ai'
]

PLAYER_POINT_SOUNDS = [
    'ayrton-senna',
    'bambam-aqui-noix-constroi-fibra',
    'bambam-arrhhhhhhhh',
    'bambam-birl',
    'bambam-ta-saindo-da-jaula',
    'bambam-uhhh-body-builder',
    'chama-o-bombeiro-la',
    'saiu-bem',
    'serjao-onca',
    'so-um-genio-pra-ganhar-essa-prova',
    'super-mario-bros-coin-sound-effect',
    'sweet-dreams-1',
    'sweet-dreams-2',
    'bambam-hora-do-show',
    'vai-perder-vai-ganhar'
]

THEME_SOUNDS = [
    'chapeleiro-disco-voador-original'
]

THEME_SOUNDS = [
    'chapeleiro-disco-voador-original'
]

AUDIO_PATH = '../sounds/'

VOLUME_LOW = 0.3
VOLUME_HIGH = 1.0
CHANNEL = 1

class Audio:

    def __init__(self):
        mixer.init(44100, -16, 1, 1024)
        self.bg_sound = mixer.music.load(AUDIO_PATH + THEME_SOUNDS[0] + '.ogg')

    def play_background(self):  # Background music
        mixer.music.play(-1, 70.0)
    
    def fade_sound_controller(self):
        mixer.music.set_volume(VOLUME_LOW)
        while mixer.get_busy():
            time.wait(100)
        mixer.music.set_volume(VOLUME_HIGH)

    def play_robot_point(self): # Robot sound effects
        sound = mixer.Sound(AUDIO_PATH + ROBOT_POINT_SOUNDS[random.randint(0, 15)] + '.ogg')
        mixer.Channel(CHANNEL).play(sound)
        self.fade_sound_controller()

    def play_player_point(self): # Player sound effects
        sound = mixer.Sound(AUDIO_PATH + PLAYER_POINT_SOUNDS[random.randint(0, 13)] + '.ogg')
        mixer.Channel(CHANNEL).play(sound)
        self.fade_sound_controller()