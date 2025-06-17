import json
from django.http import JsonResponse



def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    print(request.GET) # url query parameters (params)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) #string of JSON data becomes a Python Dict
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers) # Same as old request.META
    data['content_type'] = request.content_type
    print(data)
    return JsonResponse(data)
