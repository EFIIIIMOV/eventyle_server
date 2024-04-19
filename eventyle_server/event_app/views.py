from django.http import JsonResponse


def getRoutes(request):
    return JsonResponse("hello world!", safe=False)
