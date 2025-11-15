
from __future__ import annotations
from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from orm_base import Base

class PiecePart(Base):
    """
    pieceParts has a PK on (part_number) and FKs to parts and vendors.
    """
    __tablename__ = "pieceparts"

    part_number: Mapped[str] = mapped_column(
        String(10),
        ForeignKey("parts.part_number", name="pieceParts_parts"),
        primary_key=True,
    )
    vendor_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("vendors.vendor_id", name="pieceParts_vendors"),
        nullable=False,
    )

    # Relationships
    vendor: Mapped["Vendor"] = relationship("Vendor", back_populates="piece_parts")
    part= relationship("Part",back_populates="piece_part", uselist=False)
    
    def __init__(self, part_number: str, vendor_id: int):
        self.part_number = part_number
        self.vendor_id = vendor_id
    def __repr__(self):
        return f"<PiecePart(part_number='{self.part_number}, vendor_id='{self.vendor_id}')>"
    def __str__(self):
        return f"Part_number= {self.part_number}, Vendor_id= {self.vendor_id} "
