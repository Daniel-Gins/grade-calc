catdict={}
confirm_list=["y","yes"]
while True:
    try:
        cat=int(input("How many Graded categories are there: "))
        break
    except ValueError:
        print("Please enter a postive integer: \n")
        continue 
        
for i in range(0,cat):
    try:
        catname=input("Enter Category names: ")
        catworth=float(input("How much is it worth in decimal: "))
        
        if catname not in catdict:
            catdict[catname]=catworth          
                
    except ValueError:
        print("please Enter Correct format: ")
        continue
    
    print(catdict)
while True:
            try:
                confirm=str(input("Is this correct?: ")).lower()
                if confirm in confirm_list:
                    print("Okay Moving on...")
                    break
       
            except ValueError:
                print("wrong input")
               
        
            



