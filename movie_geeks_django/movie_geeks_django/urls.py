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
from awards.views import (FilmAwardReceivedView, FilmAwardReceivedViewForLists,
                          FilmAwardView)
from django.contrib import admin
from django.urls import include, path
from movies.views import (FilmReviewForUserView, FilmReviewView,
                          FilmReviewViewForLists, FilmsDirectedViewForLists,
                          FilmsStarredInViewForLists, FilmView, GenreView)
from performers.views import PerformerView, PerformerViewForCastLists, PerformerViewForRecipientLists
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("films", FilmView, basename="film-view")
router.register("performers", PerformerView, basename="performer-view")
router.register("film-awards", FilmAwardView, basename="film-award-view")
router.register("genres", GenreView, basename="genre-view")
router.register(
    "film-reviews", FilmReviewView, basename="film-reviews"
)  # this is here just for dev purposes
router.register("my-film-reviews", FilmReviewForUserView, basename="my-film-reviews")

# ------------------------------------------ Nested Routers below ------------------------------------------------- #

performer_router = routers.NestedSimpleRouter(router, r"performers", lookup="performer")
performer_router.register(
    r"directed", FilmsDirectedViewForLists, basename="director-films"
)
performer_router.register(
    r"starred-in", FilmsStarredInViewForLists, basename="actor-films"
)
performer_router.register(
    r"awards-received", FilmAwardReceivedViewForLists, basename="performer-awards"
)

film_router = routers.NestedSimpleRouter(router, r"films", lookup="film")
film_router.register(r"full-cast", PerformerViewForCastLists, basename="film-cast")
film_router.register(r"reviews", FilmReviewViewForLists, basename="film-reviews")

film_award_router = routers.NestedSimpleRouter(router, r'film-awards', lookup='filmaward')
film_award_router.register(r'recipients', PerformerViewForRecipientLists, basename='award-recipients')
film_award_router.register(r'awarded', FilmAwardReceivedView, basename='award-instances')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", include("rest_framework.urls")),
    path("", include(router.urls)),
    path("", include(performer_router.urls)),
    path("", include(film_router.urls)),
    path("", include(film_award_router.urls)),
]
