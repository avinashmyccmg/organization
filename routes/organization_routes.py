from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import organizatio_schema
from service import organization_service
from database import get_db

router = APIRouter()
service = organization_service.OrganizationService()


@router.post("/organizations")
def create_organization(request: organizatio_schema.OrganizationBase, db: Session = Depends(get_db)):
  return service.create_organization(db=db, request=request)


@router.get("/")
def read_organizations(db: Session = Depends(get_db)):
  return service.get_organizations(db=db)
