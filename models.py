# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_nisit = Column(String(255))
    password = Column(String(255))
    coupon_meal_used = Column(Integer, default=0)
    coupon_sweet_used = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

    orders = relationship("Order", back_populates="user")

class Store(Base):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True, autoincrement=True)
    store_type = Column(String(255))
    user_store = Column(String(255))
    password = Column(String(255))
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

    orders = relationship("Order", back_populates="store")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    store_id = Column(Integer, ForeignKey("stores.id"))
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="orders")
    store = relationship("Store", back_populates="orders")
