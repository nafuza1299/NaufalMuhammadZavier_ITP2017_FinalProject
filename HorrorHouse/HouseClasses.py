from pygame import *
from pygame.sprite import *

#This module contains all the custom classes needed for the game'''


class imagesprite(Sprite):

    '''This class is used to create and display an image as a sprite onto the screen'''

    def __init__(self, filename, xpos, ypos):  #fill in the parameters so that it is reusable
        Sprite.__init__(self)
        self.image = image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

class textsprite (Sprite):

    '''This class is used to create and display a text as a sprite onto the screen'''

    def __init__(self, fontstyle, text, fontsize, xpos, ypos, R, G, B):
        Sprite.__init__(self)
        self.font = pygame.font.SysFont(fontstyle, fontsize)
        self.image = self.font.render(text, False, (R, G, B))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

class MainScreen():

    '''This class is used to set an image as the background'''

    def __init__(self, imagefile):
        self.display  = pygame.display.set_mode((1120, 590))
        pygame.display.set_caption("House")
        self.image = image.load(imagefile)
        self.display.blit(self.image, (0,0))

class sound():

    '''This class is used to play the music continously without interrruptions'''

    def __init__(self, musicfile):
        pygame.mixer.Sound(musicfile).play() #Use Sound instead of music as it won't be interrupted

class jump():

    '''This class is used to play the jumpscare sound effect'''

    def __init__(self):
        pygame.mixer.music.load("Jump2.wav") #Use mixer.music so that it won't interrupt the background music
        pygame.mixer.music.play() #plays the sound file

class coloredbackground():

    '''This class is used to create a colored background'''

    def __init__(self, R, G, B):
        self.screen  = pygame.display.set_mode((1120, 590))
        pygame.display.set_caption("House")
        self.screen.fill((R, G, B))

