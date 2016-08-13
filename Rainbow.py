from PIL import Image

# https://en.wikibooks.org/wiki/Python_Imaging_Library/Editing_Pixels
# code nicked from above for testing/learning

img = Image.new( 'RGB', (1000,1000), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        r = int((i / img.size[0]) * 255)
        g = int((j / img.size[1]) * 255)
        b = g
        pixels[i,j] = (r, g, b) # set the colour accordingly

img.save('out/rainbow4.jpg', format='JPEG')