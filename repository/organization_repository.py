from sqlalchemy.orm import Session
from models import organization_model
from schemas import organizatio_schema

class OrganizationRepository:
  def create_organization(self, db: Session, request: organizatio_schema.OrganizationBase):
    new_org = organization_model.Organization(name=request.name)
    db.add(new_org)
    db.commit()
    db.refresh(new_org)
    return new_org

  def get_organizations(self, db: Session):
    return db.query(organization_model.Organization).all()
