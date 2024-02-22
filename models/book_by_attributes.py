from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from models.database_setup import db, db_engine, Base


class BookByAttributes(Base):
    __tablename__ = "book_by_attributes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    book_id = Column(UUID(as_uuid=True), ForeignKey("book.id"), nullable=False)
    attribute = Column(String(20), nullable=False)
    value = Column(String(50), nullable=False)
    count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<BookByAttributes {self.id} - {self.book_id} - {self.attribute} - {self.value} - {self.count}>"
