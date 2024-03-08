from customtkinter import *
from tkinter import Button
from PIL import Image, ImageTk
import os
import random
from singlepage import SingleFrame

def extract_recipe_info(file):
    recipe_info = {}
    for line in file:
        if ': ' in line:
            key, value = line.strip().split(': ', 1)
            recipe_info[key.lower()] = value

    return recipe_info

# Function to create a list of recipe dictionaries from all text files in a folder
def create_recipe_list(folder_path):
    recipe_list = []
    file_names = os.listdir(folder_path)
    selected_files = random.sample(file_names, min(6, len(file_names)))
    for file_name in selected_files:
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                recipe_info = extract_recipe_info(file)
                recipe_list.append(recipe_info)
    return recipe_list

# Specify the folder path containing the recipe text files
folder_path = 'recipes'

# Create the list of recipes
food = create_recipe_list(folder_path)



class DashboardFrame(CTkFrame):
    def __init__(self, parent_frame, **kwargs):
        super().__init__(parent_frame, **kwargs)
        self.configure(fg_color="#1B1C22",bg_color="#44454A")


        Tagline = CTkLabel(self,text="Unleash Your Inner Chef:\nExplore, Create, and Indulge\nin a Feast of Flavors",text_color="white",font=('Helvetica',30,'bold'),justify='left',anchor=W)
        Tagline.place(relx=0.07, rely=0.05, relwidth=0.6)
        CoverImage = Image.open("burger.png")
        logo_label = CTkLabel(self, text="", image=CTkImage(light_image=CoverImage, size=(200, 200)))
        logo_label.place(relx=0.6, rely=0.0, relwidth=0.4)
        Recommendation = CTkLabel(self,text="Recommendations",text_color="white",font=('Helvetica',20,'bold'),justify='left',anchor=W)
        Recommendation.place(relx=0.07, rely=0.25, relwidth=0.9)

        self.flex_frame = CTkFrame(self, fg_color="#1B1C22", height=1000,bg_color="#1B1C22")
        self.flex_frame.place(relx=0.05, rely=0.30, relwidth=0.9, relheight=0.9)
        
        self.display_recipes()

        # self.single()
       
    def single(self):
        self.single_recipe = SingleFrame(self)
        self.single_recipe.place(relx= 0.03, rely=0.05, relheight=0.95 ,relwidth= 0.92 )

    def display_recipes(self):
        num_items_per_row = 3
        for i, singleFood in enumerate(food):
            row = i // num_items_per_row
            col = i % num_items_per_row
         
            flex_frame = RecipeFrame(self.flex_frame, recipe_data=singleFood, corner_radius=10, parent_dashboard= self )
            flex_frame.grid(column=col, row = row,  padx=5, pady=5)
  



    def clear_recipes(self):
        self.flex_frame.grid_remove()

    def initialize(self):
        self.grid(row=0,column=1,sticky="nsew")
        self.clear_recipes()
        self.display_recipes()






class RecipeFrame(CTkFrame):
    def __init__(self, parent_frame, recipe_data,parent_dashboard, **kwargs):
        super().__init__(parent_frame, **kwargs)
        self.recipe_data = recipe_data
        self.configure(parent_frame, fg_color="#1B1C22", bg_color="transparent")
        self.parent_dashboard = parent_dashboard
        # Description label
        # image = image.resize((100, 100))  
        # photo = ImageTk.PhotoImage(image)
        # self.image_label.image = photo 
        name = self.recipe_data['recipe']
        image = CTkImage(light_image= Image.open('./photos/'+"_".join(name.lower().split(" "))+'.jpg'), size= (210,170))
        self.image_label = CTkLabel(self, image=image, text="", corner_radius=10)
        self.image_label.pack()

        title_frame = CTkFrame(self, bg_color='#1B1C22', fg_color='transparent' )
        title_frame.pack(padx=5)
        title_frame.grid_columnconfigure(0, weight=1)  
        title_frame.grid_columnconfigure(1, weight=1)  
        title_frame.grid_rowconfigure(0, weight=1)
        title_frame.grid_rowconfigure(1, weight=1)

        self.title_label = CTkLabel(title_frame, text=self.recipe_data['recipe'], text_color="white",anchor=W, font=("", 14,'bold'),width=100,height=20)
        self.title_label.grid(row=0,column=0,pady=(5,0))

        # Information labels on the right side
        time_label = CTkLabel(title_frame, text= self.recipe_data.get('time', '')+"  ", anchor=E,text_color="white",width=100,height=20,image=CTkImage(light_image= Image.open('./photos/timeicon.png'), size= (15,15)),compound=RIGHT)
        time_label.grid(row=0,column=1,pady=(5,0))
        difficulty_label = CTkLabel(title_frame, text= self.recipe_data.get('difficulty', '')+"  ",anchor=E, text_color="white",width=100,height=15,image=CTkImage(light_image= Image.open('./photos/difficultyicon.png'), size= (15,10)),compound=RIGHT)
        difficulty_label.grid(row=1,column=1,pady=(5,0))

        transparency = CTkImage(light_image=Image.open("./photos/nothing.png"), size=(300,300))

        invisible_button = CTkButton(master=self,text="",image= transparency, bg_color="transparent", hover=True,  width=self.winfo_screenwidth(), height= self.winfo_screenwidth(), command = self.parent_dashboard.single )
        invisible_button.place(relx=0.0, rely=0.0)

    # def openSingle(self):
    #     print("clicked")
    #     self.parent_dashboard.single()
    
        
