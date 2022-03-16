import json, uuid

from django.http import JsonResponse, HttpResponse
from django.views import View

from users.decorators import *
from .models import *
from products.models import *
from users.models import *
from carts.models import *