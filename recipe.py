# recipe.py
import os
class Recipe:
    def __init__(self, name, time_mins, ingredients, steps):
        self.name = name
        self.time_mins = time_mins
        self.ingredients = ingredients
        self.steps = steps
        self.store_to_file()

    def store_to_file(self):
        filename = f"{self.name.replace(' ', '_').lower()}_recipe.txt"  # Generate a filename based on the recipe name
        with open("recipies\\"+filename, 'w') as file:  # Using 'w' to overwrite the file if it already exists
            file.write(f"Recipe: {self.name}\n")
            file.write(f"Time: {self.time_mins} mins\n")
            file.write(f"Ingredients: {', '.join(self.ingredients)}\n")
            file.write(f"Steps: {self.steps}\n\n")
            
    def delete_recipe(self):
        filename = f"{self.name.replace(' ', '_').lower()}_recipe.txt"
        try:
            os.remove(filename)
            print(f"Recipe '{self.name}' deleted successfully.")
        except FileNotFoundError:
            print(f"Recipe '{self.name}' not found.")
    
