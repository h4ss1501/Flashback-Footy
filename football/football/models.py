from database import db

class Shootout(db.Model):
    __tablename__ = 'shootouts'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    home_team = db.Column(db.String)
    away_team = db.Column(db.String)
    winner = db.Column(db.String)
    first_shooter = db.Column(db.String)

class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    home_team = db.Column(db.String)
    away_team = db.Column(db.String)
    home_score = db.Column(db.Integer)
    away_score = db.Column(db.Integer)
    tournament = db.Column(db.String)
    city = db.Column(db.String)
    country = db.Column(db.String)
    neutral = db.Column(db.Boolean)

