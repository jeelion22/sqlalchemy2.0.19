from models import User, Comment
from main import session


eva = User(
    username="eva",
    email_address="eva@gmail.com",
    comments=[Comment(text="Hello World"), Comment(text="easy learn sqlalchemy")],
)

harry = User(
    username="Harry",
    email_address="harry@gmail.com",
    comments=[Comment(text="Hello!"), Comment(text="It is a AI world")],
)


shri = User(
    username="shri",
    email_address="shri@gmail.com",
    comments=[Comment(text="Whats up guys"), Comment(text="Chil morining")],
)

session.add_all([eva, harry, shri])

session.commit()
