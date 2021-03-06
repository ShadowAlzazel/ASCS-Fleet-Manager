import pygame, sys, time
from pygame.constants import K_DOWN, K_ESCAPE, K_F4, K_LALT, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, QUIT, K_c, K_e, K_i, K_m, K_r, K_x, K_z
from gameField import *
from levelLogger import *
from pygame.locals import *

#-----------------------------------------------------------------------
#main game function
def main():
    pygame.init()
    screen_flags = FULLSCREEN | SCALED
    #screen_flags = SCALED 

    #set up main game screen
    pygame.display.set_caption("INVICTUS: SAMAR")
    pygame.display.set_icon(GAME_ICON)
    game_screen = pygame.display.set_mode((LENGTH, WIDTH), screen_flags, 8)
    game_screen.blit(FIT_SPACE, (0, 0))
    pygame.mouse.set_visible(False)
    pygame.display.update()

    global game_font_2A
    game_font_4A = Font(FONT_2A, 3)
    game_font_2A = Font(FONT_1A, 3)

    #variables
    main_running = True
    mouse_clicked = False

    #time
    game_clock = pygame.time.Clock()

    while main_running:
        game_clock.tick(MENU_FPS)
        game_screen.blit(FIT_SPACE, (0, 0))
        mx, my = pygame.mouse.get_pos()

        #menu buttons
        button_menu_start = pygame.Rect((LENGTH // 2) - (48 * 2), WIDTH // 4, 48 * 4, 18)
        if button_menu_start.collidepoint((mx, my)) and mouse_clicked: 
            level_selector(game_screen)

        pygame.draw.rect(game_screen, (2, 2, 2), button_menu_start)
        game_font_2A.render_font(game_screen, 'INVICTUS SAMAR', ((LENGTH // 2) - (48 * 2), WIDTH // 4))

        #event loop
        mouse_clicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Quitting...")
                main_running = False 
                pygame.quit()
                sys.exit()

            if (event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == KEYDOWN and event.key == K_LALT and event.key == K_F4):
                print("Quitting...")
                main_running = False
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True 

        
        mouse_GUI(game_screen, 'L')
        pygame.display.update()
    #end game

#------------------------------------------------------------------------------------------
#menu for combat 
def level_selector(game_screen):

    #variables 
    game_running = True
    mouse_clicked = False 

    #time 
    game_clock = pygame.time.Clock()

    while game_running:
        game_clock.tick(MENU_FPS)
        game_screen.blit(FIT_SPACE, (0, 0))
        mx, my = pygame.mouse.get_pos()

        button_game_selecter = pygame.Rect(16, 32, 48 * 4, 48)
        if button_game_selecter.collidepoint((mx, my)) and mouse_clicked:
            #WIP currently testing presets
            #have different buttons change level number and create levels
            level = "level_Test" 
            combat_game(game_screen, level)

        pygame.draw.rect(game_screen, (2, 2, 2), button_game_selecter)
        game_font_2A.render_font(game_screen, 'COMBAT GAME L', (16, 32))

        #event loop
        mouse_clicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Quitting...")
                game_running = False 

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                print("Quitting...")
                game_running = False 

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True 

        mouse_GUI(game_screen)
        pygame.display.update() 


#-------------------------------------------------------------------------------------------
#combat game
def combat_game(game_screen, selcted_level):
    
    #levels
    combat_level = level(selcted_level)
    if not combat_level:
        return

    #create new game window
    combat_screen = map_screen(combat_level.level_hex_map, game_screen, HEX_SIZE)
    combat_level.map_game.next_fleet_turn()
    combat_screen.draw_hexes(combat_level.map_game.active_fleet.fleet_command)
    pygame.display.update()

    #animation calls
    animate_game_hexes = pygame.USEREVENT + 1
    pygame.time.set_timer(animate_game_hexes, 250)


    #variables 
    game_running = True 
    move_window_up, move_window_down, move_window_left, move_window_right = False, False, False, False
    framerate = GAME_FPS

    #time 
    game_clock = pygame.time.Clock()
    last_frame_time = time.perf_counter()
    last_second = time.perf_counter()
    a = 0

    while game_running:
        game_clock.tick(framerate)
        key_update = False 
        old_mouse_coordinate = (0, 0)
        animation_update = False 

        #frame timing
        dt = time.perf_counter() - last_frame_time
        dt *= framerate 
        last_frame_time = time.perf_counter()
        move_window_pixels = combat_screen.measurements['hex_pixel_size'] // 16

        #frame counting 
        a += 1
        if time.perf_counter() > last_second + 1:
            last_second = time.perf_counter()
            print("True FPS:", a) 
            a = 0
        
        #event loop
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Quitting...")
                game_running = False 

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                print("Quitting...")
                game_running = False 

            if event.type == KEYDOWN:
                key_update = True

            #window movement
            if event.type == KEYDOWN and event.key == K_UP:
                move_window_up = True
            if event.type == KEYUP and event.key == K_UP:
                move_window_up = False

            if event.type == KEYDOWN and event.key == K_DOWN:
                move_window_down = True
            if event.type == KEYUP and event.key == K_DOWN:
                move_window_down = False

            if event.type == KEYDOWN and event.key == K_LEFT:
                move_window_left = True
            if event.type == KEYUP and event.key == K_LEFT:
                move_window_left = False

            if event.type == KEYDOWN and event.key == K_RIGHT:
                move_window_right = True
            if event.type == KEYUP and event.key == K_RIGHT:
                move_window_right = False

            #reset window
            if event.type == KEYDOWN and event.key == K_c:
                combat_screen.measurements['moved_X'] = 0
                combat_screen.measurements['moved_Y'] = 0

            #end turn 
            if event.type == KEYDOWN and event.key == K_e:
                print('Fleet Turn Ended')
                combat_level.map_game.next_fleet_turn()
                #combat_screen.draw_hexes(combat_level.map_game.active_fleet.fleet_command, combat_level.map_game.selected_hex)

            #inspect
            if event.type == KEYDOWN and event.key == K_i:
                if combat_level.map_game.selected_hex:
                    combat_level.map_game.selected_hex.entity.full_inspect()

            #zooming
            if event.type == KEYDOWN and event.key == K_z:
                combat_screen.zoom_in_window()
                move_window_pixels = combat_screen.measurements['hex_pixel_size'] // 16
                #combat_screen.draw_hexes(combat_level.map_game.active_fleet.fleet_command, combat_level.map_game.selected_hex)

            if event.type == KEYDOWN and event.key == K_x:
                combat_screen.zoom_out_window()
                move_window_pixels = combat_screen.measurements['hex_pixel_size'] // 16
                #combat_screen.draw_hexes(combat_level.map_game.active_fleet.fleet_command, combat_level.map_game.selected_hex)

            #center
            if event.type == KEYDOWN and event.key == K_SPACE:
                if combat_level.map_game.selected_hex:
                    combat_screen.center_hex = combat_level.map_game.selected_hex.hex_coordinate_index

            #animate
            if event.type == animate_game_hexes: # and not (move_window_right or move_window_left or move_window_up or move_window_down)
                combat_screen.animate_hexes()
                animation_update = True 
                #combat_screen.draw_hexes(combat_level.map_game.active_fleet.fleet_command, combat_level.map_game.selected_hex)

            if event.type == pygame.MOUSEBUTTONDOWN:
                some_mouse_hex = pygame.mouse.get_pos()
                some_hex_coordinate_index = combat_screen.get_mouse_hex(some_mouse_hex)
                combat_screen.selected_hex_index_coordinate = some_hex_coordinate_index
                if some_hex_coordinate_index >= 0:
                    combat_level.map_game.select_hex(combat_level.level_hex_map.space_hexes[some_hex_coordinate_index])
                print(some_hex_coordinate_index)
                #combat_screen.draw_hexes(combat_level.map_game.active_fleet.fleet_command, combat_level.map_game.selected_hex)


        #move window
        if move_window_up:
            combat_screen.measurements['moved_Y'] += move_window_pixels
        if move_window_down:
            combat_screen.measurements['moved_Y'] -= move_window_pixels
        if move_window_left:
            combat_screen.measurements['moved_X'] += move_window_pixels
        if move_window_right:
            combat_screen.measurements['moved_X'] -= move_window_pixels


        #mouse GUI
        new_mouse_coordinate = pygame.mouse.get_pos()
        if new_mouse_coordinate != old_mouse_coordinate or key_update or animation_update:
            combat_screen.draw_hexes(combat_level.map_game.active_fleet.fleet_command, combat_level.map_game.selected_hex)
            mouse_hex_coordinate = combat_screen.get_mouse_hex(new_mouse_coordinate)
            mouse_GUI(game_screen, mouse_hex_coordinate, combat_level.map_game)

        old_mouse_coordinate = new_mouse_coordinate
        pygame.display.update()


# -------------------------------MOUSE-FUNCTIONS--------------------------
#@lru_cache(maxsize=1)
def mouse_GUI(a_screen, mouse_hex=-1, a_game=None):
    mouse_circle = pygame.mouse.get_pos()
    mouse_color = TRUE_WHITE

    if a_game:
        if a_game.selected_hex:
            mouse_color = CLICK_YELLOW
            if mouse_hex > -1 and a_game.ops_hex_map.space_hexes[mouse_hex].entity:
                if a_game.ops_hex_map.space_hexes[mouse_hex] == a_game.selected_hex:
                    mouse_color = CLICK_YELLOW
                elif a_game.ops_hex_map.space_hexes[mouse_hex].entity.command[0:3] == a_game.active_fleet.fleet_command[0:3]:
                    mouse_color = ALLY_GREEN
                else: 
                    mouse_color = TARGET_RED
    
    pygame.draw.circle(a_screen, mouse_color, mouse_circle, radius=3, width=1)
    pygame.draw.circle(a_screen, mouse_color, mouse_circle, radius=5, width=1)


#-------------------------------------------------------------------------------------------
#this is a runnable script
if __name__ == '__main__':
    main()