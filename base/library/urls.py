from django.urls import path
from .views import Home , AuthorList , AddAuthor , DeleteAuthor , UpdateAuthor , AuthorDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('authors/create/', AddAuthor.as_view(), name='create_author'),
    path('authors/<int:id>/delete/',DeleteAuthor.as_view(), name='delete_author'),
    path('authors/<int:id>/update/', UpdateAuthor.as_view(), name='update_author'),
    path('authors/<int:id>/', AuthorDetail.as_view(), name='author_detail')
]
