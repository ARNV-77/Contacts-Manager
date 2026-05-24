#=================================
#=====Manages All Contacts=====
#=================================

import json
import os
from contacts import Contacts

#---Creating Class To Manage Contacts

class ContactsManager:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

#---Defining save_contacts
#    (To Save Contacts
#     Object --> Dictionary in Json)  
   
    def save_contacts(self):
        try:
            with open ("contacts.json","w") as f:
                all_dicts =[]
                for contact in self.contacts:
                    dictionary = contact.to_dict()
                    all_dicts.append(dictionary)
                json.dump(all_dicts,f)   
               
        except Exception as e:
            print(f"Error Saving Contacts : {e}")   
         
     
      
        
#---Defining load_contacts()
#    (To Load Contacts.
#     Dictionary --> Object In Json)
   
    def load_contacts(self):
        if not os.path.exists("contacts.json"):
            print("Starting Fresh!!")
        else:
            try:
                with open("contacts.json", "r") as file:
                    data = json.load(file)
                    for item in data:
                        contact = Contacts.from_dict(item)
                        self.contacts.append(contact)
                
            except Exception as e:
                print(f"Error : {e}")
               
     
                    
                    