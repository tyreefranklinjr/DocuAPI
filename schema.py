from pydantic import BaseModel, Field, model_validator, computed_field
from typing import Optional
from datetime import date, time

class ReceiptItem(BaseModel):
    name: str
    price: float = Field(..., ge=0)
    quantity: int = Field(default=1, ge=1)

class Receipt(BaseModel):
    # Required
    merchant: str
    purchase_date: date
    purchase_time: time
    subtotal: float = Field(..., ge=0)
    total: float = Field(..., ge=0)
    payment_type: str
    payment_cred: str = Field(..., min_length=4, max_length=4, pattern=r"^\d{4}$")
    items: list[ReceiptItem]

    @computed_field
    @property
    def item_count(self) -> int:
        return len(self.items)

    @model_validator(mode="after")
    def check_total(self):
        if self.total < self.subtotal:
            raise ValueError("total cannot be less than subtotal")
        return self

    # Additionals
    transaction_id: Optional[int] = Field(default=None, ge=0)
    location_open: Optional[time] = None
    location_close: Optional[time] = None
    location_address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    manager_name: Optional[str] = None
    coupons: Optional[str] = None

class Letter(BaseModel):
    # Required
    sender_name: str
    sender_address: str
    recipient_address: str
    body_text: str

    # Optional Additionals
    recipient_name: Optional[str] = None
    greeting: Optional[str] = None
    closing: Optional[str] = None