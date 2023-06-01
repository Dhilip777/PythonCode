from sqlalchemy.orm import Session
from sqlalchemy import *
import Model as model

import schema


def get_movies(db:Session,skip: int=0,limit: int=100):
    return db.query(model.Movies).offset(skip).limit(limit).all()


def get_movies_by_year(db: Session,year: int):
    return db.query(model.Movies).filter(model.Movies.year==year).all()


def get_movies_by_rating(db: Session,rating: int):
    return db.query(model.Movies).filter(model.Movies.rating>=8).all()


def get_movies_by_directors(db: Session,directors: str):
    return db.query(model.Movies).filter(model.Movies.directors==directors).all()


def get_movies_by_genres(db: Session,genres: str):
    return db.query(model.Movies).filter(model.Movies.genres==genres).all()


def add_movie_details_to_db(db: Session, movie: schema.Movies):
    """
    this method will add a new record to database. and perform the commit and refresh operation to db

    """
    mv_details = model.Movies(**movie.dict())
    db.add(mv_details)
    db.commit()
    db.refresh(mv_details)
    return model.Movies(**movie.dict())


def update_movie_details(db: Session,movie: schema.Movies):
    """
    this method will update the database
  
    """
    db.query(model.Movies).filter(model.Movies.year == movie.year).update(vars(movie))
    db.commit()
    return db.query(model.Movies).filter(model.Movies.year == movie.year).first()


def delete_movie_details_by_id(db: Session, year: int):
    """
    This will delete the record from database 
   
    """
    try:
        m = db.query(model.Movies).filter(model.Movies.year ==year)
        m.delete()
        db.commit()
        return m
    except Exception as e:
        return None


