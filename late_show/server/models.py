from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey, Date, String
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from sqlalchemy.orm import validates

db = SQLAlchemy()

# Model Definitions
class Episode(SerializerMixin, db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(Date, nullable=False)
    number = db.Column(Integer, nullable=False)
    year = db.Column(Integer, nullable=False)  
    group = db.Column(String, nullable=False)  

    # Relationship to allow multiple appearances
    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')

    # Validation for date field
    @validates('date')
    def validate_date(self, key, value):
        if value > datetime.now().date():
            raise ValueError("Date must not be in the future.")
        return value

    # Validation for number field
    @validates('number')
    def validate_number(self, key, value):
        if value < 1:
            raise ValueError("Number must be a positive integer.")
        return value

    serialize_rules = ('-appearances.episode',)


class Guest(SerializerMixin, db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(String, nullable=False)
    occupation = db.Column(String, nullable=False)

    appearances = db.relationship('Appearance', back_populates='guest')

    @validates('name')
    def validate_name(self, key, value):
        if not value or value.strip() == "":
            raise ValueError(f"{key.capitalize()} must be present.")
        return value

    serialize_rules = ('-appearances.guest',)


class Appearance(SerializerMixin, db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(Integer, nullable=False)

    episode_id = db.Column(Integer, ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(Integer, ForeignKey('guests.id'), nullable=False)  

    episode = relationship('Episode', back_populates='appearances', single_parent=True)  
    guest = relationship('Guest', back_populates='appearances', single_parent=True) 

    @validates('rating')
    def validate_rating(self, key, value):
        if value < 1 or value > 5:
            raise ValueError("Rating must be between 1 and 5.")
        return value

    serialize_rules = ('-episode.appearances', '-guest.appearances',)
