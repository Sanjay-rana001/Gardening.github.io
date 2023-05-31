
from django.contrib import admin
from django.urls import path
from Mainapp import views as Mainapp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Mainapp.homepage),
    path('error/', Mainapp.errorpage),
    path('about/', Mainapp.aboutpage),
    path('contact/', Mainapp.contactpage),
    path('feature/', Mainapp.featurepage),
    path('project/', Mainapp.projectpage),
    path('quote/', Mainapp.quotepage),
    path('service/', Mainapp.servicepage),
    path('team/', Mainapp.teampage),
    path('testimonial/', Mainapp.testimonialpage),
    path("descriptions/<int:num>/",Mainapp.descriptionpage)
        
    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
