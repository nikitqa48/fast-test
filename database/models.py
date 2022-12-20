from pydantic import BaseModel


class Item(BaseModel):
    code: str
    path: str
    app: str

