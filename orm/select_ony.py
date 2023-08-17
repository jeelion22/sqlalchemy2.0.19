from main import session
from models import User

harry = session.query(User).filter_by(username="eva").first()

print(harry)
