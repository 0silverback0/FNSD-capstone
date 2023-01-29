import os
import unittest
import json, requests
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import connect_db, Trainer, Client, Workout
from config import TEST_DATABASE, COACH_TOKEN, CLIENT_TOKEN

BASEURL = 'http://127.0.0.1:5000'

class FitnessTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.database_name = "fitness_test"
        self.database_path = TEST_DATABASE #"postgres://{}/{}".format('localhost:5432', self.database_name)
        connect_db(self.app) #, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
            self.coach_token = COACH_TOKEN
            self.client_token = CLIENT_TOKEN

    def tearDown(self):
        """Executed after reach test"""
        pass

   
    def test_trainers_succes(self):
        with self.app.app_context():

            # test proper request
            res = requests.get(f'{BASEURL}/', headers={
            'Authorization': "Bearer {}".format(self.coach_token)
            })
            self.assertEqual(res.status_code, 200)

    def test_trainers_fail(self):
            # test malformed header
            error_res = requests.get(f'{BASEURL}/')
            self.assertEqual(error_res.status_code, 401)

    
    def test_create_trainer_success(self):
        res = requests.post(f'{BASEURL}', headers={
            'Authorization': "Bearer {}".format(self.coach_token)
            })
        self.assertEqual(res.status_code, 200)

    def test_create_trainer_fail(self):
        error_res = requests.post(f'{BASEURL}')
        self.assertEqual(error_res.status_code, 401)

    def test_create_client_success(self):
        res = requests.post(f'{BASEURL}/clients', headers={
            'Authorization': "Bearer {}".format(self.coach_token)
            })
        self.assertEqual(res.status_code, 200)

    def test_create_client_fail(self):
        error_res = requests.post(f'{BASEURL}/clients')
        self.assertEqual(error_res.status_code, 401)

    def test_clients_success(self):
        res = requests.get(f'{BASEURL}/clients', headers={
            'Authorization': "Bearer {}".format(self.coach_token)
            })
        self.assertEqual(res.status_code, 200)

    def test_client_fail(self):
        error_res = requests.get(f'{BASEURL}')
        self.assertEqual(error_res.status_code, 401)

    
if __name__ == "__main__":
    unittest.main()