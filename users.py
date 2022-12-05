from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str

    def __hash__(self) -> int:
        return hash(f"{self.id}{self.username}")


users: set[User] = set()
