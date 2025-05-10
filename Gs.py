from PIL import Image

def gs(image):
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            lum = int(r * 0.299 + g * 0.587 + b * 0.114)
            pixels[x, y] = (lum, lum, lum)

image = Image.open("Edwin.jpg")
image = image.convert("RGB")  # Ensure it's in RGB mode
gs(image)
image.show()  # Or image.save("gray_Edwin.jpg")
