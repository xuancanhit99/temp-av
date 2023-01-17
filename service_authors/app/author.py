from pydantic import BaseModel


class CreateAuthorModel(BaseModel):
    name: str
    username: str
    email: str
    address: str


class Author:
    def __init__(self, id_, name, username, email, address) -> None:
        self.id = id_
        self.name = name
        self.username = username
        self.email = email
        self.address = address
