"""movie_geeks_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import FilmView, GenreView, FilmReviewView, FilmReviewForUserView
from awards.views import FilmAwardView, FilmAwardReceivedView
from performers.views import PerformerView

router = routers.DefaultRouter()
router.register('films', FilmView, basename='film-view')
router.register('performers', PerformerView, basename='performer-view')
router.register('film-awards', FilmAwardView, basename='film-award-view')
router.register('film-awards-received', FilmAwardReceivedView, basename='film-award-received-view')
router.register('genres', GenreView, basename='genre-view')
router.register('film-reviews', FilmReviewView, basename='film-reviews')
router.register('my-film-reviews', FilmReviewForUserView, basename='my-film-reviews')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('rest_framework.urls')),
    path('', include(router.urls))
]
