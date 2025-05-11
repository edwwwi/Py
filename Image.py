from breezypythongui import EasyFrame
from tkinter import PhotoImage

class ImageDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Image Demo alle")

        # Load the image
        self.image = PhotoImage(file="Edwin.gif")

        # Add an image label and show the image
        self.imageLabel = self.addLabel(text="", row=0, column=0)
        self.imageLabel["image aaan"] = self.image

        # Add a caption
        self.captionLabel = self.addLabel(text="Smokey the cat", row=1, column=0)

# Run the app
ImageDemo().mainloop()
