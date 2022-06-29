import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer

def api_home(request, *args, **kwargs):
  # request body
  body = request.body
  params = request.GET # url query params
  # request.POST
  data = {}
  try:
    data = json.loads(body) # string of json data -> python dict
  except:
    pass
  print(data)
  data['params'] = dict(request.GET)
  data['headers'] = dict(request.headers)
  data['content-type'] = request.content_type
  return JsonResponse(data)

@api_view(['GET', 'POST'])
def interface(request):
  print(request.method)
  if request.method == 'GET':
    return get_product(request)
  if request.method == 'POST':
    return save_product(request)

def get_product(request, *args, **kwargs):
  """
  DRF API View
  """
  queryData = Product.objects.all().order_by('?').first()
  data = {}
  if queryData:
    # data['id'] = queryData.id
    # data['title'] = queryData.title
    # data['content'] = queryData.content
    # data['price'] = queryData.price

    # instead of doing this, we can use model_to_dict
    # data = model_to_dict(queryData, fields=['id', 'title', 'price'])

    # serializers
    data = ProductSerializer(queryData).data

  return Response(data)

def save_product(request, *args, **kwargs):
  serializer = ProductSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    instance = serializer.save()
    print(instance)
    print(serializer.data)
    return Response(serializer.data)
