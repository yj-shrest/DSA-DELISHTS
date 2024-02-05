from customtkinter import *
from PIL import Image
class AddRecipeFrame(CTkFrame):
    def __init__(self, parent_frame, **kwargs):
        super().__init__(parent_frame, **kwargs)
        self.configure(parent_frame,fg_color="#1B1C22",bg_color="#44454A")
        # self.grid(row=0, column=1, sticky="nsew")
        self.grid_rowconfigure(0,weight=2)
        self.grid_rowconfigure(1,weight=8)
        self.grid_columnconfigure(0,weight=1)

        label = CTkLabel(self, text="Add Recipe menuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu", text_color="white")
        # label.grid(row= 0,column=0, pady=20)
        # search_frame = CTkFrame(self, fg_color="transparent")
        # search_frame.grid(row=0, column=0)
        # search_frame.grid_rowconfigure(0, weight=2)
        # search_frame.grid_rowconfigure(1, weight=8)
        # search_frame.grid_columnconfigure(0, weight=4)
        # search_frame.grid_columnconfigure(1, weight=1)

        # searchBar = CTkEntry(search_frame, placeholder_text="Search Recipe",  fg_color="#393A3B", border_width=0, text_color="#BFBBBB")
        # searchBar.grid(row=0, column=0, sticky="nsew", pady=40)

        # filterBar = CTkEntry(search_frame, placeholder_text="Filter", width=50, fg_color="#393A3B", border_width=0, text_color="#BFBBBB")
        # filterBar.grid(row=0, column=1, sticky="nsew", pady=40, padx=10)