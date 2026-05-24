#=====Every Operation Related To Contacts Will Be Here=====

from contacts import Contacts
from contacts_manager import ContactsManager



#---Defining add_contact()
#  (To Add Contact To Contacts List)

def add_contact(manager):
    name = input("Enter Name : ")
    phone = input("Enter Phone : ")
    email = input("Enter Email : ")
    new_contact = Contacts(name, phone, email)
    manager.contacts.append(new_contact)
    print(f"Contact with {name} Added Successfully!!")
    manager.save_contacts()



#---Defining display_contacts()
#  (To Display All Contacts Nicely)

def display_contacts(manager):
    if not manager.contacts:
        print("No Contacts To Display!!\nTry Creating New One!!")
    else:
        for contact in manager.contacts:
            print(contact)
            print("-" * 20)

#---Defining delete_contact()
# (To Search Contact & Delete Contact From Contacts List)
        
def delete_contacts(manager):
    name = input("Enter Name of Contact To Delete : ")
    contact_to_del = None
    for contact in manager.contacts:
        if contact.name == name:
            contact_to_del = contact
            break
    if not contact_to_del == None:
        manager.contacts.remove(contact_to_del)
        manager.save_contacts()
        print("Successfully Deleted")
    else :
         print("Contact Not Found")


#---Defining search_contacts()
#  (To Search For Contacts)

def search_contacts(manager):
    name = input("Enter Name of Contact To Search : ")
    contact_to_search = None
    for contact in manager.contacts:
        if contact.name == name:
            contact_to_search = contact
            break
    if not contact_to_search == None:
        print(contact_to_search)

#--- Defining search_contact_me
#    (Search contact For me)

def search_contacts_me(manager,name):
    contact_to_search = None
    for contact in manager.contacts:
        if contact.name == name:
            contact_to_search = contact
            break
    if not contact_to_search == None:
        print(contact_to_search)        
    
#---Defining update_contacts()
#   (To Search and Update Contacts Name or Phone or Email)
def update_contacts(manager):
    name = input("Enter Name of Contact To Update : ")
    contact_to_update = None
    for contact in manager.contacts:
        if contact.name == name:
            contact_to_update = contact
            break
    if not contact_to_update == None:
        print("Contact Found!!")
        while True:           
            print("What Do You Want To Update")
            choice = input("1.Name 2.Phone 3.Email : ")
            if choice == "1":
                new_name = input("Enter New Name : ")
                contact.name = new_name
                print("Updated Contact : ")
                search_contacts_me(manager,contact.name)
                break
            elif choice == "2":
                new_phone = input("Enter New Phone : ")
                contact.phone = new_phone 
                print("Updated Contact : ")
                search_contacts_me(manager,contact.name)
                break   
            elif choice == "3":
                new_email = input("Enter New Email : ")
                contact.email = new_email
                print("Updated Contact : ")
                search_contacts_me(manager,contact.name)
                break
            else :
                print("Invalid Choice Try Again!!")     
                continue
        manager.save_contacts()  
    else:
        print("Contact Not Found. Check Spelling or Add New Contact")        


#---Defining main()
#   (To Choose Operation)

def main(manager):
    while True :
        print("\n" + "=" * 35)
        print("        CONTACTS MANAGER")
        print("=" * 35)
        print("[1] Add New Contact")
        print("[2] View All Contacts")
        print("[3] Search Contact")
        print("[4] Update Contact")
        print("[5] Delete Contact")
        print("[6] Exit")
        print("=" * 35)

        choice = int(input("Enter Your Choice : "))

        

        choices = {
                1 : add_contact,
                2 : display_contacts,
                3 : search_contacts,
                4 : update_contacts,
                5 : delete_contacts
        }

        if choice == 6:
            break

        selected_func = choices.get(choice)

        if selected_func:
            selected_func(manager)
        else:
            print("Invalid Choice. Try again!!!")

    