from app.models import teacher
from app.tests.db_test_case import DBTestCase
import json
import unittest
import time

Teachers_API_PATH = 'http://127.0.0.1:5000/teacher/teacher'
Teacher_API_PATH = 'http://127.0.0.1:5000/teacher/teacher/{id}'

class TestTeacherAPI(DBTestCase):

    def create_teacher(self):
        return {
            'teacher_name' : "Teacher" , 
            'teacher_email' : "t@gmail.com",
            'teacher_phone' : 123 
        }
    
    def test_success_add_teacher(self):
        with self.client:
            request_teacher = self.create_teacher()
            headers = {
                "Content-Type": "application/json"
            }
            response = self.client.post(Teachers_API_PATH, headers=headers, data=json.dumps(request_teacher))
            # print (response.status_code)
            self.assertEqual(response.status_code, 200, response.data)
        
    def test_get_teacher(self):
        with self.client:
            request_teacher = self.create_teacher()
            headers = {
                "Content-Type": "application/json"
            }
            response = self.client.post(Teachers_API_PATH, headers=headers, data=json.dumps(request_teacher))
            # print (response.status_code)
            self.assertEqual(response.status_code, 200, response.data)
        
            # headers = {}
            response_teacher = json.loads(response.data)
            teacher_id = response_teacher.get('id')
            time.sleep(2)
            response = self.client.get(Teacher_API_PATH.format( id = teacher_id))
            self.assertEqual(response.status_code, 200, response.data)

    def test_edit_teacher(self):
        with self.client:
            request_teacher = self.create_teacher()
            headers = {
                "Content-Type": "application/json"
            }
            response = self.client.post(Teachers_API_PATH, headers=headers, data=json.dumps(request_teacher))
            # print (response.status_code)
            self.assertEqual(response.status_code, 200, response.data)
        
            response_teacher = json.loads(response.data)
            # print(response_teacher)
            teacher_id = response_teacher.get('id')
            time.sleep(2)
            response = self.client.put(Teacher_API_PATH.format(id =teacher_id), headers=headers, data=json.dumps(response_teacher))
            self.assertEqual(response.status_code, 200, response.data)
    
    def test_delete_teacher(self):
        with self.client:
            request_teacher = self.create_teacher()
            headers = {
                "Content-Type": "application/json"
            }
            response = self.client.post(Teachers_API_PATH, headers=headers, data=json.dumps(request_teacher))
            # print (response.status_code)
            self.assertEqual(response.status_code, 200, response.data)

            
            teacher_id = json.loads(response.data)['id']
            time.sleep(2)
            response = self.client.delete(Teacher_API_PATH.format( id =teacher_id), headers=headers)
            self.assertEqual(response.status_code, 200, response.data)


