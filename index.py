from turtle import goto
from unicodedata import name

def Home():
    print("1 - Check in \n")
    print("2 - Check out \n")
    print("3 - Display info \n")
    print("4 - Search Quest's Username \n")
    print("5 - Exit Application \n")
    
    ch=int(input("->"))
        
    if ch == 1:
        print(" ")
        Check_in()

    elif ch == 2:
        print(" ")
        Check_out()   
            
    elif ch == 3:
        print(" ")
        Display
        
        
    elif ch == 4:
        print(" ")
            
    elif ch == 5:
        print("Goodbye!")
        exit()
        
    else:
        print("No Command avaliable")
        Home()


print("---------- Setting up Hotel ----------")
room_num = input("Enter number of floor:")
floor_num = input("Enter number of rooms in each floor:")
print("Hotel is already setup sucessfully with " + floor_num + " floors and "+ room_num + " rooms" )
print("--------------------------------------")
Home()



#Define check_in
def Check_in():
    print("Choose Option (1-5) > 1 \n")
    in_floor = input("Enter floor number (1-" + floor_num + ") > ")
    in_room = input("Enter room number (1-)" + room_num + ") > ")
    if in_floor > floor_num <= 0 or in_room > room_num <= 0:
        print("Room is Unavailable")
    else:
        name = input("Enter guest's name > ")
        print(name + "has checked in sucessfully \n")

    input("Press Enter to continue...\n")
    Home()
      
#Define Check_out
def Check_out():
    print("Choose Option (1-5) > 2 \n")
    print("Check out process \n")
    out_floor = input("Enter floor number (1-" + floor_num + ") > ")
    out_room = input("Enter room number (1-)" + room_num + ") > ")
    if out_floor != in_floor or out_room != in_room:
        print("This room haven't check in yet")
    else:
        confirm = input("Guest's name " + name + " Press 1 to check out and 0 to cancel > ")
        if confirm == 1:
            print( name + " have checked out sucessfully ")
        else: 
            print( " Check out have been canceled ")

    input("Press Enter to continue...\n")
    Home()

    
#Define Display
def Display():
    print("Choose Option (1-5) > 3 \n")

#Define Search 
def Search():
    print("Choose Option (1-5) > 4 \n")
    check_name = input("Enter guest's name > ")
    if check_name == name:
        print(check_name + " Stay on " + in_floor + " and room number " + in_room )
    else:
        print("Guest no Found \n")

    input("Press Enter to continue...\n")
    Home()
