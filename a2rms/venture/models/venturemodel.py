from mongoengine import Document, StringField, IntField
from pydentic import BaseModel

class VentureTable(Document):
    venturename = StringField(required=True)
    ventureLogo = StringField(required=True)
    prefix = StringField(required = True)
    cureentVentureEmpCount = IntField(required =True)

class VentureCreateModel(BaseModel):
    venturename:str
    ventureLogo:str
    cureentVentureEmpCount:int
    prefix : str