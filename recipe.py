# recipe.py
import os
import shutil
from hasher import customhash

class Recipe:
    def __init__(self, name,hr,min,diff,des,ingredients, steps,photoPath):
        self.name = name
        self.des = des
        self.min = min
        self.hr = hr
        self.diff = diff
        self.ingredients = ingredients
        self.steps = steps
        self.store_to_file()
        if photoPath:
            filename = (f"{name}.jpg")
            destination = os.path.join("photos", filename)
            shutil.copyfile(photoPath, destination)

    def store_to_file(self):
        filename = f"{self.name.replace(' ', '_').lower()}_recipe.txt"  # Generate a filename based on the recipe name
        with open("recipies\\"+filename, 'w') as file:  # Using 'w' to overwrite the file if it already exists
            file.write(f"Recipe: {self.name}\n")
            file.write(f"Descirption: {self.des}\n")
            file.write(f"Difficulty: {self.diff}\n")
            file.write(f"Time: {self.hr} h {self.min} m\n")
            file.write(f"Ingredients: {self.ingredients}\n")
            file.write(f"Steps: {self.steps}\n\n")
   
    def has(self):
        
        ingredients=self.ingredients.split()
        for i in ingredients:
            customhash(ingredients.lower())
        





        
            
    def delete_recipe(self):
        filename = f"{self.name.replace(' ', '_').lower()}_recipe.txt"
        try:
            os.remove(filename)
            print(f"Recipe '{self.name}' deleted successfully.")
        except FileNotFoundError:
            print(f"Recipe '{self.name}' not found.")
    

