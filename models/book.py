from datetime import datetime
from typing import List
import uuid
from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import validates
from models.database_setup import db, db_engine, Base


class Book(Base):
    __tablename__ = "book"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(80), nullable=False)
    auther = Column(String(80), nullable=False)
    isbn = Column(String(13), unique=True, nullable=True)
    genre = Column(String(50), nullable=False)
    synopsis = Column(Text, nullable=False)
    publication_date = Column(DateTime, nullable=False)
    publisher = Column(String(80), nullable=False)
    edition = Column(String(50), nullable=True)
    language = Column(String(20), nullable=False)
    pages = Column(Integer, nullable=True)
    format = Column(String(20), nullable=False)
    cover_image_url = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    @validates("auther", "genre")
    def flatten_list(self, key: str, lst: List) -> str:
        return ", ".join(lst)

    def __repr__(self) -> str:
        return f"<Book {self.title}>"
