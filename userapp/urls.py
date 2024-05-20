from django.urls import path
from . import views

urlpatterns=[path('',views.listbook,name='listbook'),
             path('user_details/<int:book_id>',views.detailsview,name='user_details'),
             path('user_search',views.Searchbook,name='user_search'),
             path('add_to_cart/<int:book_id>/',views.add_to_cart,name='addtocart'),
             path('view_cart/',views.view_cart,name='viewcart'),
             path('increase/<int:item_id>/',views.increase_quantity,name='increase_quantity'),
             path('decrease/<int:item_id>/',views.decrease_quantity,name='decrease_quantity'),
             path('removecart/<int:item_id>',views.remove_from_cart,name='remove_cart'),
             path('create_checkout_session/',views.create_checkout_session,name='create_checkout_session'),
             path('success/',views.success,name='success'),
             path('cancel/',views.cancel,name='cancel')
             ]


# path('createbook/',views.Createbook,name='createbook'),
#     path('author/',views.CreateAuthor,name='author'),
#     path('listview/',views.listbook,name='listview'),
#     path('detailsview/<int:book_id>',views.detailsview,name='details'),
#     path('updateview/<int:book_id>',views.updatebook,name='update'),
#     path('deleteview/<int:book_id>',views.deletebook,name='delete'),
#     path('base/',views.index),
#     path('search/',views.Searchbook,name='search')
# ]