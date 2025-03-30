from django.urls import path
from money_transfers import views 

urlpatterns = [
    path('', views.TransferListView.as_view(), name='transfer_list'),
    path('create/', views.TransferCreateView.as_view(), name='transfer_create'),
    path('<int:transfer_id>/delete/', views.TransferDeleteView.as_view(), name='transfer_delete'),
]