from customtkinter import *
from PIL import Image, ImageTk

food = [
    {
        "name": "This",
        "category": "hard",
        "image_path": "bla.jpg"
    },
    {
        "name": "is",
        "category": "hard",
        "image_path": "bla.jpg"
    },
    {
        "name": "the",
        "category": "easy",
        "image_path": "bla.jpg"
    },
    {
        "name": "worst",
        "category": "hard",
        "image_path": "bla.jpg"
    },
    {
        "name": "way",
        "category": "easy",
        "image_path": "bla.jpg"
    },
    {
        "name": "to",
        "category": "hard",
        "image_path": "bla.jpg"
    },
    {
        "name": "achieve",
        "category": "easy",
                "image_path": "bla.jpg"
    },
    {
        "name": "GUI",
        "category": "hard",
        "image_path": "bla.jpg"
    },
    {
        "name": "THE",
        "category": "easy",
        "image_path": "bla.jpg"
    },
    {
        "name": "WORST",
        "category": "hard",
        "image_path": "bla.jpg"
    },
]

class RecipeFrame(CTkFrame):
    def __init__(self, parent_frame, recipe_data, **kwargs):
        super().__init__(parent_frame, **kwargs)
        self.recipe_data = recipe_data
        self.configure(parent_frame, fg_color="transparent", bg_color="transparent")

        # Description label
        # image = image.resize((100, 100))  
        # photo = ImageTk.PhotoImage(image)
        # self.image_label.image = photo 

        image = CTkImage(light_image= Image.open('./photos/pakauda.jpg'), size= (280,280))
        self.image_label = CTkLabel(self, image=image, text="", corner_radius=10)
        self.image_label.pack()

         
        title_frame = CTkFrame(self, bg_color='transparent', fg_color='transparent' )
        title_frame.pack(side=LEFT, padx=10)

        self.title_label = CTkLabel(title_frame, text=self.recipe_data['name'].upper(), text_color="white", font=("", 20))
        self.title_label.pack()

        # Information labels on the right side
        info_frame = CTkFrame(self, bg_color='transparent', fg_color="transparent")
        info_frame.pack(side=RIGHT, padx=5)

        time_label = CTkLabel(info_frame, text="Time: " + self.recipe_data.get('time_required', ''), text_color="white")
        time_label.pack(anchor=W)

        difficulty_label = CTkLabel(info_frame,text="Difficulty: " + self.recipe_data.get('difficulty', ''), text_color="white")
        difficulty_label.pack(anchor=W)
class DashboardFrame(CTkFrame):
    def __init__(self, parent_frame, **kwargs):
        super().__init__(parent_frame, **kwargs)
       
        self.flex_frame = CTkScrollableFrame(self, orientation = "vertical", fg_color="transparent", height=1000)
        self.flex_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
        
        self.display_recipes()
        
    
    def display_recipes(self):
        num_items_per_row = 3
       
       
        for i, singleFood in enumerate(food):
            row = i // num_items_per_row
            col = i % num_items_per_row
         
            flex_frame = RecipeFrame(self.flex_frame, recipe_data=singleFood, corner_radius=10)
            flex_frame.grid(column=col, row = row,  padx=5, pady=10)
   

    def clear_recipes(self):
        for label in self.displayed_labels:
            label.destroy()  # Destroy each displayed label
        self.displayed_labels = []


    def initialize(self):
        self.grid(row=0,column=1,sticky="nsew")
        self.display_recipes()
        self.clear_recipes()

