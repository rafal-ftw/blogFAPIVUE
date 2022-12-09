from pydantic import BaseModel

class PostBase(BaseModel):
    title:str
    content: str | None = None
    author:str | None = None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id:int
    class Config:
        orm_mode=True