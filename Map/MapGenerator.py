import random
from contextlib import nullcontext

from AddOns import Mechanics

posibilities = [
    (0, 0.15),
    (1, 0.10),
    (2, 0.30),
    (3, 0.15),
    (5, 0.15),
    (6, 0.15)

]



def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

def generate_map(width: int, height: int, type = 0) -> list:
    if not isinstance(type, int):
        raise TypeError("Type must be an integer")

    options = {
        0: generate_Island(width, height),
        1: generate_Islands(width, height),
        2: generate_Continent(width, height),
    }
    option = options.get(type)
    return option


def generate_Island(width: int, height: int) -> list:
    harta = []
    for i in range(height):
        harta.append([])
        for j in range(width):
            if i == 0 or j == 0 or i == height - 1 or j == width - 1:
                tile = W
            else:
                tile = random.choice((W, S, G, F))
            harta[i].append(tile)

    return harta

def generate_Continent(width: int, height: int) -> list:
    harta = []
    for i in range(height):
        harta.append([])
        for j in range(width):
            tile = random.choice((S, G, F))
            harta[i].append(tile)

    return harta


def generate_Islands(width: int, height: int) -> list:
    harta = []
    if width < 20 and height < 20:
        raise Exception("Map too small for more than 1 Island")
    islands = random.choice(range(2, 5))
    if is_prime(width) or is_prime(height):
        islands = 1

    if width % 2 == 0 and height % 2 == 0:
        harta = evenheight_evenwidth(height, width)
    elif width % 2 == 0 and height % 2 != 0:
        harta = oddheight_evenwidth(height, width)
    elif width % 2 != 0 and height % 2 == 0:
        harta = evenheight_oddwidth(height, width)
    else:
        harta = oddheight_oddwidth(height, width)


    # for i in range(height):
    #     harta.append([])
    #     for j in range(width):
    #         if mid_width1 == mid_width2 == mid_width3 and mid_height1 == mid_height2 == mid_height3:
    #             if i == 0 or j == 0 or i == height - 1 or j == width - 1 or i == mid_height1 or j == mid_width1:
    #                 tile = W
    #             else:
    #                 water = random.choice((True, False, False, False))
    #                 if water:
    #                     tile = random.choice((W, S, G, F))
    #                 else:
    #                     tile = random.choice((S, G, F))
    #         else:
    #             if i == 0 or j == 0 or i == height - 1 or j == width - 1 or i == mid_height1 or j == mid_width1\
    #                     or i == mid_height2 or j == mid_width2 or i == mid_height3 or j == mid_width3 or i == height - 1\
    #                     or j == width - 1:
    #                 tile = W
    #             else:
    #                 water = random.choice((True, False, False, False))
    #                 if water:
    #                     tile = random.choice((W, S, G, F))
    #                 else:
    #                     tile = random.choice((S, G, F))
    #         harta[i].append(tile)


    return harta

def oddheight_oddwidth(height:int, width:int) -> list:
    harta = []
    mid_width1 = width//2 - 1
    mid_width2 = width//2
    mid_width3 = width//2 + 1





    mid_height1 = height//2 - 1
    mid_height2 = height//2
    mid_height3 = height//2 + 1

    for i in range(height):
        harta.append([])
        for j in range(width):
            if i == 0 or j == 0 or i == height - 1 or j == width - 1 or i == mid_height1 or j == mid_width1 \
            or i == mid_height2 or j == mid_width2 or i == mid_height3 or j == mid_width3 or i == height - 1\
            or j == width - 1:
                tile = W
            else:
                water = random.choice((True, False, False, False))
                if water:
                    tile = random.choice((W, S, G, F))
                else:
                    tile = random.choice((S, G, F))
            harta[i].append(tile)

    return harta

def evenheight_oddwidth(height:int, width:int) -> list:
    pass

def oddheight_evenwidth(height:int, width:int) -> list:
    pass

def evenheight_evenwidth(height:int, width:int) -> list:
    harta = []
    mid_width1 = width // 2
    mid_width2 = width // 2 + 1

    mid_height1 = height // 2
    mid_height2 = height // 2 + 1

    for i in range(height):
        harta.append([])
        for j in range(width):
            if i == 0 or j == 0 or i == height - 1 or j == width - 1 or i == mid_height1 or j == mid_width1 \
                    or i == mid_height2 or j == mid_width2 or i == height - 1 or j == width - 1:
                tile = W
            else:
                water = random.choice((True, False, False, False))
                if water:
                    tile = random.choice((W, S, G, F))
                else:
                    tile = random.choice((S, G, F))
            harta[i].append(tile)

    return harta


# print(generate_map(24, 24, 1))





'''New map generation'''

def pick_terrain(tile_prob:list):
    # Filter out zero or negative probabilities
    filtered = [(tile, prob) for tile, prob in tile_prob if prob > 0]
    if not filtered:
        raise ValueError("No tiles have positive probability!")

    # Normalize so total probability = 1.0
    total_prob = sum(prob for _, prob in filtered)
    normalized = [(tile, prob / total_prob) for tile, prob in filtered]

    r = random.random()
    cumulative = 0
    for tile, prob in normalized:
        cumulative += prob
        if r <= cumulative:
            return tile

def generate_initial_map(width:int, height:int, tile_prob:list) -> list:
    return [[pick_terrain(tile_prob) for _ in range(width)] for _ in range(height)]

#smoth the map

def smooth_map(initial_map, passes = 3) -> list:
    width = len(initial_map[0])
    height = len(initial_map)

    for _ in range(passes):
        new_map = [[0]*width for j in range(height)]

        for i in range(width):
            for j in range(height):
                neighbot_tiles = [] #coutnneighbours

                for di in [-1,0,1]:
                    for dj in [-1,0,1]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < width and 0 <= nj < height:
                            neighbot_tiles.append(initial_map[ni][nj])

                # pick most common
                new_map[i][j] = max(set(neighbot_tiles), key=neighbot_tiles.count)

        return new_map


def generate_naturaly(width:int, height:int, posibility = posibilities) -> list:

    initial_map = generate_initial_map(width, height, posibility)
    natural_map = smooth_map(initial_map)

    natural_map = aditional_smooth(natural_map)

    Mechanics.generate_trader(natural_map)
    # natural_map = initial_map

    for i in range(height):
        for j in range(width):
            if i == 0 or j == 0 or i == height - 1 or j == width - 1:
                natural_map[i][j] = 0  # Water edges

    return natural_map


def search_water(x: int, y: int, mapp) -> list:
    """Find connected water cells starting from (x, y)."""
    width = len(mapp[0])
    height = len(mapp)
    visited = []
    stack = [(x, y)]

    while stack:
        cx, cy = stack.pop()
        if [cx, cy] not in visited and 0 < cx < width - 1 and 0 < cy < height - 1:
            if mapp[cy][cx] == 0:  # water
                visited.append([cx, cy])
                stack.extend([
                    (cx - 1, cy), (cx + 1, cy),
                    (cx, cy - 1), (cx, cy + 1)
                ])
    return visited


def aditional_smooth(generated_map) -> list:
    width = len(generated_map[0])
    height = len(generated_map)

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if generated_map[y][x] == 0:  # only check water
                water_neighbors = 0
                total_neighbors = 0

                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < height and 0 <= nx < width:
                            total_neighbors += 1
                            if generated_map[ny][nx] == 0:
                                water_neighbors += 1

                # If isolated (few water neighbors) → overwrite with land
                if water_neighbors <= 2:
                    generated_map[y][x] = pick_terrain(posibilities)

    return generated_map






