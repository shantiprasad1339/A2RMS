from mongoengine import Document, StringField, IntField, BooleanField
from pydantic import BaseModel

class EmployeTable(Document):
    Prefix = StringField(required = True)
    StaffId = StringField(required = True)
    Role = StringField(required = True)
    Designation = StringField(required = True)
    Departmen = StringField(required = True)
    Firstname = StringField(required = True)
    Lastname = StringField(required = True)
    Father_name = StringField(required = True)
    Mother_name = StringField(required = True)
    Login_email = StringField(required = True)
    Office_email = StringField(required = True)
    Gender = StringField(required = True)
    DateOfBirth = StringField(required = True)
    Dateofjoining = StringField(required = True)
    Phone = IntField(required = True)
    Emergencycontact = IntField(required = True)
    Merital_status = StringField(required = True)
    Photo = StringField(required = True)
    Current_address = StringField(required = True)
    Permanent_address = StringField(required = True)
    Qualification = StringField(required = True)
    Work_experience = StringField(required = True)
    Note = StringField(required = True)
    AAdhar_number = IntField(required = True)
    Pan_number = StringField(required = True)
    PL = IntField(required = True)
    AL = IntField(required = True)
    Bank_title = StringField(required = True)
    Acount_number = IntField(required = True)
    Bank_name = StringField(required = True)
    IFSC_code = StringField(required = True)
    Branch_name = StringField(required = True)
    FacebookURL = StringField(required = True)
    InstaURL = StringField(required = True)
    TWitterURL = StringField(required = True)
    LinkdinUrl = StringField(required = True)
    Resume = StringField(required = True)
    Joiningletter = StringField(required = True)
    Other_documents = StringField(required = True)

    
    
    

class Employeetablecreate(BaseModel):
    Prefix: str
    StaffId: str
    Role: str
    Designation: str
    Departmen: str 
    Firstname: str
    Lastname: str
    Father_name: str
    Mother_name: str
    Login_email: str
    Office_email: str
    Gender: str
    DateOfBirth: str
    Dateofjoining: str
    Phone: int
    Emergencycontact: int
    Merital_status: str
    Photo: str
    Current_address: str
    Permanent_address: str
    Qualification: str
    Work_experience: str
    Note: str
    AAdhar_number: int
    Pan_number: str
    PL: int
    AL: int
    Bank_title: str
    Acount_number: int
    Bank_name: str
    IFSC_code: str
    Branch_name: str
    FacebookURL: str
    InstaURL: str
    TWitterURL: str
    LinkdinUrl: str
    Resume: str
    Joiningletter: str
    Other_documents: str

    