import sys
from PIL import Image
from tile import Tile

def format_byte_string(byte_int):
        return str.format('0x{:02x}', byte_int)

def extract_tile(coordinates, image):
    region = image.crop(coordinates)
    return Tile(region)

for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            tile = extract_tile((0,0,8,8), im)
            all_bytes = map(format_byte_string, tile.to_gb_bytes())
            print(",".join(all_bytes))
    except OSError:
        pass