from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('registration',views.registration,name='registration'),
    path('submit',views.submit,name='submit'),
    path('login',views.login,name='login'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('mark_attendence/<str:name>/<int:month>/<int:date>/<int:year>',views.mark_attendence,name='mark_attendence'),
    path('show_attendence/<str:name>',views.show_attendence, name='show_attendence')
]
