from datetime import datetime
from uuid import uuid4
from sqlalchemy import Boolean, Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from models.database_setup import db, db_engine, Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    book_id = Column(UUID(as_uuid=True), ForeignKey("book.id"), nullable=False)
    availibility = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Inventory {self.id} - {self.book_id}>"
