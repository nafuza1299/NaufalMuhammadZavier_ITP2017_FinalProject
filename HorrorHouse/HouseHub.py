from pygame import *
from HouseClasses import *
from HouseFunctions import *

pygame.init()
'''This module contains the hub area for the game such as menu, levelscreen, intro and outro.'''

def start_screen():
    while True:
        transition_screen("HOUSE")
        start_screen_wait = event.wait()
        if start_screen_wait.type == MOUSEBUTTONDOWN:
            menu()
        display.update()


def menu():

    '''Opens the menu screen containing, the features, play, levels and quit'''

    menuscreen = MainScreen("Menu.png")
    play = textsprite("YouMurderer BB", "Play", 60, 100, 100, 255, 255, 255)
    quit = textsprite("YouMurderer BB", "Quit", 60, 100, 300, 255, 255, 255)
    level = textsprite("YouMurderer BB", "Level", 60, 100, 200, 255, 255, 255)
    while True:

        #'''Lines 19 to 27 creates the text with rect features, and changes colors when hovered.'''

        play_text = Group(play)
        play_text.draw(menuscreen.display)
        text_button(play, menuscreen, "Image", "YouMurderer BB", "Play", 60, 100, 100)
        quit_text = Group(quit)
        quit_text.draw(menuscreen.display)
        text_button(quit, menuscreen, "Image", "YouMurderer BB", "Quit", 60, 100, 300)
        level_text = Group(level)
        level_text.draw(menuscreen.display)
        text_button(level, menuscreen, "Image", "YouMurderer BB", "Level", 60, 100, 200)
        menu_wait = event.wait()
        image_click(play.rect, menu_wait), image_click(quit.rect, menu_wait), image_click(level.rect, menu_wait)
        if play.rect.collidepoint(mouse.get_pos()):
            if menu_wait.type == MOUSEBUTTONDOWN:
                while True:
                    Ghost(menuscreen, "Menu.png", "Jumpscare.png", 0, 0)
                    intro()
                    break
        if quit.rect.collidepoint(mouse.get_pos()):
            if menu_wait.type == MOUSEBUTTONDOWN:
                pygame.quit()
                break
        if level.rect.collidepoint(mouse.get_pos()):
            if menu_wait.type == MOUSEBUTTONDOWN:
                levelscreen()
    display.update()


def levelscreen():

    '''Opens the level selection screen'''

    selection_screen = coloredbackground(0, 0, 0,)
    while True:
        level1 = textsprite("Diediedie", "Level 1", 50, 50, 100, 255, 255, 255)
        level1_text = Group(level1)
        level1_text.draw(selection_screen.screen)
        text_button(level1, selection_screen, "Fill", "Diediedie", "Level 1", 50, 50, 100)
        level2 = textsprite("Diediedie", "Level 2", 50, 350, 100, 255, 255, 255)
        level2_text = Group(level2)
        level2_text.draw(selection_screen.screen)
        text_button(level2, selection_screen, "Fill", "Diediedie", "Level 2", 50, 350, 100)
        back = textsprite("Diediedie", "Back", 25, 0, 0, 255, 255, 255)
        back_text = Group(back)
        back_text.draw(selection_screen.screen)
        text_button(back, selection_screen, "Fill", "Diediedie", "Back", 25, 0, 0)
        level_wait = event.wait()
        image_click(level1.rect, level_wait), image_click(level2.rect, level_wait), image_click(back.rect, level_wait)
        if level1.rect.collidepoint(mouse.get_pos()):
            if level_wait.type == MOUSEBUTTONDOWN:
                import Room_One; Room_One.transition_screen1()
        if level2.rect.collidepoint(mouse.get_pos()):
            if level_wait.type == MOUSEBUTTONDOWN:
                import Room_Two; Room_Two.transition_screen2()
        if back.rect.collidepoint(mouse.get_pos()):
            if level_wait.type == MOUSEBUTTONDOWN:
                menu()
                break
        if level_wait.type == QUIT:
            pygame.quit()
            break
        display.update()

def intro():

    '''Opens the introduction screen with the text containing the back story'''

    intro_screen = coloredbackground(0, 0, 0,)
    intro = textsprite("Diediedie", "This is your first night moving in into this board house", 30, 0, 0, 255, 255, 255)
    skip = textsprite("YouMurderer BB", "Skip", 35, 1000, 0, 255, 255, 255)
    while True:
        intro_text = Group(intro, skip)
        intro_text.draw(intro_screen.screen)
        intro_wait = event.wait()
        skip_button = text_button(skip, intro_screen, "Fill", "YouMurderer BB", "Skip", 35, 1000, 0)
        image_hover(intro.rect)
        image_click(intro.rect, intro_wait)
        if skip.rect.collidepoint(mouse.get_pos()):
            if intro_wait.type == MOUSEBUTTONDOWN:
                import Room_One; Room_One.transition_screen1()
                break
        if intro_wait.type == MOUSEBUTTONDOWN:
            intro1 = textsprite("Diediedie", "The place has a history with the supernatural", 30, 0, 100, 255, 255, 255)
            call_sprite(intro1, "Fill", intro_screen)
            if intro_wait.type == MOUSEBUTTONDOWN:
                intro2 = textsprite("Diediedie", "It is said that the restless spirit still haunts this place to this day", 30, 0, 200, 255, 255, 255)
                call_sprite(intro2, "Fill", intro_screen)
                if intro_wait.type == MOUSEBUTTONDOWN:
                    intro3 = textsprite("Diediedie", "You woke up stressed and locked in your room", 30, 0, 300, 255, 255, 255)
                    call_sprite(intro3, "Fill", intro_screen)
                    if intro_wait.type == MOUSEBUTTONDOWN:
                        intro4 = textsprite("Diediedie", "If you want to live, escape the house.", 30, 0, 400, 255, 255, 255)
                        call_sprite(intro4, "Fill", intro_screen)
                        continue_text = textsprite("YouMurderer BB", "Continue", 35, 1000, 500, 255, 255, 255)
                        continue_call = Group(continue_text)
                        continue_call.draw(intro_screen.screen)
                        text_button(continue_text, intro_screen, "Fill", "YouMurderer BB", "Continue", 35, 1000, 500,)
                        if continue_text.rect.collidepoint(mouse.get_pos()):
                            if intro_wait.type == MOUSEBUTTONDOWN:
                                import Room_One; Room_One.transition_screen1()
                                break
        display.update()

def Outro():

    '''Opens the outro screen, displaying the text explaining the ending of the game.'''

    outro_screen = coloredbackground(0, 0, 0,)
    outro = textsprite("Diediedie", "You have escaped the place...", 30, 0, 0, 255, 255, 255)
    skip = textsprite("YouMurderer BB", "Skip", 35, 1000, 0, 255, 255, 255)
    while True:
        outro_text = Group(outro, skip)
        outro_text.draw(outro_screen.screen)
        skip_button = text_button(skip, outro_screen, "Fill", "YouMurderer BB", "Skip", 35, 1000, 0)
        outro_wait = event.wait()
        image_hover(outro.rect)
        image_click(outro.rect, outro_wait)
        if skip.rect.collidepoint(mouse.get_pos()):
            if outro_wait.type == MOUSEBUTTONDOWN:
                game_completed()
                break
        if outro_wait.type == MOUSEBUTTONDOWN:
            outro1 = textsprite("Diediedie", "However, the memory still haunts you", 30, 0, 100, 255, 255, 255)
            call_sprite(outro1, "Fill", outro_screen)
            if outro_wait.type == MOUSEBUTTONDOWN:
                outro2 = textsprite("Diediedie", "Even if you have escaped the place, your mind is still haunted", 30, 0, 200, 255, 255, 255)
                call_sprite(outro2, "Fill", outro_screen)
                if outro_wait.type == MOUSEBUTTONDOWN:
                    outro3 = textsprite("Diediedie", "Still... life continues", 30, 0, 300, 255, 255, 255)
                    call_sprite(outro3, "Fill", outro_screen)
                    if outro_wait.type == MOUSEBUTTONDOWN:
                        outro4 = textsprite("Diediedie", "But a dead man has no business breathing", 30, 0, 400, 255, 255, 255)
                        call_sprite(outro4, "Fill", outro_screen)
                        continue_text = textsprite("YouMurderer BB", "Continue", 35, 1000, 500, 255, 255, 255)
                        continue_call = Group(continue_text)
                        continue_call.draw(outro_screen.screen)
                        continue_button = text_button(continue_text, outro_screen, "Fill", "YouMurderer BB", "Continue", 35, 1000, 500,)
                        if continue_text.rect.collidepoint(mouse.get_pos()):
                            if outro_wait.type == MOUSEBUTTONDOWN:
                                game_completed()
                                break

        display.update()









