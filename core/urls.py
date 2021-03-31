from django.contrib import admin
from django.urls import path
from .views import Home, UserUpdateView, GeneralPage, chrome_download, firefox_download, userstastics, Delete_user, Usercreation

app_name = "core"

urlpatterns = [
    path('home/', Home.as_view(), name="home" ),
    path('userdetail/<slug:userid>/', userstastics.as_view(), name="userdetail" ),
    path('deleteuser/<slug:userid>/', Delete_user.as_view(), name="delete_user" ),
    path('update/<slug:userid>/', UserUpdateView.as_view(), name="update" ),
    path('create-user', Usercreation.as_view(), name="create_user" ),
    path('', GeneralPage.as_view(), name="index" ),
    path('chrome-download', chrome_download, name="chrome-download"),
    path('firefox-download', firefox_download, name="firefox-download"),
]
