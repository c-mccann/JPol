from PIL import Image
from random import randint as r
import numpy as np


class custom_design():

    def __init__(self):
        pass

    def create(self):
        # canvas like

        cream = np.array([252, 251, 227])
        turquoise = np.array([64, 224, 208])
        light_pink = np.array([255, 192, 203])

        img = Image.new('RGB', (1000, 1000), 'black') # create a new black image
        pixels = img.load() # create the pixel map

        for i in range(img.size[0]):    # for every pixel:
            for j in range(img.size[1]):
                # pixels[i,j] = (i, j, 100) # set the colour accordingly
                new_i = r(0, 255)
                new_j = r(0, 255)
                percentage = (i + j) / (img.size[0] + img.size[1])
                pixels[i,j] = tuple(self.gradient_vector(light_pink, turquoise, percentage))

        img.save('out/custom_design4.jpg', format='JPEG')

    def gradient_vector(self, start, end, percentage):
        return (start + (percentage * (end - start))).astype(int)


if __name__ == '__main__':
    cd = custom_design()
    cd.create()
