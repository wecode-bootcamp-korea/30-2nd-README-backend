from django.test     import TestCase, Client
from products.models import Product, Author, Image, Publisher, Translator, Category
from reviews.models  import Review
from users.models    import User, Gender

class ProductListViewTest(TestCase):
    def setUp(self):

        Author.objects.bulk_create([
            Author(
                id   = 1,
                name = '1번책 작가'
            ),
            Author(
                id   = 2,
                name = '2번책 작가'
            ),
            Author(
                id   = 3,
                name = '3번책 작가'
            ),
            Author(
                id   = 4,
                name = '4번책 작가'
            ),
            Author(
                id   = 5,
                name = '5번책 작가'
            ),
            Author(
                id   = 6,
                name = '6번책 작가'
            ),
            Author(
                id   = 10,
                name = '10번책 작가'
            ),
            Author(
                id   = 11,
                name = '11번책 작가'
            ),
            Author(
                id   = 12,
                name = '12번책 작가'
            )
        ])

        Publisher.objects.bulk_create([
            Publisher(
                id   = 1,
                name = '1번책 출판사'
            ),
            Publisher(
                id   = 2,
                name = '2번책 출판사'
            ),
            Publisher(
                id   = 3,
                name = '3번책 출판사'
            ),
            Publisher(
                id   = 4,
                name = '4번책 출판사'
            ),
            Publisher(
                id   = 5,
                name = '5번책 출판사'
            ),
            Publisher(
                id   = 6,
                name = '6번책 출판사'
            ),
            Publisher(
                id   = 10,
                name = '10번책 출판사'
            ),
            Publisher(
                id   = 11,
                name = '11번책 출판사'
            ),
            Publisher(
                id   = 12,
                name = '12번책 출판사'
            )
        ])

        Translator.objects.bulk_create([
            Translator(
                id   = 1,
                name = '1번책 번역가'
            ),
            Translator(
                id   = 2,
                name = '2번책 번역가'
            ),
            Translator(
                id   = 3,
                name = '3번책 번역가'
            ),
            Translator(
                id   = 4,
                name = '4번책 번역가'
            ),
            Translator(
                id   = 5,
                name = '5번책 번역가'
            ),
            Translator(
                id   = 6,
                name = '6번책 번역가'
            ),
            Translator(
                id   = 10,
                name = '10번책 번역가'
            ),
            Translator(
                id   = 11,
                name = '11번책 번역가'
            ),
            Translator(
                id   = 12,
                name = '12번책 번역가'
            )
        ])

        Category.objects.bulk_create([
            Category(
                id   = 1,
                name = '1번책 카테고리'
            ),
            Category(
                id   = 2,
                name = '2번책 카테고리'
            ),
            Category(
                id   = 3,
                name = '3번책 카테고리'
            ),
            Category(
                id   = 4,
                name = '4번책 카테고리'
            ),
            Category(
                id   = 5,
                name = '5번책 카테고리'
            ),
            Category(
                id   = 6,
                name = '6번책 카테고리'
            ),
            Category(
                id   = 10,
                name = '10번책 카테고리'
            ),
            Category(
                id   = 11,
                name = '11번책 카테고리'
            ),
            Category(
                id   = 12,
                name = '12번책 카테고리'
            )
        ])

        Product.objects.bulk_create([
            Product(
                id              = 1,
                name            = '1번책',
                description     = '1번책 내용',
                publisher_id    = 1,
                translator_id   = 1,
                author_id       = 1,
                category_id     = 1
            ),
            Product(
                id              = 2,
                name            = '2번책',
                description     = '2번책 내용',
                publisher_id    = 2,
                translator_id   = 2,
                author_id       = 2,
                category_id     = 2
            ),
            Product(
                id              = 3,
                name            = '3번책',
                description     = '3번책 내용',
                publisher_id    = 3,
                translator_id   = 3,
                author_id       = 3,
                category_id     = 3
            ),
            Product(
                id              = 4,
                name            = '4번책',
                description     = '4번책 내용',
                publisher_id    = 4,
                translator_id   = 4,
                author_id       = 4,
                category_id     = 4
            ),
            Product(
                id              = 5,
                name            = '5번책',
                description     = '5번책 내용',
                publisher_id    = 5,
                translator_id   = 5,
                author_id       = 5,
                category_id     = 5
            ),
            Product(
                id              = 6,
                name            = '6번책',
                description     = '6번책 내용',
                publisher_id    = 6,
                translator_id   = 6,
                author_id       = 6,
                category_id     = 6
            ),
            Product(
                id              = 10,
                name            = '10번책',
                description     = '10번책 내용',
                publisher_id    = 10,
                translator_id   = 10,
                author_id       = 10,
                category_id     = 10
            ),
            Product(
                id              = 11,
                name            = '11번책',
                description     = '11번책 내용',
                publisher_id    = 11,
                translator_id   = 11,
                author_id       = 11,
                category_id     = 11
            ),
            Product(
                id              = 12,
                name            = '12번책',
                description     = '12번책 내용',
                publisher_id    = 12,
                translator_id   = 12,
                author_id       = 12,
                category_id     = 12
            )
        ])

        Gender.objects.create(
            id  = 1,
            sex = 'male'
        )

        User.objects.create(
            id            = 1,
            nickname      = '노란책 닉네임',
            date_of_birth = '1989-07-06',
            gender_id     = 1,
            kakao_id      = '노란책 카카오 아이디',
            point         = 100000
        )

        Image.objects.bulk_create([
            Image(
                id         = 1,
                image_url  = '1번책 이미지 유알엘',
                product_id = 1
            ),
            Image(
                id         = 2,
                image_url  = '2번책 이미지 유알엘',
                product_id = 2
            ),
            Image(
                id         = 3,
                image_url  = '3번책 이미지 유알엘',
                product_id = 3
            ),
            Image(
                id         = 4,
                image_url  = '4번책 이미지 유알엘',
                product_id = 4
            ),
            Image(
                id         = 5,
                image_url  = '5번책 이미지 유알엘',
                product_id = 5
            ),
            Image(
                id         = 6,
                image_url  = '6번책 이미지 유알엘',
                product_id = 6
            ),
            Image(
                id         = 10,
                image_url  = '10번책 이미지 유알엘',
                product_id = 10
            ),
            Image(
                id         = 11,
                image_url  = '11번책 이미지 유알엘',
                product_id = 11
            ),
            Image(
                id         = 12,
                image_url  = '12번책 이미지 유알엘',
                product_id = 12
            )
        ])

        Review.objects.bulk_create([
            Review(
                id         = 1,
                content    = '1번책 리뷰',
                rating     = 5,
                product_id = 1,
                user_id    = 1
            ),
            Review(
                id         = 2,
                content    = '2번책 리뷰',
                rating     = 5,
                product_id = 2,
                user_id    = 1
            ),
            Review(
                id         = 3,
                content    = '3번책 리뷰',
                rating     = 5,
                product_id = 3,
                user_id    = 1
            ),
            Review(
                id         = 4,
                content    = '4번책 리뷰',
                rating     = 5,
                product_id = 4,
                user_id    = 1
            ),
            Review(
                id         = 5,
                content    = '5번책 리뷰',
                rating     = 5,
                product_id = 5,
                user_id    = 1
            ),
            Review(
                id         = 6,
                content    = '6번책 리뷰',
                rating     = 5,
                product_id = 6,
                user_id    = 1
            ),
            Review(
                id         = 10,
                content    = '10번책 리뷰',
                rating     = 5,
                product_id = 10,
                user_id    = 1
            ),
            Review(
                id         = 11,
                content    = '11번책 리뷰',
                rating     = 5,
                product_id = 11,
                user_id    = 1
            ),
            Review(
                id         = 12,
                content    = '12번책 리뷰',
                rating     = 5,
                product_id = 12,
                user_id    = 1
            )
        ])

    def tearDown(self):
        Author.objects.all().delete()
        Publisher.objects.all().delete()
        Translator.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()
        Gender.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()
        Review.objects.all().delete()

    def test_success_product_list_view_get_handler_method(self):
        client = Client()
        response = client.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['result']), 9)

    def test_success_product_list_view_query_param_get_handler_method(self):
        client = Client()
        response = client.get('/products?category=1번책 카테고리')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                "result": [
                    {
                        "name"          : '1번책',
                        "book_img"      : ['1번책 이미지 유알엘'],
                        "author"        : '1번책 작가',
                        "rating_avg"    : 5.0,
                        "comment_count" : 1,
                        'product_id'    : 1
                    }
                ]    
            }
        ) 


class ProductBestsellerViewTest(TestCase):
    def setUp(self):

        Author.objects.bulk_create([
            Author(
                id   = 1,
                name = '1번책 작가'
            ),
            Author(
                id   = 2,
                name = '2번책 작가'
            ),
            Author(
                id   = 3,
                name = '3번책 작가'
            )
        ])

        Publisher.objects.bulk_create([
            Publisher(
                id   = 1,
                name = '1번책 출판사'
            ),
            Publisher(
                id   = 2,
                name = '2번책 출판사'
            ),
            Publisher(
                id   = 3,
                name = '3번책 출판사'
            )
        ])

        Translator.objects.bulk_create([
            Translator(
                id   = 1,
                name = '1번책 번역가'
            ),
            Translator(
                id   = 2,
                name = '2번책 번역가'
            ),
            Translator(
                id   = 3,
                name = '3번책 번역가'
            )
        ])

        Category.objects.bulk_create([
            Category(
                id = 1,
                name = '1번책 카테고리'
            ),
            Category(
                id = 2,
                name = '2번책 카테고리'
            ),
            Category(
                id = 3,
                name = '3번책 카테고리'
            )
        ])

        Product.objects.bulk_create([
            Product(
                id              = 1,
                name            = '1번책',
                description     = '1번책 내용',
                publisher_id    = 1,
                translator_id   = 1,
                author_id       = 1,
                category_id     = 1
            ),
            Product(
                id              = 2,
                name            = '2번책',
                description     = '2번책 내용',
                publisher_id    = 2,
                translator_id   = 2,
                author_id       = 2,
                category_id     = 2
            ),
            Product(
                id              = 3,
                name            = '3번책',
                description     = '3번책 내용',
                publisher_id    = 3,
                translator_id   = 3,
                author_id       = 3,
                category_id     = 3
            )
        ])

        Gender.objects.create(
            id  = 1,
            sex = 'male'
        )

        User.objects.create(
            id            = 1,
            nickname      = '노란책 닉네임',
            date_of_birth = '1989-07-06',
            gender_id     = 1,
            kakao_id      = '노란책 카카오 아이디',
            point         = 100000
        )

        Image.objects.bulk_create([
            Image(
                id         = 1,
                image_url  = '1번책 이미지 유알엘',
                product_id = 1
            ),
            Image(
                id         = 2,
                image_url  = '2번책 이미지 유알엘',
                product_id = 2
            ),
            Image(
                id         = 3,
                image_url  = '3번책 이미지 유알엘',
                product_id = 3
            )
        ])

        Review.objects.bulk_create([
            Review(
                id         = 1,
                content    = '1번책 리뷰',
                rating     = 5,
                product_id = 1,
                user_id    = 1
            ),
            Review(
                id         = 2,
                content    = '2번책 리뷰',
                rating     = 4,
                product_id = 2,
                user_id    = 1
            ),
            Review(
                id         = 3,
                content    = '3번책 리뷰',
                rating     = 3,
                product_id = 3,
                user_id    = 1
            )
        ])

    def tearDown(self):
        Author.objects.all().delete()
        Publisher.objects.all().delete()
        Translator.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()
        Gender.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()
        Review.objects.all().delete()

    def test_success_product_bestseller_view_get_handler_method(self):
        client = Client()
        response = client.get('/products/bestseller')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                "result": [
                    {
                        'name'          : '1번책',
                        'book_img'      : ['1번책 이미지 유알엘'],
                        'author'        : '1번책 작가',
                        'rating_avg'    : 5.0,
                        'comment_count' : 1,
                        'product_id'    : 1
                    },
                    {
                        'name'          : '2번책',
                        'book_img'      : ['2번책 이미지 유알엘'],
                        'author'        : '2번책 작가',
                        'rating_avg'    : 4.0,
                        'comment_count' : 1,
                        'product_id'    : 2
                    },
                    {
                        'name'          : '3번책',
                        'book_img'      : ['3번책 이미지 유알엘'],
                        'author'        : '3번책 작가',
                        'rating_avg'    : 3.0,
                        'comment_count' : 1,
                        'product_id'    : 3
                    }
                ]    
            }
        )            


class ProductRecommendViewTest(TestCase):
    def setUp(self):

        Author.objects.bulk_create([
            Author(
                id   = 1,
                name = '1번책 작가'
            ),
            Author(
                id   = 2,
                name = '2번책 작가'
            ),
            Author(
                id   = 3,
                name = '3번책 작가'
            )
        ])

        Publisher.objects.bulk_create([
            Publisher(
                id   = 1,
                name = '1번책 출판사'
            ),
            Publisher(
                id   = 2,
                name = '2번책 출판사'
            ),
            Publisher(
                id   = 3,
                name = '3번책 출판사'
            )
        ])

        Translator.objects.bulk_create([
            Translator(
                id   = 1,
                name = '1번책 번역가'
            ),
            Translator(
                id   = 2,
                name = '2번책 번역가'
            ),
            Translator(
                id   = 3,
                name = '3번책 번역가'
            )
        ])

        Category.objects.bulk_create([
            Category(
                id = 1,
                name = '1번책 카테고리'
            ),
            Category(
                id = 2,
                name = '2번책 카테고리'
            ),
            Category(
                id = 3,
                name = '3번책 카테고리'
            )
        ])

        Product.objects.bulk_create([
            Product(
                id              = 1,
                name            = '1번책',
                description     = '1번책 내용',
                publisher_id    = 1,
                translator_id   = 1,
                author_id       = 1,
                category_id     = 1
            ),
            Product(
                id              = 2,
                name            = '2번책',
                description     = '2번책 내용',
                publisher_id    = 2,
                translator_id   = 2,
                author_id       = 2,
                category_id     = 2
            ),
            Product(
                id              = 3,
                name            = '3번책',
                description     = '3번책 내용',
                publisher_id    = 3,
                translator_id   = 3,
                author_id       = 3,
                category_id     = 3
            )
        ])

        Gender.objects.create(
            id  = 1,
            sex = 'male'
        )

        User.objects.create(
            id            = 1,
            nickname      = '노란책 닉네임',
            date_of_birth = '1989-07-06',
            gender_id     = 1,
            kakao_id      = '노란책 카카오 아이디',
            point         = 100000
        )

        Image.objects.bulk_create([
            Image(
                id         = 1,
                image_url  = '1번책 이미지 유알엘',
                product_id = 1
            ),
            Image(
                id         = 2,
                image_url  = '2번책 이미지 유알엘',
                product_id = 2
            ),
            Image(
                id         = 3,
                image_url  = '3번책 이미지 유알엘',
                product_id = 3
            )
        ])

        Review.objects.bulk_create([
            Review(
                id         = 1,
                content    = '1번책 리뷰',
                rating     = 5,
                product_id = 1,
                user_id    = 1
            ),
            Review(
                id         = 2,
                content    = '2번책 리뷰',
                rating     = 4,
                product_id = 2,
                user_id    = 1
            ),
            Review(
                id         = 3,
                content    = '3번책 리뷰',
                rating     = 3,
                product_id = 3,
                user_id    = 1
            )
        ])

    def tearDown(self):
        Author.objects.all().delete()
        Publisher.objects.all().delete()
        Translator.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()
        Gender.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()
        Review.objects.all().delete()

    def test_success_product_recommend_view_get_handler_method(self):
        client = Client()
        response = client.get('/products/recommend')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                "result": [
                    {
                        'name'          : '1번책',
                        'book_img'      : ['1번책 이미지 유알엘'],
                        'author'        : '1번책 작가',
                        'rating_avg'    : 5.0,
                        'comment_count' : 1,
                        'product_id'    : 1
                    },
                    {
                        'name'          : '2번책',
                        'book_img'      : ['2번책 이미지 유알엘'],
                        'author'        : '2번책 작가',
                        'rating_avg'    : 4.0,
                        'comment_count' : 1,
                        'product_id'    : 2
                    },
                    {
                        'name'          : '3번책',
                        'book_img'      : ['3번책 이미지 유알엘'],
                        'author'        : '3번책 작가',
                        'rating_avg'    : 3.0,
                        'comment_count' : 1,
                        'product_id'    : 3
                    }
                ]    
            }
        )


class ProductReadmePickViewTest(TestCase):
    def setUp(self):
        Author.objects.bulk_create([
            Author(
                id   = 1,
                name = '1번책 작가'
            ),
            Author(
                id   = 2,
                name = '2번책 작가'
            ),
            Author(
                id   = 3,
                name = '3번책 작가'
            ),
            Author(
                id   = 4,
                name = '4번책 작가'
            ),
            Author(
                id   = 5,
                name = '5번책 작가'
            ),
            Author(
                id   = 6,
                name = '6번책 작가'
            ),
            Author(
                id   = 7,
                name = '7번책 작가'
            ),
            Author(
                id   = 8,
                name = '8번책 작가'
            ),
            Author(
                id   = 9,
                name = '9번책 작가'
            )
        ])

        Publisher.objects.bulk_create([
            Publisher(
                id   = 1,
                name = '1번책 출판사'
            ),
            Publisher(
                id   = 2,
                name = '2번책 출판사'
            ),
            Publisher(
                id   = 3,
                name = '3번책 출판사'
            ),
            Publisher(
                id   = 4,
                name = '4번책 출판사'
            ),
            Publisher(
                id   = 5,
                name = '5번책 출판사'
            ),
            Publisher(
                id   = 6,
                name = '6번책 출판사'
            ),
            Publisher(
                id   = 7,
                name = '7번책 출판사'
            ),
            Publisher(
                id   = 8,
                name = '8번책 출판사'
            ),
            Publisher(
                id   = 9,
                name = '9번책 출판사'
            )
        ])

        Translator.objects.bulk_create([
            Translator(
                id   = 1,
                name = '1번책 번역가'
            ),
            Translator(
                id   = 2,
                name = '2번책 번역가'
            ),
            Translator(
                id   = 3,
                name = '3번책 번역가'
            ),
            Translator(
                id   = 4,
                name = '4번책 번역가'
            ),
            Translator(
                id   = 5,
                name = '5번책 번역가'
            ),
            Translator(
                id   = 6,
                name = '6번책 번역가'
            ),
            Translator(
                id   = 7,
                name = '7번책 번역가'
            ),
            Translator(
                id   = 8,
                name = '8번책 번역가'
            ),
            Translator(
                id   = 9,
                name = '9번책 번역가'
            )
        ])

        Category.objects.bulk_create([
            Category(
                id   = 1,
                name = '1번책 카테고리'
            ),
            Category(
                id   = 2,
                name = '2번책 카테고리'
            ),
            Category(
                id   = 3,
                name = '3번책 카테고리'
            ),
            Category(
                id   = 4,
                name = '4번책 카테고리'
            ),
            Category(
                id   = 5,
                name = '5번책 카테고리'
            ),
            Category(
                id   = 6,
                name = '6번책 카테고리'
            ),
            Category(
                id   = 7,
                name = '7번책 카테고리'
            ),
            Category(
                id   = 8,
                name = '8번책 카테고리'
            ),
            Category(
                id   = 9,
                name = '9번책 카테고리'
            )
        ])

        Product.objects.bulk_create([
            Product(
                id              = 1,
                name            = '1번책',
                description     = '1번책 내용',
                publisher_id    = 1,
                translator_id   = 1,
                author_id       = 1,
                category_id     = 1
            ),
            Product(
                id              = 2,
                name            = '2번책',
                description     = '2번책 내용',
                publisher_id    = 2,
                translator_id   = 2,
                author_id       = 2,
                category_id     = 2
            ),
            Product(
                id              = 3,
                name            = '3번책',
                description     = '3번책 내용',
                publisher_id    = 3,
                translator_id   = 3,
                author_id       = 3,
                category_id     = 3
            ),
            Product(
                id              = 4,
                name            = '4번책',
                description     = '4번책 내용',
                publisher_id    = 4,
                translator_id   = 4,
                author_id       = 4,
                category_id     = 4
            ),
            Product(
                id              = 5,
                name            = '5번책',
                description     = '5번책 내용',
                publisher_id    = 5,
                translator_id   = 5,
                author_id       = 5,
                category_id     = 5
            ),
            Product(
                id              = 6,
                name            = '6번책',
                description     = '6번책 내용',
                publisher_id    = 6,
                translator_id   = 6,
                author_id       = 6,
                category_id     = 6
            ),
            Product(
                id              = 7,
                name            = '7번책',
                description     = '7번책 내용',
                publisher_id    = 7,
                translator_id   = 7,
                author_id       = 7,
                category_id     = 7
            ),
            Product(
                id              = 8,
                name            = '8번책',
                description     = '8번책 내용',
                publisher_id    = 8,
                translator_id   = 8,
                author_id       = 8,
                category_id     = 8
            ),
            Product(
                id              = 9,
                name            = '9번책',
                description     = '9번책 내용',
                publisher_id    = 9,
                translator_id   = 9,
                author_id       = 9,
                category_id     = 9
            )
        ])

        Gender.objects.create(
            id  = 1,
            sex = 'male'
        )

        User.objects.create(
            id            = 1,
            nickname      = '노란책 닉네임',
            date_of_birth = '1989-07-06',
            gender_id     = 1,
            kakao_id      = '노란책 카카오 아이디',
            point         = 100000
        )

        Image.objects.bulk_create([
            Image(
                id         = 1,
                image_url  = '1번책 이미지 유알엘',
                product_id = 1
            ),
            Image(
                id         = 2,
                image_url  = '2번책 이미지 유알엘',
                product_id = 2
            ),
            Image(
                id         = 3,
                image_url  = '3번책 이미지 유알엘',
                product_id = 3
            ),
            Image(
                id         = 4,
                image_url  = '4번책 이미지 유알엘',
                product_id = 4
            ),
            Image(
                id         = 5,
                image_url  = '5번책 이미지 유알엘',
                product_id = 5
            ),
            Image(
                id         = 6,
                image_url  = '6번책 이미지 유알엘',
                product_id = 6
            ),
            Image(
                id         = 7,
                image_url  = '7번책 이미지 유알엘',
                product_id = 7
            ),
            Image(
                id         = 8,
                image_url  = '8번책 이미지 유알엘',
                product_id = 8
            ),
            Image(
                id         = 9,
                image_url  = '9번책 이미지 유알엘',
                product_id = 9
            )
        ])

        Review.objects.bulk_create([
            Review(
                id         = 1,
                content    = '1번책 리뷰',
                rating     = 5,
                product_id = 1,
                user_id    = 1
            ),
            Review(
                id         = 2,
                content    = '2번책 리뷰',
                rating     = 5,
                product_id = 2,
                user_id    = 1
            ),
            Review(
                id         = 3,
                content    = '3번책 리뷰',
                rating     = 5,
                product_id = 3,
                user_id    = 1
            ),
            Review(
                id         = 4,
                content    = '4번책 리뷰',
                rating     = 5,
                product_id = 4,
                user_id    = 1
            ),
            Review(
                id         = 5,
                content    = '5번책 리뷰',
                rating     = 5,
                product_id = 5,
                user_id    = 1
            ),
            Review(
                id         = 6,
                content    = '6번책 리뷰',
                rating     = 5,
                product_id = 6,
                user_id    = 1
            ),
            Review(
                id         = 7,
                content    = '7번책 리뷰',
                rating     = 5,
                product_id = 7,
                user_id    = 1
            ),
            Review(
                id         = 8,
                content    = '8번책 리뷰',
                rating     = 5,
                product_id = 8,
                user_id    = 1
            ),
            Review(
                id         = 9,
                content    = '9번책 리뷰',
                rating     = 5,
                product_id = 9,
                user_id    = 1
            )
        ])

    def tearDown(self):
        Author.objects.all().delete()
        Publisher.objects.all().delete()
        Translator.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()
        Gender.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()
        Review.objects.all().delete()

    def test_success_product_readmepick_view_get_handler_method(self):
        client = Client()
        response = client.get('/products/readmepick')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['result']), 9)
    
