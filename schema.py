import strawberry
from typing import List, Optional
from sqlalchemy.orm import Session
from models import User, Store, Order
from db import get_db

#Query
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

#Mutations

@strawberry.input
@strawberry.input
class UserInput:
    user_nisit: str
    password: Optional[str] = None

@strawberry.input
class StoreInput:
    store_type: str
    user_store: str

@strawberry.input
class OrderInput:
    user_id: int
    store_id: int

@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_user(self, info, user: UserInput) -> UserType:
        db: Session = get_db()
        db_user = User(
            user_nisit=user.user_nisit,
            password=user.password,
            coupon_meal_used=0,
            coupon_sweet_used=0
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @strawberry.mutation
    def create_store(self, info, store: StoreInput) -> StoreType:
        db: Session = get_db()
        db_store = Store(store_type=store.store_type, user_store=store.user_store)
        db.add(db_store)
        db.commit()
        db.refresh(db_store)
        return db_store

    @strawberry.mutation
    def create_order(self, info, order: OrderInput) -> OrderType:
        db: Session = get_db()
        user = db.query(User).get(order.user_id)
        store = db.query(Store).get(order.store_id)
        db_order = Order(user_id=order.user_id, store_id=order.store_id)
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return OrderType(
            id=db_order.id,
            user=user,
            store=store,
            created_at=str(db_order.created_at)
        )

schema = strawberry.Schema(query=Query,mutation=Mutation)
