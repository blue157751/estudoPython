from pygame import mixer
mixer.init()
mixer.music.load('funk.mp3')
mixer.music.play()
input('digite algo para parar a musica')