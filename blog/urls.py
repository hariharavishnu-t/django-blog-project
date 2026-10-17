from django.urls import path
from . import views
app_name = "blog"
urlpatterns =[
    path("", views.index, name="index"),
    path("post/<str:slug>/", views.detail, name="detail"),
    path("new_hats_url", views.new_url_views, name="new_page_url"),
    path("old_url", views.old_url_redirect, name="old_url"),
    path("contact", views.contact_view, name="contact"),
    path("about", views.about_View, name="about"),
]