from connect import engine
from tables import users_table, comments_table, metadata_obj

print(">>>CREATE DATABASE")
metadata_obj.create_all(bind=engine)
