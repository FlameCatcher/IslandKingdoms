from AddOns.Mechanics import gather_resources
from main_settings import *
import random
from AddOns import *
import pygame

def draw_map(mapp, window):
    """
    Draws the map
    :return: None
    """
    for row in range(map_height):
        for col in range(map_width):
            if mapp[row][col] == B:
                pygame.draw.rect(window, bridge,
                                 (col * tile_size, row * tile_size, tile_size - 5, tile_size - 5))
            else:
                pygame.draw.rect(window, TileColour[mapp[row][col]],
                                 (col * tile_size, row * tile_size, tile_size, tile_size))


def draw_player(player_poz, window):
    """
    Draws the player
    :return: None
    """
    pygame.draw.rect(window, red,
                     (player_poz[1] * tile_size + tile_size / 4, player_poz[0] * tile_size + tile_size / 4, tile_size - tile_size / 2, tile_size - tile_size / 2))

def move_player(keys, player_pos: list, facing: list):
    if keys == pygame.K_UP and player_pos[0] > 0:
        player_pos[0] -= 1
        facing[0] = "North"
    if keys == pygame.K_DOWN and player_pos[0] < map_height - 1:
        player_pos[0] += 1
        facing[0] = "South"
    if keys == pygame.K_LEFT and player_pos[1] > 0:
        player_pos[1] -= 1
        facing[0] = "West"
    if keys == pygame.K_RIGHT and player_pos[1] < map_width - 1:
        player_pos[1] += 1
        facing[0] = "East"

    return player_pos


def spawn(map):
    """
    Spawns the player on the first available tile
    :return: None
    """
    spawn_points = []
    for row in range(map_height):
        for col in range(map_width):
            if map[row][col] != W and map[row][col] == F:
                spawn_points.append([row, col])
    if len(spawn_points) > 0:
        return random.choice(spawn_points)
    else:
        for row in range(map_height):
            for col in range(map_width):
                if map[row][col] != W:
                    map[row][col] = F
                    return [row, col]


def controls(key, player_pos: list, facing: list, mapp):

    gather_resources(player_pos, key, mapp)

    if key == pygame.K_i:
        print(f"Wood: " + str(resurces["Wood"]))
        print(f"Stone: " + str(resurces["Stone"]))
        print(f"Gold: " + str(resurces["Gold"]))
        print(f"Food: " + str(resurces["Food"]))

    if key == pygame.K_LALT:
        print("Haaaaaaaaaa1")
        if resurces["Wood"] >= 10 and -1 < player_pos[0] < map_height and -1 < player_pos[1] < map_width:
            if player_pos[0] != map_height - 1 != 1 and player_pos[1] != map_width - 1 != 1:
                if facing[0] == "North":
                    if mapp[player_pos[0]-1][player_pos[1]] == 0:
                        mapp[player_pos[0]-1][player_pos[1]] = B
                elif facing[0] == "South":
                    if mapp[player_pos[0]+1][player_pos[1]] == 0:
                        mapp[player_pos[0]+1][player_pos[1]] = B
                elif facing[0] == "West":
                    if mapp[player_pos[0]][player_pos[1]-1] == 0:
                        mapp[player_pos[0]][player_pos[1]-1] = B
                elif facing[0] == "East":
                    if mapp[player_pos[0]][player_pos[1]+1] == 0:
                        mapp[player_pos[0]][player_pos[1]+1] = B

    what_face(key, facing)
    what_face(key, facing)


    pygame.display.update()

def what_face(key, facing: list):
    if key == pygame.K_w:
        facing[0] = "North"
    elif key == pygame.K_s:
        facing[0] = "South"
    elif key == pygame.K_a:
        facing[0] = "West"
    elif key == pygame.K_d:
        facing[0] = "East"
