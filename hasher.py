import os
import hashlib
import json
class IngredientsRecipe:
    def __init__(self, file_name, ingredient_name):
        self.ingredient_name = ingredient_name
        self.file_name = file_name  

class HashTable:
    def __init__(self):
        self.hash_table = [set() for _ in range(1024)]
    def hasher(self):
        for file in os.listdir("recipes"):
            with open("recipes/" + file, "r") as file_opened:
                recipe_info = file_opened.read()
                data = json.loads(recipe_info)
                ingredientsandqty = data["ingredients"]
                for ing in ingredientsandqty:
                    temp=IngredientsRecipe(file,ing["name"].lower())                
                    k = self.hash(ing["name"].lower())%1024
                    if len(self.hash_table[k])==0:
                        self.hash_table[k] = {temp}
                    else:
                        self.hash_table[k].add(temp)
    def search_ing(self,string):
        result=[]
        result_merge=set()
        result_final=set()
        i=0

        for z in string:
            r=set()
            k = self.hash(z.lower())%1024
            if len(self.hash_table[k])!=0:
                for item in self.hash_table[k]:
                    if item.ingredient_name==z.lower():
                        r.add(item.file_name)
                result.append(r)
                result_merge.update(result[i])
                #print(r)
                i=i+1
                
            if len(r)==0:
                return (set())   
                #print("result for ",i-1 ,"is",result[i-1])
        #print(result_merge)    
        for z in result_merge:
            for j in range (0,i):
                k=0
                if z not in result[j]:
                    k=333
                    break            
            if k!=333:
                result_final.add(z)
                
        return result_final     
    def hash(self,word):
        hash_value = 0
        for char in word:
            hash_value = (hash_value * 256 + ord(char)) % 1024
        index = hash_value
        return index


