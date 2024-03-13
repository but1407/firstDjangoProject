from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('list/', views.viewlists, name= 'viewlist'),
    path('detail/<int:question_id>',views.detailView, name="detail"),
    path('sanpham/', views.products, name= 'products'),
    path('<int:question_id>/',views.vote, name="vote"),
    
    
]
