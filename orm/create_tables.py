from models import Base, User, Comment
from connect import engine

print("CREATING tABLES >>>")

Base.metadata.create_all(bind=engine)
