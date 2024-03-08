import os
import hashlib

recipes_list = []
hash_table = [set() for _ in range(999)]


class IngredientsRecipe:
    def __init__(self, file_name, ingredient_name):
        self.ingredient_name = ingredient_name
        self.file_name = file_name  #use va xaina tara chaiyo vane vanera rakhiraako. mero suruko vision ma chaiethyo


def hasher():
    for file in os.listdir("recipes"):
        with open("recipes/" + file, "r", encoding="utf-8") as file_opened:
            content = file_opened.read()
            start_index = content.find("Ingredients") + len("ingredients:")
            end_index = content.find("Steps")
            ingredients_string = content[start_index:end_index]
            ingredients_list = ingredients_string.split(' ')
            temp = IngredientsRecipe(file, ingredients_list)
            recipes_list.append(temp)

            for ing in ingredients_list:
                
                k = hash(ing.lower())%1024
                if hash_table[k]==None:
                    hash_table[k] = {file}
                else:
                    hash_table[k].add(file)


def search_ing(string):
    result=[]
    result_merge=set()
    result_final=set()
    i=0
    for z in string:
        k = hash(z.lower())%999
        if len(hash_table[k])!=0:
            result.append(hash_table[k])
            result_merge.update(result[i])
            i=i+1
            print("result for ",i-1 ,"is",result[i-1])
    print(result_merge)    
    for z in result_merge:
        for j in range (0,i):
            if z not in result[j]:
                k=333
                break            
        if k!=333:
            result_final.add(z)
    return result_final    


hasher()


print(search_ing({"yogurt","onion"}))


