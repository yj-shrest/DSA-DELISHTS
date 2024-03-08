from customtkinter import *
from PIL import Image, ImageTk
import os
import random


temp = {
    "recipe": "Food", 
    "img": "./photos/piro_chatpate.jpg",
    "description":"this is where description goes ",
    "ingredients": ["one","two", "three"],
    "steps":["step one this is step one this is step one", "step two this is step two testp teow rejweri fijjsd e", "step three dfihfs sffd fsd fsdf sdf sd", "step fsdfd sjfsd fsdjf dsfdsf sdjf sdjf dsj fsdj fjdsf dsjf dsj four"],
    "difficulty": "difficult",
    "time": "long"
}
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


class SingleFrame(CTkFrame):
    def __init__(self, parent_frame, recipe_data=temp):
        super().__init__(parent_frame)
        self.configure(parent_frame, bg_color="transparent", fg_color="transparent", corner_radius= 10)

        left_side= CTkFrame(self,width= self.winfo_screenwidth()*0.3, bg_color="transparent", fg_color="transparent")
        left_side.pack(side= LEFT, fill= Y)
        right_side= CTkFrame(self,width= self.winfo_screenwidth()*0.7, fg_color="transparent")
        right_side.pack(side= RIGHT, fill= BOTH)
        
        image = CTkImage(light_image= Image.open(recipe_data["img"]), size= (350,350))
        image_label = CTkLabel(left_side, image=image, text="", corner_radius=10, anchor='nw')
        image_label.place(relx= 0.02, rely=0.02, relwidth=1, relheight= 0.6)

        # # Title frame
        # title_frame = CTkFrame(self, bg_color="#292929")
        
        title_frame = CTkFrame(left_side, bg_color='transparent', fg_color='transparent', width= 350 )
        # title_frame.pack(padx=5)
        title_frame.place(relx= 0.02, rely=0.6, relwidth =0.9, relheight= 0.3)
        title_label = CTkLabel(title_frame, text=temp["recipe"].upper(), text_color="white",anchor=W, font=("Arial", 40,'bold'),width=100,height=30)
        title_label.pack(pady=1)
        detail_frame = CTkFrame(title_frame, bg_color="transparent",fg_color="transparent")
        detail_frame.pack(pady=2, padx= 2, fill= X)
        
        diff_frame= CTkFrame(detail_frame )
        time_frame= CTkFrame(detail_frame )

        diff_img_label = CTkLabel(diff_frame,text="" ,  image=CTkImage(light_image= Image.open('./photos/difficultyicon.png'), size= (20,15)))
        time_img_label = CTkLabel(time_frame,text="", anchor=E, image=CTkImage(light_image= Image.open('./photos/timeicon.png'), size= (20,20)))
        
        difficulty_label = CTkLabel(diff_frame, text= " "+ temp["difficulty"].upper(),anchor=W,  font=("Arial", 20,'normal'), fg_color="transparent", bg_color= "transparent", text_color="white",width=100,height=15,)
        time_label = CTkLabel(time_frame, text= " "+ temp["time"].upper(),anchor=W,bg_color= "transparent", font=("Arial", 20,'normal'), fg_color="transparent", text_color="white",width=100,height=15,)
        
        diff_img_label.pack(padx=1,side= "left")
        difficulty_label.pack(padx=1, side= "left")
        time_img_label.pack(padx=1, side= 'left')
        time_label.pack(padx=1, side="left")

        diff_frame.pack(padx=20, side = "left")
        time_frame.pack(padx=20 , side = "right")


        start_button = CTkButton(title_frame,hover=False,corner_radius=30,text="Start Timer", text_color="white", fg_color="#2196F3", font=("Arial", 20,"bold"), height=40 , command = lambda: print("Jesse, it's time to cook"))
        start_button.pack(pady=20)


        ing_frame = CTkFrame(right_side, bg_color='transparent', fg_color='transparent')
        ing_frame.place( relx= 0, rely= 0.01, relwidth=1, relheight=0.3 )
        ing_label = CTkLabel(ing_frame, text="Ingredients", text_color="white",anchor=W, font=("Arial", 30,'bold'),width=300,height=30)
        ing_label.pack(pady=1)
        
        for item in enumerate(temp["ingredients"]):
            ing_item = CTkLabel(ing_frame, text=f"• {item[1]}",anchor=W,bg_color= "transparent", font=("Arial", 20,'bold'), text_color="white",width=300,height=15)
            ing_item.pack(pady=3)
       
        step_frame = CTkFrame(right_side, bg_color='transparent', fg_color='transparent')
        step_frame.place( relx= 0, rely= 0.32, relwidth=1, relheight=0.8 )
        step_label = CTkLabel(step_frame, text="Steps", text_color="white",anchor=W, font=("Arial", 30,'bold'),width=200,height=30)
        step_label.pack(pady=1)

        back_img = CTkImage(light_image= Image.open("./photos/pakauda.jpg"), size= (350,350))
        back_button = CTkButton(self,hover=False, image= back_img ,corner_radius=30,text="GO BACK", text_color="white", bg_color="transparent", font=("Arial", 20,"bold"), height=40 , command = self.close)
        back_button.place(relx= 0.01, rely= 0.01, relheight= 0.05, relwidth= 0.05)
        
        
        for i, item in enumerate(temp["steps"]):

            item = wrap_text(item, 50)
            mystr = f"{i+1}. {item}" 
            ing_item = CTkLabel(step_frame, text=mystr,anchor=W,bg_color= "transparent", font=("Arial", 20,'bold'), justify= LEFT, text_color="white",width=200,height=15)
            ing_item.pack(pady=4, padx= 30, fill= X)

    
    def close (self):
        self.destroy()

