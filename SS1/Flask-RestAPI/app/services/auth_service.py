from ..models.user import User
from ..extensions import db

def register_user(username, password):
    if User.query.filter_by(username=username).first():
        return None
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user
