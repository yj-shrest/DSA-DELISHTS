from customtkinter import *
from PIL import Image
from recipe import Recipe


def adder(recipe_name, recipe_time, recipe_ingredients, recipe_steps):
    ingredients_list = [ingredient.strip() for ingredient in recipe_ingredients.split(',')]
    user_recipe = Recipe(recipe_name, int(recipe_time), ingredients_list, recipe_steps)
    print("added")

def reset(name,time,ingredients,steps):
     name.delete(0,'end')
     time.delete(0,'end')
     ingredients.delete(0,'end')
     steps.delete(0,'end')
     print("reset")


class AddRecipeFrame(CTkFrame):
    def __init__(self, parent_frame, **kwargs):
        super().__init__(parent_frame, **kwargs)
        self.configure(parent_frame,fg_color="#1B1C22",bg_color="#44454A")
       
        #label

        font_size=10

        name_label= CTkLabel(self, text="Name of the recipe:",font=("",font_size))
        time_label= CTkLabel(self, text="Time required (in minutes):",font=("",font_size))
        ingredients_label= CTkLabel(self, text="Ingredients:",font=("",font_size))
        steps_label= CTkLabel(self, text="Procedure:",font=("",font_size))
       
        #entries
        name=CTkEntry(self)
        time=CTkEntry(self)
        ingredients=CTkEntry(self)
        steps=CTkEntry(self)

        #buttons
        save_button = CTkButton(self,text="Save",fg_color="#F85656",corner_radius=30, command=lambda: adder(name.get(), time.get(), ingredients.get(), steps.get()))
        reset_button= CTkButton(self,text="Reset",fg_color="#5684F8",corner_radius=30,command=lambda: reset(name,time,ingredients,steps) )


        
        #put the things
        after_label=20
        after_entry=50
        ypos=after_label
        xpos=50

        name_label.place(x=xpos,y=ypos)
        ypos=ypos+after_label

        name.place(x=xpos,y=ypos)
        ypos=ypos+after_entry

        time_label.place(x=xpos,y=ypos)
        ypos=ypos+after_label

        time.place(x=xpos,y=ypos)
        ypos=ypos+after_entry

        ingredients_label.place(x=xpos,y=ypos)        
        ypos=ypos+after_label

        ingredients.place(x=xpos,y=ypos)
        ypos=ypos+after_entry

        steps_label.place(x=xpos,y=ypos)
        ypos=ypos+after_label

        steps.place(x=xpos,y=ypos)
        ypos=ypos+after_entry

       
        reset_button.place(x=xpos,y=ypos)   
        save_button.place(x=xpos+450,y=ypos)
   


    

       










        
        


       