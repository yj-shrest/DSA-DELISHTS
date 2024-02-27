from customtkinter import *
from PIL import Image
class FilterSort(CTkFrame):
    def __init__(self, parent_frame, **kwargs):
        super().__init__(parent_frame, **kwargs)
        self.configure(parent_frame, fg_color="#1B1C22", bg_color="#44454A")

        search_frame = CTkFrame(self, fg_color="transparent")
        search_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.05)

        searchBar = CTkEntry(search_frame, placeholder_text="Search Recipe", fg_color="#393A3B", border_width=0, text_color="#BFBBBB")
        searchBar.place(relx=0, rely=0, relwidth=0.8, relheight=1)

        sortBy = CTkEntry(search_frame, placeholder_text="Sort By", fg_color="#393A3B", border_width=0, text_color="#BFBBBB")
        sortBy.place(relx=0.85, rely=0, relwidth=0.15, relheight=1)
        