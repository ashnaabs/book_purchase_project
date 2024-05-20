from django.urls import path
from . import views

urlpatterns=[
path('createbook/',views.Createbook,name='createbook'),
    path('author/',views.CreateAuthor,name='author'),
    path('listview/',views.listbook,name='listview'),
    path('detailsview/<int:book_id>',views.detailsview,name='details'),
    path('updateview/<int:book_id>',views.updatebook,name='update'),
    path('deleteview/<int:book_id>',views.deletebook,name='delete'),
    path('base/',views.index),
    path('search/',views.Searchbook,name='search'),

]