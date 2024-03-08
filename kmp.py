import os

class filewithpriority:
    def __init__(self,file,priority):
            self.file=file
            self.priority=priority                      #yo chai sort garna banako, dict use garda hunthyo hola tara aadha garda gardai dimag ma ayo
        

def namesearcher(string):
    array=[]
    output_file=[]
    array.append(0)
    this_is_the_last_variable=[]
    j=0
    for i in range (1,len(string)):
        if string[i]==string[j]:
            j=j+1
            array.append(j)
        else:
            while (j!=0):
                j=j-1
                j=array[j]
                if string[j]==string[i]:
                    j=j+1
                    array.append(j)
                    break
            if j==0:
                array.append(j)                 #kmp array
            
    
    
    for file in os.listdir("recipes"):
        file=file.replace('_',' ')
        file=file.rstrip('.json')
        j=0
        k=0
        for char in (file):
            k=k+1
            if string[j]==char:
                
                j=j+1
                if j>=len(string):
                    file=file.replace(' ','_')
                    file=file+'.json'
                    temp=filewithpriority(file,k)
                    output_file.append(temp)
                    break
            else:
                j=array[j]                          #read file name, _ .json hataidina ani string search hanne. ani priority ra filename vako object ko list banaune
        
        
    for i in range (0,len(output_file)):            
        for j in range (i+1,len(output_file)):
            if output_file[i].priority>=output_file[j].priority:                
                output_file[i],output_file[j]=output_file[j],output_file[i]             #sorting objects by priority

    j=0
    for i in output_file:
        this_is_the_last_variable.append(output_file[j].file)
        j=j+1
    
    return this_is_the_last_variable
    
    

                

    
    
    
            
print(namesearcher("chat"))