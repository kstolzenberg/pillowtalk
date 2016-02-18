# from examples here https://pillow.readthedocs.org/en/3.1.x/index.html
from PIL import Image, ImageFilter, ImageChops, ImageOps

img = Image.open('Rem-Koolhaas.jpg')
img.show()
img = img.filter(ImageFilter.BLUR)

box = (100,100,400,400)
region = img.crop(box)
region = region.transpose(Image.ROTATE_180)
img.paste(region, box)

px = img.load()
print (px[4,4])
px[4,4] = (0,0,0)
print (px[4,4])

img.save("changed.jpg", "JPEG")
img2 = Image.open('changed.jpg')
img2.show()


imgB = Image.open('Bjarke.jpg')
img3 = ImageChops.add(img, imgB)
img3.save("joined.jpg", "JPEG")
img3.show()

# def roll(image, delta):
#     "Roll an image sideways"

#     xsize, ysize = image.size

#     delta = delta % xsize
#     if delta == 0: return image

#     part1 = image.crop((0, 0, delta, ysize))
#     part2 = image.crop((delta, 0, xsize, ysize))
#     image.paste(part2, (0, 0, xsize-delta, ysize))
#     image.paste(part1, (xsize-delta, 0, xsize, ysize))

#     return image

# imgB = Image.open('Bjarke.jpg')
# imgB.show()
# roll(imgB, 100)
# imgB.save("changedB.jpg", "JPEG")