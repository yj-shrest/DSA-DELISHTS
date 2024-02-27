from customtkinter import *
from PIL import Image
class DashboardFrame(CTkFrame):
    def __init__(self, parent_frame, **kwargs):
        super().__init__(parent_frame, **kwargs)
        self.configure(parent_frame, fg_color="#1B1C22", bg_color="#44454A")


        search_frame = CTkFrame(self, fg_color="transparent")
        search_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.05)

        searchBar = CTkEntry(search_frame, placeholder_text="Search Recipe", fg_color="#393A3B", border_width=0, text_color="#BFBBBB")
        searchBar.place(relx=0, rely=0, relwidth=0.8, relheight=1)

        sortBy = CTkEntry(search_frame, placeholder_text="Sort By", fg_color="#393A3B", border_width=0, text_color="#BFBBBB")
        sortBy.place(relx=0.85, rely=0, relwidth=0.15, relheight=1)
        self.displayed_labels = []
        self.display_recipes()
    def display_recipes(self):
        recipe_files = [file for file in os.listdir("recipies") if file.endswith(".txt")]
        ypos = 100
        for recipe_file in recipe_files:
            with open(os.path.join("recipies", recipe_file), 'r') as file:
                recipe_data = file.readlines()
                recipe_name = recipe_data[0].split(":")[1].strip()
                label = CTkLabel(self, text=recipe_name, text_color="white")
                label.place(x=50, y=ypos)
                self.displayed_labels.append(label)  # Add label to the list
                ypos += 40

    def clear_recipes(self):
        for label in self.displayed_labels:
            label.destroy()  # Destroy each displayed label
        self.displayed_labels = []  # Clear the list
    def initialize(self):
        self.grid(row=0,column=1,sticky="nsew")
        self.clear_recipes()
        self.display_recipes()

