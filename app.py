from sqlite3 import IntegrityError
from flask import Flask, render_template, jsonify, request, json, abort

from config import DATABASE_URI
from models import Workout, connect_db, db, Trainer, Client
from auth import AuthError, requires_auth
from sqlalchemy import orm, exc
from psycopg2 import errors
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

with app.app_context():
    connect_db(app)

#get trainers
@app.route('/')
@requires_auth('get:trainers')
def get_trainers(payload):
    try:
        if 'get:trainers' in payload['permissions']:
            trainers = Trainer.query.all()

            return jsonify({
                'trainers': [trainer.name for trainer in trainers],
                'success': True
            })
    except exc.IntegrityError:
        abort(404)

# create new trainer
@app.route('/', methods=['POST'])
@requires_auth('post:trainers')
def create_trainer(payload):
    name = request.get_json('name')
    print(name)
    try:
        if 'post:trainers' in payload['permissions']:
            new_trainer = Trainer(name=name['name'])
            db.session.add(new_trainer)
            db.session.commit()

            return jsonify({
                'trainers': new_trainer.name,
                'success': True
            })
    except exc.IntegrityError:
        abort(400)

#create new client
@app.route('/clients', methods=['POST'])
@requires_auth('get:clients')
def create_client(payload):
    name = request.form.get('name')
    try:
        if 'get:clients' in payload['permissions']:
            client = Client(name=name)
            db.session.add(client)
            db.session.commit()

            return jsonify({
                'client': client.name,
                'success': True
            })
    except exc.IntegrityError:
        print(exc.IntegrityError)
        abort(404)
        
    

#get all clients
@app.route('/clients')
@requires_auth('get:clients')
def get_clients(payload):
    if 'get:clients' in payload['permissions']:
        clients = Client.query.all()
        return jsonify({
            'clients': [client.name for client in clients],
            'success': True
        })
    else:
        return jsonify({
            'succes': False
        })

@app.route('/workouts', methods=['POST'])
@requires_auth('post:workouts')
def create_workouts(payload):
    
    try:
        if 'post:workouts' in payload['permissions']:
            ex1 = request.form.get('ex1')
            ex2 = request.form.get('ex2')
            ex3 = request.form.get('ex3')
            exercises = [ex1, ex2, ex3]
            
            workout = Workout(exercises=exercises)
            db.session.add(workout)
            db.session.commit()
        
            return jsonify({
                "trainer_id": workout.trainer_id,
                "workout":  workout.exercises   
            })
    except IntegrityError:
        abort(404)

#double check this route
@app.route('/workouts/edit/<int:id>', methods=['PATCH'])
@requires_auth('patch:workout')
def edit_workout(payload, id):
    workout = Workout.query.get(id)
    if 'patch:workout' in payload['permissions']:
        ex1 = request.form.get('ex1') or workout.exercises[0]
        ex2 = request.form.get('ex2') or workout.exercises[1]
        ex3 = request.form.get('ex3') or workout.exercises[2]
        workout.exercises = [ex1,ex2,ex3]
        db.session.commit()
        return jsonify({
            'success': True,
            'exercises': workout.exercises
        })

@app.route('/workouts/delete/<int:id>', methods=['DELETE'])
@requires_auth('delete:workout')
def delete_workout(payload, id):
    workout = Workout.query.get(id)
    try:
        if 'delete:workout' in payload['permissions']:
            db.session.delete(workout)
            db.session.commit()

            return jsonify({
                'success': True,
                'workout': f'workout id: {workout.id} deleted'
            })

    except orm.exc.UnmappedInstanceError:
        abort(404)

"""
error handlers
"""

@app.errorhandler(AuthError)
def auth_error(error):
    
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error.get('description')
    }), error.status_code

@app.errorhandler(400)
def bad_request(e):
    return jsonify({
        'success': False,
        'error': e.code,
        'description': e.description
    })

@app.errorhandler(403)
def bad_request(e):
    return jsonify({
        'success': False,
        'error': e.code,
        'description': 'Cannot delete. Does Not Exist'
    })

@app.errorhandler(500)
def others(e):
    return jsonify({
        'succes': False,
        'code': e.code
    })