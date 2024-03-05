from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(32))
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    links = db.relationship('Link', backref='user', lazy=True, cascade='all, delete')

class Link(db.Model):
    __tablename__ = 'links'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(300), nullable=False)
    image_url = db.Column(db.String(300), nullable=False)
    likes = db.relationship('Like', backref='link', lazy=True, cascade='all, delete')

class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    link_id = db.Column(db.Integer, db.ForeignKey('links.id'), nullable=False)
