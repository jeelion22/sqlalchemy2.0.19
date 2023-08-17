from models import User, Comment
from main import session


jeeva = User(
    username="Jeeva",
    email_address="jeelion22@gmail.com",
    comments=[Comment(text="Hello World"), Comment(text="easy learn sqlalchemy")],
)

harry = User(
    username="Harry",
    email_address="harrykarthik.01@gmail.com",
    comments=[Comment(text="Hello!"), Comment(text="It is a AI world")],
)


shri = User(
    username="Poornashri",
    email_address="pshri08@gmail.com",
    comments=[Comment(text="Whats up guys"), Comment(text="Chil morining")],
)

session.add_all([jeeva, harry, shri])

session.commit()
