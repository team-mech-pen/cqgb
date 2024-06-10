import sys
from PIL import Image
from tile import Tile

def format_byte_string(byte_int):
    return str.format('0x{:02x}', byte_int)

def extract_tile(coordinates, image):
    region = image.crop(coordinates)
    return Tile(region)

"""for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as image:
            tile = extract_tile((0,0,8,8), image)
            all_bytes = map(format_byte_string, tile.to_gb_bytes())
            print(",".join(all_bytes))
    except OSError:
        pass
"""
# output is 8 x 8 

 # There is a new python module with a function parse_image(img)
 # parse_image(img) returns a tuple, (pattern_table, tile_indexes), where pattern_table is a list of Tiles, and tile_indexes is a list of numbers
 # pattern_table shouldn't contain any tiles which have the same pattern
 # If the image provided to the function is not a multiple of 8 in width and height, the function should throw an error
 # Create a new pytest test suite for your function capturing the main functionality and any key edge cases

""" def parse_image(img):
    # go along map, 00+88, 80+815
    # extract tile from image, 
    # get the list of integers
    # check with tile list, if unique bang it in,
    # find location of tile list if in, and then add to indexes
    for i in img:
        pattern_table = []
        tile_indexes = []"""


def derive_coords(tile_number):
    x = tile_number % 20
    y = tile_number / 16
    return (x, y, x + 8, y + 8)


def tile_reducer(image, tile_number, pattern_indexes, pattern_table):
    tile = extract_tile(derive_coords(tile_number), image)
    existing_index = pattern_table.get(tile)
    if existing_index:
        pattern_indexes.append(existing_index)
    else:
        index = len(pattern_table)
        pattern_table[tile] = len(pattern_table)
        pattern_indexes.append(index)

for infile in sys.argv[1:]:
    try:
        # Open image and confirm correct shape
        im = Image.open(infile)
        width, height = im.size

        pattern_indexes = []
        pattern_table = {}

        for tile_number in range(320):
            tile_reducer(im, tile_number, pattern_indexes, pattern_table)

        print(pattern_indexes)
        print(pattern_table)
    
    except OSError:
        pass
 