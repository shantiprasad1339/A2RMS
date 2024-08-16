from mongoengine import Document, StringField, IntField, BooleanField
from pydantic import BaseModel

class ShiftTable(Document):
    name=StringField(required = True)
    start_time=StringField(required = True)
    end_time=StringField(required = True)
    # break_start=StringField(required = True)
    # break_end=StringField(required = True)


class NoteTable(Document):
    user_id=StringField(required = True)
    shift_id=StringField(required = True)
    note=StringField(required = True)



class AttendanceTable(Document):
    user_id=StringField(required = True)
    shift_id=StringField(required = True)
    note=StringField(required = True)





class Shiftcreate(BaseModel):
    name: str
    start_time: str
    end_time: str
    # break_start: str
    # break_end: str

class Notecreate(BaseModel):
    user_id: str
    shift_id: str
    note: str

class Attendancecreate(BaseModel):
    user_id: str
    shift_id: str
    check_in_time: str
