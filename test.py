def Home():
    print("1 - Check in \n")
    print("2 - Check out \n")
    print("3 - Display info \n")

    selection=int(input("Enter choise"))
        
    if selection == 1:
       
        Check_in()

    elif selection == 2:
      
        Check_out()   
            
    elif selection == 3:
       
        exit
        
    else:
        print("No Command avaliable")
        Home()

print("---------- Setting up Hotel ----------")
room_num = input("Enter number of floor:")
floor_num = input("Enter number of rooms in each floor:")
print("Hotel is already setup sucessfully with " + floor_num + " floors and "+ room_num + " rooms" )
print("--------------------------------------")





#Define check_in
def Check_in():
    print("you")
      
#Define Check_out
def Check_out():
    print("me")

    
Home()