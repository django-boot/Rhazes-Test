from django.http import HttpResponse
from rhazes.context import ApplicationContext

from app1.services.name_generator import StringGeneratorService


# @inject(
#     configuration={
#         StringGeneratorService: {"lazy": True}
#     }
# )
def name_generator_view(request, *args, **kwargs):
    string_generator: StringGeneratorService = ApplicationContext.get_lazy_bean(StringGeneratorService)
    qs: dict = request.GET.dict()
    return HttpResponse(content=string_generator.generate(int(qs.get("length", 10))), status=200)

#
# class NameGeneratorView(APIView):
#
#     def __int__(self, string_generator: StringGeneratorService, **kwargs):
#         self.string_generator = string_generator
#
#
