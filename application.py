from typing import List
from fastapi import Depends,FastAPI,HTTPException
from sqlalchemy.orm import Session
import uvicorn
import crud
import Model as model
import schema
from db_handler import SessionLocal,engine
model.Base.metadata.create_all(bind=engine)
app=FastAPI(
    title="Movie Details",
    description="you can perform crud operation by using this api",
    version="1.0.0"
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/retrieve_all_movies_details',response_model=List[schema.Movies])
def retrieve_all_movies_details(skip: int=0,limit: int=100,db:Session=Depends(get_db)):
    movies=crud.get_movies(db=db,skip=skip,limit=limit)
    return movies

@app.get('/retrieve_movies_based_on_year',response_model=List[schema.Movies])
def retrieve_movies_by_year(year, db:Session=Depends(get_db)):
    movies=crud.get_movies_by_year(db=db,year=year)
    return movies

@app.get('/retrieve_movies_based_on_rating',response_model=List[schema.Movie_rating])
def retrieve_movies_by_rating(rating, db:Session=Depends(get_db)):
    movies=crud.get_movies_by_rating(db=db,rating=rating)
    return movies

@app.get('/retrieve_movies_based_on_directors',response_model=List[schema.Movies])
def retrieve_movies_by_directors(directors, db:Session=Depends(get_db)):
    movies=crud.get_movies_by_directors(db=db,directors=directors)
    return movies

@app.get('/retrieve_movies_based_on_genres',response_model=List[schema.Movie_genres])
def retrieve_movies_by_genres(genres, db:Session=Depends(get_db)):
    movies=crud.get_movies_by_genres(db=db,genres=genres)
    return movies


@app.post('/add_new_movie', response_model=schema.Movies)
def add_new_movie(movie: schema.Movies, db: Session = Depends(get_db)):
    movies=crud.add_movie_details_to_db(db=db, movie=movie)
    return movies


@app.put('/update_movie_details', response_model=schema.Movies)
def update_movie_details(movie: schema.Movies, db: Session = Depends(get_db)):
    movies = crud.update_movie_details(db=db, movie=movie)
    return movies


@app.delete('/delete_movie_by_year')
def delete_movie_by_id(year: int, db: Session = Depends(get_db)):
    details = crud.delete_movie_details_by_id(db=db, year=year)
    if details is None:
        return {"delete status": "no record found"}
    return {"delete status": "success"}


if __name__ == "__main__":
    uvicorn.run('application:app', host='0.0.0.0', port=8000, reload=False, root_path="/")




