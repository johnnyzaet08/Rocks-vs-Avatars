import pygame
import animation
import level
import random
import images
import battlefield
import avatar
import rook
import rookattack
import coins
import time
import csv
import numpy as np
from classs import *

pygame.init()

# Set matrix and time when load_game
load_game = False
matriz = []
load_time = 0

def play(user_name, configuraciones, kills):
    rook.rook_attack_frequency = configuraciones[8]
    avatar.set_values_avatars(configuraciones)

    # init music and music background
    pygame.mixer.init()
    nivel1_music = 'Sonidos/nivel1.mp3'
    pygame.mixer.music.load(nivel1_music)

    # set win and lose sounds
    win_sound = pygame.mixer.Sound('Sonidos/winsound.wav')
    gameover_sound = pygame.mixer.Sound('Sonidos/gameoversound.wav')

    GAME_TITLE = "Battle: Avatars vs Rookies"

    # screen dimensions
    SCREEN_SIZE = (1200, 700)
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # screen settings
    pygame.display.set_caption(GAME_TITLE)
    pygame.display.set_icon(images.ARCHER_AVATAR_IMG)
    
    # create battle field
    battle_field = battlefield.BattleField()

    # main

    timer_font = pygame.font.SysFont(None, 50)
    coins_font = pygame.font.SysFont(None, 80)
    user_font = pygame.font.SysFont(None, 60)
    level_font = pygame.font.SysFont(None, 100)
    kills_font = pygame.font.SysFont(None, 25)

    FPS = 60
    clock = pygame.time.Clock()

    # set timer
    start_time = pygame.time.get_ticks()

    # set user text
    user = user_name
    user_text = user_font.render(user, True, (255, 255, 255))
    user_textrect = user_text.get_rect()
    user_textrect.center = (420, 60)

    # set game over text
    game_text = coins_font.render(str("GAME"), True, (255, 255, 255))
    game_textrect = game_text.get_rect()
    game_textrect.center = (470, 300)
    screen.blit(game_text, game_textrect)
    over_text = coins_font.render(str("OVER"), True, (255, 255, 255))
    over_textrect = over_text.get_rect()
    over_textrect.center = (670, 300)

    # set level
    Level = level.Level(1, level.AVATARS_NIVEL1, images.BACKGROUND1_IMG, level.TIMEFORAVATAR_NIVEL1)

    # set animation
    animation_time = 5 * FPS

    # main
    running = True
    playing = True
    victory = False
    paused = False
    selected_rook_value = None
    selected_coin = False
    game = None
    over = None
    victorysound = None
    ranking = True
    save = False
    musica = True
    musicstate = 0

    # load game
    if load_game:
        battle_field.total_kills = kills
        start_time -= load_time
        battle_field.set_matrix(matriz)
        battle_field.find_avatar_and_move()

    # create first avatar
    battle_field.place(9, 2, avatar.Avatar(avatar.ARCHER_VALUES))

    while running:
        #pos del mouse
        pos = pygame.mouse.get_pos()
        
        if save == True:
            matrix = battle_field.get_matrix()
            kills = battle_field.get_kills()
            with open('PartidaG/'+user_name, 'w') as saved:
                saved.write(str(pygame.time.get_ticks()-start_time)+'\n')
                saved.write(str(kills)+'\n')
                saved.write(str(coins.total_coins)+'\n')
                saved.write(str(configuraciones)+'\n')
            with open('PartidaG/'+user_name+'Matrix.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(matrix)
            save = False
                            
            
        if playing:
            screen.fill(images.TEAL)
            screen.blit(Level.background, [0, 0])

            #Save bottom
            save = Button('Imagenes/save.png','Imagenes/save1.png')
            save.setCords(1100,20), save.setrangeEnd(50,50), save.draw(screen, pos)

            if musicstate == 0:
                if musica == True:
                    music = Button('Imagenes/musicon.png','Imagenes/musicoff.png')
                    music.setCords(600,20), music.setrangeEnd(50,50)
                    pygame.mixer.music.play(-1)
                    musicstate = 1
                elif musica == False:
                    music.setimage('Imagenes/musicon.png','Imagenes/musicoff.png')
                    pygame.mixer.music.stop()
                    musicstate = 1
            music.draw(screen, pos)

            # get time
            minutes = (pygame.time.get_ticks() - start_time) // 1000 // 60
            seconds = (pygame.time.get_ticks() - start_time) // 1000 - minutes * 60
            milliseconds = ((pygame.time.get_ticks() - start_time) // 10 - seconds * 100) // 10 - 600 * minutes    

            # check win
            if battle_field.total_kills == level.AVATARS_NIVEL1 + level.AVATARS_NIVEL2 + level.AVATARS_NIVEL3:
                time.sleep(1)
                final_ticks = pygame.time.get_ticks()
                final_time = [minutes, seconds, milliseconds]
                playing = False
                victory = True

            # check loss
            if battle_field.lost:
                time.sleep(1)
                playing = False
                victory = False

            # set level
            if Level.check_level(battle_field.total_kills):
                battle_field.clear_level()

            # create timer text
            timer_text = timer_font.render(str(minutes) + ":" + str(seconds) + ":" + str(milliseconds), True,
                                       (255, 255, 255))
            timer_textrect = timer_text.get_rect()
            timer_textrect.center = (75, 520)
            screen.blit(timer_text, timer_textrect)

            # create coins text
            coins_text = coins_font.render(str(coins.total_coins), True, (255, 255, 255))
            coins_textrect = coins_text.get_rect()
            coins_textrect.center = (900, 50)
            screen.blit(coins_text, coins_textrect)

            # create user text
            screen.blit(user_text, user_textrect)

            level_text = level_font.render("LVL" + str(Level.level), True, (255, 255, 255))
            level_textrect = level_text.get_rect()
            level_textrect.center = (270, 50)
            screen.blit(level_text, level_textrect)

            # create total kills text
            kills_text = kills_font.render("Total Kills: " + str(battle_field.total_kills), True, (255, 255, 255))
            kills_textrect = kills_text.get_rect()
            kills_textrect.center = (75, 560)
            screen.blit(kills_text, kills_textrect)

            battle_field.draw_matrix(battlefield.MATRIX_STARTX, battlefield.MATRIX_STARTY, screen)
            battle_field.place_avatar(Level.timeforavatar)
            battle_field.find_avatar_and_move()
            battle_field.place_coin()
            battle_field.remove_coin()
            battle_field.launch_rook_attack(screen)
            battle_field.launch_avatar_attack(screen)

            rook.draw_constant_rooks(screen)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                    if event.key == pygame.K_SPACE:
                        paused = not paused

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_battlefield = battle_field.mouse_pos_to_matrix(pos)

                    if save.pressed(pos):
                        save = True
                    if music.pressed(pos):
                        if musica == True:
                            musica = False
                            musicstate = 0
                        else:
                            musica = True
                            musicstate = 0
                        
                    if pos_battlefield:

                        if selected_rook_value:
                            coins.total_coins -= rook.get_rook_cost(rook.Rook(selected_rook_value))

                            if coins.total_coins >= 0:

                                if not isinstance(battle_field.get(pos_battlefield[0], pos_battlefield[1]),
                                              (avatar.Avatar, coins.Coin)):
                                    battle_field.place(pos_battlefield[0], pos_battlefield[1],
                                                   rook.Rook(selected_rook_value))

                            else:
                                coins.total_coins += rook.get_rook_cost(rook.Rook(selected_rook_value))
                            selected_rook_value = False

                        elif isinstance(battle_field.get(pos_battlefield[0], pos_battlefield[1]), rook.Rook):
                            battle_field.remove(pos_battlefield[0], pos_battlefield[1])

                        else:
                            element = battle_field.get(pos_battlefield[0], pos_battlefield[1])

                            if isinstance(element, coins.Coin):
                                battle_field.remove(pos_battlefield[0], pos_battlefield[1])
                                coins.add_coin(element)

                    pos_left_margin = rook.find_selected_rook(pos)
                    if pos_left_margin:
                        selected_rook_value = rook.assign_selected_rook(pos_left_margin)

                if not paused:
                    counting_time = pygame.time.get_ticks() - start_time
                    counting_minutes = str(counting_time / 1000)
                
        else:
            if victory:
                screen.fill(images.BLACK)
                screen.blit(images.VICTORY_IMG, [0, 0])
                pygame.mixer_music.stop()
                if ranking == True:
                    with open('ranking.csv', 'a', newline='') as csvfile:
                        name = user_name
                        tiempo = final_time[0]*60 + final_time[1] + final_time[2]/10
                        fieldnames = ['Name', 'Time']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writerow({'Name': name, 'Time': tiempo})
                        ranking = False
                if victorysound:
                    time.sleep(0.5)
                    if not animation.end_animation():
                        total_ticks = pygame.time.get_ticks() - final_ticks
                        screen.blit(animation.display_broken_attacks(total_ticks)[0], [animation.display_broken_attacks(total_ticks)[1], 300])
                    else:
                        running = False
                    minutes = final_time[0]
                    seconds = final_time[1]
                    milliseconds = final_time[2]
                    timer_text = timer_font.render("YOUR TIME: " + str(minutes) + ":" + str(seconds) + ":" + str(milliseconds), True,
                                               (255, 255, 255))
                    timer_textrect = timer_text.get_rect()
                    timer_textrect.center = (610, 330)
                    screen.blit(timer_text, timer_textrect)
                    pass
                else:
                    win_sound.play()
                    victorysound = True
            else:
                screen.fill(images.BLACK)
                pygame.mixer_music.stop()
                if over:
                    time.sleep(1.5)
                    running = False
                if game:
                    time.sleep(1)
                    screen.blit(game_text, game_textrect)
                    screen.blit(over_text, over_textrect)
                    over = True
                else:
                    gameover_sound.play()
                    time.sleep(0.5)
                    game = True
                    screen.blit(game_text, game_textrect)


            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

        pygame.display.update()

        clock.tick(FPS)
