from django.urls import path
from AppTwo import views

urlpatterns=[
    path('',views.help,name='help'),
    #path('help/',views.index,name='index'), -> wrong (This indicates /help/help)
]
