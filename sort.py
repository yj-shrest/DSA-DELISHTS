import json
import os


class RecipeForSort:
    def __init__(self, filename, time, diff):
        self.filename = filename
        self.time = parse_time(time)
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
   
def parse_time(time_str):
  time_str = time_str.replace(" ", "")
  
  # Split the string into hours and minutes
  if "h" in time_str:
      hours, minutes = time_str.split("h")
      minutes = minutes.replace("m", "")
  else:
      hours = "0"
      minutes = time_str.replace("m", "")
  
  # Convert hours and minutes to integers
  hours = int(hours)
  minutes = int(minutes)
  
  # Calculate total time in minutes
  total_minutes = hours * 60 + minutes
  return total_minutes

def sort_time(recipe_list, ascending=True):
    if not recipe_list:  # Handle empty list case for clarity
        return []
    time_counts = [0] * (max(recipe.time for recipe in recipe_list) + 1)  # Efficient counter allocation

    # Initialize time counters
    for recipe in recipe_list:
        time_counts[recipe.time] += 1

    # Calculate cumulative counts (optimized based on feedback)
    for i in range(1, len(time_counts)):
        time_counts[i] += time_counts[i - 1]

    sorted_filenames = [None] * len(recipe_list)  # List to store sorted filenames

    # Fill sorted list using time counters in reverse order
    for i in range(len(recipe_list) - 1, -1, -1):
        recipe = recipe_list[i]
        time = recipe.time
        sorted_filenames[time_counts[time] - 1] = recipe.filename  # Get filename using counter
        time_counts[time] -= 1
    return sorted_filenames if ascending else sorted_filenames[::-1]

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

# print(sort_diff(Recipe_list,0))
