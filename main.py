from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from auth import verify_basic_auth
from schema import schema
from models import Base
from db import engine

# Create tables
Base.metadata.create_all(bind=engine)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(graphql_app, prefix="/graphql", dependencies=[Depends(verify_basic_auth)])
