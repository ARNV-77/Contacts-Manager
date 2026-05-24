#=====Main File=====
#---To Execute Program

from operations import main
from contacts_manager import ContactsManager

if __name__ == "__main__":
    manager = ContactsManager()
    main(manager)