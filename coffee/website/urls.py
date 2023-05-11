from django.urls import path

from . import views
from website.views import index, about, contact, coffees, blog

urlpatterns = [
    path("", index),
    path("", about),
    path("", contact),
    path("", coffees),
    path("", blog),
    path("index.html", index),
    path("about.html", about),
    path("contact.html", contact),
    path("coffees.html", coffees),
    path("blog.html", blog),

]
