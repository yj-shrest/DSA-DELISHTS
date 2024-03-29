from customtkinter import *
from PIL import Image
from dashboard import DashboardFrame
from addrecipe import AddRecipeFrame
from filtersort import FilterSort
from favorites import FavoritesFrame
import os

app = CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

app.geometry(f"{screen_width}x{screen_height}+0+0")
nav =1
def callnav1():
    global nav
    filter_sort_frame.grid_remove()
    add_recipe_frame.grid_remove()
    favotites_frame.clearSinglePage()
    favotites_frame.grid_remove()
    dashboard_frame.initialize()
    nav=1
    placeitems()

def callnav2():
    global nav
    filter_sort_frame.grid_remove()
    dashboard_frame.clearSinglePage()
    dashboard_frame.grid_remove()
    favotites_frame.clearSinglePage()
    favotites_frame.grid_remove()
    add_recipe_frame.grid(row=0,column=1,sticky="nsew")
    nav=2
    placeitems()
def callnav3():
    global nav
    add_recipe_frame.grid_remove()
    dashboard_frame.clearSinglePage()
    dashboard_frame.grid_remove()
    favotites_frame.clearSinglePage()
    favotites_frame.grid_remove()
    filter_sort_frame.grid(row=0,column=1,sticky="nsew")
    nav=3
    placeitems()
def callnav4():
    global nav
    add_recipe_frame.grid_remove()
    dashboard_frame.clearSinglePage()
    dashboard_frame.grid_remove()
    filter_sort_frame.grid_remove()
    favotites_frame.initialize()
    nav=4
    placeitems()

def getnavcolor(n,nav):
    if(n==nav): 
        return "#F85656"
    else:
        return "transparent"
app.grid_columnconfigure(0, weight=1)  
app.grid_columnconfigure(1, weight=3)  
app.grid_rowconfigure(0, weight=1)

navigation_frame = CTkFrame(app, fg_color="#191A1F", bg_color="#44454A",width=350)
navigation_frame.grid(row=0, column=0,sticky="snew")
navigation_frame.grid_rowconfigure(0, weight=1)
navigation_frame.grid_rowconfigure(1, weight=3)
navigation_frame.grid_columnconfigure(0, weight=1)

# Logo frame
logo_frame = CTkFrame(navigation_frame, fg_color="transparent")
logo_frame.grid(row=0, column=0, sticky="nsew", pady=(10, 0))
logo_frame.grid_rowconfigure(0, weight=1)
logo_frame.grid_columnconfigure(0, weight=1)

logo_image = Image.open("LOGO.png")
logo_image = logo_image.resize(size=(1100, 1100))

logo_label = CTkLabel(logo_frame, text="", image=CTkImage(light_image=logo_image, size=(150, 130)))
logo_label.grid(row=0, column=0, sticky="nsew")

# Navigation items
navigation_items_frame = CTkFrame(navigation_frame, fg_color="transparent")
navigation_items_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 10))
def placeitems():
    for widget in navigation_items_frame.winfo_children():
        widget.destroy()
    button_dashboard = CTkButton(navigation_items_frame,hover=False,corner_radius=30,text="Dashboard", text_color="white", fg_color=getnavcolor(1,nav),command=callnav1,font=(' ',18))
    button_dashboard.pack(pady=8)

    button_add_recipe = CTkButton(navigation_items_frame,hover=False,corner_radius=30, text="Add Recipe", text_color="white", fg_color=getnavcolor(2,nav),command=callnav2,font=(' ',18))
    button_add_recipe.pack(pady=8)

    button_filter_sort = CTkButton(navigation_items_frame,hover=False,corner_radius=30, text="Filter Sort", text_color="white", fg_color=getnavcolor(3,nav),command=callnav3,font=(' ',18))
    button_filter_sort.pack(pady=8)

    button_favourites = CTkButton(navigation_items_frame,hover=False,corner_radius=30, text="Favourites", text_color="white", fg_color=getnavcolor(4,nav),command=callnav4,font=(' ',18))
    button_favourites.pack(pady=8)
placeitems()
print(1)
dashboard_frame = DashboardFrame(app,width=650)
add_recipe_frame = AddRecipeFrame(app,width=650)
filter_sort_frame = FilterSort(app,width=650)
favotites_frame = FavoritesFrame(app,width=650)
dashboard_frame.grid(row=0,column=1,sticky="nsew")
app.mainloop()

