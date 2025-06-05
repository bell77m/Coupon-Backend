import strawberry
from typing import List, Optional
from sqlalchemy.orm import Session
from models import User, Store, Order
from db import get_db

@strawberry.type
class UserType:
    id: int
    user_nisit: str
    coupon_meal_used: int
    coupon_sweet_used: int
    created_at: str

@strawberry.type
class StoreType:
    id: int
    store_type: str
    user_store: str
    created_at: str

@strawberry.type
class OrderType:
    id: int
    user: UserType
    store: StoreType
    created_at: str

@strawberry.type
class Query:

    @strawberry.field
    def users(self, info) -> List[UserType]:
        db: Session = get_db()
        return db.query(User).all()

    @strawberry.field
    def stores(self, info) -> List[StoreType]:
        db: Session = get_db()
        return db.query(Store).all()

    @strawberry.field
    def orders(self, info) -> List[OrderType]:
        db: Session = get_db()
        return db.query(Order).all()

schema = strawberry.Schema(query=Query)
