from django.contrib import admin
from django.urls import path
from Login import views
admin.site.site_header="Login Information Portal"
admin.site.site_title="Login Information Portal"
admin.site.index_title="Welcome to Login Portal"
urlpatterns = [
    path("",views.login,name="Login"),
    path("login",views.login,name="Login"),
    path("user",views.user,name="User"),
    
    
    
]
