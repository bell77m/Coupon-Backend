from fastapi import FastAPI, Depends, HTTPException
from starlette.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from auth import create_access_token, verify_jwt
from schema import schema
from models import Base
from db import engine
from pydantic import BaseModel

# Create tables
Base.metadata.create_all(bind=engine)

graphql_app = GraphQLRouter(schema)

class LoginRequest(BaseModel):
    username: str
    password: str
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/login")
def login(data: LoginRequest):
    # Dummy check — replace with DB validation in real use
    if data.username == "admin" and data.password == "1234":
        token = create_access_token({"sub": data.username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


app.include_router(graphql_app, prefix="/graphql", dependencies=[Depends(verify_jwt)])
