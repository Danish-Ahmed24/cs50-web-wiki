from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addEntry",views.addEntry,name="addEntry"),
    path("<str:TITLE>",views.displayEntryContentByTitle,name="entry")
]
 