
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
