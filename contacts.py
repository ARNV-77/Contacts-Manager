#===========================================
#=====Defining Classes And Methods=====
#===========================================

# Creating Contacts Class
class Contacts:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    # Object --> Dictionary
    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
        }

    # Dictionary --> Object
    @staticmethod
    def from_dict(data):
        new_contact = Contacts(data["name"], data["phone"], data["email"])
        return new_contact

    # Display Contact Nicely
    def __str__(self):
        return f"Name : {self.name}\nPhone: {self.phone}\nEmail: {self.email}"