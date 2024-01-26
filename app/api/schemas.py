import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class PostBase(BaseModel):
    """Post model."""

    # model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    created_at: datetime
    # updated_at: datetime


class PostPayload(BaseModel):
    """Post payload model."""

    title: str = Field(min_length=1, max_length=127)
    content: str
    published: bool = Field(default=True)


class Post(PostPayload, PostBase):
    class Config:
        orm_mode = True

    pass


class PostResponse(PostPayload, PostBase):
    pass
