from django.contrib import admin
from django.urls import path
# from learn.views import Home
from learn.views import home_render,tset_render, getName, about, coursedetail, userForm, submitfrm

# urlpatterns = [
#     path('home/', Home.as_view(
#     )),
# ]

urlpatterns = [
    path('home/', home_render, name="home"),
    path('ch/', tset_render, name="landing"),
    path("getName/", getName),
    path("about/", about),
    path("coursedetail/<coursedetail>", coursedetail),
    path("form", userForm),
    path("submitfrm", submitfrm)

    # path("coursedetail/<int:coursedetail>", coursedetail)
]