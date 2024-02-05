from customtkinter import *
from PIL import Image
from dashboard import DashboardFrame
from addrecipe import AddRecipeFrame
app = CTk()
app.geometry("1000x700")

def callnav1():
    add_recipe_frame.grid_remove()
    dashboard_frame.grid(row=0,column=1,sticky="nsew")

def callnav2():
    dashboard_frame.grid_remove()
    add_recipe_frame.grid(row=0,column=1,sticky="nsew")
app.grid_columnconfigure(0, weight=1)  
app.grid_columnconfigure(1, weight=3)  
app.grid_rowconfigure(0, weight=1)

navigation_frame = CTkFrame(app, fg_color="#191A1F", bg_color="#44454A")
navigation_frame.grid(row=0, column=0, sticky="nsew")
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

button_dashboard = CTkButton(navigation_items_frame,hover=False,corner_radius=30,text="Dashboard", text_color="white", fg_color="#F85656",command=callnav1)
button_dashboard.pack(pady=5)

button_add_recipe = CTkButton(navigation_items_frame,hover=False, text="Add Recipe", text_color="white", fg_color="transparent",command=callnav2)
button_add_recipe.pack(pady=5)

button_filter_sort = CTkButton(navigation_items_frame,hover=False, text="Filter Sort", text_color="white", fg_color="transparent")
button_filter_sort.pack(pady=5)

button_favourites = CTkButton(navigation_items_frame,hover=False, text="Favourites", text_color="white", fg_color="transparent")
button_favourites.pack(pady=5)
dashboard_frame = DashboardFrame(app)
add_recipe_frame = AddRecipeFrame(app)
# dashboard_frame.grid(row=0,column=1,sticky="nsew")
app.mainloop()

