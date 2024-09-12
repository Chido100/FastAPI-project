from pydantic import BaseModel



class TodoSchema(BaseModel):
    id: int
    title: str
    content: str
    date_created: str


class TodoUpdateSchema(BaseModel):
    title: str
    content: str


    