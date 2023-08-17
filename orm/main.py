from models import User, Comment
from sqlalchemy.orm import Session
from connect import engine

session = Session(engine)
