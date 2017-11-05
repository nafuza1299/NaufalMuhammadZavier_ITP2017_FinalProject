from pygame import *
from HouseFunctions import *
from HouseClasses import *

def transition_screen2():

    '''Opens the transition screen for Room 2'''

    while True:
        transition_screen("Room 2")
        transition_wait = event.wait()
        display.update()
        if transition_wait.type == MOUSEBUTTONDOWN:
            screen2()

def screen2():

    '''Opens the screen for the second level'''

    music = sound("BackgroundMusic.wav")
    bathroom = MainScreen("Bathroom.jpg")
    bathroom_event = 0
    lives_remaining = 3
    key = 0

    while True:

        '''Draws the rectangle behind the screen so that it is invisible'''

        book = pygame.draw.rect(bathroom.display, ((0, 0, 0)), (910, 320, 80,140))
        mirror = pygame.draw.rect(bathroom.display, ((0, 0, 0)), (750, 380, 45,45))
        sink = pygame.draw.rect(bathroom.display, ((0, 0, 0)), (710, 410, 35,35))
        vase3 = pygame.draw.rect(bathroom.display, ((0, 0, 0)), (760, 240, 35,32))
        vase2 = pygame.draw.rect(bathroom.display, ((0, 0, 0)), (740, 300, 35,42))
        vase1 = pygame.draw.rect(bathroom.display, ((0, 0, 0)), (740, 160, 30,42))
        clock = pygame.draw.rect(bathroom.display, ((0, 0, 0)), (770, 110, 30,80))
        showerhead = pygame.draw.rect(bathroom.display, ((0, 0, 0)), (560, 80, 60, 55))
        button1 = pygame.draw.rect(bathroom.display, ((0, 0, 0)), (325, 270, 10, 10))
        button2 = pygame.draw.rect(bathroom.display, ((0, 0, 0)), (325, 288, 10, 10))
        button3 = pygame.draw.rect(bathroom.display, ((0, 0, 0)), (325, 310, 10, 10))
        door = pygame.draw.rect(bathroom.display, ((0, 0, 0)), (0, 0, 105, 590))
        black_stand = pygame.draw.rect(bathroom.display, ((0, 0, 0)), (213, 290, 12, 90))
        black_box = pygame.draw.rect(bathroom.display, ((0, 0, 0)), (160, 355, 42, 45))
        bathroom.display.blit(bathroom.image, (0,0))

        lives_text = textsprite("YouMurderer BB", "Lives: " + str(lives_remaining) + "/3", 50, 950, 0, 255, 0, 0,)
        call_sprite(lives_text, "Image", bathroom)
        room2_wait = event.wait()

        '''Calls the sound effect for each rectangle'''
        image_hover(book), image_hover(sink), image_hover(sink), image_hover(vase3), image_hover(vase2), image_hover(vase1)
        image_hover(clock), image_hover(showerhead), image_hover(button1), image_hover(button2), image_hover(button3)
        image_hover(black_stand), image_hover(black_box), image_hover(door)
        image_click(book, room2_wait), image_click(sink, room2_wait), image_click(vase3, room2_wait), image_click(vase2, room2_wait), image_click(vase1, room2_wait)
        image_click(clock, room2_wait), image_click(showerhead, room2_wait), image_click(button1, room2_wait), image_click(button2, room2_wait), image_click(button3, room2_wait)
        image_click(black_box, room2_wait), image_click(door, room2_wait), image_click(black_stand, room2_wait)
        #Interactions for the "first event" (lines 58 - 93)
        if bathroom_event == 0:
            if vase1.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    lives_remaining -= 1
                    Ghost(bathroom, 'Bathroom.jpg', 'Scare.png', 250, 0)
            if mirror.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    Ghost(bathroom, 'Bathroom.jpg', 'Scare.png', 250, 0)
                    lives_remaining -= 1
            if book.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    bathroom_event += 1
                    while True:
                        hint = imagesprite("paperhint3.png", 300, 100)
                        call_sprite(hint, "Image", bathroom)
                        hint_wait = event.wait()
                        image_click(hint.rect, hint_wait)
                        if hint_wait.type == MOUSEBUTTONDOWN:
                            break
            if sink.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        sink_text = textsprite("YouMurderer BB", "Clear water flows through the sink", 30, 560, 295, 255, 255, 255)
                        call_sprite(sink_text, "Image", bathroom)
                        sink_wait = event.wait()
                        image_click(sink_text.rect, sink_wait)
                        if sink_wait.type == MOUSEBUTTONDOWN:
                            break
            if showerhead.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        pygame.display.set_caption("I really tried my best...")
                        hint_wait = event.wait()
                        if hint_wait.type == MOUSEBUTTONDOWN:
                            pygame.display.set_caption("House")
                            break

        #Interactions for the "second event" (lines 96 - 149)
        if bathroom_event == 1:
            if sink.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        sink_text = textsprite("Diediedie", "Blood red water is pouring...", 50, 300, 295, 255, 0, 0)
                        call_sprite(sink_text, "Image", bathroom)
                        sink_wait = event.wait()
                        image_click(sink, sink_wait)
                        if sink_wait.type == MOUSEBUTTONDOWN:
                            break
            if book.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        hint = imagesprite("paperhint4.png", 300, 100)
                        call_sprite(hint, "Image", bathroom)
                        hint_wait = event.wait()
                        image_click(hint.rect, hint_wait)
                        if hint_wait.type == MOUSEBUTTONDOWN:
                            break
            if vase2.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    Ghost(bathroom, 'Bathroom.jpg', 'Scare.png', 250, 0)
                    lives_remaining -= 1
            if vase3.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    Ghost(bathroom, 'Bathroom.jpg', 'Scare.png', 250, 0)
                    lives_remaining -= 1
            if black_box.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    bathroom_event += 1
                    key += 1
                    while True:
                        black_box_text = textsprite("Diediedie", "Obtained a key", 40, 100, 300, 255, 255, 255)
                        call_sprite(black_box_text, "Image", bathroom)
                        black_box_wait = event.wait()
                        image_click(black_box_text.rect, black_box_wait)
                        if black_box_wait.type == MOUSEBUTTONDOWN:
                            break
            if button1.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        pygame.display.set_caption("Beware of vases")
                        hint_wait = event.wait()
                        if hint_wait.type == MOUSEBUTTONDOWN:
                            pygame.display.set_caption("House")
                            break
            if showerhead.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        pygame.display.set_caption("I didn't know that things would go this bad...")
                        hint_wait = event.wait()
                        if hint_wait.type == MOUSEBUTTONDOWN:
                            pygame.display.set_caption("House")
                            break
        #Interactions for the "third event" (lines 150 - 190)
        if bathroom_event == 2:
            if mirror.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        mirror_text = textsprite("Diediedie", "There's somebody behind you", 40, 100, 300, 255, 255, 255)
                        call_sprite(mirror_text, "Image", bathroom)
                        mirror_wait = event.wait()
                        image_click(mirror_text.rect, mirror_wait)
                        if mirror_wait.type == MOUSEBUTTONDOWN:
                            break
            if book.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    Ghost(bathroom, 'Bathroom.jpg', 'Scare.png', 250, 0)
                    lives_remaining -= 1
            if vase3.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    bathroom_event += 1
                    while True:
                        hint = imagesprite("paperhint5.png", 300, 100)
                        call_sprite(hint, "Image", bathroom)
                        hint_wait = event.wait()
                        image_click(hint.rect, hint_wait)
                        if hint_wait.type == MOUSEBUTTONDOWN:
                            break
            if button2.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        pygame.display.set_caption("Something resonates in one of the vases")
                        hint_wait = event.wait()
                        if hint_wait.type == MOUSEBUTTONDOWN:
                            pygame.display.set_caption("House")
                            break
            if showerhead.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        pygame.display.set_caption("Sometimes it's better to stop than to try")
                        hint_wait = event.wait()
                        if hint_wait.type == MOUSEBUTTONDOWN:
                            pygame.display.set_caption("House")
                            break
        #Interactions for the "fourth event" (lines 192 - 228)
        if bathroom_event == 3:
            if showerhead.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        pygame.display.set_caption("See you on the other side")
                        hint_wait = event.wait()
                        if hint_wait.type == MOUSEBUTTONDOWN:
                            pygame.display.set_caption("House")
                            break
            if button3.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        pygame.display.set_caption("We are behind times")
                        hint_wait = event.wait()
                        if hint_wait.type == MOUSEBUTTONDOWN:
                            pygame.display.set_caption("House")
                            break
            if clock.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    import Puzzle; Puzzle.Puzzle1()
                    break
            if black_box.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    Ghost(bathroom, 'Bathroom.jpg', 'Scare.png', 250, 0)
                    lives_remaining -= 1
            if book.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    Ghost(bathroom, 'Bathroom.jpg', 'Scare.png', 250, 0)
                    lives_remaining -= 1
            if black_stand.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    Ghost(bathroom, 'Bathroom.jpg', 'Scare.png', 250, 0)
                    lives_remaining -= 1
            if sink.collidepoint(mouse.get_pos()):
                if room2_wait.type == MOUSEBUTTONDOWN:
                    Ghost(bathroom, 'Bathroom.jpg', 'Scare.png', 250, 0)
                    lives_remaining -= 1

        pause_quit(room2_wait, bathroom)

        if lives_remaining == 0:
            Gameover()

        display.update()
