from app.models import teacher
from app.tests.db_test_case import DBTestCase
import json
import unittest
import time


Teachers_API_PATH = 'http://127.0.0.1:5000/teacher/teacher'

Courses_API_PATH = 'http://127.0.0.1:5000/course/course'
Course_API_PATH = 'http://127.0.0.1:5000/course/course/{id}'

class TestCourseAPI(DBTestCase):

    def create_course(self , teacher_id):
        return {
            'title' : "Course" , 
            'price' : 1000 ,
            'teacher_id' : teacher_id
        }


    def create_teacher(self):
        return {
            'teacher_name' : "Teacher" , 
            'teacher_email' : "t@gmail.com",
            'teacher_phone' : 123 
        }
        
    def test_success_add_course(self):
        with self.client:
            request_teacher = self.create_teacher()
            headers = {
                "Content-Type": "application/json"
            }
            response = self.client.post(Teachers_API_PATH, headers=headers, data=json.dumps(request_teacher))
            # print (response.status_code)
            self.assertEqual(response.status_code, 200, response.data)
            teacher_id = json.loads(response.data)['id']
            request_course = self.create_course(teacher_id)


            headers = {
                "Content-Type": "application/json"
            }
            response = self.client.post(Courses_API_PATH, headers=headers, data=json.dumps(request_course))
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
            teacher_id = json.loads(response.data)['id']
            request_course = self.create_course(teacher_id)


            headers = {
                "Content-Type": "application/json"
            }
            response = self.client.post(Courses_API_PATH, headers=headers, data=json.dumps(request_course))
            # print (response.status_code)
            self.assertEqual(response.status_code, 200, response.data)



            # headers = {}
            response_course = json.loads(response.data)
            course_id = response_course.get('id')
            time.sleep(2)
            response = self.client.get(Course_API_PATH.format( id = course_id))
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
            teacher_id = json.loads(response.data)['id']
            request_course = self.create_course(teacher_id)


            headers = {
                "Content-Type": "application/json"
            }
            response = self.client.post(Courses_API_PATH, headers=headers, data=json.dumps(request_course))
            # print (response.status_code)
            self.assertEqual(response.status_code, 200, response.data)

            response_course = json.loads(response.data)
            # print(response_teacher)
            course_id = response_course.get('id')
            time.sleep(2)
            response = self.client.put(Course_API_PATH.format(id =course_id), headers=headers, data=json.dumps(response_course))
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
            request_course = self.create_course(teacher_id)


            headers = {
                "Content-Type": "application/json"
            }
            response = self.client.post(Courses_API_PATH, headers=headers, data=json.dumps(request_course))
            # print (response.status_code)
            self.assertEqual(response.status_code, 200, response.data)

            course_id = json.loads(response.data)['id']
            time.sleep(2)
            response = self.client.delete(Course_API_PATH.format( id =course_id), headers=headers)
            self.assertEqual(response.status_code, 200, response.data)


