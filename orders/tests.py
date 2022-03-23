from django.http import response
import jwt, json

from django.test import TestCase, Client

from my_settings     import SECRET_KEY, ALGORITHM
from .models         import Order, OrderSeries
from users.models         import User, Gender
from products.models import Product, Author, Publisher, Translator, Series, Category
from carts.models    import Cart, CartSeries

class OrderTest(TestCase):
    def setUp(self):
        Gender.objects.create(
            id  = 1,
            sex = 'male'
        )
        User.objects.create(
            id        = 1,
            kakao_id  = 12345,
            nickname  = 'gwang',
            point     = 50,
            gender_id = 1
        )

        Author.objects.create(
            id   = 1,
            name = '광작'
        )

        Translator.objects.create(
            id   = 1,
            name = '팡'
        )

        Publisher.objects.create(
            id   = 1,
            name = '오르골출판'
        )

        Category.objects.create(
            id   = 1,
            name = '자서전'
        )
        
        Product.objects.create(
            id            = 1,
            name          = '광',
            description   = '광일',
            author_id     = 1,
            translator_id = 1,
            publisher_id  = 1,
            category_id   = 1
        )
        
        Series.objects.create(
            id           = 1,
            name         = '광일',
            price        = 1000,
            sequence     = 1,
            published_at = '2020-02-02',
            product_id   = 1
        )

        Series.objects.create(
            id           = 2,
            name         = '광이',
            price        = 500,
            sequence     = 2,
            published_at = '2020-02-04',
            product_id   = 1
        )

        Cart.objects.create(
            id         = 1,
            user_id    = 1,
            product_id = 1
        )
        
        CartSeries.objects.create(
            id        = 1,
            cart_id   = 1,
            series_id = 1
        )
        
        CartSeries.objects.create(
            id        = 2,
            cart_id   = 1,
            series_id = 2
        )

    def tearDown(self):
        Gender.objects.all().delete()
        User.objects.all().delete()
        Author.objects.all().delete()
        Translator.objects.all().delete()
        Publisher.objects.all().delete()
        Product.objects.all().delete()
        Series.objects.all().delete()
        Cart.objects.all().delete()
        CartSeries.objects.all().delete()

    def test_order_success(self):
        client = Client()

        access_token = jwt.encode({'id':12345}, SECRET_KEY, ALGORITHM)
        headers      = {'HTTP_Authorization' : access_token}

        order = {
            'product_id' : 1,
            'series_ids' : [1,2]
        }

        response = client.post('/orders', json.dumps(order), 
                            content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)

    def test_order_404_error_DOES_NOT_EXIST_CART(self):
        client = Client()

        access_token = jwt.encode({'id':12345}, SECRET_KEY, ALGORITHM)
        headers      = {'HTTP_Authorization' : access_token}

        order = {
            'product_id' : 1,
            'series_ids' : [3],
        }

        response = client.post('/orders', json.dumps(order), 
                            content_type='application/json', **headers)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'message' : 'CART_DOES_NOT_EXIST'})