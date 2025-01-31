from fastapi import APIRouter
from models.family import FamilyMember

router = APIRouter()

@router.get("/family")
async def get_family():
    members = await FamilyMember.all()
    return members