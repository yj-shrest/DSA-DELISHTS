from PIL import Image, ImageDraw, ImageTk
from customtkinter import *
root = CTk()
root.geometry("1000x1000")
def create_rounded_image(image_path, size, corner_radius, opacity=255):
  with Image.open(image_path) as image:
    # Resize image if needed
    image = image.resize(size, Image.ANTIALIAS)
    
    # Create a mask with transparent background
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size[0], size[1]), radius=corner_radius, fill=255)
    
    # Apply mask to the image with desired opacity
    image = image.convert('RGBA')
    image.putalpha(mask.point(lambda p: p * opacity // 255))
    
    # Convert PIL image to PhotoImage
    return ImageTk.PhotoImage(image)

class RoundedImageButton(CTkFrame):
  """
  A custom CTkFrame class with a rounded image displayed inside.
  """
  def __init__(self, master, image_path, size=(100, 100), corner_radius=20, opacity=255):
    super().__init__(master)
    
    self.image_label = CTkLabel(self, image=create_rounded_image(image_path, size, corner_radius, opacity))
    self.image_label.pack(padx=0, pady=0)

# Example usage
image_button = RoundedImageButton(root, "photos/pakauda.jpg", size=(150, 150), corner_radius=30, opacity=200)
image_button.pack()
# Run the Tkinter main loop
root.mainloop()