from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rhazes.decorator import inject

from app1.services.name_generator import StringGeneratorService


@inject()
class NameGeneratorView(APIView):
    def __init__(self, string_generator: StringGeneratorService, **kwargs):
        self.string_generator = string_generator
        super(NameGeneratorView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        qs: dict = request.GET.dict()
        return Response(data={"name": self.string_generator.generate(int(qs.get("length", 10)))})



# This doesnt work
@inject()
def view_function(request, string_generator: StringGeneratorService):
    qs: dict = request.GET.dict()
    return HttpResponse(content="Hey")
