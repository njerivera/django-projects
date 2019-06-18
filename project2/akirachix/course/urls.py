from django.urls import path
from.views import add_course

urlpatterns=[
        path("add/",add_course,name="add_course"),
    ]
# if settings.DEBUG:
#     urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

    # python manage.py collectstatic  
             