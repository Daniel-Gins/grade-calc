from ast import Return
from functions import cat_function
def main():
    def score():
        x = cat_function()
        print(x)
        def catpointfun():
                catpointlist=[]
                while len(catpointlist)!=len(x):
                    try:
                        catpoints=int(input("What will your total grade be in that category?(don't include percent sign): "))
                        catpointlist.append(catpoints)
                    except ValueError:
                        print("Please enter integers")
                        continue
                    print(catpointlist,) 
                    
                return catpointlist
        print("---------")        
        wholenumlist=catpointfun()
        fractlist=[]
        for item in wholenumlist:
            fractlist.append(item/100)
        convdictlist=list(x.values())
        arithmaticlist=[fractlist[i]*convdictlist[i] for i in range(len(fractlist)) ]
        total=sum(arithmaticlist)
        return total
    total=score()
    print("Your total grade will be: ",total,"%")
    y=input("Press enter to exit or type rerun to start over: ")
    while True:
        if y=="rerun":
            main()
            break
        else:
            SystemExit
            break
if __name__ == "__main__":
    main()
    
            
        
    
        
       




        

            
    




                    
                
                
            
               
        
            



