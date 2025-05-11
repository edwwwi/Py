from images import Image  # type: ignore

def gs(image):
    for y in range(image.get_height()):
        for x in range(image.get_width()):
            r, g, b = image.get_pixel(x, y)
            lum = int(r * 0.299 + g * 0.587 + b * 0.114)
            image.set_pixel(x, y, (lum, lum, lum))

image = Image("try.png")
gs(image)
image.show()
