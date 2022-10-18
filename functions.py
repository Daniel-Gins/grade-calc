def cat_function():
    catdict={}
    while True:
        try:
            global cat
            cat=int(input("How many Graded categories are there: "))
            break
        except ValueError:
            print("Please enter a postive integer: \n")
            continue 
           
    for i in range(0,cat):
        while True:
            try:
                catname=input("Enter Category names: ")
                catworth=float(input("How much is it worth in decimal: "))
                if catname not in catdict:
                    catdict[catname]=catworth 
            except ValueError:
                print("please Enter Correct format: ")
                continue
    
            print(catdict)
        
            while len(catdict) == cat:
                confirmset={"y","yes"}
                noset={"no","n"}
                confirm=(input("Is this correct?: ")).lower()
                if confirm in confirmset:
                    print("Okay Moving on...")
                    return False
                elif confirm in noset:
                    cat_function()
                    return False
                else:
                    print("Try Again: ")