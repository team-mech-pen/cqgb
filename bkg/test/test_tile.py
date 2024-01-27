from PIL import Image
from tile import Tile

def test_tile_to_gb_bytes():
    with Image.open("./test/test_tile.png") as tile_image:
        tile = Tile(tile_image)
        assert tile.to_gb_bytes() == [160, 128, 0, 80, 16, 0, 0, 20, 116, 52, 0, 20, 53, 36, 2, 50]
