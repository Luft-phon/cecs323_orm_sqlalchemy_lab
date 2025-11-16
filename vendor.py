from __future__ import annotations

from typing import List
from sqlalchemy import (
    CheckConstraint,
    Identity,
    Integer,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from orm_base import Base

class Vendor(Base):
    __tablename__ = "vendors"

    vendor_id: Mapped[int] = mapped_column(
        Integer,
        Identity(always=True),
        primary_key=True,
    )
    supplier_name: Mapped[str] = mapped_column(String(80), nullable=False)

    __table_args__ = (
        CheckConstraint("length(supplier_name) >= 3", name="vendors_supplier_name_len_ck"),
    )

    # Relationships
    piece_parts: Mapped[List["PiecePart"]] = relationship(
        "PiecePart",
        back_populates="vendor",
        cascade="all, delete-orphan",   # xóa piece_parts khi xóa vendor
        lazy="selectin",                # tối ưu n+1 khi load danh sách
    )

    def __init__(self, vendor_id: int, supplier_name: str):
        self.vendor_id = vendor_id
        self.supplier_name = supplier_name
    
    def __repr__(self):
        return f"<Vendor(vendor_id='{self.vendor_id}', supplier_name='{self.supplier_name}')>"
    def __str__(self):
        return f"Vendor_id= {self.vendor_id}, Supplier_name= {self.supplier_name} "