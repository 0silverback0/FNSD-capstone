from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    with app.app_context():
        db.app = app
        db.init_app(app)
        # db.drop_all()
        db.create_all()


class Trainer(db.Model):
    __tablename__ = 'trainers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)

    clients = db.relationship(
        'Client',
        secondary='workouts',
        backref='trainers',
        lazy='subquery')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)
    trainer_id = db.Column(
        db.Integer,
        db.ForeignKey('trainers.id'),
        default=None)
    workouts = db.Column(
        db.Integer,
        db.ForeignKey('workouts.id'),
        default=None)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trainer_id = db.Column(
        db.Integer,
        db.ForeignKey('trainers.id'),
        default='1')
    exercises = db.Column(db.ARRAY(db.String), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
