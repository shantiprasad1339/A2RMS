from fastapi import FastAPI, Form,  FastAPI, File, UploadFile, HTTPException
from mongoengine import connect
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
app = FastAPI()
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from employe.models.employemodel import Employeetablecreate, EmployeTable
from ShiftManegment.model.shiftmodel import Attendancecreate,Notecreate,Shiftcreate,AttendanceTable,NoteTable,ShiftTable
import json
from datetime import datetime, timedelta
import io
import os
from boto3 import client
import uuid
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, replace with specific origins as needed
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

connect('A2rms', host="mongodb+srv://avbigbuddy:nZ4ATPTwJjzYnm20@cluster0.wplpkxz.mongodb.net/A2rms")   
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.post("/login")
async def loginpage( username: str = Form(...), password: str = Form(...)):
    if username == "admin":
        if password == "admin": 
            return RedirectResponse(url="/home")

@app.get("/", response_class=HTMLResponse)
async def get_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/attendanceReport", response_class=HTMLResponse)
async def attendanceReport(request: Request):
    return templates.TemplateResponse("attendanceReport.html", {"request": request})

@app.get("/leaveApplications", response_class=HTMLResponse)
async def leaveApplications(request: Request):
    return templates.TemplateResponse("leaveApplications.html", {"request": request})
@app.get("/balanceReport", response_class=HTMLResponse)
async def balanceReport(request: Request):
    return templates.TemplateResponse("balanceReport.html", {"request": request})
@app.get("/changepassword", response_class=HTMLResponse)
async def changepassword(request: Request):
    return templates.TemplateResponse("changepassword.html", {"request": request})
@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
@app.get("/holidays", response_class=HTMLResponse)
async def holidays(request: Request):
    return templates.TemplateResponse("holidays.html", {"request": request})
@app.get("/Leavebalance", response_class=HTMLResponse)
async def Leavebalance(request: Request):
    return templates.TemplateResponse("Leavebalance.html", {"request": request})
@app.get("/leaveReport", response_class=HTMLResponse)
async def leaveReport(request: Request):
    return templates.TemplateResponse("leaveReport.html", {"request": request})
@app.get("/markAttendance", response_class=HTMLResponse)
async def markAttendance(request: Request):
    return templates.TemplateResponse("markAttendance.html", {"request": request})
@app.get("/Noticeboard", response_class=HTMLResponse)
async def Noticeboard(request: Request):
    return templates.TemplateResponse("Noticeboard.html", {"request": request})





@app.get("/awards", response_class=HTMLResponse)
async def awards(request: Request):
    return templates.TemplateResponse("awards.html", {"request": request})



@app.get("/perticulerstaff", response_class=HTMLResponse)
async def perticulerUser(request: Request):
    return templates.TemplateResponse("userdetail.html", {"request": request})

@app.get("/addstaff", response_class=HTMLResponse)
async def perticulerUser(request: Request):
    return templates.TemplateResponse("info.html", {"request": request})
def upload_image_to_space(file_content: bytes, filename: str):
    spaces_access_key = 'DO009G8J4HEUMUWVJ4Q4'
    spaces_secret_key = '+w9XGrS/zvMX6Z4mIk+cMkMTh2LtBApvYb8TfBWHOqs'
    spaces_endpoint_url = 'https://work-pool.blr1.digitaloceanspaces.com'
    spaces_bucket_name = 'socialMedia_songs'

    # Generate a random filename using UUID
    # Generate a random filename using UUID
    random_filename = str(uuid.uuid4())
    file_extension = os.path.splitext(filename)[1]  # Extract file extension from the original filename

    random_filename_with_extension = f"{random_filename}{file_extension}"

    s3 = client('s3',
                 
                region_name='blr1',
                endpoint_url=spaces_endpoint_url,
                aws_access_key_id=spaces_access_key,
                aws_secret_access_key=spaces_secret_key, )

    # Create a BytesIO object to read file conte nt from memory
    file_content_stream = io.BytesIO(file_content)

    s3.upload_fileobj(file_content_stream, spaces_bucket_name, random_filename_with_extension,  ExtraArgs={'ACL': 'public-read'})

    return f"{spaces_endpoint_url}/{spaces_bucket_name}/{random_filename_with_extension}"

@app.post("/api/v1/upload")
async def uploadimage( image: UploadFile = File(...), ):
    file_content = await image.read()

    # Call the upload function with the random filename and the original file extension
    imagepath = upload_image_to_space(file_content, image.filename)
    return {
        "message":"file added",
        "data":imagepath,
        "status":True
    }

@app.post("/api/v1/addstaff")
async def addStaff(body: Employeetablecreate):
    data = EmployeTable(**body.dict())
    data.save()
    tojson = data.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Staff Added",
        "data": fromjson,
        "status":True 
    }
    
@app.post("/shifts/")
async def create_shift(body:Shiftcreate):
    data = ShiftTable(**body.dict())
    data.save()
    tojson = data.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Shift Added",
        "data": fromjson,
        "status":True 
    }

@app.get("/shifts/get")
async def get_shifts():
    data = ShiftTable.objects.all()
    tojson = data.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Shift get",
        "data": fromjson,
        "status":True 
    }
