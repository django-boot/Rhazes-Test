"""
core URL Configuration

"""
import logging

from django.urls import path, include
from rhazes.context import ApplicationContext

from app1.views import NameGeneratorView, view_function

urlpatterns = [
    path("generate-name/", NameGeneratorView.as_view(), name="generate-name-1"),
    path("generate-name-2/", view_function, name="generate-name-2"),
]


ApplicationContext.initialize()
print(ApplicationContext._builder_registry)