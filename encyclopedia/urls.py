from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addEntry",views.addEntry,name="addEntry"),
    path("randomPage",views.randomPage,name="randomPage"),
    path("<str:TITLE>",views.displayEntryContentByTitle,name="entry"),
    path("<str:TITLE>/edit",views.editEntry,name="editEntry")
]
#  edit entry ka title kese malom karoge pagal 