from fastapi import FastAPI, Form,  FastAPI, File, UploadFile
from mongoengine import connect
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
app = FastAPI()
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from employe.models.employemodel import Employeetablecreate, EmployeTable
import json
import io
import os
from boto3 import client
import uuid


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
    
