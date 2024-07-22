from fastapi import FastAPI, APIRouter
from venture.models.venturemodel import VentureTable, VentureCreateModel

router = APIRouter()

@router.post("/api/v1/venture-add/{userid}")
async def ventureadd(body:VentureCreateModel, userid:str):
    savedata = VentureTable(
        venturename = body.venturename,
        ventureLogo = body.ventureLogo,
        cureentVentureEmpCount = body.cureentVentureEmpCount
    )
    savedata.save()
    return {
        "message":"Venture Added",
        "status":True
    }