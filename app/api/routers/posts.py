import uuid

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import schemas
from app.database import models as db_models
from app.database.session import get_db_session

router = APIRouter(prefix="/v1/posts", tags=["v1"])


@router.get("", status_code=status.HTTP_200_OK)
async def get_posts(
    session: AsyncSession = Depends(get_db_session),
) -> list[schemas.Post]:
    posts = await session.scalars(select(db_models.Post))
    return posts


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_post(
    id: uuid.UUID,
    session: AsyncSession = Depends(get_db_session),
) -> schemas.Post:
    post = await session.get(db_models.Post, id)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post does not exist",
        )
    return post


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_post(
    data: schemas.PostPayload,
    session: AsyncSession = Depends(get_db_session),
) -> schemas.Post:
    new_post = db_models.Post(**data.model_dump())
    session.add(new_post)
    await session.commit()
    await session.refresh(new_post)
    return new_post


@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_post(
    id: uuid.UUID,
    data: schemas.PostPayload,
    session: AsyncSession = Depends(get_db_session),
) -> schemas.Post:
    updated_post = await session.get(db_models.Post, id)
    await session.execute(
        update(db_models.Post)
        .where(db_models.Post.id == id)
        .values(**data.model_dump())
    )
    await session.commit()
    await session.refresh(updated_post)
    return updated_post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    id: uuid.UUID,
    session: AsyncSession = Depends(get_db_session),
):
    deleted_post = await session.get(db_models.Post, id)
    # deleted_post =
    if deleted_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post does not exist",
        )
    await session.delete(deleted_post)
    await session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
