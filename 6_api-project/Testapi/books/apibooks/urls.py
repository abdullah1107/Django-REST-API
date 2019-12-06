from django.urls import path,include
from books.apibooks import views
from books.apibooks.views import(
      api_create_book_view,
      api_update_book_view,
      api_delete_book_view,
      BookListView
)

app_name = 'books'

urlpatterns = [
   
    path('list', BookListView.as_view(), name="list"),
	path('create', api_create_book_view, name="create"),
	path('update/<pk>', api_update_book_view, name="update"),
	path('delete/<pk>',api_delete_book_view, name ="delete")

]