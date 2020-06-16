#Import Module with Auto class variables and methods
import AutoMod
#Import the prior save of the inventory file
from ImportableInventory import dictionary_name
Stored_Inventory=dictionary_name
Text_List=['make','model','year','color','mileage']

#This function is designed to export data to a txt file per parameters.
def Print_External(inventory):
    with open('Inventory.txt','w') as data:
        data.write(str(inventory))
    
#This function is designed to export data to a .py file so that existing inventory can be reloaded at the start of each program re-boot
def Export_File(inventory):
    with open('ImportableInventory.py','w') as data2:
        data2.write("dictionary_name = { \n")
        for k in sorted (inventory.keys()):
            data2.write(" %s : %s, \n" % (k, inventory[k]))
        data2.write("}")

selection=True
Vehicle=AutoMod.Auto()

#Menu for program main
while selection:
    print('Welcome to the Auto Inventory Manager Main Menu:')
    print('1) View all inventory on screen.')
    print('2) Add a vehicle to inventory.')
    print('3) Remove a vehicle from inventory.')
    print('4) Edit an existing vehicle.')
    print('5) Print inventory to a text file.')
    print('6) Exit the program.')
    selection=input('Please select an option:')
    #Selection 1-Print to screen
    if selection =='1':
        print(Stored_Inventory)
    #Selection 2-Add an auto.  Set to save updates to master file for next reload after each change.
    elif selection =='2':
        Vehicle.Add_Auto(Stored_Inventory)
        Export_File(Stored_Inventory)
    #Selection 3-Delete an auto.  Save update to master file.
    elif selection =='3':
        Vehicle.Delete_Auto(Stored_Inventory)
        Export_File(Stored_Inventory)
    #Selection 4-Edit an auto.  Save update to master file.
    elif selection =='4':
        Vehicle.Edit_Auto(Stored_Inventory)
        Export_File(Stored_Inventory)
    #Selection 5-Print inventory to external txt file.
    elif selection =='5':
        Print_External(Stored_Inventory)
    #Selection 7-Exit
    elif selection =='6':
        print('Exiting')
        break
    #Error control
    else:
        print('Please give a valid option.')
        continue
        