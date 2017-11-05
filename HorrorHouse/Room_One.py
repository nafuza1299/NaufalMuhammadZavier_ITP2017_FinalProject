from pygame import *
from HouseClasses import *
from HouseFunctions import *

def transition_screen1():

    '''Opens the transition screen for the first Room'''

    music = sound("BackgroundMusic.wav")
    while True:
        transition_screen("Room 1")
        transition_wait = event.wait()
        display.update()
        if transition_wait.type == MOUSEBUTTONDOWN:
            screen1()

def screen1():

    '''Opens the first level of the game'''

    key = 0
    picturecount = 0
    door_unlock = 0
    scare = 0
    kharon = []
    Bedroom = MainScreen('Bedroom.jpg')
    while True:

        picture = pygame.draw.rect(Bedroom.display, ((0, 0, 0)), (0, 150, 100, 100))
        picturecross = pygame.draw.rect(Bedroom.display, ((0, 0, 0)), (545, 170, 50, 90))
        picturedoor = pygame.draw.rect(Bedroom.display, ((0, 0, 0)), (870, 140, 200, 390))
        drawer = pygame.draw.rect(Bedroom.display, ((0, 0, 0)), (510 , 350, 65, 50))
        ouija = pygame.draw.rect(Bedroom.display, ((0, 0, 0)), (670 ,535, 40, 25))
        medicine = pygame.draw.rect(Bedroom.display, ((0, 0, 0)), (145 , 340, 90, 50))
        cupboard = pygame.draw.rect(Bedroom.display, ((0, 0, 0)), (115 , 385, 150, 160))
        grab_key = textsprite("Diediedie","Do you want to grab the? (Yes)", 45, 300, 100, 255, 255, 255)
        Bedroom.display.blit(Bedroom.image, (0,0))

        room1_wait = event.wait()
        #Lines 41 - 42 adds the sound effects for clicking and hovering
        image_hover(picturecross), image_hover(drawer), image_hover(picturedoor), image_hover(grab_key.rect)
        image_click(picturecross, room1_wait), image_click(drawer, room1_wait), image_click(picturedoor, room1_wait), image_click(grab_key.rect, room1_wait)
        if picturecount < 3:
            image_hover(picture), image_click(picture, room1_wait)
        if key == 1 and door_unlock == 0:
            image_hover(ouija), image_click(ouija, room1_wait), image_hover(cupboard), image_click(cupboard, room1_wait)
        if picturecount < 3:
            image_hover(medicine), image_click(medicine, room1_wait)
        #Interaction with the picture (lines 50 - 66)
        if picturecount < 3:
            if picture.collidepoint(mouse.get_pos()):
                if room1_wait.type == MOUSEBUTTONDOWN:
                    picturecount +=1
                    while True:
                        family = imagesprite("Family.jpg", 100, 0)
                        call_sprite(family, "Image", Bedroom)
                        picture_wait = event.wait()
                        image_click(family.rect, picture_wait)
                        if family.rect.collidepoint(mouse.get_pos()):
                            if picture_wait.type == MOUSEBUTTONDOWN:
                                break
                        if picturecount == 3:
                            if family.rect.collidepoint(mouse.get_pos()):
                                if room1_wait.type == MOUSEBUTTONDOWN:
                                    Ghost(Bedroom, 'Bedroom.jpg', 'Scare.png', 250, 0)
                                break

        #Under the conditions in line 69, this will open the ouija board
        if key == 1 and door_unlock == 0:
            if ouija.collidepoint(mouse.get_pos()):
                '''Opens the ouija board'''
                if room1_wait.type == MOUSEBUTTONDOWN:
                    yes = textsprite("Diediedie", "Yes", 50, 100, 100, 255, 255, 255)
                    no = textsprite("Diediedie", "No", 50, 1000, 100, 255, 255, 255)
                    goodbye = textsprite("Diediedie", "Goodbye", 50, 480, 500, 255, 255, 255)
                    dash1 = textsprite("Diediedie", "_", 50, 400, 210, 255, 255, 255)
                    dash2 = textsprite("Diediedie", "_", 50, 450, 210, 255, 255, 255)
                    dash3 = textsprite("Diediedie", "_", 50, 500, 210, 255, 255, 255)
                    dash4 = textsprite("Diediedie", "_", 50, 550, 210, 255, 255, 255)
                    dash5 = textsprite("Diediedie", "_", 50, 600, 210, 255, 255, 255)
                    dash6 = textsprite("Diediedie", "_", 50, 650, 210, 255, 255, 255)
                    A = textsprite("Diediedie", "A", 50, 250, 275, 255, 255, 255)
                    B = textsprite("Diediedie", "B", 50, 300, 275, 255, 255, 255)
                    C = textsprite("Diediedie", "C", 50, 350, 275, 255, 255, 255)
                    D = textsprite("Diediedie", "D", 50, 400, 275, 255, 255, 255)
                    E = textsprite("Diediedie", "E", 50, 450, 275, 255, 255, 255)
                    F = textsprite("Diediedie", "F", 50, 500, 275, 255, 255, 255)
                    G = textsprite("Diediedie", "G", 50, 550, 275, 255, 255, 255)
                    H = textsprite("Diediedie", "H", 50, 600, 275, 255, 255, 255)
                    I = textsprite("Diediedie", "I", 50, 650, 275, 255, 255, 255)
                    J = textsprite("Diediedie", "J", 50, 700, 275, 255, 255, 255)
                    K = textsprite("Diediedie", "K", 50, 750, 275, 255, 255, 255)
                    L = textsprite("Diediedie", "L", 50, 800, 275, 255, 255, 255)
                    M = textsprite("Diediedie", "M", 50, 850, 275, 255, 255, 255)
                    N = textsprite("Diediedie", "N", 50, 250, 350, 255, 255, 255)
                    O = textsprite("Diediedie", "O", 50, 300, 350, 255, 255, 255)
                    P = textsprite("Diediedie", "P", 50, 350, 350, 255, 255, 255)
                    Q = textsprite("Diediedie", "Q", 50, 400, 350, 255, 255, 255)
                    R = textsprite("Diediedie", "R", 50, 450, 350, 255, 255, 255)
                    S = textsprite("Diediedie", "S", 50, 500, 350, 255, 255, 255)
                    T = textsprite("Diediedie", "T", 50, 550, 350, 255, 255, 255)
                    U = textsprite("Diediedie", "U", 50, 600, 350, 255, 255, 255)
                    V = textsprite("Diediedie", "V", 50, 650, 350, 255, 255, 255)
                    W = textsprite("Diediedie", "W", 50, 700, 350, 255, 255, 255)
                    X = textsprite("Diediedie", "X", 50, 750, 350, 255, 255, 255)
                    Y = textsprite("Diediedie", "Y", 50, 800, 350, 255, 255, 255)
                    Z = textsprite("Diediedie", "Z", 50, 850, 350, 255, 255, 255)
                    display.update()

                    while True:
                        text = Group(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, yes,no, goodbye, dash1, dash2, dash3, dash4, dash5, dash6)
                        text.draw(Bedroom.display)
                        ouija_wait = event.wait()
                        # Generates every element in the ouija board, if an element is highlighted, it will change color
                        if goodbye.rect.collidepoint(mouse.get_pos()):
                            goodbye = textsprite("Diediedie", "Goodbye", 50, 480, 500, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                reset_kharon()
                                break
                        else:
                            goodbye = textsprite("Diediedie", "Goodbye", 50, 480, 500, 255, 255, 255)

                        if B.rect.collidepoint(mouse.get_pos()):
                            B = textsprite("Diediedie", "B", 50, 300, 275, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            B = textsprite("Diediedie", "B", 50, 300, 275, 255, 255, 255)

                        if C.rect.collidepoint(mouse.get_pos()):
                            C = textsprite("Diediedie", "C", 50, 350, 275, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            C = textsprite("Diediedie", "C", 50, 350, 275, 255, 255, 255)

                        if D.rect.collidepoint(mouse.get_pos()):
                            D = textsprite("Diediedie", "D", 50, 400, 275, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            D = textsprite("Diediedie", "D", 50, 400, 275, 255, 255, 255)

                        if E.rect.collidepoint(mouse.get_pos()):
                            E = textsprite("Diediedie", "E", 50, 450, 275, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            E = textsprite("Diediedie", "E", 50, 450, 275, 255, 255, 255)

                        if F.rect.collidepoint(mouse.get_pos()):
                            F = textsprite("Diediedie", "F", 50, 500, 275, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            F = textsprite("Diediedie", "F", 50, 500, 275, 255, 255, 255)

                        if G.rect.collidepoint(mouse.get_pos()):
                            G = textsprite("Diediedie", "G", 50, 550, 275, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            G = textsprite("Diediedie", "G", 50, 550, 275, 255, 255, 255)

                        if I.rect.collidepoint(mouse.get_pos()):
                            I = textsprite("Diediedie", "I", 50, 650, 275, 255, 0, 0)
                            display.flip()
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            I = textsprite("Diediedie", "I", 50, 650, 275, 255, 255, 255)

                        if J.rect.collidepoint(mouse.get_pos()):
                            J = textsprite("Diediedie", "J", 50, 700, 275, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            J = textsprite("Diediedie", "J", 50, 700, 275, 255, 255, 255)

                        if L.rect.collidepoint(mouse.get_pos()):
                            L = textsprite("Diediedie", "L", 50, 800, 275, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            L = textsprite("Diediedie", "L", 50, 800, 275, 255, 255, 255)

                        if M.rect.collidepoint(mouse.get_pos()):
                            M = textsprite("Diediedie", "M", 50, 850, 275, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            M = textsprite("Diediedie", "M", 50, 850, 275, 255, 255, 255)

                        if P.rect.collidepoint(mouse.get_pos()):
                            P = textsprite("Diediedie", "P", 50, 350, 350, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            P = textsprite("Diediedie", "P", 50, 350, 350, 255, 255, 255)

                        if Q.rect.collidepoint(mouse.get_pos()):
                            Q = textsprite("Diediedie", "Q", 50, 400, 350, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            Q = textsprite("Diediedie", "Q", 50, 400, 350, 255, 255, 255)

                        if S.rect.collidepoint(mouse.get_pos()):
                            S = textsprite("Diediedie", "S", 50, 500, 350, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            S = textsprite("Diediedie", "S", 50, 500, 350, 255, 255, 255)

                        if T.rect.collidepoint(mouse.get_pos()):
                            T = textsprite("Diediedie", "T", 50, 550, 350, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            T = textsprite("Diediedie", "T", 50, 550, 350, 255, 255, 255)

                        if U.rect.collidepoint(mouse.get_pos()):
                            U = textsprite("Diediedie", "U", 50, 600, 350, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            U = textsprite("Diediedie", "U", 50, 600, 350, 255, 255, 255)

                        if V.rect.collidepoint(mouse.get_pos()):
                            V = textsprite("Diediedie", "V", 50, 650, 350, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            V = textsprite("Diediedie", "V", 50, 650, 350, 255, 255, 255)

                        if W.rect.collidepoint(mouse.get_pos()):
                            W = textsprite("Diediedie", "W", 50, 700, 350, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            W = textsprite("Diediedie", "W", 50, 700, 350, 255, 255, 255)

                        if X.rect.collidepoint(mouse.get_pos()):
                            X = textsprite("Diediedie", "X", 50, 750, 350, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            X = textsprite("Diediedie", "X", 50, 750, 350, 255, 255, 255)

                        if Y.rect.collidepoint(mouse.get_pos()):
                            Y = textsprite("Diediedie", "Y", 50, 800, 350, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            Y = textsprite("Diediedie", "Y", 50, 800, 350, 255, 255, 255)

                        if Z.rect.collidepoint(mouse.get_pos()):
                            Z = textsprite("Diediedie", "Z", 50, 850, 350, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                clicknoise = sound("Click.wav")
                                scare += 1
                        else:
                            Z = textsprite("Diediedie", "Z", 50, 850, 350, 255, 255, 255)

                        if K.rect.collidepoint(mouse.get_pos()):
                            K = textsprite("Diediedie", "K", 50, 750, 275, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                if "K" not in kharon:
                                    kharon.append("K")
                                clicknoise = sound("Click.wav")
                                K = textsprite("Diediedie", "K", 50, 400, 200, 255, 255, 255)
                                text = Group(K)
                                text.draw(Bedroom.display)
                        else:
                            K = textsprite("Diediedie", "K", 50, 750, 275, 255, 255, 255)

                        if H.rect.collidepoint(mouse.get_pos()):
                            H = textsprite("Diediedie", "H", 50, 600, 275, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                if "H" not in kharon:
                                    kharon.append("H")
                                clicknoise = sound("Click.wav")
                                H = textsprite("Diediedie", "H", 50, 450, 200, 255, 255, 255)
                                text = Group(H)
                                text.draw(Bedroom.display)
                        else:
                            H = textsprite("Diediedie", "H", 50, 600, 275, 255, 255, 255)

                        if A.rect.collidepoint(mouse.get_pos()):
                            A = textsprite("Diediedie", "A", 50, 250, 275, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                if "A" not in kharon:
                                    kharon.append("A")
                                clicknoise = sound("Click.wav")
                                A = textsprite("Diediedie", "A", 50, 500, 200, 255, 255, 255)
                                text = Group(A)
                                text.draw(Bedroom.display)
                        else:
                            A = textsprite("Diediedie", "A", 50, 250, 275, 255, 255, 255)

                        if R.rect.collidepoint(mouse.get_pos()):
                            R = textsprite("Diediedie", "R", 50, 450, 350, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                if "R" not in kharon:
                                    kharon.append("R")
                                clicknoise = sound("Click.wav")
                                R = textsprite("Diediedie", "R", 50,
                                               550, 200, 255, 255, 255)
                                text = Group(R)
                                text.draw(Bedroom.display)
                        else:
                            R = textsprite("Diediedie", "R", 50, 450, 350, 255, 255, 255)

                        if O.rect.collidepoint(mouse.get_pos()):
                            O = textsprite("Diediedie", "O", 50, 300, 350, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                if "O" not in kharon:
                                    kharon.append("O")
                                clicknoise = sound("Click.wav")
                                O = textsprite("Diediedie", "O", 50, 600, 200, 255, 255, 255)
                                text = Group(O)
                                text.draw(Bedroom.display)
                        else:
                            O = textsprite("Diediedie", "O", 50, 300, 350, 255, 255, 255)

                        if N.rect.collidepoint(mouse.get_pos()):
                            N = textsprite("Diediedie", "N", 50, 250, 350, 255, 0, 0)
                            if ouija_wait.type == MOUSEBUTTONDOWN:
                                if "N" not in kharon:
                                    kharon.append("N")
                                clicknoise = sound("Click.wav")
                                N = textsprite("Diediedie", "N", 50, 650, 200, 255, 255, 255)
                                text = Group(N)
                                text.draw(Bedroom.display)
                        else:
                            N = textsprite("Diediedie", "N", 50, 250, 350, 255, 255, 255)
                        #If the following elements (lines 357 - 362) is in the list, the event will unlock
                        if "K" in kharon:
                            if "H" in kharon:
                                if "A" in kharon:
                                    if "R" in kharon:
                                        if "O" in kharon:
                                            if "N" in kharon:
                                                door_unlock += 1
                                                unlock_sound = sound("Door Unlock.wav")
                                                kharon_wait = event.wait()
                                                if kharon_wait.type == MOUSEBUTTONDOWN:
                                                    while True:
                                                        warning_event = event.wait()
                                                        display.update()
                                                        pass
                                                break
                        if scare == 3:
                            while True:
                                Ghost(Bedroom, 'Bedroom.jpg', "Scare.png", 250, 0)
                                import HouseHub; HouseHub.Gameover()
                                break
                            break
                        display.update()

            display.update()
        #Interaction with the drawer (lines 382 - 422)
        if drawer.collidepoint(mouse.get_pos()):
            if key == 0 and picturecount < 3:
                if room1_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        blocking_drawer = textsprite("Diediedie","Something is blocking the drawer", 45, 300, 400, 255, 255, 255)
                        call_sprite(blocking_drawer, "Image", Bedroom)
                        drawer_wait = event.wait()
                        if drawer_wait.type == MOUSEBUTTONDOWN:
                            break
            if picturecount == 3:
                if room1_wait.type == MOUSEBUTTONDOWN:
                    picturecount += 1
                    while True:
                        open_drawer = textsprite("Diediedie","The drawer is now open", 45, 300, 500, 255, 255, 255)
                        call_sprite(open_drawer, "Image", Bedroom)
                        drawer_wait2 = event.wait()
                        if drawer_wait2.type == MOUSEBUTTONDOWN:
                            break
                    while True:
                             call_sprite(grab_key, "Image", Bedroom)
                             drawer_wait3 = event.wait()
                             if grab_key.rect.collidepoint(mouse.get_pos()):
                                 if drawer_wait3.type == MOUSEBUTTONDOWN:
                                    key += 1
                                    while True:
                                        obtained = textsprite("Diediedie","You obtained the key", 45, 300, 200, 255, 255, 255)
                                        call_sprite(obtained, "Image", Bedroom)
                                        drawer_wait4 = event.wait()
                                        if drawer_wait4.type == MOUSEBUTTONDOWN:
                                            break
                                        break
                                    break

            if picturecount == 4:
              if room1_wait.type == MOUSEBUTTONDOWN:
                while True:
                    empty = textsprite("Diediedie", "The drawer is empty", 45, 300, 400, 255, 255, 255)
                    call_sprite(empty, "Image", Bedroom)
                    wait = event.wait()
                    if wait.type == MOUSEBUTTONDOWN:
                        break
        #Interaction with cross picture (line 424 - 439)
        if picturecross.collidepoint(mouse.get_pos()):
            if room1_wait.type == MOUSEBUTTONDOWN:
                if key == 0:
                    while True:
                        presence = textsprite("Diediedie","You feel a presence", 45, 300, 400, 255, 255, 255)
                        call_sprite(presence, "Image", Bedroom)
                        presence_wait = event.wait()
                        if presence_wait.type == MOUSEBUTTONDOWN:
                            break
                else:
                    while True:
                        beneath = textsprite("Diediedie","Something is resonating beneath the bed", 45, 300, 400, 255, 255, 255)
                        call_sprite(beneath, "Image", Bedroom)
                        presence_wait = event.wait()
                        if presence_wait.type == MOUSEBUTTONDOWN:
                            break
        #Interaction with the door (lines 441 - 463)
        if picturedoor.collidepoint(mouse.get_pos()):
            if key == 0:
                if room1_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        locked = textsprite("Diediedie", "Its locked", 45, 300, 400, 255, 255, 255)
                        call_sprite(locked, "Image", Bedroom)
                        lock_wait = event.wait()
                        if lock_wait.type == MOUSEBUTTONDOWN:
                            break
            if door_unlock == 1:
                if room1_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        Ghost(Bedroom, 'Bedroom.jpg', 'Scare.png', 250, 0)
                        import Room_Two; Room_Two.transition_screen2()
                        break
            if key == 1:
                if room1_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        blocking = textsprite("Diediedie", "There's something blocking this door", 45, 300, 400, 255, 255, 255)
                        call_sprite(blocking, "Image", Bedroom)
                        block_wait = event.wait()
                        if block_wait.type == MOUSEBUTTONDOWN:
                            break
        #Interaction with the medicine (lines 465 - 473)
        if picturecount < 3:
            if medicine.collidepoint(mouse.get_pos()):
                if room1_wait.type == MOUSEBUTTONDOWN:
                    while True:
                        paper1 = imagesprite("paperhint1.png", 300, 100)
                        call_sprite(paper1, "Image", Bedroom)
                        hint_wait = event.wait()
                        if hint_wait.type == MOUSEBUTTONDOWN:
                            break
        #Text appears under the conditions of line 475 - 480
        if "K" in kharon:
            if "H" in kharon:
                if "A" in kharon:
                    if "R" in kharon:
                        if "O" in kharon:
                            if "N" in kharon:
                                leave = textsprite("YouMurderer BB", "Leave", 75, 600, 200, 255, 0, 0)
                                call_sprite(leave, "Image", Bedroom)
        #Interaction with the cupboard (lines 484 - 492)
        if key == 1 and door_unlock == 0:
            if cupboard.collidepoint(mouse.get_pos()):
                    if room1_wait.type == MOUSEBUTTONDOWN:
                        while True:
                            paper2 = imagesprite("paperhint2.png", 300, 100)
                            call_sprite(paper2, "Image", Bedroom)
                            hint_wait = event.wait()
                            if hint_wait.type == MOUSEBUTTONDOWN:
                                break

        pause_quit(room1_wait, Bedroom)
        display.update()
