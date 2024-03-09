import os
directory_path="recipes"
import json

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
        
        temp = Node_object(file_name, data['time'])
        Recipe_list.append(temp)
    return Recipe_list


class Node_object:
    def __init__(self, filename,time):
        self.filename = filename
        self.time=parse_time(time)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key.time <= root.key.time:
            root.left = self._insert(root.left, key)
        elif key.time > root.key.time:
            root.right = self._insert(root.right, key)
        return root

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.key.filename)
            self._inorder_traversal(root.right, result)

bst=BST()


def createtree():                   #call at starup always
    for i in file_loader():
        bst.insert(i)
        #x=bst.inorder_traversal()
        
def updatetree(filename):           #call immediately after adding a file
    x=file_loader(filename)
    for x in x:
        bst.insert(x)
        #x=bst.inorder_traversal()
        

    
def sort_time(ascending__not_descending,filenames=set()):
        x=bst.inorder_traversal()
        if filenames:
            output=[]
            for y in x:
                if y in filenames:
                    output.append(y)
        
        else:
            output=x
        
        if (ascending__not_descending==1):
            return output
        else:
            output.reverse()
            return output
createtree()
            
                
            
            

        
