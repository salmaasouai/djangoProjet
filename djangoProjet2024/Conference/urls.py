from django.urls import path
from .views import *
from . import views 

urlpatterns = [
    path('list/',conferenceList,name="listeconf"),  #affichage liste des conferences sans details #path mt3 l vue fonctionnelle
    path('listViewConference/',ConferenceListView.as_view(),  # path mt3 l vue geenrique 
         name="listeViewconf"),
    
    
    path('deleteConference/<int:pk>/', ConferenceDeleteView.as_view(), name="delete_conference"),  # Accept pk parameter
    
    path('update/<int:pk>', ConferenceUpdateView.as_view(), name="update_conference"),
    
    path('details/<int:pk>/',DetailsViewConference.as_view(),
         name="detailConf"), #affiche une conference bien determine selon le nombre entree
    
    path('addform/',AddConference.as_view(), name='add_conference'),

] 