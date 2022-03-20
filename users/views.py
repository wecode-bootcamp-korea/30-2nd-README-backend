from wsgiref import headers
import requests, json, jwt

from requests.exceptions import Timeout

from django.http         import HttpResponse, JsonResponse
from django.views        import View
       
from .models             import User, Gender
from .decorators         import login_decorator
from my_settings         import SECRET_KEY, ALGORITHM

class KakaoSignin():
    def __init__(self):
        self.BASE_URL  = 'https://kapi.kakao.com'
        self.USER_PATH = '/v2/user/me'

    def user_information(self, kakao_access_token):
        user_information = requests.get(
                    self.BASE_URL + self.USER_PATH,
                    headers = {
                        'Authorization' : f'Bearer {kakao_access_token}'
                    },
                    timeout = 5
                ).json()

        kakao_id  = user_information['id']
        nickname  = user_information['properties']['nickname']
        gender_id = Gender.objects.get(sex = user_information['kakao_account']['gender']).id

        return kakao_id, nickname, gender_id

class SignInView(View):
    def get(self,request):
        try:
            kakao_access_token   = request.headers.get('Authorization',None)
            kakao_signin    = KakaoSignin()
            kakao_id, nickname, gender_id = kakao_signin.user_information(kakao_access_token)

            POINT     = 500000
            
            user, is_created = User.objects.get_or_create(
                kakao_id  = kakao_id,
                gender_id = gender_id,
                defaults  = {
                    'point'    : POINT,
                    'nickname' : nickname
                }
            )

            access_token = jwt.encode({'id' : kakao_id}, SECRET_KEY, ALGORITHM)

            status = 201 if is_created else 200

            return JsonResponse({'access_token' : access_token}, status = status)
            
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        except Timeout:
            return JsonResponse({'message' : 'TIME_OUT_ERROR'}, status = 408)

    
    @login_decorator
    def patch(self, request):
        try:
            user = request.user

            data = json.loads(request.body)

            nickname      = data['nickname']
            date_of_birth = data['date_of_birth']
        
            user.nickname      = nickname
            user.date_of_birth = date_of_birth 
            
            user.save()

            return HttpResponse(status = 200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)