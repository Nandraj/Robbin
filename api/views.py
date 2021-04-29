from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def apiOverView(request):
    api_urls = {}
    return Response(api_urls)
