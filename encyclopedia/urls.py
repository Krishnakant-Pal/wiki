from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entry_page, name="title"),
    path("wiki/", views.get_search_query, name="search_query"),
    path("new", views.new_entry_page, name="new_entry"),
    path("wiki/edit/<str:title>", views.edit_entry, name="edit_entry"),
    path("random", views.random_entry, name="random_entry"),
]   
