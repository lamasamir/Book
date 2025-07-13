from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("",views.homepage,name = "homepage"),
    path("create/", views.insert_book,name="insert_book"),
    path("contact/",views.contact,name="contact"),
    path("privacy/",views.privacy_policy,name="privacy_policy"),
    path("term of use/",views.terms,name="term_of_use"),
    path("signup/",views.signin,name="signup"),
    path("delete/<int:id>/",views.delete_book,name="delete_books"),
    path("edit/<int:id>/",views.edit_book,name="edit_books"),
    path("searchbook/",views.search_books,name="search_book"),
    path("newbooks/",views.new_books,name="new_books"),
    path("login/",views.login_user,name="login",),
    path("logout/",views.logout_user,name="logout"),
     path('book/<int:id>/',views.book_detail, name='bookdetails'),
]

     
   

 




