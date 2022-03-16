import requests, json, jwt, uuid

from requests.exceptions import Timeout

from django.http         import HttpResponse, JsonResponse
from django.views        import View
       
from .models             import User, Gender
from .decorators         import login_decorator
from my_settings         import SECRET_KEY, ALGORITHM

class SignInView(View):
    def get(self,request):
        try:
            kakao_access_token   = request.headers.get('Authorization',None)
            USER_INFORMATION_API = 'https://kapi.kakao.com/v2/user/me'
            user_information     = requests.get(
                USER_INFORMATION_API,
                headers = {
                    'Authorization' : f'Bearer {kakao_access_token}'
                }, 
                timeout = 5
            ).json()

            kakao_id             = user_information['id']
            POINT                = 500000
            gender_id            = Gender.objects.get(sex = user_information['kakao_account']['gender']).id
            
            user, is_created = User.objects.get_or_create(
                kakao_id  = kakao_id,
                gender_id = gender_id,
                defaults  = {
                    'point'         : POINT,
                    'date_of_birth' : '1945-08-15'
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