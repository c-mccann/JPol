from PIL import Image
from random import randint as r

img = Image.new( 'RGB', (1000, 1000), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        # pixels[i,j] = (i, j, 100) # set the colour accordingly
        new_i = r(0, 255)
        new_j = r(0, 255)
        pixels[i,j] = (new_i, new_j, 100) # set the colour accordingly

img.save('out/random_speckle.jpg', format='JPEG')