"""
core URL Configuration

"""
import logging

from django.urls import path, include
from rhazes.context import ApplicationContext

from app1.views import name_generator_view

urlpatterns = [
    path("generate-name/", name_generator_view, name="name-generator"),
]


ApplicationContext.initialize()
print(ApplicationContext._builder_registry)