from typing import Optional
from pydantic import BaseModel, NonNegativeInt
from typing import Any, List, Optional


class Movies(BaseModel):
    year : Optional[int]
    title : Optional[str]
    directors : Optional[str]
    release_date : Optional[str]
    rating : Optional[int]
    genres : Optional[str]
    image_url : Optional[str]
    plot : Optional[str]
    rank : Optional[int]
    running_time_secs : Optional[str]
    actors : Optional[str]
    class Config:
        orm_mode = True
class Movie_rating(BaseModel):
    title: Optional[str]
    directors: Optional[str]
    rating :Optional[int]
    class Config:
        orm_mode = True

class Movie_genres(BaseModel):
    year: Optional[int]
    title: Optional[str]
    directors: Optional[str]
    genres :Optional[str]

    class Config:
        orm_mode = True


class Add_Movie(BaseModel):
    year: Optional[int]
    title: Optional[str]
    directors: Optional[str]
    genres: Optional[str]
    class Config:
        orm_mode = True







