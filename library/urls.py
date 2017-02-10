from django.conf.urls import url
from library import views
urlpatterns = [
    url(r'^book/(?P<book_id>\d+)/', views.book),
    url(r'^', views.library),
]