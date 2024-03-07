from customtkinter import *
from PIL import Image,ImageTk
def resize_image(image, width, height):
    aspect_ratio = image.width / image.height

    # Calculate new width and height to maintain aspect ratio
    if aspect_ratio > (width / height):
        new_width = int(height * aspect_ratio)
        new_height = height
    else:
        new_width = width
        new_height = int(width / aspect_ratio)

    # Resize the image while maintaining aspect ratio
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

    # Calculate coordinates for cropping
    left = (new_width - width) / 2
    top = (new_height - height) / 2
    right = (new_width + width) / 2
    bottom = (new_height + height) / 2

    # Crop the resized image to the desired width and height
    cropped_image = resized_image.crop((left, top, right, bottom))

    return cropped_image
class FilterSort(CTkFrame):
    def __init__(self, parent_frame, **kwargs):
        super().__init__(parent_frame, **kwargs)
        self.configure(parent_frame, fg_color="#1B1C22", bg_color="#44454A")

        search_frame = CTkFrame(self, fg_color="transparent")
        search_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.05)

        searchBar = CTkEntry(search_frame, placeholder_text="Search Recipe", fg_color="#393A3B", border_width=0, text_color="#BFBBBB")
        searchBar.place(relx=0, rely=0, relwidth=0.8, relheight=1)

        sortBy = CTkEntry(search_frame, placeholder_text="Sort By", fg_color="#393A3B", border_width=0, text_color="#BFBBBB")
        sortBy.place(relx=0.85, rely=0, relwidth=0.15, relheight=1)
        
        results_frame = CTkFrame(self,fg_color="transparent")
        results_frame.place(relx=0.05,rely=0.15, relwidth= 0.9,relheight=0.8)

        recipe_item= CTkFrame(results_frame,fg_color="transparent",border_color="#393A3B",border_width=2,corner_radius=20)
        recipe_item.place(relx=0.0,rely=0.03,relheight=0.25,relwidth=1)

        recipe_image_frame = CTkFrame(recipe_item,fg_color="transparent",corner_radius=20,border_width=1)
        recipe_image_frame.place(relx=0.002,rely=0.01,relheight=0.98,relwidth=0.25)
        recipe_image = Image.open("photos/pakauda.jpg")
        recipe_image = resize_image(recipe_image,200,160)
        image_label = CTkLabel(recipe_image_frame, text="", image=CTkImage(light_image=recipe_image, size=(200, 200)))
        image_label.place(relx=0,rely=0,relheight=1,relwidth=1)
        # Corner = CTkFrame(recipe_image_frame, fg_color="transparent",bg_color="black",border_width=0,corner_radius=20)
        # Corner.place(relx=0,rely=0,relheight=1,relwidth=1)