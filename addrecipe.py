from customtkinter import *
from PIL import Image
from recipe import Recipe


def adder(recipe_name,description, recipe_time, recipe_ingredients, recipe_steps):
    ingredients_list = [ingredient.strip() for ingredient in recipe_ingredients.split(',')]
    user_recipe = Recipe(recipe_name,description, int(recipe_time), ingredients_list, recipe_steps)
    print("added")

def reset(name,time,ingredients,steps):
     name.delete(0,'end')
     time.delete(0,'end')
     ingredients.delete(0,'end')
     steps.delete(0,'end')
     print("reset")
def clear_default_text(event, des):
    current_text = des.get("0.0","end")
    if current_text.strip() == "Add a short description":
        print("del")
        des.delete(1.0, "end")
def restore_default_text(event, des):
    current_text = des.get("0.0", "end")
    if not current_text.strip():  # Check if the text is empty
        des.insert("0.0", "Add a short description")
class AddRecipeFrame(CTkFrame):
    def __init__(self, parent_frame, **kwargs):
        super().__init__(parent_frame, **kwargs)
        self.configure(parent_frame,fg_color="#1B1C22",bg_color="#44454A")
       
        #label

        font_size=10
       
        #entries
        name=CTkEntry(self,placeholder_text="Add Title Here...",text_color="white",fg_color="#1B1C22",placeholder_text_color="#BFBBBB", border_width=0,font=("",30),width=400)
        description=CTkTextbox(self,text_color="white",fg_color="#1B1C22", border_width=0,font=("",14),width=400)
        description.insert("0.0","Add a short description")
        description.bind("<FocusIn>", lambda event, des=description: clear_default_text(event, des))
        description.bind("<FocusOut>", lambda event, des=description: restore_default_text(event, des))
        time=CTkEntry(self,placeholder_text="Add Title Here...",text_color="white",fg_color="#1B1C22",placeholder_text_color="#BFBBBB", border_width=0,)
        ingredients=CTkEntry(self,placeholder_text="Add Title Here...",text_color="white",fg_color="#1B1C22",placeholder_text_color="#BFBBBB", border_width=0,)
        steps=CTkEntry(self,placeholder_text="Add Title Here...",text_color="white",fg_color="#1B1C22",placeholder_text_color="#BFBBBB", border_width=0,)

        #buttons
        save_button = CTkButton(self,text="Save",fg_color="#F85656",corner_radius=30, command=lambda: adder(name.get(),description.get("0.0","end"), time.get(), ingredients.get(), steps.get()))
        reset_button= CTkButton(self,text="Reset",fg_color="#5684F8",corner_radius=30,command=lambda: reset(name,time,ingredients,steps) )


        
        #put the things
        after_label=20
        after_entry=50
        ypos=after_label
        xpos=50

        # name_label.place(x=xpos,y=ypos)
        ypos=ypos+after_label

        name.place(x=xpos,y=ypos)
        ypos=ypos+after_entry

        description.place(x=xpos,y=ypos)
        ypos=ypos+after_entry

        # time_label.place(x=xpos,y=ypos)
        ypos=ypos+after_label

        time.place(x=xpos,y=ypos)
        ypos=ypos+after_entry

        # ingredients_label.place(x=xpos,y=ypos)        
        ypos=ypos+after_label

        ingredients.place(x=xpos,y=ypos)
        ypos=ypos+after_entry

        # steps_label.place(x=xpos,y=ypos)
        ypos=ypos+after_label

        steps.place(x=xpos,y=ypos)
        ypos=ypos+after_entry

       
        reset_button.place(x=xpos,y=ypos)   
        save_button.place(x=xpos+450,y=ypos)
   


    

       










        
        


       