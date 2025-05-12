from images import Image

def blur(image):
    new = image.clone()
    for y in range(1, image.getHeight() - 1):
        for x in range(1, image.getWidth() - 1):
            oldP = image.getPixel(x, y)
            left = image.getPixel(x - 1, y)
            right = image.getPixel(x + 1, y)
            top = image.getPixel(x, y - 1)
            bottom = image.getPixel(x, y + 1)
            
            avg_r = (oldP[0] + left[0] + right[0] + top[0] + bottom[0]) // 5
            avg_g = (oldP[1] + left[1] + right[1] + top[1] + bottom[1]) // 5
            avg_b = (oldP[2] + left[2] + right[2] + top[2] + bottom[2]) // 5
            
            new.setPixel(x, y, (avg_r, avg_g, avg_b))
    return new

image = Image("smokey.gif")
image = blur(image)
image.draw()