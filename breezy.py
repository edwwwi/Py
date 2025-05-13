from breezypythongui import EasyFrame
from tkinter import PhotoImage

class ImageDemo(EasyFrame):
    """Displays an image and a caption."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Image Demo")
        

        # Add image label
        imageLabel = self.addLabel(text="", row=0, column=0, sticky="NSEW")

        # Add caption label
        textLabel = self.addLabel(text="Smokey the cat", row=1, column=0, sticky="NSEW")

        # Load and display the image
        self.image = PhotoImage(file="Edwin.gif")
        imageLabel["image"] = self.image

# Run the program
if __name__ == "__main__":
    ImageDemo().mainloop()
