from PIL import Image
from random import randint as r

img = Image.new( 'RGB', (1000, 1000), "black") # create a new black image
pixels = img.load() # create the pixel map

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

l = [red, green, blue]

for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):

        # pixels[i,j] = (i, j, 100) # set the colour accordingly

        pixels[i,j] = l[r(0,2)]


img.save('out/random_rgb.jpg', format='JPEG')