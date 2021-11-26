import unittest
import sqlalchemy

from app import app , db

class DBTestCase(unittest.TestCase):

    def setUp(self):
        with app.app_context():
            url = 'postgresql://mohamed:root@localhost:5432/proj_course.test'
            app.config['SQLALCHEMY_DATABASE_URI'] = url
            app.config['TESTING'] = True
            
            self.engine = sqlalchemy.create_engine(url)

            db.create_all()
            self.client = app.test_client()


    def tearDown(self):
        with app.app_context():
            db.session.close()
            db.session.remove()
            db.drop_all()