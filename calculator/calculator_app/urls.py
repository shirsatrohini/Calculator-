from django.urls import path
from calculator_app import views

urlpatterns = [
      path('',views.index,name='index'),
      path('submitquery',views.submitquery,name='submitquery'),
      path('history',views.history,name='history'),
      path('history/delete/<int:pk>',views.delete,name='delete')
]