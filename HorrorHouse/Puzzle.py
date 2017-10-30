from pygame import *
from HouseClasses import *
from HouseFunctions import*
from random import *

pygame.init()

def Puzzle1():

    '''Opens the first screen of the puzzle'''

    music = sound("BackgroundMusic.wav")
    screen = pygame.display.set_mode((1120, 560))
    pygame.display.set_caption("There's no cure for loneliness")
    background_image = pygame.image.load("Bathroom.jpg")
    puzzle_pos = imagesprite('Position1.png', 299, 111)
    puzzle = imagesprite('puzzleholder.png', 300, 100)
    puzzle1 = imagesprite('puzzle1.png', randint(0, 800), randint(0, 300))
    while True:
        screen.blit(background_image,(0,0))
        puzzle_call = Group(puzzle1, puzzle)
        puzzle_call.draw(screen)
        puzzle_wait = event.wait()
        if puzzle1.rect.collidepoint(mouse.get_pos()):
            if puzzle_wait.type == MOUSEBUTTONDOWN:
                image_click(puzzle1.rect, puzzle_wait)
                while True:
                    for event1 in pygame.event.get():
                        if event1.type == pygame.QUIT:
                            pygame.quit()
                    mx,my = pygame.mouse.get_pos()
                    screen.blit(background_image,(0,0))
                    puzzle_call = Group(puzzle)
                    puzzle_call.draw(screen)
                    screen.blit(puzzle1.image, (mx-100,my-100))
                    pygame.display.flip()
                    move_wait = event.wait()
                    if puzzle_pos.rect.collidepoint(mouse.get_pos()):
                        if move_wait.type == MOUSEBUTTONDOWN:
                            image_click(puzzle_pos.rect, move_wait)
                            Puzzle2()
                    if move_wait.type == QUIT:
                        pygame.quit()
                        break
        display.update()

def Puzzle2():

    '''Opens the second screen of the puzzle'''

    music = sound("BackgroundMusic.wav")
    screen = pygame.display.set_mode((1120, 560))
    pygame.display.set_caption("But at least I have you")
    background_image = pygame.image.load("Bathroom.jpg")
    puzzle_pos = imagesprite('Position2.png', 685, 275)
    puzzle = imagesprite('puzzleholder.png', 300, 100)
    puzzle1 = imagesprite('puzzle1.png', 302, 105)
    puzzle2 = imagesprite('puzzle2.png', randint(0, 800), randint(0, 300))
    while True:
        screen.blit(background_image,(0,0))
        puzzle_call = Group(puzzle1, puzzle, puzzle2)
        puzzle_call.draw(screen)
        puzzle_wait = event.wait()
        if puzzle2.rect.collidepoint(mouse.get_pos()):
            if puzzle_wait.type == MOUSEBUTTONDOWN:
                image_click(puzzle2.rect, puzzle_wait)
                while True:
                    for event1 in pygame.event.get():
                        if event1.type == pygame.QUIT:
                            pygame.quit()
                    mx,my = pygame.mouse.get_pos()
                    screen.blit(background_image,(0,0))
                    puzzle_call = Group(puzzle, puzzle1)
                    puzzle_call.draw(screen)
                    screen.blit(puzzle2.image, (mx-300,my-100))
                    pygame.display.flip()
                    move_wait = event.wait()
                    if puzzle_pos.rect.collidepoint(mouse.get_pos()):
                        if move_wait.type == MOUSEBUTTONDOWN:
                            image_click(puzzle_pos.rect, move_wait)
                            Puzzle3()
                    if move_wait.type == QUIT:
                        pygame.quit()
                        break
        display.update()

def Puzzle3():

    '''Opens the third screen of the puzzle'''

    music = sound("BackgroundMusic.wav")
    screen = pygame.display.set_mode((1120, 560))
    background_image = pygame.image.load("Bathroom.jpg")
    pygame.display.set_caption("Tonight The World Dies")
    puzzle_pos = imagesprite('Position3.png', 310, 325)
    puzzle = imagesprite('puzzleholder.png', 300, 100)
    puzzle1 = imagesprite('puzzle1.png', 302, 105)
    puzzle2 = imagesprite('puzzle2.png', 454, 310)
    puzzle3 = imagesprite('puzzle3.png', randint(0, 800), randint(0, 300))
    while True:
        screen.blit(background_image,(0,0))
        puzzle_call = Group(puzzle1, puzzle, puzzle2, puzzle3)
        puzzle_call.draw(screen)
        puzzle_wait = event.wait()
        if puzzle3.rect.collidepoint(mouse.get_pos()):
            if puzzle_wait.type == MOUSEBUTTONDOWN:
                image_click(puzzle3.rect, puzzle_wait)
                while True:
                    for event1 in pygame.event.get():
                        if event1.type == pygame.QUIT:
                            pygame.quit()
                    mx,my = pygame.mouse.get_pos()
                    screen.blit(background_image,(0,0))
                    puzzle_call = Group(puzzle, puzzle1, puzzle2)
                    puzzle_call.draw(screen)
                    screen.blit(puzzle3.image, (mx-20, my-100))
                    pygame.display.flip()
                    move_wait = event.wait()
                    if puzzle_pos.rect.collidepoint(mouse.get_pos()):
                        if move_wait.type == MOUSEBUTTONDOWN:
                            image_click(puzzle_pos.rect, move_wait)
                            Puzzle4()
                    if move_wait.type == QUIT:
                        pygame.quit()
                        break
        display.update()

def Puzzle4():

    '''Opens the fourth screen of the puzzle'''

    music = sound("BackgroundMusic.wav")
    screen = pygame.display.set_mode((1120, 560))
    background_image = pygame.image.load("Bathroom.jpg")
    pygame.display.set_caption("")
    pygame.display.set_caption("But I will always be here")
    puzzle_pos = imagesprite('Position4.png', 615, 110)
    puzzle = imagesprite('puzzleholder.png', 300, 100)
    puzzle1 = imagesprite('puzzle1.png', 302, 105)
    puzzle2 = imagesprite('puzzle2.png', 454, 310)
    puzzle3 = imagesprite('puzzle3.png', 310, 292)
    puzzle4 = imagesprite('puzzle4.png', randint(0, 800), randint(0, 300))
    while True:
        screen.blit(background_image,(0,0))
        puzzle_call = Group(puzzle1, puzzle, puzzle2, puzzle3, puzzle4)
        puzzle_call.draw(screen)
        puzzle_wait = event.wait()
        if puzzle4.rect.collidepoint(mouse.get_pos()):
            if puzzle_wait.type == MOUSEBUTTONDOWN:
                image_click(puzzle4.rect, puzzle_wait)
                while True:
                    for event1 in pygame.event.get():
                        if event1.type == pygame.QUIT:
                            pygame.quit()
                    mx,my = pygame.mouse.get_pos()
                    screen.blit(background_image,(0,0))
                    puzzle_call = Group(puzzle, puzzle1, puzzle2, puzzle3)
                    puzzle_call.draw(screen)
                    screen.blit(puzzle4.image, (mx-230, my-100))
                    pygame.display.flip()
                    move_wait = event.wait()
                    if puzzle_pos.rect.collidepoint(mouse.get_pos()):
                        if move_wait.type == MOUSEBUTTONDOWN:
                            image_click(puzzle_pos.rect, move_wait)
                            Puzzle5()
                    if move_wait.type == QUIT:
                        pygame.quit()
                        break
        display.update()

def Puzzle5():

    '''Opens the last screen of the puzzle'''

    music = sound("BackgroundMusic.wav")
    puzzle_screen = MainScreen("Bathroom.jpg")
    pygame.display.set_caption("Goodbye")
    puzzle = imagesprite('puzzleholder.png', 300, 100)
    puzzle1 = imagesprite('puzzle1.png', 302, 105)
    puzzle2 = imagesprite('puzzle2.png', 454, 310)
    puzzle3 = imagesprite('puzzle3.png', 310, 292)
    puzzle4 = imagesprite('puzzle4.png', 530, 115)
    while True:
        puzzle_call = Group(puzzle1, puzzle, puzzle2, puzzle3, puzzle4)
        puzzle_call.draw(puzzle_screen.display)
        puzzle_wait = event.wait()
        if puzzle_wait.type == MOUSEBUTTONDOWN:
            while True:
                Ghost(puzzle_screen, 'Bathroom.jpg', 'Scare.png', 250, 0)
                import HouseHub; HouseHub.Outro()
                break
        display.update()
