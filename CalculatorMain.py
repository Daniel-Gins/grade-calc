from functions import cat_function
from functions import cat 

if __name__ == "__main__":
    print("running...")


cat_function()


for i in range(0,cat):
    catpointlist=[]
    while True:
        try:
            catpoints=float(input("What will you score for each category?: "))
            if catpoints not in catpointlist:
                catpointlist.append(catpoints)
        except ValueError:
            print("Please enter integers")
            continue 
    
        print(catpointlist)
        
            
    




                    
                
                
            
               
        
            



