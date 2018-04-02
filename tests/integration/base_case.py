import unittest
from app import app, db


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.headers = {'Content-Type': 'application/json'}
        self.db = db
        self.db.drop_all()
        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
        self.db.get_engine(self.app).dispose()