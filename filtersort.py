from customtkinter import *
from PIL import Image,ImageTk
def resize_image(image, new_width, new_height):
    desired_aspect_ratio = new_width/new_height  
    # Calculate the new image size while maintaining the desired aspect ratio
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height
    if aspect_ratio > desired_aspect_ratio:
        # Image is wider than desired aspect ratio
        new_height = original_height
        new_width = int(new_height * desired_aspect_ratio)
    else:
        # Image is taller than desired aspect ratio
        new_width = original_width
        new_height = int(new_width / desired_aspect_ratio)

    # Crop the image to the desired aspect ratio
    left = (original_width - new_width) // 2
    top = (original_height - new_height) // 2
    right = left + new_width
    bottom = top + new_height
    cropped_image = image.crop((left, top, right, bottom))
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
        recipe_image = Image.open("photos/milk_tea.jpg")
        recipe_image = resize_image(recipe_image,200,160)
        image_label = CTkLabel(recipe_image_frame, text="", image=CTkImage(light_image=recipe_image, size=(200, 200)))
        image_label.place(relx=0,rely=0,relheight=1,relwidth=1)
        # Corner = CTkFrame(recipe_image_frame, fg_color="transparent",bg_color="black",border_width=0,corner_radius=20)
        # Corner.place(relx=0,rely=0,relheight=1,relwidth=1)