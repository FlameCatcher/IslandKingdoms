from Map import MapGenerator
import pygame, sys
import time
import random
from Functions import Functions_for_game
from Map.MapGenerator import generate_naturaly

""" Tiles """
W = 0  # Water
S = 1  # Sand
G = 2  # Grass
F = 3  # Forest
B = 4  # Bridge
M = 5  # Mountain
FARM = 6  # Farmland
T = -1 # Trader


""" Colours """
red = (255, 0, 0)
blue = (0, 0, 255)
sand_yellow = (194, 178, 128)
grass_green = (124, 252, 0)
forest_green = (0, 100, 0)
bridge =  (140, 80, 0)
mountain_gray = (169, 169, 169)
farm = (196, 196, 0)
trader = (100, 50, 0)

"""Linking Tile to Colour"""
TileColour = {
    W: blue,
    S: sand_yellow,
    G: grass_green,
    F: forest_green,
    B: bridge,
    M: mountain_gray,
    FARM: farm,
    T: trader
}

""" Map """

# first_map = [[W, W, W, W, W, W, W, W, W, W, W, W],  # 12
#              [W, W, W, S, S, S, S, S, S, S, S, W],
#              [W, W, S, S, S, G, G, G, G, F, S, W],  # aici
#              [W, W, S, G, G, F, F, F, G, S, S, W],
#              [S, W, W, S, G, F, F, G, S, W, W, W],
#              [F, S, W, W, S, G, G, G, G, S, W, W],
#              [F, G, S, W, W, S, S ,S ,S, S, S, W],
#              [F, F, G, S, W, W, W, W, W, W, W, W],
#              [F, F, G, G, S, S, S, S, S, S, S, S],
#              [G, W, G, G, G, F, F, F, F, F, F, G],
#              [G, G, G, G, F, G, F, G, G, G, F, F],
#              [G, G, G, G, G, F, F, F, F, F, F, F],
#              ]


# first_map = [
# [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
# [W, W, W, S, S, S, S, S, S, S, S, W, W, W, W, S, S, S, S, S, S, S, S, W, W, W, W, S, S, S, S, S, S, S, S, W, W, W, W],
# [W, W, S, S, S, G, G, G, G, F, S, W, W, W, S, S, S, G, G, G, G, F, S, W, W, W, S, S, S, G, G, G, G, F, S, W, W, W, S],
# [W, W, S, G, G, F, F, F, G, S, S, W, W, W, S, G, G, F, F, F, G, S, S, W, W, W, S, G, G, F, F, F, G, S, S, W, W, W, S],
# [S, W, W, S, G, F, F, G, S, W, W, W, S, W, W, S, G, F, F, G, S, W, W, W, S, W, W, S, G, F, F, G, S, W, W, W, S, W, W],
# [F, S, W, W, S, G, G, G, G, S, W, W, F, S, W, W, S, G, G, G, G, S, W, W, F, S, W, W, S, G, G, G, G, S, W, W, F, S, W],
# [F, G, S, W, W, S, S, S, S, S, S, W, F, G, S, W, W, S, S, S, S, S, S, W, F, G, S, W, W, S, S, S, S, S, S, W, F, G, S],
# [F, F, G, S, W, W, W, W, W, W, W, W, F, F, G, S, W, W, W, W, W, W, W, W, F, F, G, S, W, W, W, W, W, W, W, W, F, F, G],
# [F, F, G, G, S, S, S, S, S, S, S, S, F, F, G, G, S, S, S, S, S, S, S, S, F, F, G, G, S, S, S, S, S, S, S, S, F, F, G],
# [G, W, G, G, G, F, F, F, F, F, F, G, G, W, G, G, G, F, F, F, F, F, F, G, G, W, G, G, G, F, F, F, F, F, F, G, G, W, G],
# [G, G, G, G, G, F, F, F, F, F, F, F, G, G, G, G, F, F, F, F, F, F, F, F, G, G, G, G, F, F, F, F, F, F, F, F, G, G, G],
# [G, G, G, G, G, F, F, F, F, F, F, F, G, G, G, G, F, F, F, F, F, F, F, F, G, G, G, G, F, F, F, F, F, F, F, F, G, G, G],
# [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
# [W, W, W, S, S, S, S, S, S, S, S, W, W, W, W, S, S, S, S, S, S, S, S, W, W, W, W, S, S, S, S, S, S, S, S, W, W, W, W],
# [W, W, S, S, S, G, G, G, G, F, S, W, W, W, S, S, S, G, G, G, G, F, S, W, W, W, S, S, S, G, G, G, G, F, S, W, W, W, S],
# [W, W, S, G, G, F, F, F, G, S, S, W, W, W, S, G, G, F, F, F, G, S, S, W, W, W, S, G, G, F, F, F, G, S, S, W, W, W, S],
# [S, W, W, S, G, F, F, G, S, W, W, W, S, W, W, S, G, F, F, G, S, W, W, W, S, W, W, S, G, F, F, G, S, W, W, W, S, W, W],
# [F, S, W, W, S, G, G, G, G, S, W, W, F, S, W, W, S, G, G, G, G, S, W, W, F, S, W, W, S, G, G, G, G, S, W, W, F, S, W],
# [F, G, S, W, W, S, S, S, S, S, S, W, F, G, S, W, W, S, S, S, S, S, S, W, F, G, S, W, W, S, S, S, S, S, S, W, F, G, S],
# [F, F, G, S, W, W, W, W, W, W, W, W, F, F, G, S, W, W, W, W, W, W, W, W, F, F, G, S, W, W, W, W, W, W, W, W, F, F, G]
# ]

# first_map = generate_map(25, 25,1)

# print(len(first_map2),len(first_map2[0]))

"""Map Size"""
tile_size = 20
map_width = 24
map_height = 24

"""Players"""
# player_poz = [2, 2]
resurces = {
    "Wood" : 0,
    "Stone": 0,
    "Food" : 0,
    "Gold" : 0
}
facing = ["None"]

"""Create display"""
pygame.init()
window = pygame.display.set_mode((map_width * tile_size, map_height * tile_size))

first_map = generate_naturaly(map_width, map_height)

"""User interface"""

def main():
    run = True
    player_poz = Functions_for_game.spawn(first_map)
    print(first_map)

    while run:
        """ Draw """

        Functions_for_game.draw_map(first_map, window)
        Functions_for_game.draw_player(player_poz, window)

        """Quit from window"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            """ Actions """

            if event.type == pygame.KEYDOWN:
                key = event.key
                
                """ Movement """
                last_pos = player_poz[:]
                new_player_poz = Functions_for_game.move_player(key, player_poz, facing)
                x, y = new_player_poz
                if first_map[x][y] == W:
                    player_poz = last_pos[:]

                """ Controls """
                Functions_for_game.controls(key, player_poz, facing, first_map)

        """Update display"""
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
