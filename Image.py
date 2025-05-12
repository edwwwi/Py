from images import Image

def shrink(image, factor):
    """Returns a new image that is smaller by the given factor."""
    width = image.getWidth()
    height = image.getHeight()
    
    # Create a new blank image with reduced dimensions
    new = Image(width // factor, height // factor)
    
    newY = 0
    for oldY in range(0, height, factor):
        newX = 0
        for oldX in range(0, width, factor):
            pixel = image.getPixel(oldX, oldY)
            new.setPixel(newX, newY, pixel)
            newX += 1
        newY += 1
    
    new.draw()  # Show the new shrunk image
    return new

# Load the original image
image = Image("smokey11.gif")

# Shrink it by a factor of 2
shrink(image, 2)
