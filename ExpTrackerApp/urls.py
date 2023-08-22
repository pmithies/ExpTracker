from django.urls import path
from . import views

urlpatterns = [
    path("ExpTrack/", views.index, name='index'),
    path("ExpTrack/add/", views.add, name = 'add'),
    path('ExpTrack/add/addrecord/', views.addrecord, name = 'addrecord'),
    path('ExpTrack/Delete/<int:id>', views.delete, name = 'delete'),
    path('ExpTrack/Update/<int:id>', views.update, name = 'update'),
    path('ExpTrack/Update/UpdateRecord/<int:id>', views.updaterecord, name = 'updaterecord')
]