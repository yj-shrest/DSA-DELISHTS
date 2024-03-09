from customtkinter import *
from PIL import Image,ImageTk,ImageDraw,ImageOps
import json,random
from hasher import HashTable
from kmp import namesearcher
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
  def __init__(self, master, image_path, size=(100, 100), corner_radius=20, opacity=255):
    super().__init__(master)
    
    self.image_label = CTkLabel(self,bg_color="#1B1C22",fg_color="#1B1C22",text=" ", image=create_rounded_image(image_path, size, corner_radius, opacity))
    self.image_label.pack(padx=0, pady=0)
    
def create_recipe_list(filenames):
    recipe_list = []
    selected_files = filenames
    for file_name in selected_files:
        print(file_name)
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
            filenames = hashtable.search_ing(input)
            print(filenames)
            food = create_recipe_list(filenames)
            self.results_frame.destroy()
            self.dispayRecipes()
        def onkeypress(event):
            global food
            input = searchBar.get()
            filenames = namesearcher(input)
            print(filenames)
            if filenames:
                food = create_recipe_list(filenames)
                self.results_frame.destroy()
                self.dispayRecipes()
        search_frame = CTkFrame(self, fg_color="transparent")
        search_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.05)

        searchBar = CTkEntry(search_frame, placeholder_text="Search Recipe", fg_color="#393A3B", border_width=0, text_color="#BFBBBB")
        searchBar.place(relx=0, rely=0, relwidth=0.8, relheight=1)
        searchBar.bind("<Return>",onenter)
        searchBar.bind("<KeyRelease>",onkeypress)

        sortBy = CTkEntry(search_frame, placeholder_text="Sort By", fg_color="#393A3B", border_width=0, text_color="#BFBBBB")
        sortBy.place(relx=0.85, rely=0, relwidth=0.15, relheight=1)
        
        self.results_frame = CTkFrame(self,fg_color="transparent")
        self.results_frame.place(relx=0.05,rely=0.10, relwidth= 0.9,relheight=0.90)
        self.dispayRecipes()
    def dispayRecipes(self):
        self.results_frame = CTkFrame(self,fg_color="transparent")
        self.results_frame.place(relx=0.05,rely=0.10, relwidth= 0.9,relheight=0.90)
        for i,singleFood in enumerate(food):
            recipe_item= CTkFrame(self.results_frame,fg_color="transparent",border_color="#393A3B",border_width=2,corner_radius=40)
            recipe_item.place(relx=0.0,rely=0.03+0.23*i,relheight=0.20,relwidth=1)
            recipe_image_frame = CTkFrame(recipe_item,fg_color="transparent",height=recipe_item.winfo_screenheight()*0.95,width=recipe_item.winfo_screenwidth()*0.25)
            recipe_image_frame.pack(side=LEFT)
            name = singleFood["recipe"]
            image_path = './photos/'+"_".join(name.lower().split(" "))+'.jpg'
            image_button = RoundedImageButton(recipe_image_frame, image_path, size=(228, 185), corner_radius=40, opacity=200)
            image_button.pack(side=LEFT,fill=BOTH)

            detail_frame = CTkFrame(recipe_item,fg_color="transparent",height=recipe_item.winfo_screenheight()*0.95,width=recipe_item.winfo_screenwidth()*0.7 )
            detail_frame.pack(side=LEFT,padx=15)

            title = CTkLabel(detail_frame,text= singleFood["recipe"],anchor=W,bg_color="transparent",fg_color="transparent",text_color="white",font=(' ',22,'bold'))
            title.pack(fill=X)
            description = CTkLabel(detail_frame,justify=LEFT,text= wrap_text(singleFood["description"],120),anchor=W,bg_color="transparent",fg_color="transparent",text_color="#BFBBBB",font=(' ',16))
            description.pack(fill=X,pady=5)

            another_frame = CTkFrame(detail_frame,fg_color="transparent",width=recipe_item.winfo_screenwidth())
            another_frame.pack(fill=X)

            time_label = CTkLabel(another_frame, text= ' '+ singleFood['time']+"  ", anchor=W,text_color="white",width=150,height=20,font=(' ',20,'normal'),image=CTkImage(light_image= Image.open('./photos/timeicon.png'), size= (20,20)),compound=LEFT,justify=LEFT)
            time_label.pack(side=LEFT)

            diff_label = CTkLabel(another_frame, text= ' '+ singleFood['difficulty']+"  ", anchor=W,text_color="white",width=100,height=20,font=(' ',20,'normal'),image=CTkImage(light_image= Image.open('./photos/difficultyicon.png'), size= (22,15)),compound=LEFT,justify=LEFT)
            diff_label.pack(side=LEFT, padx= 20)
        

