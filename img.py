from PIL import Image

def shrink(image, factor):
    w = image.getWidth()
    h = image.getHeight()
    small = Image(w // factor, h // factor)

    for y in range(0, h, factor):
        for x in range(0, w, factor):
            pixel = image.getPixel(x, y)
            small.setPixel(x // factor, y // factor, pixel)

    small.draw()

# Use the function
img = Image("Edwin.gif")
shrink(img, 2)
