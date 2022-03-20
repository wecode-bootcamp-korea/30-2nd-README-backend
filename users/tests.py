import jwt, json

from django.test   import TestCase, Client
from unittest.mock import patch, MagicMock

from .models     import User, Gender
from my_settings import SECRET_KEY, ALGORITHM


class SignInTest(TestCase):
    def setUp(self):
        Gender.objects.create(
            id  = 1,
            sex = 'male',
        )
        Gender.objects.create(
            id  = 2,
            sex = 'female',
        )
        User.objects.create(
            id            = 1,
            nickname      = 'gwang',
            date_of_birth = '1945-08-15',
            kakao_id      = 12345,
            point         = 500000,
            gender_id     = 1
        )
      
    def tearDown(self):
        Gender.objects.all().delete()
        User.objects.all().delete()

    @patch('users.views.requests')
    def test_kakao_signin_get_user_success(self, mocked_requests):
        client = Client()
        
        class MockedResponse:
            def json(self):
                return {
                    'id'           : 12345,
                    'kakao_account': { 
                        'gender' : 'male',
                    },
                    'properties' : {
                        'nickname' : 'gwang'
                    }
                }        
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        
        headers  = {'Authorization' : 'access_token'}
        response = client.get('/users/signin', **headers)

        access_token = jwt.encode({'id': 12345}, SECRET_KEY, ALGORITHM)

        self.assertEqual(response.json(), {'access_token' : access_token})
        self.assertEqual(response.status_code, 200)

    @patch('users.views.requests')
    def test_kakao_signin_new_user_success(self, mocked_requests):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
                    'id':12343,
                    'kakao_account': { 
                        'gender' : 'male',
                    },
                    'properties' : {
                        'nickname' : 'pang'
                    }
                }        
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        
        headers  = {'Authorization' : 'access_token'}
        response = client.get('/users/signin', **headers)

        access_token = jwt.encode({'id': 12343}, SECRET_KEY, ALGORITHM)

        self.assertEqual(response.json(), {'access_token' : access_token})
        self.assertEqual(response.status_code, 201)

    def test_user_information_update_nickname_date_of_birth_success(self):
        client = Client()

        access_token = jwt.encode({'id' : 12345}, SECRET_KEY, ALGORITHM)
        headers      = {'HTTP_Authorization' : access_token}

        user = {
            'nickname' : '잉',
            'date_of_birth' : '2000-01-01'
        }

        response = client.patch('/users/signin',
             json.dumps(user), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 200)

    def test_user_information_update_key_error(self):
        client = Client()

        access_token = jwt.encode({'id' : 12345}, SECRET_KEY, ALGORITHM)
        headers      = {'HTTP_Authorization' : access_token}

        invalid_user = {
            'nick_name'     : '하',
            'date_of_birth' : '2000-01-01'
        }

        response = client.patch('/users/signin', json.dumps(invalid_user), 
                content_type='application/json', **headers)

        self.assertEqual(response.json(), {'message' : 'KEY_ERROR'})
        self.assertEqual(response.status_code, 400)