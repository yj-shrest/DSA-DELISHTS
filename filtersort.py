from customtkinter import *
from PIL import Image,ImageTk,ImageDraw,ImageOps
import json,random
from hasher import HashTable
from kmp import namesearcher
from singlepage import SingleFrame
import time
from sort import file_loader,sort_diff
import bst
def wrap_text(text, width):
    lines = []
    current_line = ""
    words = text.split()
    for word in words:
        if len(current_line + word) <= width:
            current_line += word + " "
        else:
            lines.append(current_line)
            current_line = word + " "
    if current_line:
        lines.append(current_line)
    return "\n".join(lines)
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
  def __init__(self, master, image_path,myparent,  size=(100, 100), corner_radius=20, opacity=255):
    super().__init__(master)
    
    self.image_label = CTkLabel(self,bg_color="#1B1C22",fg_color="#1B1C22",text=" ", image=create_rounded_image(image_path, size, corner_radius, opacity))
    self.image_label.pack(padx=0, pady=0)
    self.image_label.bind("<Button-1>", myparent.openSingle)
    
def create_recipe_list(filenames):
    recipe_list = []
    selected_files = filenames
    for file_name in selected_files:
        if file_name.endswith('.json'):
            file_path = os.path.join('recipes/', file_name)
            with open(file_path, 'r') as file:
                recipe_info = file.read()
                recipe_list.append(json.loads(recipe_info))
    return recipe_list

folder_path = 'recipes'
food = create_recipe_list(os.listdir(folder_path))


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
        hashtable = HashTable()
        hashtable.hasher()
        self.filenames =[]
        def onenter(event):
            global food
            input = searchBar.get()
            input = input.split(",")
            j=0
            for i in input:
                if i[len(i)-1] == ' ':
                    i = i[:-1]
                while i[0]==' ':
                    i = i[1:]
                input[j]=i
                j+=1
            self.filenames = hashtable.search_ing(input)
            self.update("check")
        def onkeypress(event):
            global food
            print(event.keysym)
            if(event.keysym !="Return"):
                input = searchBar.get()
                if not input:
                    input = " "
                self.filenames = namesearcher(input)
                self.update("no")
        
        search_frame = CTkFrame(self, fg_color="transparent")
        search_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.05)

        searchBar = CTkEntry(search_frame, placeholder_text="Search Recipe", fg_color="#393A3B", border_width=0, text_color="#BFBBBB")
        searchBar.place(relx=0, rely=0, relwidth=0.8, relheight=1)
        searchBar.bind("<Return>",onenter)
        searchBar.bind("<KeyRelease>",onkeypress)

        self.sortBy = CTkOptionMenu(search_frame, values=["Time","Difficulty"],fg_color="#393A3B",button_color="#393A3B",dropdown_fg_color="#393A3B",button_hover_color="#393A3B",dropdown_hover_color="#393A3B",dropdown_text_color="white",text_color="white",command= self.sort)
        self.sortBy.place(relx=0.85, rely=0, relwidth=0.15, relheight=1)
        self.dispayRecipes()
    def update(self,flag):
            print(self.filenames)
            global food
            if(flag =="Difficulty"):
                self.filenames = sort_diff(1,self.filenames)
            if(flag=="check"):
                flag = self.sortBy.get()
                self.update(flag)
                # print(self.filenames)
            if(flag=="Time"):
                if(self.sortBy.get()):
                    self.filenames = bst.sort_time(1,0,self.filenames)
                else:
                    self.filenames = bst.sort_time(1,1,self.filenames)
            food = create_recipe_list(self.filenames)
            self.results_frame.destroy()
            self.dispayRecipes()
    def single(self,temp):
        self.single_recipe = SingleFrame(self,temp)
        # print(temp)
        self.single_recipe.place(relx= 0.03, rely=0.03, relheight=0.95 ,relwidth= 0.96)

    def sort(self,t):
        self.update(t)
    def dispayRecipes(self):
        self.results_frame = CTkScrollableFrame(self,fg_color="transparent",bg_color="transparent",height=1000)
        self.results_frame.place(relx=0.05,rely=0.10, relwidth= 0.9,relheight=0.90)
        for i,singleFood in enumerate(food):
            recipe_item= RecipeFrame(self.results_frame,  parent_dashboard=self, singleFood=singleFood,height = self.results_frame.winfo_screenheight()*0.25)
            # recipe_item.place(relx=0.0,rely=0.03+0.23*i,relheight=0.20,relwidth=1)
            recipe_item.pack(fill=X,pady=10)


class RecipeFrame(CTkFrame):
    def __init__(self, parent_frame,parent_dashboard, singleFood,height, **kwargs):
        super().__init__(parent_frame, **kwargs)
        self.recipe_data = singleFood
        self.configure( parent_frame, fg_color="transparent",border_color="#393A3B",border_width=2,corner_radius=40,height =height)
        self.parent_dashboard = parent_dashboard
        # Description label
        # image = image.resize((100, 100))  
        # photo = ImageTk.PhotoImage(image)
        # self.image_label.image = photo 
      
        recipe_image_frame = CTkFrame(self,fg_color="transparent",height=self.winfo_screenheight()*0.8,width=self.winfo_screenwidth()*0.25)
        recipe_image_frame.pack(side=LEFT)
        name = singleFood["recipe"]
        image_path = './photos/'+"_".join(name.lower().split(" "))+'.jpg'
        image_button = RoundedImageButton(recipe_image_frame, image_path, self, size=(228, 170), corner_radius=40, opacity=255)
        image_button.pack(side=LEFT,fill=X)

        detail_frame = CTkFrame(self,fg_color="transparent",height=self.winfo_screenheight()*0.95,width=self.winfo_screenwidth()*0.7 )
        detail_frame.pack(side=LEFT,padx=15)

        title = CTkLabel(detail_frame,text= singleFood["recipe"],anchor=W,bg_color="transparent",fg_color="transparent",text_color="white",font=(' ',22,'bold'))
        title.pack(fill=X)
        description = CTkLabel(detail_frame,justify=LEFT,text= wrap_text(singleFood["description"],120),anchor=W,bg_color="transparent",fg_color="transparent",text_color="#BFBBBB",font=(' ',16))
        description.pack(fill=X,pady=5)

        another_frame = CTkFrame(detail_frame,fg_color="transparent",width=self.winfo_screenwidth())
        another_frame.pack(fill=X)

        time_label = CTkLabel(another_frame, text= ' '+ singleFood['time']+"  ", anchor=W,text_color="white",width=150,height=20,font=(' ',20,'normal'),image=CTkImage(light_image= Image.open('./photos/timeicon.png'), size= (20,20)),compound=LEFT,justify=LEFT)
        time_label.pack(side=LEFT)

        diff_label = CTkLabel(another_frame, text= ' '+ singleFood['difficulty']+"  ", anchor=W,text_color="white",width=100,height=20,font=(' ',20,'normal'),image=CTkImage(light_image= Image.open('./photos/difficultyicon.png'), size= (22,15)),compound=LEFT,justify=LEFT)
        diff_label.pack(side=LEFT, padx= 20)
        title.bind("<Button-1>",self.openSingle)
        time_label.bind("<Button-1>",self.openSingle)
        description.bind("<Button-1>",self.openSingle)
        diff_label.bind("<Button-1>",self.openSingle)
        self.bind("<Button-1>",self.openSingle)
        another_frame.bind("<Button-1>",self.openSingle)


        # invisible_button = Button(master=self,image=transparency, width=20, height= 20, command = self.parent_dashboard.single )
        # invisible_button.place(relx=0.0, rely=0.0)
    def openSingle(self,t):
        current_data= self.recipe_data
        self.parent_dashboard.single(current_data)
    
        
