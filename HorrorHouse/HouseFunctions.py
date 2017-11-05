from pygame import *
from HouseClasses import *
'''This module contains Custom Built Functions'''

def text_button(textname, mainscreen, screen_type, fontstyle, text, size, xpos, ypos):

    ''' This function changes the text's color and plays a sound effect when it is hovered'''

    if textname.rect.collidepoint(mouse.get_pos()):
        sound("Click2.wav")
        txt = textsprite(fontstyle, text, size, xpos, ypos, 255, 0, 0)
        grouping = Group(txt)
        if screen_type == "Image":
            grouping.draw(mainscreen.display)
        if screen_type == "Fill":
            grouping.draw(mainscreen.screen)
    display.update()

def call_sprite(text, screen_type, mainscreen):

    '''This function displays the sprite into the screen'''

    text_group = Group(text)
    if screen_type == "Image":
        text_group.draw(mainscreen.display)
    if screen_type == "Fill":
            text_group.draw(mainscreen.screen)
    display.update()

def Ghost(screen_name, screen_display, image_call, xpos, ypos):

    '''This function calls the Jumpscare with the ghost and the sound'''

    screen_name= MainScreen(screen_display)
    jumpscare = imagesprite(image_call, xpos, ypos)
    pop = jump ()
    while True:
        ghost = Group(jumpscare)
        ghost.draw(screen_name.display)
        ghost_wait = event.wait()
        if ghost_wait.type == MOUSEBUTTONDOWN:
            break
        display.update()


def reset():
    '''This function resets the values for the event triggers to it's original value'''
    global kharon, picturecount, door_unlock, key, scare, lives_remaining, bathroom_event
    kharon = []
    picturecount = 0
    door_unlock = 0
    key = 0
    lives_remaining = 3
    bathroom_event = 0

def reset_kharon():

    '''A reset specifically for the ouija board; resets value of kharon and scare'''

    global kharon, scare
    kharon = []
    scare = 0

def image_hover(rect_name):

    '''Plays a sound effect when an image/text is hovered'''

    if rect_name.collidepoint(mouse.get_pos()):
        pygame.mixer.Sound("Click2.wav").play()

def image_click(rect_name, event):

    '''Plays a sound effect when an image/text is hovered'''

    if rect_name.collidepoint(mouse.get_pos()):
        if event.type == MOUSEBUTTONDOWN:
            pygame.mixer.Sound('Click.wav').play()


def transition_screen(text):

    '''Creates a transitional screen with black background and a text'''

    black = coloredbackground(0, 0, 0)
    transition_text = textsprite("YouMurderer BB", text, 100, 440, 170, 255, 255, 255)
    call_sprite(transition_text, "Fill", black)
    display.update()

def Gameover():

    '''Creates the Game Over screen'''

    while True:
        transition_screen("Game Over")
        gameover_wait = event.wait()
        if gameover_wait.type == MOUSEBUTTONDOWN:
            reset()
            import HouseHub; HouseHub.menu()
            break
        display.update()


def game_completed():

    '''Creates the Game Over screen'''

    while True:
        transition_screen("GAME COMPLETE")
        gameover_wait = event.wait()
        if gameover_wait.type == MOUSEBUTTONDOWN:
            reset()
            import HouseHub; HouseHub.menu()
            break
        display.update()

def pause_quit(eventname, mainscreen):

    '''Pauses the game, allows for quitting the game and gives the player to option to go back to the menu screen'''

    if eventname.type == KEYDOWN:
            if eventname.key == K_SPACE:
                while True:
                    pause = textsprite("Diediedie", "Paused", 50, 490, 295, 255, 255, 255)
                    menu_button = textsprite("Diediedie", "Menu", 50, 0, 0, 255, 255, 255)
                    menu_text = Group(menu_button)
                    menu_text.draw(mainscreen.display)
                    text_button(menu_button, mainscreen, "Image", "Diediedie", "Menu", 50, 0, 0)
                    call_sprite(pause, "Image", mainscreen)
                    pause_wait = event.wait()
                    if menu_button.rect.collidepoint(mouse.get_pos()):
                        if pause_wait.type == MOUSEBUTTONDOWN:
                            import HouseHub; HouseHub.menu()
                            break
                    if pause_wait.type == KEYDOWN:
                        if pause_wait.key == K_SPACE:
                            break

    if eventname.type == QUIT:
        pygame.quit()
        return False
