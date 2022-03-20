import jwt,json

from django.test import TestCase, Client

from users.models    import User, Gender
from carts.models    import Cart, CartSeries
from products.models import Product, Series, Author, Translator, Publisher, Category, Image
from my_settings     import SECRET_KEY, ALGORITHM
# Create your tests here.

class CartTest(TestCase):

    maxDiff=None

    def setUp(self):
        Gender.objects.create(
            id  = 1,
            sex = 'male',
        )

        User.objects.create(
            id        = 1,
            nickname  = 'gwang',
            kakao_id  = 12345,
            point     = 500000,
            gender_id = 1
        )

        Author.objects.create(
            id   = 1,
            name = "광일킴"
        )

        Publisher.objects.create(
            id   = 1,
            name = "팡일출판사"
        )

        Translator.objects.create(
            id   = 1,
            name = "팡민님"
        )

        Category.objects.create(
            id   = 1,
            name = "시"
        )

        Product.objects.create(
            id            = 1,
            name          = "맛난 간식 조아",
            description   = "간식을 먹으며 떠오른 시상을 옮겨적은 책입니다.",
            author_id     = 1,
            category_id   = 1,
            publisher_id  = 1,
            translator_id = 1
        )

        Image.objects.create(
            id         = 1,
            product_id = 1,
            image_url  = 'image'
        )
        Series.objects.create(
            id           = 1,
            name         = '코코볼과 함께',
            price        = 1000,
            sequence     = 1,
            published_at = '2022-03-01',
            product_id   = 1
        )

        Series.objects.create(
            id           = 2,
            name         = '첵스초코와 함께',
            price        = 500,
            sequence     = 2,
            published_at = '2022-03-02',
            product_id   = 1
        )

        Cart.objects.create(
            id         = 1,
            product_id = 1,
            user_id    = 1
        )

        CartSeries.objects.create(
            id        = 1,
            cart_id   = 1,
            series_id = 1
        )

    def tearDown(self):
        Gender.objects.all().delete()
        User.objects.all().delete()
        Author.objects.all().delete()
        Publisher.objects.all().delete()
        Translator.objects.all().delete()
        Category.objects.all().delete()
        Series.objects.all().delete()
        Product.objects.all().delete()
        Cart.objects.all().delete()
        CartSeries.objects.all().delete()

    def test_cart_post_success(self):
        client = Client()

        access_token = jwt.encode({'id' : 12345}, SECRET_KEY, ALGORITHM)
        headers      = {'HTTP_Authorization' : access_token}

        cart = {
            'user_id'    : 1,
            'product_id' : 1,
            'series_ids' : [2]
        }

        response = client.post('/carts', json.dumps(cart), 
                content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message' : 'CREATE_CART'})

    def test_cart_get_successs(self):
        client = Client()

        access_token = jwt.encode({'id' : 12345}, SECRET_KEY, ALGORITHM)
        headers      = {'HTTP_Authorization' : access_token}
        cart_list = [{
            'product_id'   : 1,
            'series_id'    : 1,
            'author'       : '광일킴',
            'series_name'  : '코코볼과 함께',
            'series_price' : '1000.00',
            'image'        : 'image'
        }]
        response = client.get('/carts', **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'result' : cart_list})

    def test_cart_delete_success(self):
        client = Client()

        access_token = jwt.encode({'id' : 12345}, SECRET_KEY, ALGORITHM)
        headers      = {'HTTP_Authorization' : access_token}
        
        cart_series = {
            'cart_series_id' : [1]
        }

        response = client.delete('/carts', json.dumps(cart_series), 
                content_type='application/json', **headers)

        self.assertEqual(response.status_code, 204)