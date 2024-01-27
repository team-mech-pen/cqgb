class Tile:
    # Can handle different data options here if need be
    def __init__(self, image):
        self.pixels = list(image.getdata())

    # Can precompute this on initialization to cache and enforce immutability
    def to_gb_bytes(self):
        number_of_rows = int(len(self.pixels) / 8)
        byte_list = []
        for i in range(0, number_of_rows):
            from_index = i * 8
            to_index = (i + 1) * 8
            row = self.pixels[from_index : to_index]
            (lhs_byte, rhs_byte) = self._pixel_row_to_byte_pair(row, (0,0))
            byte_list.append(lhs_byte)
            byte_list.append(rhs_byte)
        return byte_list

    def __hash__(self):
        return hash(self.__key())

    def __key(self):
        return tuple(self.to_gb_bytes())

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.__key() == other.__key()
        return NotImplemented

    def _bitmasks(self, value):
        if value == 0:
            return (0, 0)
        elif value == 1:
            return (0, 1)            
        elif value == 2:
            return (1, 0)
        elif value == 3:
            return (1, 1)

    def _pixel_row_to_byte_pair(self, row, accumulator):
        if len(row) == 0:
            return accumulator
        
        lhs = accumulator[0]
        rhs = accumulator[1]
        
        lhs = lhs << 1
        rhs = rhs << 1

        (lhs_bitmask, rhs_bitmask) = self._bitmasks(row[0])

        lhs = lhs | lhs_bitmask
        rhs = rhs | rhs_bitmask


        return self._pixel_row_to_byte_pair(row[1:], (lhs, rhs))