from django.urls import path
from.views import add_teacher

urlpatterns=[
        path("add/",add_teacher,name="add_teacher"),
    ]
             