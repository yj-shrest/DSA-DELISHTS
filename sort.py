import json
import os

Recipe_list = []        #yo sab thau use garda hunxa ni ta ek choti load garesi feri load garna paparos

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

def file_loader():
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        temp = RecipeForSort(file_name, data['time'], data['difficulty'])
        Recipe_list.append(temp)

    #for i in range(len(Recipe_list)):
     #   print(Recipe_list[i].filename, Recipe_list[i].diff)

file_loader()               #this function should be called once at startup or when new files added


def sort_diff(Recipe_list,ascending__notdescending): #parameter kina deko vanda paxi search garda kheri sort garnu pare tei search le deko list lai yesma halde hunxa
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

print(sort_diff(Recipe_list,0))