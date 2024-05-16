from sqlalchemy.orm import Session
from schemas import organizatio_schema
from repository.organization_repository import OrganizationRepository


class OrganizationService:
  def __init__(self):
    self.repo = OrganizationRepository()

  def create_organization(self, db: Session, request: organizatio_schema.OrganizationBase):
    return self.repo.create_organization(db=db, request=request)

  def get_organizations(self, db: Session):
    return self.repo.get_organizations(db=db)
