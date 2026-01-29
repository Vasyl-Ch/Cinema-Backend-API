from pydantic import BaseModel, ConfigDict
from typing import List, Optional


class GenreBase(BaseModel):
    name: str


class Genre(GenreBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class StarBase(BaseModel):
    name: str


class Star(StarBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class DirectorBase(BaseModel):
    name: str


class Director(DirectorBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class CertificationCreate(BaseModel):
    name: str


class Certification(CertificationCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class MovieBase(BaseModel):
    name: str
    year: int
    time: int
    imdb: float
    votes: int
    meta_score: Optional[float] = None
    gross: Optional[float] = None
    description: str
    price: float
    certification_id: int

    genres: List[int] = []
    directors: List[int] = []
    stars: List[int] = []


class MovieCreate(MovieBase):
    pass


class Movie(BaseModel):
    id: int
    uuid: str
    name: str
    year: int
    time: int
    imdb: float
    votes: int
    meta_score: Optional[float]
    gross: Optional[float]
    description: str
    price: float

    certification: Certification
    genres: List[Genre]
    directors: List[Director]
    stars: List[Star]

    model_config = ConfigDict(from_attributes=True)
