from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name', 'phone_number')
    def validate_author(self, key, value):
        if key == 'name':
            if not value:
                raise ValueError("there's no name")
            authors = Author.query.all()
            for auther in authors:
                if auther.name == value:
                    raise ValueError("name must be unique")
        if key == 'phone_number':
            if len(value) != 10:
                raise ValueError("invalid number")
        return value



    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title', 'content', 'summary')
    def validate_post(self, key, value):
        if key == 'title' and not value:
                raise ValueError("enter a title")
        if key == 'title' and not "Won't Believe" in value and not "Secret" in value and not "Top" in value and not "Guess" in value:
                raise ValueError("not clickbait")
        if key == 'content' and len(value) < 250:
                raise ValueError("too short")
        if key == 'summary' and len(value) >= 250:
                raise ValueError("too long")
        return value
    @validates('category')
    def validate_category(self, key, category):
        if category != 'Fiction' and category != 'Non-Fiction':
            raise ValueError("Category must be Fiction or Non-Fiction.")
        return category

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
