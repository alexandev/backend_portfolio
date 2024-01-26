from sqlalchemy import TIMESTAMP, Boolean, Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql.expression import text


class Base(DeclarativeBase):
    """Base database model."""

    id = Column(
        UUID, primary_key=True, nullable=False, server_default=text("gen_random_uuid()")
    )
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()")
    )


class Post(Base):
    """Post database model."""

    __tablename__ = "posts"

    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default="true")
