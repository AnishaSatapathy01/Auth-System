from fastapi import FastAPI
from app.database import Base, engine
from routes import auth_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(auth_routes.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():

    return {"message": "API running"}