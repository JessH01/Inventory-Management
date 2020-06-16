#Get_String and Get_Integer are repetitive codes for retreiving my info in Add_Auto.  These are useful functions, but not directly attributed to the Auto class, so are outside of it.
def Get_String(StrType):
    string=str(input("Please enter the %s of this vehicle:" %StrType))
    string=string.title()
    return string
    
def Get_Integer(IntType):
    integer=input("Please enter the %s of this vehicle:" %IntType)
    while not integer.isdigit():
        integer=input("Please enter the %s of this vehicle in integer form:" %IntType)
    integer=int(integer)
    return integer

#Initialize my class
class Auto:
    def __init__(self):
        self.make=''
        self.model=''
        self.color=''
        self.year=0
        self.mileage=0
    
    #Function to add a vehicle into inventory.  Automatically requests ALL data points in fixed order to create consistency in
    #dictionary for later.
    def Add_Auto(self,inventory):
        self.inventory=inventory
        Text_List=['make','model','year','color','mileage']
        Master_List=[self.make,self.model,self.year,self.color,self.mileage]
        Output_List=[]
        x=0
        y=max(self.inventory.keys())+1
        print('Creating New Vehicle.  Inventory #%d' % y)
        for new in Master_List:
            call=Text_List[x]
            if isinstance(new,int):
                Output_List.append(Get_Integer(call))
                x=x+1
            else:
                Output_List.append(Get_String(call))
                x=x+1
        return self.inventory.update({y:Output_List})
            
    #Function to delete a vehicle.
    def Delete_Auto(self,inventory):
        self.inventory=inventory
        call=int(input('Enter the Inventory # for the unit you wish to remove:'))
        if call in self.inventory.keys():
            print('The vehicle you are deleting is:')
            print(self.inventory[call])
            check=input('If this is the correct vehicle, press y, otherwise press any key to exit:')
            if check.lower()=='y':
                del self.inventory[call]
            else:
                print('Exiting to Main Menu.')
        else:
            print('That is an incorrect Inventory #.  Returning to Mai Menu.')
        return self.inventory
    
    #Function to update any or all parts of a vehicle's info.
    def Edit_Auto(self,inventory):
        self.inventory=inventory
        Text_List=['make','model','year','color','mileage']
        My_List=[]
        edit=int(input('Enter the Inventory # for the unit you need to edit:'))
        if edit in self.inventory.keys():
            My_List=self.inventory[edit]
            print('The vehicle you are editing is:', My_List)
            string=''
            while string != 'r':
                string=input('Please enter which feature you need to edit.  Enter ''R'' to return to the main menu:')
                string=string.lower()
                if string=='r':
                    break
                elif string in Text_List:
                    call=Text_List.index(string)
                    if isinstance(My_List[call],int):
                        My_List[call]=Get_Integer(string)
                    else:
                        My_List[call]=Get_String(string)
                else:
                    print('That is not a valid entry.  Available features to edit are:', Text_List)
            self.inventory[edit]=My_List
        else:
            print('That is an incorrect Inventory #.  Returning to Main Menu.')
        return self.inventory