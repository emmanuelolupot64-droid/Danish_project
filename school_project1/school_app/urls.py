from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from.import views
urlpatterns=[
    
 
 path('',views.about_page, name='HOME'),
 path('contact.html/',views.contact_page, name='CONTACT'),
 path('register/',views.register_student,name='REGISTER'),
 path('success/',views.success_page,name='success')
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    