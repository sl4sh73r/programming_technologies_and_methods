from PIL import Image, ImageTk

class ImageHandler:
    def __init__(self, image_data):
        self.image_data = image_data

    def get_image(self, size):
        img = Image.open(self.image_data)
        img = img.resize(size, Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        return photo
