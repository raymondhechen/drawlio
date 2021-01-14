import io
import math
import numpy as np
import cv2


def read_file_bytes(path):

    bytelist = []

    with open(path, "rb") as f:
        byte = f.read(1)
        while byte != b"":
            byte = f.read(1)
            if (byte):
                dec = ord(byte)
                bytelist.append(dec)

    return np.array(bytelist)


def reshape_bytelist(bytelist):
    # byte -> 0-256 in decimal
    # need 3 bytes per pixel for rgb
    missing_byte_count = 3 - len(bytelist) % 3
    for _ in range(0, missing_byte_count):
        bytelist = np.append(bytelist, 0)  # append empty bytes

    # want square picture, but keep all bytes, so ceiling
    num_pixels = len(bytelist) / 3
    dimension = math.ceil(math.sqrt(num_pixels))

    print(dimension)

    pixel_list = []
    for i in range(0, len(bytelist), 3):
        pixel_list.append(bytelist[i:i+3])
    template = np.full((dimension, dimension, 3), [0, 0, 0])

    row = 0
    col = 0
    for i in range(0, len(pixel_list)):
        # increment row
        if (col == dimension):
            row += 1
            col = 0

        # increment col
        template[row, col] = pixel_list[i]

        col += 1

    return template


def write_png(bytelist):
    cv2.imwrite('test.png', bytelist)

bytelist = read_file_bytes('video-1610615255.mp4')
bytelist = reshape_bytelist(bytelist)
write_png(bytelist)
