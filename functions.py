def cat_function():
    catdict={}
    while True:
        try:
            cat=int(input("How many Graded categories are there in 1 course: "))
            break
        except ValueError:
            print("Please enter a postive integer: \n")
            continue 
           
    for i in range(0,cat):
        while True:
            try:
                catname=input("Enter Category names: ")
                catworth=float(input("How much is it weighted/worth(don't include percent sign): "))
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
                    return catdict               
                elif confirm in noset:
                    cat_function()
                    return catdict
                else:
                    print("Try Again: ")


