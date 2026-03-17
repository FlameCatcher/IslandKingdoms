import pygame
import random
from main_settings import *

def trade():
    if resurces["Stone"] == 0 or resurces["Food"] == 0 or resurces["Wood"] == 0:
        print("Not enough resources to trade! Need at least 1 of each")
    else:
        resurces["Wood"] -= 1
        resurces["Food"] -= 1
        resurces["Stone"] -= 1
        resurces["Gold"] += 1

def gather_resources (player_pos, key, mapp):
    tile = mapp[player_pos[0]][player_pos[1]]
    if key  == pygame.K_SPACE:
        if tile == F:
            resurces["Wood"] += 1
        elif tile == M:
            resurces["Stone"] += 1
        elif tile == FARM:
            resurces["Food"] += 1
        elif tile == T:
            trade()

def generate_trader(mapp):
    positions = []
    for i in range(map_width):
        for j in range(map_height):
            if mapp[i][j] != W:
                if 0 < i < map_width - 1 and  0 < j < map_height - 1:
                    if mapp[i][j-1] != W and mapp[i][j+1] != W and mapp[i-1][j] != W and mapp[i+1][j] != W:
                        positions.append((i, j))

    trader_pos = random.choice(positions)
    mapp[trader_pos[0]][trader_pos[1]] = T
    return