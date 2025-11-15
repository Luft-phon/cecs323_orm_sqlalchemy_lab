
from __future__ import annotations

from typing import List
from sqlalchemy import (
    ForeignKey,
    String
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from orm_base import Base

class Assembly(Base):
    __tablename__ = "assemblies"

    assembly_part_number: Mapped[str] = mapped_column(  
        String(10),
        ForeignKey("parts.part_number", name="assemblies_parts"),
        primary_key=True,
    )

    # Relationships
    part: Mapped["Part"] = relationship(          #return to Part Object using Mapped[Part]
        "Part",
        back_populates="assembly",
        uselist=False,          # one-to-one relationship
    )
    usages: Mapped[List["Usage"]] = relationship(         #1-to-many relationship
        "Usage",
        back_populates="assembly",
        cascade="all, delete-orphan",
    )

    def __init__(self, assembly_part_number: str):
        self.assembly_part_number = assembly_part_number

    def __repr__(self):
        return f"<Part(assembly_part_number='{self.assembly_part_number}'>"
    def __str__(self):  #print use __str__, if not => use __repr__
        return f"Assembly_part_number='{self.assembly_part_number}'"