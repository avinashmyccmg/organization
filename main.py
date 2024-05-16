from fastapi import FastAPI
from routes import organization_routes
from models import organization_model
from database import engine

app = FastAPI()


organization_model.Base.metadata.create_all(bind=engine)

app.include_router(organization_routes.router)
