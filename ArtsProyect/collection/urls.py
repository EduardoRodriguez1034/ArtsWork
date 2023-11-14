from django.urls import path
from . import views
#Importar la accion add_to_collection
from .views import add_to_collection
#Importar la accion collection_detail
from .views import collection_detail, remove_from_collection, logout_view

urlpatterns = [
    path("", views.index, name="index"),
    path("artwork/<int:artwork_id>", views.artwork, name="artwork"),
    path("artworks/search", views.search_artworks, name="search_artworks"),
    path("artworks/random", views.random_artworks, name="random_artworks"),
    path("collections/", views.collections, name="collections"),
    path("collection_list/", views.collection_list, name="collection_list"),
    path("collection/add", views.collection_add, name="collection_add"),
    path("accounts/profile/", views.index, name="index"),
    path("accounts/register/", views.register, name="register"),
    path('editar_coleccion/<int:collection_id>/', views.editar_coleccion, name='editar_coleccion'),
    #Esta es la direccion para agregar a la coleccion
    path('add_to_collection/<int:artwork_id>/', add_to_collection, name='add_to_collection'),
    path('collection/<int:collection_id>/', collection_detail, name='collection_detail'),
    #Direccion para el about
    path('about/', views.about, name='about'),
    #Path para remover el artwork de la coleccion desde el collection detail
    path('collections/<int:collection_id>/remove/<int:artwork_id>/', remove_from_collection, name='remove_from_collection'),
    #Path para remover una lista de coleccion
    path('collection/delete/<int:collection_id>/', views.delete_collection, name='delete_collection'),
    path('logout/', logout_view, name='logout'),
]