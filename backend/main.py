from fastapi import FastAPI
from database import engine
import models  # Import models to create tables
from routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include router
app.include_router(router)

# Create tables if they don't exist
models.Base.metadata.create_all(bind=engine)