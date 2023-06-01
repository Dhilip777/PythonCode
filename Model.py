from sqlalchemy import Boolean,Column, Integer,String

from db_handler import Base
class Movies(Base):
    __tablename__="Movies"
    year=Column(Integer)
    title=Column(String, primary_key=True)
    directors=Column(String)
    release_date=Column(String)
    rating=Column(Integer)
    genres=Column(String)
    image_url=Column(String)
    plot=Column(String)
    rank=Column(Integer)
    running_time_secs=Column(Integer)
    actors=Column(String)









