# recipe.py
import os
import shutil
import json
# from hasher import customhash
import bst
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
        if not photoPath:
            photoPath=os.path.dirname(os.path.abspath(__file__))+'/logo.png'
            
        filename = (f"{name.lower().replace(' ','_')}.jpg")
        destination = os.path.join("photos", filename)
        shutil.copyfile(photoPath, destination)
        print(photoPath)
        
            

    def store_to_file(self):
        dict ={
      "recipe": f"{self.name}",
      "description": self.des,
      "difficulty": self.diff,
      "time": f"{self.hr} h {self.min} m",
      "ingredients": self.ingredients,
      "steps": self.steps,
      "isfav": False
    }
        filename = self.name.lower().replace(' ','_')+".json"
        with open(f"recipes/{filename}","+w") as file:
            json.dump(dict,file,indent=4)
        
        bst.updatetree({filename})
    # def has(self):
    #     ingredients=self.ingredients.split()
    #     for i in ingredients:
    #         customhash(ingredients.lower())

    def delete_recipe(self):
        filename = f"{self.name.replace(' ', '_').lower()}_recipe.txt"
        try:
            os.remove(filename)
            print(f"Recipe '{self.name}' deleted successfully.")
        except FileNotFoundError:
            print(f"Recipe '{self.name}' not found.")
    

