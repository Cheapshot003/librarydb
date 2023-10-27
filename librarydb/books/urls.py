from django.urls import path
from .views import FavBook
from .views import BookCreate # Neu
from .views import BookDetail
from .views import BookUpdate
from .views import BookDelete

urlpatterns = [
    path('', FavBook.as_view(), name='book_start'),
    path('neu/', BookCreate.as_view(), name='neues_buch'),
    path('<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('<int:pk>/update/', BookUpdate.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDelete.as_view(), name='book_delete'),
]
