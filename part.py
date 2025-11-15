from __future__ import annotations

from typing import List, Optional
from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from orm_base import Base
from sqlalchemy import String
from sqlalchemy import CheckConstraint

# from assembly import Assembly
# from piecePart import PiecePart    

class Part(Base):
    __tablename__ = "parts"

    part_number: Mapped[str] = mapped_column(String(10), primary_key=True)
    part_name: Mapped[str] = mapped_column(String(80), nullable=False)

    __table_args__ = (
        CheckConstraint("length(part_number) >= 1", name="parts_part_number_len_ck"),
        CheckConstraint("length(part_name) >= 3", name="parts_part_name_len_ck"),
    )

    # Relationships
    assembly = relationship(
        "Assembly",
        back_populates="part",
        uselist=False,
        cascade="save-update",
    )
    piece_part= relationship(
        "PiecePart",
        back_populates="part",
        uselist=False,
        cascade="save-update",
    )
    
    usages: Mapped[List["Usage"]] = relationship(
        "Usage",
        back_populates="part",
        cascade="all, delete-orphan",
    )

# many to many relationship between Part and Assembly via Usage
    assemblies: Mapped[list["Assembly"]] = relationship(
        "Assembly",
        # secondary="usages",
        back_populates="part",
        viewonly=True
    )

    def __init__(self, part_number: str, part_name: str):
        self.part_number = part_number
        self.part_name = part_name

    def __repr__(self):
        return f"<Part(part_number='{self.part_number}', part_name='{self.part_name}')>"
    def __str__(self):
        return f"{self.part_number} - {self.part_name}"
    


