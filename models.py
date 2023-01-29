from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    with app.app_context():
        db.app = app
        db.init_app(app)
        #db.drop_all()
        db.create_all()

class Trainer(db.Model):
    __tablename__ = 'trainers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)

    clients = db.relationship('Client', secondary='workouts', backref='trainers', lazy='subquery')

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'), default=None)
    workouts = db.Column(db.Integer, db.ForeignKey('workouts.id'), default=None)

class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'), default='1')
    #bot sure what im trying to do here
    #client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), default='Not Assigned')
    exercises = db.Column(db.ARRAY(db.String), nullable=False)
