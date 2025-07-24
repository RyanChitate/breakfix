from pydantic import BaseModel

class MallBase(BaseModel):
    name: str
    location: str | None = None

class MallCreate(MallBase):
    pass

class MallResponse(MallBase):
    id: int
    class Config:
        orm_mode = True
