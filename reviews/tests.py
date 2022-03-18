import jwt, json

from django.test   import TestCase, Client

from my_settings import ALGORITHM, SECRET_KEY

from .models         import Review
from products.models import Product, Image, Author, Translator, Publisher, Category
from users.models    import User, Gender

class ReviewTest(TestCase):
    def setUp(self):
        Category.objects.create(
            id   = 1,
            name = '베스트셀러'
        )
        Author.objects.create(
            id   = 1,
            name = '김작가'
        )
        Translator.objects.create(
            id   = 1,
            name = '김번역'
        )
        Publisher.objects.create(
            id   = 1,
            name = '출판사'
        )
        Product.objects.create(
            id            = 1,
            name          = '빨간책',
            category_id   = 1,
            publisher_id  = 1,
            translator_id = 1,
            author_id     = 1,
            description   = '책 설명',
        )
        Product.objects.create(
            id            = 2,
            name          = '파란책',
            category_id   = 1,
            publisher_id  = 1,
            translator_id = 1,
            author_id     = 1,
            description   = '책 설명',
        )
        Image.objects.create(
            id         = 1,
            image_url  = 'www.google.com',
            product_id = 1
        )
        Gender.objects.create(
            id  = 1,
            sex = 'male'
        )
        User.objects.create(
            id            = 1,
            nickname      = 'jayce',
            gender_id     = 1,
            date_of_birth = '1993-11-23',
            kakao_id      = 12345,
            point         = 500000
        )
        User.objects.create(
            id            = 2,
            nickname      = 'jayce2',
            gender_id     = 1,
            date_of_birth = '1993-11-23',
            kakao_id      = 12346,
            point         = 500000
        )
        User.objects.create(
            id            = 3,
            nickname      = 'jayce3',
            gender_id     = 1,
            date_of_birth = '1993-11-23',
            kakao_id      = 12347,
            point         = 500000
        )
        Review.objects.create(
            id         = 1,
            rating     = 2.5,
            content    = '리뷰내용1',
            user_id    = 1,
            product_id = 1,
        )
        Review.objects.create(
            id         = 2,
            rating     = 3,
            content    = '리뷰내용2',
            user_id    = 2,
            product_id = 1,
        )
        Review.objects.create(
            id         = 3,
            rating     = 3,
            content    = '리뷰내용3',
            user_id    = 3,
            product_id = 1,
        )

    def tearDown(self):
        Category.objects.all().delete()
        Author.objects.all().delete()
        Translator.objects.all().delete()
        Publisher.objects.all().delete()
        Image.objects.all().delete()
        Product.objects.all().delete()
        Gender.objects.all().delete()
        User.objects.all().delete()
        Review.objects.all().delete()
        
    def test_review_get_handler_method_success(self):
        client = Client()

        access_token = jwt.encode({'id':12345},SECRET_KEY, ALGORITHM) 
        headers      = {"HTTP_Authorization" : access_token}
        response     = client.get('/reviews/1',**headers)

        self.assertEqual(response.json(),
            {
                "results": {
                    "top_review": {
                        "review_id": 1,
                        "user_id": 1,
                        "nickname": "jayce",
                        "rating": 2.5,
                        "content": "리뷰내용1",
                        "created_at": "2022-03-20",
                        "updated_at": "2022-03-20"
                    },
                    "list_review": [
                        {
                            "review_id": 2,
                            "user_id": 2,
                            "nickname": "jayce2",
                            "rating": 3,
                            "content": "리뷰내용2",
                            "created_at": "2022-03-20",
                            "updated_at": "2022-03-20"
                        },
                        {
                            "review_id": 3,
                            "user_id": 3,
                            "nickname": "jayce3",
                            "rating": 3,
                            "content": "리뷰내용3",
                            "created_at": "2022-03-20",
                            "updated_at": "2022-03-20"
                        }
                    ]    
                }
            }
        )
        self.assertEqual(response.status_code, 200)

    def test_review_get_handler_method_invaild_user(self):
        client = Client()
        
        access_token = jwt.encode({'id':1234},SECRET_KEY, ALGORITHM) 
        headers      = {"HTTP_Authorization" : access_token}
        response     = client.get('/reviews/1',**headers)
        
        self.assertEqual(response.json(),
            {
                'message': 'INVALID_USER'
            }
        )
        self.assertEqual(response.status_code, 401)

    def test_review_get_handler_method_not_existed_user(self):
        client = Client()
        
        access_token = jwt.encode({'id':12345},SECRET_KEY, ALGORITHM) 
        headers      = {"HTTP_Authorization" : access_token}
        response     = client.get('/reviews/19',**headers)
        
        self.assertEqual(response.json(),
            {
                'message': 'NOT_EXIST_REVIEW'
            }
        )
        self.assertEqual(response.status_code, 404)

    def test_review_post_handler_method_success(self):
        client = Client()

        reviews = {
                "id"         : 2,
                "user_id"    : 2,
                "product_id" : 2,
                "rating"     : 2.5,
                "content"    : 'asdfg'
        }	
        access_token = jwt.encode({'id':12346},SECRET_KEY, ALGORITHM)
        headers      = {"HTTP_Authorization" : access_token}
        response     = client.post('/reviews/2',
                                    json.dumps(reviews),
                                    content_type='application/json',
                                    **headers
                                    )
        
        self.assertEqual(response.json(),
            {
                'message' : 'SUCCESS'
            }
        )
        self.assertEqual(response.status_code, 201)
        
    def test_review_post_handler_method_key_error(self):
        client = Client()

        reviews = {
                "id"         : 2,
                "user_id"    : 1,
                "rating"     : 2.5,
                "contnet"    : 'asdfg'
        }	
        access_token = jwt.encode({'id':12346},SECRET_KEY, ALGORITHM)
        headers      = {"HTTP_Authorization" : access_token}
        response     = client.post('/reviews/1',
                                    json.dumps(reviews),
                                    content_type='application/json',
                                    **headers
                                    )
        
        self.assertEqual(response.json(),
            {
                'message':'KEY_ERROR'
            }
        )
        self.assertEqual(response.status_code, 400)
        
    def test_review_post_handler_method_review_already_existed(self):
        client = Client()

        reviews = {
                "user_id"    : 1,
                "product_id" : 1,
                "rating"     : 4,
                "content"    : 'asdfg'
        }	
        access_token = jwt.encode({'id':12345},SECRET_KEY, ALGORITHM)
        headers      = {"HTTP_Authorization" : access_token}
        response     = client.post('/reviews/1',
                                    json.dumps(reviews),
                                    content_type='application/json',
                                    **headers
                                    )
        
        self.assertEqual(response.json(),
            {
                'message':'REVIEW_ALREADY_EXISTED'
            }
        )
        self.assertEqual(response.status_code, 400)
        
    def test_review_patch_handler_method_success(self):
        client = Client()

        reviews = {
                "review_id"  : 1,
                "rating"     : 5,
                "content"    : 'qwert'
        }	
        access_token = jwt.encode({'id':12346},SECRET_KEY, ALGORITHM)
        headers      = {"HTTP_Authorization" : access_token}
        response     = client.patch('/reviews/1',
                                    json.dumps(reviews),
                                    content_type='application/json',
                                    **headers
                                    )
        
        self.assertEqual(response.json(),
            {
                'message' : 'SUCCESS'
            }
        )
        self.assertEqual(response.status_code, 200)
        
    def test_review_patch_handler_method_not_exist_review(self):
        client = Client()

        reviews = {
                "review_id"  : 3,
                "rating"     : 5,
                "content"    : 'qwert'
        }	
        access_token = jwt.encode({'id':12346},SECRET_KEY, ALGORITHM)
        headers      = {"HTTP_Authorization" : access_token}
        response     = client.patch('/reviews/2',
                                    json.dumps(reviews),
                                    content_type='application/json',
                                    **headers
                                    )
        
        self.assertEqual(response.json(),
            {
                'message':'NOT_EXIST_REVIEW'
            }
        )
        self.assertEqual(response.status_code, 404)
        
    def test_review_patch_handler_method_key_error(self):
        client = Client()

        reviews = {
                "rating"     : 5,
                "content"    : 'qwert'
        }	
        access_token = jwt.encode({'id':12346},SECRET_KEY, ALGORITHM)
        headers      = {"HTTP_Authorization" : access_token}
        response     = client.patch('/reviews/2',
                                    json.dumps(reviews),
                                    content_type='application/json',
                                    **headers
                                    )
        
        self.assertEqual(response.json(),
            {
                'message':'KEY_ERROR'
            }
        )
        self.assertEqual(response.status_code, 400)

    def test_review_delete_handler_method_success(self):
        client = Client()

        access_token = jwt.encode({'id':12345},SECRET_KEY, ALGORITHM)
        headers      = {"HTTP_Authorization" : access_token}
        response     = client.delete('/reviews/1?review_id=1',
                                    **headers
                                    )
        
        self.assertEqual(response.json(),
            {
                'message' : 'SUCCESS'
            }
        )
        self.assertEqual(response.status_code, 200)
        
    def test_review_delete_handler_method_not_exist_review(self):
        client = Client()

        access_token = jwt.encode({'id':12345},SECRET_KEY, ALGORITHM)
        headers      = {"HTTP_Authorization" : access_token}
        response     = client.delete('/reviews/1?review_id=5',
                                    **headers
                                    )
        
        self.assertEqual(response.json(),
            {
                'message': 'NOT_EXIST_REVIEW'
            }
        )
        self.assertEqual(response.status_code, 404)