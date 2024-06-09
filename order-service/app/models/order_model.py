from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from typing import Optional


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    product_id: int
    quantity: int
    status: str = "Pending"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class OrderCreate(SQLModel):
    user_id: int
    product_id: int
    quantity: int


class OrderRead(SQLModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    status: str
    created_at: datetime
    updated_at: datetime


class OrderUpdate(SQLModel):
    quantity: Optional[int] = None
    status: Optional[str] = None
