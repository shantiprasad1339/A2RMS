from fastapi import APIRouter
from fastapi.responses import JSONResponse 
from employe.models.employemodel import Employeetablecreate, EmployeTable
import json
import io
import os
from boto3 import client
import uuid

router = APIRouter()
from fastapi import FastAPI, File, UploadFile

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

@router.post("/api/v1/upload-song")
async def uploadimage( image: UploadFile = File(...), ):
    file_content = await image.read()

    # Call the upload functi 
