import json
import os


class RecipeForSort:
    def __init__(self, filename, time, diff):
        self.filename = filename
        self.time = time
        if diff == "Easy" or diff==" Easy":
            self.diff = 0
        elif diff == " Medium" or diff == "Medium":
            self.diff = 1
        else:
            self.diff = 2

directory_path = "recipes"

def file_loader(recipe_ko_vandaar=set()):
    Recipe_list = []       
    file_list=[]
    if recipe_ko_vandaar:
        file_list=recipe_ko_vandaar
    else:
        file_list=os.listdir(directory_path)
    for file_name in file_list:
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        temp = RecipeForSort(file_name, data['time'], data['difficulty'])
        Recipe_list.append(temp)
    return Recipe_list


def sort_diff(ascending__notdescending,Recipe_list=set()): 
    Recipe_list=file_loader(Recipe_list)
    counter = [0] * 3
    output = [None] * len(Recipe_list)

    for i in range(len(Recipe_list)):
        n = Recipe_list[i].diff
        counter[n] += 1    #initialise counter 

    for i in range(1,3):
        counter[i]+=counter[i-1]  #CUMulative array idk why...algorithm ma tei thyo..bujna jhyau lagyo
        
    

    for i in range(len(Recipe_list)):
        n = Recipe_list[i].diff
        output[counter[n] - 1] = Recipe_list[i].filename
        counter[n] -= 1

    if ascending__notdescending==1:
        return output
    else:
        output.reverse()
        return output

print(sort_diff(1,{"buff_momo.json","milk_tea.json"}))