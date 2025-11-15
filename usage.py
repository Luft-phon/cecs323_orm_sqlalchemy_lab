from __future__ import annotations

from sqlalchemy import (
    CheckConstraint,
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

class Usage(Base):
    __tablename__ = "usages"

    usage_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    parts_part_number: Mapped[str] = mapped_column(
        String(10),
        ForeignKey("parts.part_number", name="usages_parts"),
        primary_key=True,
    )
    assemblies_assembly_part_number: Mapped[str] = mapped_column(
        String(10),
        ForeignKey("assemblies.assembly_part_number", name="usages_assemblies"),
        primary_key=True,
    )

    __table_args__ = (
        CheckConstraint("usage_quantity >= 1 AND usage_quantity <= 20", name="usages_qty_1_20_ck"),
    )

    # Relationships
    part: Mapped["Part"] = relationship("Part", back_populates="usages")
    assembly: Mapped["Assembly"] = relationship("Assembly",back_populates="usages")

    