from pygame import mixer
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
    'voar-nos-metros-finais'
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
    'serjao-berrante',
    'serjao-onca',
    'so-um-genio-pra-ganhar-essa-prova',
    'super-mario-bros-coin-sound-effect',
    'sweet-dreams-1',
    'sweet-dreams-2'
]

ON_SOUNDS = [
    'aperta-o-numero-1-liga',
    'bambam-hora-do-show',
    'ja-tava-baum'
]

OFF_SOUNDS = [
    'e-agora-desliga',
    'e-agora-pra-desligar-essa-merda-ai',
    'nem-quem-ganhar-ou-perder',
    'vai-perder-vai-ganhar'
]

THEME_SOUNDS = [
    'chapeleiro-disco-voador-original'
]

class Audio():

    def __init__(self) -> object:
        mixer.pre_init(44100, 16, 2, 4096)
        mixer.init()
        self.bg_sound = mixer.music.load('./sounds/'+ THEME_SOUNDS[0] + '.ogg')

    def play_background(self):  # Background music
        mixer.music.play(-1)

    def play_robot_point(self): # Robot sound effects
        sound = mixer.Sound('./sounds/'+ ROBOT_POINT_SOUNDS[random.randint(0, 15)] + '.ogg')
        mixer.Sound.play(sound)

    def play_player_point(self): # Player sound effects
        sound = mixer.Sound('./sounds/'+ PLAYER_POINT_SOUNDS[random.randint(0, 14)] + '.ogg')
        mixer.Sound.play(sound)

    def play_on(self): # Table ON sound effects
        sound = mixer.Sound('./sounds/'+ ON_SOUNDS[random.randint(0, 2)] + '.ogg')
        mixer.Sound.play(sound)

    def play_off(self): # Table OFF sound effects
        sound = mixer.Sound('./sounds/'+ OFF_SOUNDS[random.randint(0, 3)] + '.ogg')
        mixer.Sound.play(sound)

sound = Audio()
sound.play_background()

try:

    while(True):

        number = input("")
        print(number)
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