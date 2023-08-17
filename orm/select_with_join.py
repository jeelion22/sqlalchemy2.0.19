from main import session
from models import User, Comment
from sqlalchemy import select


stmt = (
    select(Comment)
    .join(Comment.user)
    .where(User.username == "eva")
    .where(Comment.text == "easy learn sqlalchemy")
)

result = session.scalars(stmt).one()

print(result.user_id)
