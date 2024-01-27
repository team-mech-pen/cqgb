from PIL import Image
from tile import Tile

def test_tile_to_gb_bytes():
    with Image.open("./test/test_tile.png") as tile_image:
        tile = Tile(tile_image)
        assert tile.to_gb_bytes() == [160, 128, 0, 80, 16, 0, 0, 20, 116, 52, 0, 20, 53, 36, 2, 50]

def test_tile_hash_is_same_for_same_tile():
    with Image.open("./test/test_tile.png") as tile_image:
        tile1 = Tile(tile_image)
        tile2 = Tile(tile_image)
        assert tile1.__hash__() == tile2.__hash__()


def test_tile_hash_is_different_for_different_tiles():
    tile_1_image = Image.open("./test/test_tile.png")
    tile_2_image = Image.open("./test/test_tile_2.png")
    tile1 = Tile(tile_1_image)
    tile2 = Tile(tile_2_image)
    assert tile1.__hash__() != tile2.__hash__()

def test_tile_equality_is_true_for_same_tile():
    with Image.open("./test/test_tile.png") as tile_image:
        tile1 = Tile(tile_image)
        tile2 = Tile(tile_image)
        assert tile1 == tile2

def test_tile_equality_is_false_for_different_tiles():
    tile_1_image = Image.open("./test/test_tile.png")
    tile_2_image = Image.open("./test/test_tile_2.png")
    tile1 = Tile(tile_1_image)
    tile2 = Tile(tile_2_image)
    assert tile1 != tile2