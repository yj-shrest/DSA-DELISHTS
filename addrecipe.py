from customtkinter import *
from PIL import Image
from recipe import Recipe
from tkinter import filedialog



def reset(name,time,ingredients,steps):
     name.delete(0,'end')
     time.delete(0,'end')
     ingredients.delete(0,'end')
     steps.delete(0,'end')
     print("reset")
def clear_default_text(event, des):
    current_text = des.get("0.0","end")
    if current_text.strip() == "Add a short description":
        des.delete(1.0, "end")
def restore_default_text(event, des):
    current_text = des.get("0.0", "end")
    if not current_text.strip():  # Check if the text is empty
        des.insert("0.0", "Add a short description")
def clear_default_text2(event, des):
    current_text = des.get("0.0","end")
    if current_text.strip() == "Write steps here........":
        des.delete(1.0, "end")
def restore_default_text2(event, des):
    current_text = des.get("0.0", "end")
    if not current_text.strip():  # Check if the text is empty
        des.insert("0.0", "Write steps here........")
class AddRecipeFrame(CTkFrame):
    def __init__(self, parent_frame, **kwargs):
        super().__init__(parent_frame, **kwargs)
        self.configure(fg_color="#1B1C22",bg_color="#44454A")
        self.photo_path = ''

        #label
        ingredientslabel = CTkLabel(self,text="Ingredients required",text_color="#BFBBBB",bg_color="#1B1c22",font=("",14))
        self.Difficultylabel = CTkLabel(self,text="Select Difficulty",text_color="#BFBBBB",bg_color="#1B1c22",font=("",14))
        self.PrepTime = CTkLabel(self,text="Set Preparation Time",text_color="#BFBBBB",bg_color="#1B1c22",font=("",14))
        self.hrlabel = CTkLabel(self,text="hr",text_color="#BFBBBB",bg_color="#1B1c22",font=("",20))
        self.minlabel = CTkLabel(self,text="min",text_color="#BFBBBB",bg_color="#1B1c22",font=("",20))
        self.UploadPhotoLabel = CTkLabel(self,text="Select a cover picture",text_color="#BFBBBB",bg_color="#1B1c22",font=("",14))
        self.PhotoPathLabel = CTkLabel(self,text="photo_path",text_color="#BFBBBB",bg_color="#1B1c22",font=("",12))
        self.stepslabel = CTkLabel(self,text="Detail Steps",text_color="#BFBBBB",bg_color="#1B1c22",font=("",16))
        font_size=10
       
        #entries
        self.name=CTkEntry(self,placeholder_text="Add Title Here...",text_color="white",fg_color="#1B1C22",placeholder_text_color="#BFBBBB", border_width=0,font=("",30),width=350)
        self.description=CTkTextbox(self,text_color="white",fg_color="#1B1C22", border_width=0,font=("",14),width=350,height=90)
        self.description.insert("0.0","Add a short description")
        self.description.bind("<FocusIn>", lambda event, des=self.description: clear_default_text(event, des))
        self.description.bind("<FocusOut>", lambda event, des=self.description: restore_default_text(event, des))
        self.Steps=CTkTextbox(self,text_color="#BFBBBB",fg_color="#1B1C22", border_width=0,font=("",14),width=350,height=700)
        self.Steps.insert("0.0","Write steps here........")
        self.Steps.bind("<FocusIn>", lambda event, des=self.Steps: clear_default_text2(event, des))
        self.Steps.bind("<FocusOut>", lambda event, des=self.Steps: restore_default_text2(event, des))
        self.hr=CTkEntry(self,text_color="white",fg_color="#393A3B", border_width=0,font=("",20),width=60,corner_radius=15)
        self.min=CTkEntry(self,text_color="white",fg_color="#393A3B", border_width=0,font=("",20),width=60,corner_radius=15)
       
        
        self.ingredient_entries = []  # List to hold ingredient entry fields

        self.difficulty = CTkOptionMenu(self, values=["Easy", "Medium","Hard"],fg_color="#393A3B",button_color="#393A3B",dropdown_fg_color="#393A3B",button_hover_color="#393A3B",dropdown_hover_color="#393A3B",dropdown_text_color="white",text_color="white")

        #buttons
        save_button = CTkButton(self,text="Save",fg_color="#F85656",corner_radius=30, command=lambda: self.adder(self.name.get(),self.hr.get(),self.min.get(),self.difficulty.get(),self.description.get("0.0","end"), self.ingredient_entries, self.Steps.get("0.0","end"),self.photo_path))
        
        self.upload_button = CTkButton(self,text="Browse",text_color="white", fg_color="#393A3B",corner_radius=30, command=self.upload_photo,width=50 )
        
        # reset_button= CTkButton(self,text="Reset",fg_color="#5684F8",corner_radius=30,command=lambda: reset(name,ingredientName,ingredients,steps) )
        self.plus_button = CTkButton(self, text="+", fg_color="#1B1C22", text_color="#848484", font=("", 20), width=20, hover_color="#1B1C22", command=self.add_ingredient_entry)
        self.add_ingredient_entry()  # Initially add one set of ingredient entry fields

        # Layout
        x = 50
        x2 = 440
        y = 50
        y2=50
        self.name.place(x=x, y=y)
        y += 40

        self.description.place(x=x, y=y)
        y += 100

        ingredientslabel.place(x=x + 10, y=y)
        y += 40

        self.stepslabel.place(x=x2,y=y2)
        y2+= 30
        self.Steps.place(x=x2,y=y2)

        save_button.place(x=x2+50,y = y2+500)
        
    def add_ingredient_entry(self,add=1):
        if(add==1):
            self.ingredient_name_entry = CTkEntry(self, placeholder_text="Ingredient Name", text_color="white", fg_color="#393A3B", placeholder_text_color="#848484", border_width=0, corner_radius=20, font=("", 16), width=200)
            self.ingredient_qty_entry = CTkEntry(self, placeholder_text="Qty", text_color="white", fg_color="#393A3B", placeholder_text_color="#848484", border_width=0, corner_radius=20, font=("", 16), width=80)
            self.ingredient_entries.append((self.ingredient_name_entry, self.ingredient_qty_entry))
        start_y = 230
        x = 50
        for entry_pair in self.ingredient_entries:
            entry_pair[0].place(x=x + 10, y=start_y)
            entry_pair[1].place(x=x + 220, y=start_y)
            start_y += 40
        self.plus_button.place(x=x+100+230, y=start_y-40)
        self.Difficultylabel.place(x=x+10,y=start_y)
        self.difficulty.place(x=x+150,y=start_y)
        start_y+=40
        self.PrepTime.place(x=x+10,y=start_y)
        start_y+=40
        self.hr.place(x=x+10,y=start_y)
        self.min.place(x=x+130,y=start_y)
        self.hrlabel.place(x=x+80,y=start_y)
        self.minlabel.place(x=x+200,y=start_y)
        start_y+=40
        self.UploadPhotoLabel.place(x=x+10,y=start_y)
        self.upload_button.place(x=x+160,y = start_y)
        start_y+=30
        filename =os.path.basename(self.photo_path)
        PhotoPathLabel = CTkLabel(self,text=filename,text_color="#BFBBBB",bg_color="#1B1c22",font=("",12))
        PhotoPathLabel.place(x=x+10,y=start_y)
        
    def deleter(self):
        if self.added_message:
            self.added_message.destroy()
        if self.incomplete_message:
            self.incomplete_message.destroy()
        if self.type_message:
            self.type_message.destroy()
        
    def clearer(self):
        self.clearAll()
    
   

        
        
        
    def upload_photo(self):
        print("OPen box")
        # Open file dialog to select photo
        file_path = filedialog.askopenfilename()
        if file_path:
            self.photo_path = file_path
        self.add_ingredient_entry(0)
    def clearAll(self):
        
        self.name.delete(0,'end')
        self.description.delete(0.0,'end')
        self.Steps.delete(0.0,'end')
        for entry_pair in self.ingredient_entries:
            entry_pair[0].delete(0,'end')
            entry_pair[1].delete(0,'end')
        self.ingredient_name_entry.delete(0,'end')
        self.ingredient_qty_entry.delete(0,'end')
        self.hr.delete(0,'end')
        self.min.delete(0,'end')
    def adder(self,recipe_name,hr, min,diff, description,ingredientsEntry,recipe_steps,photopath):
        self.added_message=CTkLabel(self,text="Recipe added succesfully🧑‍🍳",text_color="#BFBBBB",bg_color="#1B1c22",font=("",14))
        self.type_message=CTkLabel(self,text="Oops! Please enter a valid number",text_color="#BFBBBB",bg_color="#1b1c22")
        self.incomplete_message=CTkLabel(self,text="Oops! It seems like we're missing some details.",text_color="#BFBBBB",bg_color="#1b1c22")
        ingredients_list = []
        all_ingredient = []
        for entry_pair in ingredientsEntry:
            ingredient_name = entry_pair[0].get()
            ingredient_qty = entry_pair[1].get()
            ingredient_info ={}
            ingredient_info["name"]= ingredient_name
            ingredient_info["qty"]= ingredient_qty
            all_ingredient.append(ingredient_info)
            ingredients_list.append(ingredient_info)
            steplist= recipe_steps.splitlines()
            if (not ingredient_info or not ingredient_name or not ingredient_qty):
                self.incomplete_message.place(relx=0.1,rely=0.65,relheight=0.1)
                self.after(3000, self.deleter)
                return
            
            if (not hr.isdigit() or not min.isdigit() or int(min)>=60):
                self.type_message.place(relx=0.1,rely=0.65,relheight=0.1)
                self.after(3000, self.deleter)
                return
            
        print(recipe_steps)
        Recipe(recipe_name,int(hr),int (min),diff,description,all_ingredient, steplist,photopath)
        
        self.added_message.place(relx=0.1,rely=0.65,relheight=0.1)
        self.after(2,self.clearer)
        self.after(2000, self.deleter)
        

    #def added_info(self):
      #  self.toast=CTkLabel(text="Added successfully")
        
   


    

       










        
        


       