from django.urls import path
from.views import add_course,list_courses

urlpatterns=[
        path("add/",add_course,name="add_course"),
        path("list/",list_courses,name="list_course"),
    ]
# if settings.DEBUG:
#     urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

    # python manage.py collectstatic  
             