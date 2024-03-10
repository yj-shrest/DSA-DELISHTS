from customtkinter import *
from PIL import Image, ImageTk
# from filtersort import resize_image
import time
import json
from pydub import AudioSegment
from pydub.playback import play
import tempfile

song = AudioSegment.from_wav('timer.wav')
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


clock =0
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
class FavImage(CTkLabel):
    def __init__(self,parent_frame,parent):
        super().__init__(parent_frame)
        self.parent = parent
        self.parent_frame = parent_frame
        if(self.parent.recipe_data["isfav"]):
            path = './photos/redfav.png'
        else:
            path = './photos/fav.png'
        self.configure(text="" ,anchor=E, bg_color="#1B1C22",fg_color="#1B1C22", image=CTkImage(light_image= Image.open(path), size= (40,40)))
        self.pack(side=RIGHT,pady=5)
        self.bind("<Button-1>",self.toggleFav)
    def toggleFav(self,t):
        self.parent.recipe_data["isfav"]=not self.parent.recipe_data["isfav"]
        name = self.parent.recipe_data["recipe"]
        with open(f"recipes/{name.lower().replace(' ','_')}.json","+w") as file:
            json.dump(self.parent.recipe_data,file,indent=4)
        if(self.parent.recipe_data["isfav"]):
            with open(f"fav/{name.lower().replace(' ','_')}.json","+w") as file:
                json.dump(self.parent.recipe_data,file,indent=4)
        else:
            os.remove("fav/"+name.lower().replace(' ','_')+".json")
        favlabel = FavImage(self.parent_frame,self.parent)
        self.destroy()


class ClockFrame(CTkFrame):
    def __init__(self,parent_frame,sec):
        super().__init__(parent_frame)
        self.parent_frame = parent_frame
        self.configure(parent_frame,bg_color="transparent",fg_color="transparent")
        self.pack(fill=X)
        self.seconds = sec
        self.label = CTkLabel(self, text=time.strftime("%H:%M:%S", time.gmtime(self.seconds)),text_color="white",font=("Arial", 24))
        self.label.pack(pady=20)

    def start_timer(self):
        self.after(1000, self.update_timer)

    def update_timer(self):
        self.seconds -= 1
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(self.seconds))
        self.label.configure(text=formatted_time)
        if(self.seconds>0):
            self.after(1000, self.update_timer)
        else:
            play(song)
class SingleFrame(CTkFrame):
    def __init__(self, parent_frame, recipe_data):
        global min,clock
        super().__init__(parent_frame)
        self.configure(parent_frame, bg_color="transparent", fg_color="transparent", corner_radius= 10)
        self.recipe_data = recipe_data
        left_side= CTkFrame(self,width= self.winfo_screenwidth()*0.3, bg_color="transparent", fg_color="transparent")
        left_side.pack(side= LEFT, fill= Y)
        right_side= CTkFrame(self,width= self.winfo_screenwidth()*0.7, fg_color="transparent")
        right_side.pack(side= RIGHT, fill= BOTH)
        image = Image.open('photos/'+recipe_data["recipe"].lower().replace(' ','_')+'.jpg')
        image = resize_image(image, 400,350)
        image = CTkImage(light_image= image,size=(400,350))
        image_label = CTkLabel(left_side, image=image, text="", corner_radius=10, anchor='nw')
        image_label.place(relx= 0.02, rely=0.03, relwidth=1, relheight= 0.6)

        # # Title frame
        # self.title_frame = CTkFrame(self, bg_color="#292929")
        
        self.title_frame = CTkFrame(left_side, bg_color='transparent', fg_color='transparent', width= 350 )
        # self.title_frame.pack(padx=5)
        self.title_frame.place(relx= 0.02, rely=0.48, relwidth =0.9, relheight= 0.3)
        headerframe = CTkFrame(self.title_frame, bg_color="transparent",fg_color="transparent",width=self.title_frame.winfo_screenwidth())
        headerframe.pack(fill=X,pady=5)
        title_label = CTkLabel(headerframe, text=recipe_data["recipe"].upper(), text_color="white",anchor=W, font=("Arial", 21,'bold'),width=100,height=30)
        title_label.pack(pady=1,side=LEFT)
        fav_label = FavImage(headerframe,self)
        # self.fav_label = CTkLabel(headerframe,text="" ,anchor=E, bg_color="#1B1C22",fg_color="#1B1C22", image=CTkImage(light_image= Image.open('./photos/fav.png'), size= (40,40)))
        # self.fav_label.pack(side=RIGHT,pady=5)
        # self.fav_label.bind("<Button-1>",self.toggleFav)



        detail_frame = CTkFrame(self.title_frame, bg_color="transparent",fg_color="transparent")
        detail_frame.pack(pady=2, padx= 2, fill= X)
        
        diff_frame= CTkFrame(detail_frame,bg_color="transparent",fg_color="transparent" )
        time_frame= CTkFrame(detail_frame,bg_color="transparent",fg_color="transparent" )

        diff_img_label = CTkLabel(diff_frame,text="" ,  image=CTkImage(light_image= Image.open('./photos/difficultyicon.png'), size= (20,15)))
        time_img_label = CTkLabel(time_frame,text="", anchor=E, image=CTkImage(light_image= Image.open('./photos/timeicon.png'), size= (20,20)))
        
        difficulty_label = CTkLabel(diff_frame, text= " "+ recipe_data["difficulty"].upper(),anchor=W,  font=("Arial", 20,'normal'), fg_color="transparent", bg_color= "transparent", text_color="white",width=100,height=15,)
        time_label = CTkLabel(time_frame, text= " "+ recipe_data["time"].upper(),anchor=W,bg_color= "transparent", font=("Arial", 20,'normal'), fg_color="transparent", text_color="white",width=100,height=15,)
        
        diff_img_label.pack(padx=1,side= "left")
        difficulty_label.pack(padx=1, side= "left")
        time_img_label.pack(padx=1, side= 'left')
        time_label.pack(padx=1, side="left")

        diff_frame.pack(padx=20, side = "left")
        time_frame.pack(padx=20 , side = "right")
        self.brek = False
        timer_frame = CTkFrame(self.title_frame,bg_color="transparent",fg_color="transparent")
        timer_frame.pack(fill=X)
        timer_label = CTkLabel(timer_frame,anchor= W,text="Set timer", font=(' ',18),text_color="white" )
        timer_label.pack(side=LEFT)
        self.min=CTkEntry(timer_frame,text_color="white",fg_color="#393A3B", border_width=0,font=("",20),width=60,corner_radius=15)
        min_label = CTkLabel(timer_frame,text="min",anchor=E,text_color="#BFBBBB",bg_color="#1B1c22",font=("",20))
        self.min.pack(padx=(15,0) ,side=LEFT)
        min_label.pack(padx=5 ,side=LEFT)
        start_button = CTkButton(timer_frame,hover=False,corner_radius=30,text="Start", text_color="white", fg_color="#2196F3", font=("Arial", 20,"bold"), height=30 )
        start_button.pack(pady=20,side=RIGHT)
        clock = ClockFrame(self.title_frame,0)
        start_button.configure(command=self.start)
        ing_frame1 = CTkFrame(right_side, bg_color='transparent', fg_color='transparent')
        ing_frame1.place( relx= 0, rely= 0.01, relwidth=0.48, relheight=0.3 )
        ing_frame2 = CTkFrame(right_side, bg_color='transparent', fg_color='transparent')
        ing_frame2.place( relx= 0.51, rely= 0.05, relwidth=0.48, relheight=0.3 )
        ing_label = CTkLabel(ing_frame1, text="Ingredients", text_color="white",anchor=W, font=("Arial", 20,'bold'),justify=LEFT,height=30)
        ing_label.pack(pady=1,fill=X)
        i=0
        for items in recipe_data["ingredients"]:
            name = (items["name"])
            qty = ' 'if (items["qty"])=="unspecified" else (items["qty"])
            if i<8:
                ing_item = CTkLabel(ing_frame1, text=f"• {name} {qty}",anchor=W,bg_color= "transparent", font=("Arial", 14,), text_color="white",height=15)
            else:
                ing_item = CTkLabel(ing_frame2, text=f"• {name} {qty}",anchor=W,bg_color= "transparent", font=("Arial", 14,), text_color="white",height=15)
            ing_item.pack(pady=3,fill=X)
            i+=1
       
        step_frame = CTkFrame(right_side, bg_color='transparent', fg_color='transparent')
        step_frame.place( relx= 0, rely= 0.32, relwidth=1)
        step_label = CTkLabel(step_frame, text="Steps", text_color="white",anchor=SW, font=("Arial",20,'bold'),width=200,height=30)
        step_label.pack(pady=1,fill=X)
        steps_frame = CTkScrollableFrame(right_side, bg_color='transparent', fg_color='transparent')
        steps_frame.place( relx= 0, rely= 0.36, relwidth=1,relheight=0.6)
        back_img = CTkImage(light_image= Image.open("./photos/back.png"),size=(40,40))
        back_button = CTkLabel(self, text='',image=back_img,height=40,width=40,bg_color="transparent",fg_color="transparent")
        back_button.bind("<Button-1>",self.close)
        back_button.place(relx= 0.92, rely= 0.0)
        for i, item in enumerate(recipe_data["steps"]):
            item = wrap_text(item, 69)
            mystr = f"{i+1}. {item}" 
            ing_item = CTkLabel(steps_frame, text=mystr,anchor=W,bg_color= "transparent", font=("Arial", 20), justify= LEFT, text_color="white",height=15)
            ing_item.pack(pady=4, padx= 3, fill= X)
    def close (self,t):
        self.destroy()
    def start(self):
        global clock
        clock.destroy()
        sec = int(self.min.get())*6
        clock = ClockFrame(self.title_frame,sec)
        clock.start_timer()
