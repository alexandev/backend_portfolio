from fastapi import FastAPI

from app.api.v1.routers.posts import router as v1_router
from app.config import settings

app = FastAPI(
    title=settings.project_name,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

app.include_router(v1_router, prefix="/api")

# import time
# from uuid import UUID

# import psycopg
# from fastapi import FastAPI, HTTPException, status
# from psycopg.rows import dict_row
# from pydantic import BaseModel
# from sqlalchemy import create_engine

# app = FastAPI()

# sync_engine = create_engine(
#     "postgresql+psycopg://postgres:postgres@localhost/postgres", echo=True
# )


# class Post(BaseModel):
#     # id: str
#     title: str
#     content: str
#     published: bool = True


# while True:
#     try:
#         db_conn = psycopg.connect(
#             host="localhost",
#             dbname="postgres",
#             user="postgres",
#             password="postgres",
#             row_factory=dict_row,
#         )
#         db_cursor = db_conn.cursor()
#         print("Succesfully connected to DB")
#         break
#     except Exception as error:
#         print("Couldn't connect to DB!")
#         print("Error: ", error)
#         time.sleep(3)


# @app.get("/")
# async def root():
#     return {"message": "Hello World!"}


# @app.get("/posts")
# async def get_posts():
#     db_cursor.execute("SELECT * FROM posts")
#     posts = db_cursor.fetchall()
#     return {"posts": posts}


# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# async def create_post(post: Post):
#     db_cursor.execute(
#         "INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *",
#         [post.title, post.content, post.published],
#     )
#     new_post = db_cursor.fetchone()
#     db_conn.commit()
#     return {"new_post": new_post}


# @app.get("/posts/{id}")
# async def get_post(id: UUID):
#     db_cursor.execute("SELECT * FROM posts WHERE id = %s", [id])
#     post = db_cursor.fetchone()
#     if not post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Post with id: {id} was not found",
#         )
#     return {"post": post}


# @app.delete("/posts/{id}")
# async def delete_post(id: UUID):
#     db_cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", [id])
#     deleted_post = db_cursor.fetchone()
#     if not deleted_post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Post with id: {id} was not found",
#         )
#     db_conn.commit()
#     return {"deleted_post": deleted_post}


# @app.put("/posts/{id}")
# async def update_post(id: UUID, post: Post):
#     db_cursor.execute(
#         "UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *",
#         [post.title, post.content, post.published, id],
#     )
#     updated_post = db_cursor.fetchone()
#     if not updated_post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Post with id: {id} was not found",
#         )
#     db_conn.commit()
#     return {"updated_post": updated_post}
