from pydantic import BaseModel, Field, PositiveInt
from typing import Annotated


class Game(BaseModel):
    id: PositiveInt
    name: Annotated[str, Field(min_length=3, max_length=50)]
    genre: Annotated[str, Field(min_length=3, max_length=15)]
    cost: Annotated[int, Field()]
