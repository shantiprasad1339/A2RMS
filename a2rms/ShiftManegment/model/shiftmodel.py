from mongoengine import Document, StringField, IntField, BooleanField,DateTimeField,ListField
from pydantic import BaseModel

class ShiftTable(Document):
    userid = StringField(required=True)
    note = StringField(required=True)
    intime = DateTimeField()
    outtime = DateTimeField()
    startbreak = ListField(DateTimeField())  # List to handle multiple breaks
    endbreak = ListField(DateTimeField())  # List to handle multiple breaks
class ShiftTablecreate(BaseModel):
    userid: str
    note: str